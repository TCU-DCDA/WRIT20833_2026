# Course images

## `noumena_to_wisdom_pipeline.png` — the epistemological spine

![noumena to wisdom pipeline](noumena_to_wisdom_pipeline.png)

An 8-stage pipeline that names the journey the whole course enacts:

> **NOUMENA → PHENOMENA → RAW DATA → STRUCTURED DATA → ANALYZED DATA → INSIGHT → KNOWLEDGE → WISDOM**

It extends the classic **DIKW** pyramid (Data → Information → Knowledge → Wisdom) *backward*
into epistemology: before "raw data" there is the *phenomenal appearance*, and before that the
*noumenal* thing-in-itself (Kant). The course's recurring move — "the score is not the sentiment,"
"a topic is a pattern the model proposes, not a fact the data contains" — is the **left half** of
this diagram; "earned insight over clean code" (ungrading) is the **right half**.

**Provenance:** ported from F25 (`WRIT20833_2025/_development/textbook/images/20833_noumena_wisdom_F25.png`),
where it was an **orphaned** textbook asset — built but never wired into any lecture, notebook, or
homework. Don't let that happen again: this graphic is meant to be **taught**.

### The core argument: every arrow is an occasion for human bias
Each transition is a site where a human choice enters — and bias is **constitutive and cumulative,
not "contaminating."** There is no clean origin to pollute: the phenomenon is *already* an
interpretation (we never hold the noumenon), and every step compounds the choices before it. You
can't "fix" a result back to truth; you can only make the choices **visible and accountable** — which
is exactly what the `#comments` requirement and the three reflections train.

Every arrow already has a home in the 2026 materials:

| Transition | The choice that enters | Where the course already shows it |
|---|---|---|
| Noumena → Phenomena | What is even *noticed* as worth studying | Choosing *this* law / *these* commenters at all; ML0 "the mess" |
| Phenomena → Raw data | Collection: what's captured vs. excluded | Day 8 Data Archaeology + scraping ethics; the wrap-fragments ("Of Texas") are capture artifacts; dedup/source choices |
| Raw → Structured data | Cleaning, tokenizing, what counts as a "row" | HW2 stopwords (authored deletion), `\W+` split; HW3 "clean *but keep* punctuation"; the 123-vs-93 decision |
| Structured → Analyzed data | Method + parameters | HW3 VADER lexicon + the 0.05 cutoff; HW4 `num_topics`, `random_state` |
| Analyzed → Insight | What we read into the output | HW4 A5 "*human* names the topics"; the sarcasm misread; B3/B4 |
| Insight → Knowledge | Generalizing; confirmation bias | HW4 B4 "name where the tools mislead"; "being wrong as learning" (Day 17) |
| Knowledge → Wisdom | Values — what we *do* with it | The capstone data-driven-opinion essay; ML9 "Going Public" |

### Intended use
The unifying through-line: introduce at **ML0 / Day 1** ("what can computation know?"), then **call
back at each unit** — "we're at the raw→structured arrow now; watch where the bias enters." Turns
seven separate "code is not neutral" reminders into one sustained walk down a single diagram. The
**close-vs-distant-reading hinge (Day 7)** is the other natural anchor.

*Status: graphic ported (2026-06); framing text + lecture wiring still to be authored. See WORKLOG.*
