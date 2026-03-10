# Setup Guide

## Option A — Conda (recommended)

```bash
# 1. Create the environment
conda env create -f environment.yml

# 2. Activate it
conda activate pcntoolkit-playground

# 3. Register the Jupyter kernel
python -m ipykernel install --user --name pcntoolkit-playground --display-name "PCNtoolkit Playground"

# 4. Launch Jupyter
jupyter notebook
```

## Option B — pip (virtualenv)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python -m ipykernel install --user --name pcntoolkit-playground --display-name "PCNtoolkit Playground"
jupyter notebook
```

## Verify Installation

Run this snippet in a Python terminal or notebook cell:

```python
import pcntoolkit
import nibabel
import nilearn
import torch
print("pcntoolkit:", pcntoolkit.__version__)
print("All imports OK")
```

## Common Pitfalls

- **torch / CUDA conflicts**: The default install is CPU-only. If you have a GPU and want CUDA support, replace the `torch` line in `requirements.txt` with the appropriate wheel from https://pytorch.org/get-started/locally/
- **pcntoolkit version**: If `pip install pcntoolkit` fails, try `pip install pcntoolkit --pre` for the latest pre-release.
- **nibabel on Windows**: Requires the `Microsoft C++ Build Tools`. Install from https://visualstudio.microsoft.com/visual-cpp-build-tools/ if you see compiler errors.
