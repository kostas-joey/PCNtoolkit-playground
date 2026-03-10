"""
plot_normative_deviations.py
----------------------------
Produce publication-quality figures from PCNtoolkit normative model outputs.

Usage
-----
    python plot_normative_deviations.py --output_dir ../outputs/blr/

Outputs (written to <output_dir>/figures/)
------------------------------------------
    centile_curves.png          — Predicted centile bands overlaid on observed data
    z_score_distribution.png    — Z-score histogram vs N(0,1) reference
    z_score_regions.png         — Mean Z-scores per brain region (if parcellation CSV found)
"""

import argparse
import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_pkl(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def find_suffix(output_dir):
    """Detect the output suffix used by PCNtoolkit (e.g. '_blr', '_hbr')."""
    for fname in os.listdir(output_dir):
        if fname.startswith("yhat") and fname.endswith(".pkl"):
            return fname[4:-4]  # strip 'yhat' and '.pkl'
    return ""


# ---------------------------------------------------------------------------
# Plot 1 — Centile curves
# ---------------------------------------------------------------------------

def plot_centile_curves(output_dir, suffix, figures_dir):
    yhat = load_pkl(os.path.join(output_dir, f"yhat{suffix}.pkl")).flatten()
    ys2  = load_pkl(os.path.join(output_dir, f"ys2{suffix}.pkl")).flatten()

    # Load test covariates (first column = age) if available
    cov_path = os.path.join(os.path.dirname(output_dir), "data", "cov_test.txt")
    if not os.path.exists(cov_path):
        # Fallback: dummy age axis
        age_test = np.arange(len(yhat))
        obs = None
    else:
        cov = np.loadtxt(cov_path)
        age_test = cov[:, 0]
        resp_path = os.path.join(os.path.dirname(output_dir), "data", "resp_test.txt")
        obs = np.loadtxt(resp_path).flatten() if os.path.exists(resp_path) else None

    sigma    = np.sqrt(np.abs(ys2))
    sort_idx = np.argsort(age_test)
    age_s    = age_test[sort_idx]
    yhat_s   = yhat[sort_idx]
    sigma_s  = sigma[sort_idx]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.fill_between(age_s, yhat_s - 2 * sigma_s, yhat_s + 2 * sigma_s,
                    alpha=0.15, color="steelblue", label="±2 SD (~95th)")
    ax.fill_between(age_s, yhat_s -     sigma_s,  yhat_s +     sigma_s,
                    alpha=0.30, color="steelblue", label="±1 SD (~68th)")
    ax.plot(age_s, yhat_s, color="steelblue", linewidth=2, label="Predicted mean")
    if obs is not None:
        ax.scatter(age_test, obs, s=15, alpha=0.6, color="black", label="Observed (test)")

    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Brain feature")
    ax.set_title("Normative Centile Curves")
    ax.legend(frameon=False)
    sns.despine()
    plt.tight_layout()

    out_path = os.path.join(figures_dir, "centile_curves.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  Saved: {out_path}")


# ---------------------------------------------------------------------------
# Plot 2 — Z-score distribution
# ---------------------------------------------------------------------------

def plot_z_distribution(output_dir, suffix, figures_dir):
    Z = load_pkl(os.path.join(output_dir, f"Z{suffix}.pkl")).flatten()

    frac_extreme = np.mean(np.abs(Z) > 1.96) * 100

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(Z, bins=25, density=True, alpha=0.6, color="steelblue", label="Observed Z-scores")

    x = np.linspace(-4, 4, 300)
    ax.plot(x, norm.pdf(x), "r--", linewidth=2, label="N(0,1) reference")
    ax.axvline(-1.96, color="grey", linestyle=":", linewidth=1)
    ax.axvline( 1.96, color="grey", linestyle=":", linewidth=1, label="±1.96 threshold")

    ax.set_xlabel("Z-score")
    ax.set_ylabel("Density")
    ax.set_title(f"Z-score Distribution  ({frac_extreme:.1f}% outside ±1.96)")
    ax.legend(frameon=False)
    sns.despine()
    plt.tight_layout()

    out_path = os.path.join(figures_dir, "z_score_distribution.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  Saved: {out_path}")


# ---------------------------------------------------------------------------
# Plot 3 — Per-region bar chart (optional)
# ---------------------------------------------------------------------------

def plot_z_regions(output_dir, suffix, figures_dir):
    """Plot mean Z-score per region if a parcellation CSV exists in data/."""
    data_dir   = os.path.join(os.path.dirname(output_dir), "data")
    parc_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")] if os.path.isdir(data_dir) else []

    if not parc_files:
        print("  No parcellation CSV found in data/ — skipping region plot.")
        return

    import pandas as pd
    parc_path = os.path.join(data_dir, parc_files[0])
    parc      = pd.read_csv(parc_path)

    Z = load_pkl(os.path.join(output_dir, f"Z{suffix}.pkl"))
    if Z.ndim == 1:
        Z = Z.reshape(-1, 1)

    region_col = parc.columns[0]
    regions    = parc[region_col].values
    n_regions  = min(len(regions), Z.shape[1])
    mean_z     = Z[:, :n_regions].mean(axis=0)
    colors     = ["tomato" if v > 0 else "steelblue" for v in mean_z]

    sort_idx = np.argsort(mean_z)
    fig, ax  = plt.subplots(figsize=(6, max(4, n_regions * 0.3)))
    ax.barh(np.array(regions)[sort_idx], mean_z[sort_idx],
            color=np.array(colors)[sort_idx], alpha=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Mean Z-score")
    ax.set_title("Mean Normative Deviation per Brain Region")
    sns.despine()
    plt.tight_layout()

    out_path = os.path.join(figures_dir, "z_score_regions.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  Saved: {out_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Visualise PCNtoolkit normative model outputs.")
    parser.add_argument(
        "--output_dir",
        type=str,
        default="../outputs/blr/",
        help="Path to the directory containing PCNtoolkit output .pkl files.",
    )
    args = parser.parse_args()

    output_dir  = os.path.abspath(args.output_dir)
    figures_dir = os.path.join(output_dir, "figures")
    ensure_dir(figures_dir)

    suffix = find_suffix(output_dir)
    print(f"Output directory : {output_dir}")
    print(f"Detected suffix  : '{suffix}'")
    print(f"Figures directory: {figures_dir}\n")

    print("Generating centile curves ...")
    plot_centile_curves(output_dir, suffix, figures_dir)

    print("Generating Z-score distribution ...")
    plot_z_distribution(output_dir, suffix, figures_dir)

    print("Generating region bar chart (optional) ...")
    plot_z_regions(output_dir, suffix, figures_dir)

    print("\nDone.")


if __name__ == "__main__":
    main()
