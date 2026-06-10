# Course data — WRIT 20833 (2026)

Small, ready-to-run corpora for the homework notebooks. Each is plain UTF-8 text so it
can be loaded with `open()` (no pandas required) in the pre-pandas weeks.

## Files

### `tc_youtube_comments.txt` — the public's voice
93 unique YouTube comments (one per line) reacting to the 2025 **Texas Ten
Commandments-in-schools** law. Cleaned from the Fall-2025 `TenCommandmentsTX/20833_CBS1_youtube_F25.csv`
(Instant Data Scraper export): the comment-text column only, de-duplicated, blanks removed.
~2,300 words. Vernacular, contemporary, real social media.

### `us_constitution.txt` — the document the public invokes
The full U.S. Constitution (Preamble through the amendments), ~4,550 words. Public domain,
sourced from Project Gutenberg eBook #5 with the Gutenberg/transcriber boilerplate stripped
(text begins at "THE CONSTITUTION OF THE UNITED STATES OF AMERICA, 1787").

## Why this pairing (HW2 — term frequency)
The **top comment is literally "how about putting the constitution in classrooms?"** — and
"constitution" recurs through the comments — so students compute term frequency on the
public's argument *and* on the founding text it appeals to. The contrast is vivid:
Constitution → `shall, states, president, congress`; comments → `commandments, religion,
god, children, schools`. Formal vs. vernacular, timeless vs. current. The same comment
corpus is reused for HW3 (sentiment) and is a capstone option.

## How the notebooks load these
`load_text("<filename>")` checks the local dir and `notebooks/data/`, then falls back to
downloading from `raw.githubusercontent.com/TCU-DCDA/WRIT20833_2026/main/notebooks/data/`
(works once this branch is merged to `main`, like the Colab badges).
