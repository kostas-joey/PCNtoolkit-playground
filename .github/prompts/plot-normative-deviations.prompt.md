---
description: "Generate Python plotting code to visualize PCNtoolkit normative modeling outputs: Z-score deviation maps and centile curves"
name: "Plot Normative Deviations"
agent: "agent"
---

Create a Python script at `scripts/plot_normative_deviations.py` that produces publication-quality visualizations from PCNtoolkit normative model outputs.

The script should:

1. **Centile Curves Plot**
   - Load `yhat.pkl` (predicted mean) and `ys2.pkl` (predicted variance) from a given output directory.
   - Load the test covariates (age) from `cov_test.txt`.
   - Plot the observed data points overlaid on centile bands: median (50th), ±1 SD (~16th/84th), and ±2 SD (~2.5th/97.5th) curves against age.
   - Label axes, add a legend, and save as `figures/centile_curves.png` at 300 dpi.

2. **Z-score Distribution Plot**
   - Load `Z.pkl` (deviation Z-scores for test subjects).
   - Plot a histogram with a standard normal N(0,1) reference curve overlaid.
   - Annotate with the percentage of subjects outside ±1.96 SD.
   - Save as `figures/z_score_distribution.png` at 300 dpi.

3. **Z-score Brain Map (optional stub)**
   - If a parcellation CSV with region names is found in `data/`, produce a horizontal bar chart of mean Z-scores per region, colored by direction (positive = warm, negative = cool).
   - Save as `figures/z_score_regions.png`.

Use matplotlib and seaborn. Add a `--output_dir` argparse argument so the script is reusable across different model runs. Create the `figures/` directory automatically if it does not exist.
