# Course data — WRIT 20833 (2026)

Small, ready-to-run corpora for the homework notebooks. Each is plain UTF-8 text so it
can be loaded with `open()` (no pandas required) in the pre-pandas weeks. Each comment collection
has its own folder (`ten_commandments/` for now); more may be added later in the term.

## Files

### `ten_commandments/tc_youtube_comments.txt` — the public's voice
**93 YouTube comments, stored as 123 rows** (2,235 words), reacting to the 2025 **Texas Ten
Commandments-in-schools** law. Source: the Fall-2025
[`TenCommandmentsTX/20833_CBS1_youtube_F25.csv`](https://github.com/TCU-DCDA/WRIT20833_2025/blob/main/datasets/TenCommandmentsTX/20833_CBS1_youtube_F25.csv),
an Instant Data Scraper export of the comments under one TV-news video on YouTube: CBS News,
["Court blocks Texas law requiring public classrooms to display Ten Commandments"](https://www.youtube.com/watch?v=qr_rZWbGhzI)
(Aug 20, 2025), on the federal ruling that blocked the law in some districts. Scraped between that
date and 2025-09-19, when the CSV was committed; many comments react to the judge as much as the law.
Vernacular, contemporary, real social media.

**How 143 scraped records became 123 rows** (reproducible from the CSV):
1. Keep the `comments` text column. Of 143 records, 22 are blank and 28 repeat a comment already
   kept, which leaves **93 distinct comment texts**. (Checked against the live video, 2026-10-18:
   "Of Texas" is a real standalone comment, not a scraper break — the "…already ubiquitous" comment is
   whole in its own record. Whether the standalone "The" is a one-word comment or a fragment can't be
   told from the CSV.)
2. Split each comment at its line breaks and strip whitespace. 82 comments are one line; the other
   11 ran over 2–10 lines and became 41 rows. That gives **123 rows**, in the original order.

**What a row is.** A row is one line of comment text: usually a whole comment, but 41 rows are
pieces of a longer one. A single long comment therefore counts as several rows when you score or
topic-model rows. The 93 comments and the 123 rows contain exactly the same words, so word counts
(HW2, the ML0/ML1 "commandments" figures) are unaffected. The export has **no author or date
fields**: how many people wrote these comments, and when they posted, are unknown. Don't write
"123 people" or "123 commenters."

> Both numbers are right, about different things: **93 comments, 123 rows**. The count has been
> "corrected" from one to the other twice before without checking the source. Use whichever
> matches what you are counting.

*Two data-quality warts, both deliberate and both load-bearing:* the file is **132 physical lines** —
123 rows plus 9 stray blank lines (every notebook loader filters with `if line.strip()`, so all
four homeworks see 123 rows); there are very short rows, some tiny whole comments ("Of Texas";
"The" may be one, or a fragment) and some made by the line-break split ("But i do and or have."). Harmless for HW2's whole-file word count. In **HW4** two rows (`"The"` and
`"But i do and or have."`) reduce to **zero tokens** after stopword removal and are filed under topic
`-1` — that is exactly the case HW4 **A3** asks students to predict and **B2** asks them to spot in the
chart, so **do not "clean" these away** without rewriting those exercises.

### `us_constitution.txt` — the document the public invokes
The U.S. Constitution **as signed in 1787** (Preamble through Article VII and the signatures), ~4,550 words: **no Bill of Rights or later amendments.** Its only mention of faith is Article VI's "no religious Test"; *religion* enters with the First Amendment (1791), so HW2 B3 lists it among the words the text never uses, and the HW2 prompt asks students to notice why. Public domain,
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
`load_text("<path>")` checks the local dir and `notebooks/data/`, then falls back to
downloading from `raw.githubusercontent.com/TCU-DCDA/WRIT20833_2026/main/notebooks/data/`. The path
includes the folder for a collection, e.g. `load_text("ten_commandments/tc_youtube_comments.txt")`;
`us_constitution.txt` sits at the top level. (HW3 and HW4 load the comments the same way, by path.)
**Verified live on `main` (2026-10-19, after the move to `ten_commandments/`):** both corpora return
HTTP 200 anonymously at their raw-GitHub addresses, and HW2, HW3, and HW4's setup cells load all 123 rows
by download alone (no local copy), so the Colab badge path works out of the box for students.
