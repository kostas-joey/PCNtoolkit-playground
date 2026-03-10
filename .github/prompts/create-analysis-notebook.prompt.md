---
description: "Scaffold a Jupyter notebook with a full PCNtoolkit normative modeling workflow including data loading, model fitting, and evaluation"
name: "Create Normative Modeling Notebook"
agent: "agent"
---

Create a well-documented Jupyter notebook at `notebooks/normative_modeling_walkthrough.ipynb` that demonstrates a complete PCNtoolkit normative modeling pipeline.

The notebook should have the following sections, each in its own cell(s) with markdown explanations:

1. **Introduction** — What normative modeling is and why it is useful in neuroimaging research.

2. **Imports & Setup** — Import pcntoolkit, numpy, pandas, matplotlib, and set random seeds.

3. **Synthetic Data Generation** — Generate a realistic synthetic dataset:
   - 500 training subjects, 100 test subjects
   - One continuous covariate (age, range 18–80)
   - One binary covariate (sex: 0/1)
   - One brain feature (e.g., cortical thickness) with age-related trend + noise

4. **Data Preparation** — Split into train/test, save as `resp_train.txt`, `cov_train.txt`, `resp_test.txt`, `cov_test.txt` in a `data/` folder.

5. **Model Fitting** — Fit a Bayesian Linear Regression (BLR) normative model using `pcntoolkit.normative.estimate()`.

6. **Evaluation** — Load outputs (yhat, ys2, Z scores) and print MSLL, EXPV, SMSE metrics.

7. **Visualization** — Plot:
   - Predicted mean ± 2SD centile band against age
   - Z-score histogram for test subjects

Use clear variable names and add a brief comment above each code block. The notebook should run end-to-end without errors on a clean install of the environment.
