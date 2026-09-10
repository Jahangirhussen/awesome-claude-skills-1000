# Literature Review

Goal: know the field well enough to say precisely what's new about your work, and prove no one has already done it.

## 1. Where to search

Don't rely on one source — each index covers the field differently.

- **Google Scholar** — broadest coverage, good starting point, includes citation counts.
- **Semantic Scholar** — better for finding influential papers and "cited by" graphs; has a decent TL;DR feature.
- **arXiv** — preprints, essential for ML/AI where formal publication lags 6–12 months behind the actual state of the art.
- **Papers With Code** — for ML specifically: leaderboards per task/dataset, linked code repos. Best way to find current SOTA fast.
- **ACL Anthology** — the primary index for NLP papers (ACL, EMNLP, NAACL, LREC). For Bangla/low-resource NLP, this catches papers Google Scholar under-indexes.
- **IEEE Xplore / ACM Digital Library** — for CS more broadly, especially systems and applied work.
- **Scopus / Web of Science** — use these specifically to check a journal's indexing status before submitting, not just for searching.

## 2. Search strategy

- Start broad with 2–3 keyword combinations, then narrow based on what surfaces (e.g. "Bangla text classification" → "Bangla tense classification deep learning").
- **Snowballing**: once you find one strong, relevant paper, do two passes —
  - *Backward*: check its references for earlier foundational work.
  - *Forward*: use "Cited by" (Google Scholar/Semantic Scholar) to find newer work building on it.
- Filter by recency deliberately: for a fast-moving ML subfield, papers older than ~3 years may already be superseded — note this but don't ignore foundational/classic papers that are still the standard baseline.
- Track your exact search queries somewhere (a plain note is fine) — reviewers and your future self will ask "did you check X" and you'll want to answer precisely.

## 3. Organizing what you find

Don't let this become a folder of 40 unread PDFs. For every paper worth keeping, extract:

- **Citation** (authors, year, venue)
- **Problem** they addressed
- **Method** in one or two sentences
- **Dataset/evaluation** used
- **Result** (the number that matters)
- **Relevance** — how it connects to your work (baseline? related method? different domain, same technique?)

Use `assets/lit-review-tracker-template.csv` as a starting structure, or a dedicated reference manager (see `tools-workflow.md`) if the project has 50+ sources.

## 4. From reading list to research gap

After collecting 15–30 relevant papers, synthesize rather than just list:

- Group papers by approach/theme, not by chronological order you read them.
- For each group, write one sentence: "these papers all do X but assume Y."
- The gap you're looking for is usually one of: an untested domain/language, an unaddressed failure mode, a missing comparison, or a method that hasn't been combined with another.
- Write the gap as a claim you intend to test — this becomes the seed of the research question in `research-design.md`.

## 5. Common mistakes

- Treating the lit review as a one-time step done before writing — in practice it continues throughout the project as the question sharpens.
- Only searching for papers that support the chosen approach (confirmation bias) — deliberately search for papers that might contradict or already solve the problem.
- Citing a paper without having actually read past the abstract — this shows in the writing and is easy for reviewers to catch.
- No related-work synthesis, just a list — a related work section should argue a position ("prior work does X; we differ by Y"), not just summarize each paper in a paragraph.
