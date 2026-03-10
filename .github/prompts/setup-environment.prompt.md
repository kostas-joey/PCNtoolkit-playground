---
description: "Generate a conda environment.yml and requirements.txt for PCNtoolkit neuroimaging normative modeling projects"
name: "Setup PCNtoolkit Environment"
agent: "agent"
---

Generate the environment setup files for this PCNtoolkit playground repository.

1. Create a `environment.yml` conda environment file that includes:
   - Python 3.10
   - pcntoolkit (latest stable)
   - numpy, scipy, pandas, matplotlib, seaborn
   - scikit-learn
   - torch (CPU version unless GPU is detected)
   - jupyter, ipykernel
   - nibabel, nilearn (for neuroimaging data)

2. Create a `requirements.txt` (pip-compatible) with the same dependencies and pinned versions where stability matters.

3. Create a short `SETUP.md` with step-by-step instructions for:
   - Creating the conda environment
   - Installing the packages
   - Registering the kernel for Jupyter
   - Verifying the installation with a quick import check snippet

Keep the setup beginner-friendly and note any common installation pitfalls (e.g., torch/CUDA conflicts).
