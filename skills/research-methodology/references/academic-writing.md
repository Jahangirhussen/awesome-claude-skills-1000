# Academic Writing & Publishing

Goal: turn a finished (or nearly finished) study into a paper a reviewer will accept, in the right venue.

## 1. Standard paper structure (CS/AI/ML)

| Section | Purpose | Typical length |
|---|---|---|
| Abstract | One paragraph: problem, method, key result | 150–250 words |
| Introduction | Motivate the problem, state the gap, state the contribution explicitly | 0.75–1 page |
| Related Work | Position your work against prior work — argue, don't just list | 0.5–1 page |
| Methodology | Enough detail that someone could reproduce it | 1–2 pages |
| Experiments/Results | Setup, then results with tables/figures | 1–2 pages |
| Discussion/Analysis | Why the results look the way they do, error analysis, limitations | 0.5–1 page |
| Conclusion | Restate contribution, note future work | 2–4 sentences |

Conference papers (ACL, NeurIPS-style) are usually 4–8 pages excluding references; journal papers (Scopus/Q1 targets) run longer, often 10–20 pages, with more thorough related work and discussion.

## 2. Writing the introduction (often the hardest part)

A reliable four-move structure:

1. **Context** — one or two sentences on why the general area matters.
2. **Gap** — what's missing in existing work (this is where the literature review pays off).
3. **Contribution** — state explicitly, often as a bulleted list: "In this work, we (1) ..., (2) ..., (3) ..."
4. **Results preview** — one sentence on the headline result, so the reader knows what's coming.

Write the introduction *last* or revise it heavily after the results are in — it's easier to motivate a paper once you know exactly what it proves.

## 3. Style and clarity

- Prefer short, direct sentences over long ones with multiple subordinate clauses — this isn't a fiction genre where complexity earns points.
- Say "we propose X" not "it is proposed that X" — active voice is standard in most CS venues now.
- Every claim in the abstract/intro must be backed by a result later in the paper — don't promise what the experiments don't show.
- Define every acronym at first use, even common ones in your subfield (reviewers may be adjacent, not identical, experts).
- Avoid hedge-stacking ("it may possibly potentially suggest") — pick one hedge word if the claim is uncertain, not three.

## 4. Citations

- Cite the original source of an idea, not just a survey that mentions it, when possible.
- Match the venue's required style — IEEE (numbered, e.g. [1]) is common in engineering venues; ACL/NLP venues typically use author-year (e.g. Devlin et al., 2019); check the submission template rather than assuming.
- Every citation in the text must appear in the reference list and vice versa — reference managers (see `tools-workflow.md`) handle this automatically and are worth setting up early.

## 5. Choosing a venue

- Match scope: a Bangla NLP dataset paper fits better at a workshop (e.g. a low-resource languages workshop at ACL/EMNLP) or a regional venue than a top general ML conference.
- For journal targets (especially if a Scopus-indexed or Q1 journal matters, e.g. for scholarship/grad applications), check the journal's scope and recent issues — reviewers reject fast if the paper is a poor topical fit, regardless of quality.
- Check indexing status directly on Scopus/Web of Science before committing — journal websites sometimes advertise indexing that's outdated or predatory-adjacent; verify independently.
- Note the venue's page limit and citation style *before* writing — restructuring a paper to fit a stricter limit late is painful.

## 6. Handling review and revision

- Reviewers rejecting or requesting major revisions is normal, not a signal the work is bad — most published papers went through at least one revision cycle.
- Respond to every reviewer point explicitly in a rebuttal/response letter, even ones you disagree with — explain your reasoning rather than ignoring the comment.
- If multiple reviewers flag the same weakness, treat it as real even if you think it's a misunderstanding — it means the paper didn't communicate that part clearly.

## 7. Thesis-specific notes

If this is for a thesis rather than a conference/journal paper:

- Thesis chapters can absorb more background/tutorial material than a conference paper — the audience (committee) may not be narrow specialists in every sub-area.
- A thesis usually needs a longer, standalone related-work chapter, not just a compressed related-work section.
- Keep a running "contributions" list from the start — most theses restate contributions in both the introduction and conclusion, and it's easier to write both together.
