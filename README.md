# PCNtoolkit Playground

> A hands-on repository for learning and experimenting with **normative modeling** in neuroimaging using [PCNtoolkit](https://pcntoolkit.readthedocs.io).

![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Overview

**Normative modeling** is a statistical framework that characterizes variability across a healthy reference population and then quantifies how much any individual *deviates* from that norm. Rather than asking "does this patient belong to group A or B?", it asks "how unusual is this person's brain relative to what is expected for someone their age and sex?" The result is a per-subject **deviation Z-score** — a continuous, interpretable measure of atypicality.

[PCNtoolkit](https://github.com/amarquand/PCNtoolkit) is an open-source Python toolbox that implements a range of normative models — from Bayesian Linear Regression (BLR) to Hierarchical Bayesian Regression (HBR) — and provides utilities for evaluation, transfer learning, and large-scale neuroimaging datasets.

This playground is aimed at **researchers, students, and clinicians** who want to understand normative modeling, run it on synthetic or real data, and interpret the outputs — without needing to start from scratch.

---

## Repository Structure

```
PCNtoolkit-playground/
│
├── notebooks/
│   └── normative_modeling_walkthrough.ipynb   # End-to-end BLR pipeline (synthetic data)
│
├── scripts/
│   └── plot_normative_deviations.py           # Reusable plotting script for model outputs
│
├── docs/
│   └── output_guide.md                        # Plain-language explanation of all output files
│
├── data/                                      # Generated automatically by the notebook
│   ├── cov_train.txt / cov_test.txt
│   └── resp_train.txt / resp_test.txt
│
├── outputs/                                   # Model outputs (generated at runtime)
│   └── blr/
│       ├── yhat_blr.pkl, ys2_blr.pkl, Z_blr.pkl
│       ├── MSLL_blr.txt, EXPV_blr.txt, SMSE_blr.txt ...
│       └── figures/
│
├── .github/
│   └── prompts/                               # Copilot task prompts for this repo
│
├── environment.yml                            # Conda environment
├── requirements.txt                           # Pip dependencies
└── SETUP.md                                   # Step-by-step installation guide
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/contsili/PCNtoolkit-playground.git
cd PCNtoolkit-playground
```

### 2. Set up the environment

Follow [SETUP.md](SETUP.md) for full instructions. The quick version:

```bash
conda env create -f environment.yml
conda activate pcntoolkit-playground
python -m ipykernel install --user --name pcntoolkit-playground --display-name "PCNtoolkit Playground"
```

### 3. Open the first notebook

```bash
jupyter notebook notebooks/normative_modeling_walkthrough.ipynb
```

Make sure the **PCNtoolkit Playground** kernel is selected in the top-right corner of the notebook.

---

## Notebooks

| Notebook | Description | Est. run time |
|----------|-------------|---------------|
| [normative_modeling_walkthrough.ipynb](notebooks/normative_modeling_walkthrough.ipynb) | Complete BLR normative modeling pipeline: synthetic data generation, model fitting, evaluation metrics, and centile/Z-score visualisations | ~2 min |

---

## Scripts

| Script | Description | Usage example |
|--------|-------------|---------------|
| [scripts/plot_normative_deviations.py](scripts/plot_normative_deviations.py) | Generate centile curves, Z-score distribution, and per-region bar chart from any PCNtoolkit output directory | `python scripts/plot_normative_deviations.py --output_dir outputs/blr/` |

---

## Documentation

| File | Description |
|------|-------------|
| [docs/output_guide.md](docs/output_guide.md) | Explains every output file produced by PCNtoolkit (`yhat`, `ys2`, `Z`, `MSLL`, `EXPV`, etc.) and how to interpret Z-scores clinically |
| [SETUP.md](SETUP.md) | Installation guide with conda and pip options, kernel registration, and common pitfalls |

---

## References

- **Marquand et al. (2016)** — *Understanding Heterogeneity in Clinical Cohorts Using Normative Models: Beyond Case-Control Studies*, Biological Psychiatry. [DOI](https://doi.org/10.1016/j.biopsych.2015.12.023)
- **Marquand et al. (2019)** — *Conceptualizing mental illness as deviations from normative functioning*, Molecular Psychiatry. [DOI](https://doi.org/10.1038/s41380-019-0441-1)
- **Rutherford et al. (2022)** — *Charting brain growth and aging at high spatial precision*, eLife. [DOI](https://doi.org/10.7554/eLife.72904)
- [PCNtoolkit GitHub](https://github.com/amarquand/PCNtoolkit)
- [PCNtoolkit Documentation](https://pcntoolkit.readthedocs.io)
