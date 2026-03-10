# PCNtoolkit Output Guide

A plain-language reference for every file produced by `pcntoolkit.normative.estimate()`.

---

## Output Files

### `yhat.pkl` — Predicted Mean

| Property | Details |
|----------|---------|
| **What it stores** | The normative model's predicted mean brain feature value for each test subject |
| **Shape** | `(N_test, N_features)` — one row per subject, one column per brain feature |
| **How to load** | `import pickle; yhat = pickle.load(open('yhat.pkl', 'rb'))` |

**Interpretation:** This is the "expected" value for a subject given their covariates (age, sex, etc.). If your feature is cortical thickness and `yhat[i] = 2.5 mm`, the model expects a person with those covariates to have 2.5 mm of cortical thickness.

---

### `ys2.pkl` — Predicted Variance

| Property | Details |
|----------|---------|
| **What it stores** | The model's uncertainty (variance) around the predicted mean |
| **Shape** | `(N_test, N_features)` |
| **How to load** | `ys2 = pickle.load(open('ys2.pkl', 'rb'))` |

**Interpretation:** `sqrt(ys2)` gives the predicted standard deviation. A larger `ys2` means the model is less certain about its prediction for that subject — this is common at extremes of the covariate range (e.g. very young or very old subjects).

---

### `Z.pkl` — Deviation Z-scores

| Property | Details |
|----------|---------|
| **What it stores** | Standardised deviation of each subject from the normative mean |
| **Shape** | `(N_test, N_features)` |
| **How to load** | `Z = pickle.load(open('Z.pkl', 'rb'))` |

**Interpretation:** Computed as `Z = (y_observed - yhat) / sqrt(ys2)`. This is the main output of normative modeling. See the **Interpreting Z-scores** section below.

---

### `warp_param.pkl` — Warping Parameters *(WarpedBLR only)*

| Property | Details |
|----------|---------|
| **What it stores** | Learned parameters of the output warping function (e.g. SinhArcsinh) that makes the response distribution more Gaussian |
| **Shape** | Varies by warping function |
| **How to load** | `wp = pickle.load(open('warp_param.pkl', 'rb'))` |

**Interpretation:** Only present when `warp='WarpSinhArcsinh'` (or similar) is used. These transform the predicted distribution back to the original data space. You generally do not need to inspect these manually.

---

### `MSLL.txt` — Mean Standardised Log Loss

| Property | Details |
|----------|---------|
| **What it stores** | Single float per brain feature |
| **How to load** | `msll = float(np.loadtxt('MSLL.txt'))` |

**Interpretation:** Measures predictive accuracy relative to a trivial baseline (predicting sample mean/variance). A value of **0** means the model is no better than the baseline; **negative values are better** (the lower the better). A well-fitted normative model typically shows MSLL < −0.1.

---

### `EXPV.txt` — Explained Variance

| Property | Details |
|----------|---------|
| **What it stores** | Single float in [0, 1] per brain feature |
| **How to load** | `expv = float(np.loadtxt('EXPV.txt'))` |

**Interpretation:** The proportion of variance in the test responses explained by the model. **1.0 = perfect fit; 0.0 = no better than the mean.** For typical neuroimaging features explained by age/sex, values of 0.2–0.6 are common.

---

### `SMSE.txt` — Standardised Mean Squared Error

| Property | Details |
|----------|---------|
| **What it stores** | Single float per brain feature |
| **How to load** | `smse = float(np.loadtxt('SMSE.txt'))` |

**Interpretation:** MSE normalised by the variance of the test responses. A value of **1.0** means the model is equivalent to always predicting the mean; **< 1.0 is better**. Values above 1.0 indicate the model is performing worse than the trivial baseline.

---

### `RMSE.txt` — Root Mean Squared Error

| Property | Details |
|----------|---------|
| **What it stores** | Single float in the original feature units |
| **How to load** | `rmse = float(np.loadtxt('RMSE.txt'))` |

**Interpretation:** The average prediction error in the same units as the brain feature (e.g. mm for cortical thickness). Useful for communicating practical effect sizes but hard to compare across features with different scales — prefer SMSE or EXPV for that.

---

### `Rho.txt` — Spearman Correlation

| Property | Details |
|----------|---------|
| **What it stores** | Spearman ρ between observed and predicted values |
| **How to load** | `rho = float(np.loadtxt('Rho.txt'))` |

**Interpretation:** Values close to **1.0** indicate strong rank agreement between predicted and observed. Less sensitive to outliers than Pearson correlation. Typical values: 0.3–0.8 for age-predicted brain features.

---

### `pRho.txt` — p-value for Spearman Correlation

| Property | Details |
|----------|---------|
| **What it stores** | Two-tailed p-value for the Spearman ρ |
| **How to load** | `p_rho = float(np.loadtxt('pRho.txt'))` |

**Interpretation:** Standard statistical significance. Values < 0.05 indicate the correlation is unlikely due to chance. For large test sets (N > 100) this will almost always be significant — use ρ magnitude, not just the p-value, to judge model quality.

---

### `model/` — Saved Model Directory

| Property | Details |
|----------|---------|
| **What it stores** | Serialised model weights, hyperparameters, and training metadata |
| **How to use** | Pass `model_path='outputs/model/'` to `normative.predict()` to apply the model to new data |

**Interpretation:** Contains everything needed to make predictions on a new dataset without retraining. Always save this directory if you plan to apply the normative model to new subjects.

---

## Interpreting Z-scores

The Z-score is the core output of normative modeling. It answers: *"How many standard deviations away from normal is this person?"*

### What Z = 0 means

A Z-score of 0 means the subject is exactly at the normative mean for their age and sex — perfectly "typical" according to the model.

### Common thresholds

| Threshold | Percentile | Interpretation |
|-----------|-----------|----------------|
| Z = 0 | 50th | Normative mean |
| \|Z\| > 1.0 | ~16th / 84th | Mildly atypical |
| \|Z\| > 1.65 | ~5th / 95th | Noteworthy deviation |
| \|Z\| > 1.96 | ~2.5th / 97.5th | Commonly used clinical threshold |
| \|Z\| > 2.58 | ~0.5th / 99.5th | Strong deviation |

The threshold `|Z| > 1.96` (approximately 2.5th or 97.5th centile) is most widely used in the normative modeling literature (e.g. Marquand et al. 2016, 2019).

### Positive vs negative deviations

| Direction | Z value | Clinical meaning (example: cortical thickness) |
|-----------|---------|-----------------------------------------------|
| Positive deviation | Z >> 0 | Brain feature is *larger* than expected — e.g. unusually thick cortex |
| Negative deviation | Z << 0 | Brain feature is *smaller* than expected — e.g. unusually thin cortex, associated with neurodegeneration or psychiatric conditions |

The **direction** matters as much as the magnitude. Some conditions (e.g. schizophrenia, Alzheimer's) show predominantly negative deviations in cortical thickness, while others (e.g. focal cortical dysplasia) produce positive deviations.

### Group-level summary

While Z-scores are computed per subject, you can summarise across a patient group:
- **Overlap statistic**: fraction of patients with |Z| > 1.96 in each region
- **Mean Z per region**: plotted as a deviation map across brain parcels
- **Normative distance**: Euclidean norm of the subject's Z-score vector across all features

---

## Useful Resources

- [PCNtoolkit documentation](https://pcntoolkit.readthedocs.io)
- Marquand et al. (2016) *Psychol Med* — original normative modeling framework
- Marquand et al. (2019) *Biol Psychiatry* — extension to lifespan and clinical applications
- Rutherford et al. (2022) *eLife* — PCNtoolkit paper and benchmarks
