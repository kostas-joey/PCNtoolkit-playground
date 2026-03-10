---
description: "Generate a comprehensive README.md for a PCNtoolkit playground repository by scanning existing notebooks, scripts, and data"
name: "Generate README"
agent: "agent"
---

Generate a `README.md` for this PCNtoolkit playground repository.

Scan the workspace for:
- All `.ipynb` files in `notebooks/`
- All `.py` files in `scripts/`
- Any `.md` files in `docs/`
- The `environment.yml` or `requirements.txt` if present

Then write a README with these sections:

## 1. Header
- Project title: **PCNtoolkit Playground**
- One-sentence description of what normative modeling is and what this repo demonstrates.
- Badges (if applicable): Python version, license.

## 2. Overview
2–3 paragraphs explaining:
- What PCNtoolkit is and linking to the official docs (https://pcntoolkit.readthedocs.io)
- What this playground repo is for (learning, experimentation, tutorials)
- Who the target audience is (researchers, students, clinicians)

## 3. Repository Structure
A tree of the repo's folders and files with a one-line description of each.

## 4. Getting Started
Step-by-step instructions to:
1. Clone the repo
2. Set up the environment (refer to `SETUP.md` or `environment.yml`)
3. Launch Jupyter and open the first notebook

## 5. Notebooks
A table listing each notebook with its filename, purpose, and estimated run time.

## 6. Scripts
A table listing each script with its filename and usage example.

## 7. References
- The PCNtoolkit paper (Marquand et al. 2016, and the 2021 update)
- Link to the official PCNtoolkit GitHub

Keep the tone friendly and educational. Use clear headings and minimal jargon.
