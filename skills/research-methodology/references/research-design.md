# Research Design & Methodology

Goal: turn a research gap into a study that actually proves something, with results a reviewer can trust.

## 1. Formulating the research question

A good research question is specific and falsifiable — someone should be able to look at your results and say clearly whether it was answered.

- Weak: "Can deep learning help with Bangla NLP?" (too broad, not falsifiable)
- Better: "Does a fine-tuned transformer outperform an LSTM baseline on Bangla tense classification, and by how much?"

Turn it into a hypothesis if possible: "We hypothesize that [method] improves [metric] over [baseline] on [dataset/task] because [reasoning]." This forces you to name the comparison up front.

## 2. Choosing the type of study

- **Dataset/benchmark paper**: contribution is the dataset itself (e.g. a new Bangla MRC corpus). Rigor is about annotation quality, not modeling novelty.
- **Method paper**: contribution is a new technique, evaluated against strong baselines on existing or new data.
- **Empirical/analysis paper**: contribution is a systematic study of an existing phenomenon (e.g. "how do LLMs fail on low-resource languages") — rigor is about breadth and controls, not necessarily a new method.
- **Applied/systems paper**: contribution is a working system solving a practical problem — rigor is about real-world evaluation, not just benchmark numbers.

Know which one you're writing before designing the experiment — it changes what "success" looks like.

## 3. Designing the experiment (ML/NLP specific)

- **Data splits**: fixed train/validation/test split, decided *before* looking at test performance. Never tune hyperparameters against the test set — that's leakage, and reviewers check for it.
- **Baselines**: always include at least one simple baseline (e.g. majority class, TF-IDF + logistic regression) alongside the strongest recent method you're comparing against. A win only against weak baselines isn't a convincing result.
- **Metrics**: pick metrics that match the task — accuracy alone is misleading on imbalanced classes; use F1/precision/recall, or task-specific metrics (BLEU/ROUGE for generation, exact match/F1 for QA/MRC).
- **Statistical significance**: for close results, run multiple seeds and report mean ± std, or a significance test (e.g. paired bootstrap) — a 0.5-point improvement on one run is not a finding.
- **Ablation studies**: remove or vary one component at a time to show *which part* of your method drives the improvement. Reviewers will ask for this if it's missing.
- **Error analysis**: look at actual failure cases, not just aggregate metrics — this is often what makes a paper's discussion section interesting instead of just numbers.

## 4. Dataset construction (if building your own, e.g. a Bangla NLP dataset)

- Write annotation guidelines *before* annotating — even a one-page doc defining labels and edge cases.
- If more than one annotator, measure **inter-annotator agreement** (e.g. Cohen's kappa) and report it — this is the single most-checked rigor signal for a new dataset paper.
- Document data source, collection method, and any filtering/cleaning steps — reviewers and future users need to reproduce or trust the pipeline.
- Report basic dataset statistics (size, label distribution, avg length) — always expected in a dataset paper's first table.
- Plan the split (train/val/test) so there's no leakage — e.g. no near-duplicate sentences across splits, no same source document split across train and test.

## 5. Reproducibility checklist

Before calling an experiment "done":

- [ ] Random seeds fixed and reported (or varied deliberately and averaged).
- [ ] Hyperparameters documented (learning rate, batch size, epochs, etc.).
- [ ] Code and (if permitted) data available in a public repo.
- [ ] Environment/library versions noted (a `requirements.txt` or similar).
- [ ] Results table includes enough detail that someone else could plausibly reproduce the number.

## 6. Common pitfalls

- Choosing the metric *after* seeing which one makes results look best — decide metrics before running final experiments.
- Comparing against baselines run with different data preprocessing — keep everything except the variable under test identical.
- Overclaiming: "state of the art" requires actually checking the current leaderboard (Papers With Code), not just beating the one paper you read.
- Skipping ablations because the main result "already looks good" — reviewers will ask why it works, not just that it works.
