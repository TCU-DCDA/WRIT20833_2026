# Course data — WRIT 20833 (2026)

Small, ready-to-run corpora for the homework notebooks. Each is plain UTF-8 text so it
can be loaded with `open()` (no pandas required) in the pre-pandas weeks.

## Files

### `tc_youtube_comments.txt` — the public's voice
**123 comments, one per line** (2,235 words), reacting to the 2025 **Texas Ten
Commandments-in-schools** law. Cleaned from the Fall-2025 `TenCommandmentsTX/20833_CBS1_youtube_F25.csv`
(Instant Data Scraper export): the comment-text column only, de-duplicated.
Vernacular, contemporary, real social media.

*Two data-quality warts, both deliberate and both load-bearing:* the file is **132 physical lines** —
123 comments plus 9 stray blank lines (every notebook loader filters with `if line.strip()`, so all
four homeworks see 123 rows); and a few lines are short CSV→txt wrap-fragments, e.g. "Of Texas",
"The". Harmless for HW2's whole-file word count. In **HW4** two rows (`"The"` and
`"But i do and or have."`) reduce to **zero tokens** after stopword removal and are filed under topic
`-1` — that is exactly the case HW4 **A3** asks students to predict and **B2** asks them to spot in the
chart, so **do not "clean" these away** without rewriting those exercises.

### `us_constitution.txt` — the document the public invokes
The full U.S. Constitution (Preamble through the amendments), ~4,550 words. Public domain,
sourced from Project Gutenberg eBook #5 with the Gutenberg/transcriber boilerplate stripped
(text begins at "THE CONSTITUTION OF THE UNITED STATES OF AMERICA, 1787").

## Why this pairing (HW2 — term frequency)
The **top comment is literally "how about putting the constitution in classrooms?"** — and
"constitution" recurs through the comments — so students compute term frequency on the
public's argument *and* on the founding text it appeals to. The contrast is vivid:
Constitution → `shall, states, united, state, president`; comments → `commandments, religion,
ten, god, 10`. (The comments' `ten`/`10` are what HW2 **C1** asks students to weigh as custom
stopwords — filter them and `children, schools, state, people` rise.) Formal vs. vernacular,
timeless vs. current. The same comment corpus is reused for HW3 (sentiment) and HW4 (topics),
and is a capstone option.

## How the notebooks load these
`load_text("<filename>")` checks the local dir and `notebooks/data/`, then falls back to
downloading from `raw.githubusercontent.com/TCU-DCDA/WRIT20833_2026/main/notebooks/data/`.
**Verified live on `main` (2026-09-05):** both corpora and both notebook paths return HTTP 200
anonymously, so the Colab badge path works out of the box for students.
