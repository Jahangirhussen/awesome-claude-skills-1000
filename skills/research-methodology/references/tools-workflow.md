# Research Tools & Workflow

Goal: the plumbing that keeps a research project organized, reproducible, and shareable — set this up early, not after things get messy.

## 1. Reference management

- **Zotero** (free, open-source) — browser extension saves papers with one click, auto-generates citations in any style, syncs across devices. Best default choice.
- **Mendeley** — similar feature set, owned by Elsevier; fine if already in that ecosystem.
- Either way: install the browser connector immediately when starting a literature review, so every paper opened gets saved with metadata instead of living as an unsorted PDF.
- Tag papers by theme/project as you save them — this is what turns the tool into a real literature review aid instead of just storage.

## 2. Writing

- **Overleaf** — cloud LaTeX editor, the de facto standard for CS/ML paper writing. Most conferences (ACL, NeurIPS, IEEE) provide official LaTeX templates importable directly into Overleaf.
- LaTeX is worth learning if targeting conferences/journals regularly — formatting, equations, and citations (via BibTeX/BibLaTeX) are far less painful than in Word once the initial learning curve is past.
- For early drafts or thesis chapters with heavy collaborator review, Google Docs (or Word) can be faster for comment/track-changes workflows — convert to LaTeX for final formatting.

## 3. Experiment tracking (ML/NLP specific)

- **Weights & Biases (wandb)** or **MLflow** — log every run's hyperparameters, metrics, and loss curves automatically. Essential once running more than a handful of experiments, since "which config produced this number" becomes impossible to track manually otherwise.
- **Kaggle notebooks / Colab** — fine for exploration, but export or version key notebooks (don't rely on notebook history alone) once results are being reported in a paper.
- Keep a simple results log (spreadsheet or markdown table) mapping experiment name → config → key metric, even alongside a proper tracker — makes writing the results section much faster.

## 4. Version control

- Use **Git + GitHub** for all research code, even solo projects — commit history is itself a record of what changed and when, useful when writing up the methodology.
- A clean repo structure helps reproducibility and is often expected for supplementary material:
  ```
  project/
  ├── data/           (or a script to download it — avoid committing large files)
  ├── src/             training/eval code
  ├── notebooks/       exploration
  ├── results/         logs, output tables/figures
  ├── paper/           LaTeX source (or Overleaf-synced)
  └── README.md        setup + how to reproduce
  ```
- Tag the exact commit used to produce the paper's reported results — makes "reproduce this number" trivial later.

## 5. Project/task management

- For a solo project, a simple Notion page or even a markdown TODO file tracking phases (lit review → design → experiments → writing) is usually enough — no need for heavyweight tools.
- For a project with a supervisor/co-authors, a shared doc or Trello board for tracking open questions and next steps avoids status updates getting lost in chat.

## 6. Dataset hosting/sharing

- **HuggingFace Datasets** or **Kaggle Datasets** — good default for making a new dataset (e.g. a Bangla NLP corpus) publicly accessible and citable.
- Include a datasheet/README documenting collection method, licensing, and intended use — increasingly expected by reviewers for dataset papers.
- If the dataset can't be fully released (privacy, licensing), release a sample plus the collection/annotation code so the pipeline is still reproducible.

## 7. Minimal setup for a new project (do this on day one)

1. Create a GitHub repo with the structure above.
2. Set up Zotero (or chosen reference manager) with a project-specific collection/tag.
3. Create an Overleaf project from the target venue's template (even if the venue isn't finalized — a generic template works for drafting).
4. If running ML experiments, connect wandb/MLflow before the first real experiment run, not after 20 untracked runs.
