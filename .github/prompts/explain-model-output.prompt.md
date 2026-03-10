---
description: "Explain what each PCNtoolkit output file contains and how to interpret normative modeling evaluation metrics like MSLL, EXPV, SMSE, and Z-scores"
name: "Explain PCNtoolkit Model Output"
agent: "agent"
---

Create a markdown reference document at `docs/output_guide.md` that explains every file produced by `pcntoolkit.normative.estimate()`.

For each file below, provide:
- **What it stores** (data type, shape)
- **How to load it** (Python snippet)
- **How to interpret it** (plain-language explanation, typical value ranges)

Files to cover:
| File | Contents |
|------|----------|
| `yhat.pkl` | Predicted mean of the normative distribution |
| `ys2.pkl` | Predicted variance (uncertainty) |
| `Z.pkl` | Deviation Z-scores per subject per feature |
| `warp_param.pkl` | Warping parameters (if WarpedBLR was used) |
| `MSLL.txt` | Mean Standardized Log Loss |
| `EXPV.txt` | Explained Variance |
| `SMSE.txt` | Standardized Mean Squared Error |
| `RMSE.txt` | Root Mean Squared Error |
| `Rho.txt` | Spearman correlation |
| `pRho.txt` | p-value for Spearman correlation |
| `model/` | Saved model directory |

Also include a section titled **"Interpreting Z-scores"** that explains:
- What Z = 0 means (on the normative mean)
- Thresholds typically used in the literature (|Z| > 1.96, |Z| > 2.58)
- The difference between extreme positive and negative deviations in a clinical context

Keep the tone accessible to someone new to normative modeling.
