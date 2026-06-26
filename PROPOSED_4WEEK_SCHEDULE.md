# PROPOSED — WRIT 20833, Summer 2026: 4-Week (20-Session) Schedule

> **⚠️ SUPERSEDED (2026-06-26).** The July 4-week summer section was **canceled**. The course now runs as an
> **8-week, in-person, MWF fall offering (Oct 19 – Dec 18, 2026; 24 sessions)** — see `COURSE_SCHEDULE_2026.md`
> and `SYLLABUS_2026.md` for the live plan. This document is kept only as the original design rationale
> (F25-asset mappings, scope cuts); its dates, session count, and 5-day pacing no longer apply.

> **Status: DRAFT for instructor review.** Built by sequencing existing Fall 2025
> assets into the 2026 format. Nothing here is finalized; cuts and placements are
> proposals. New content (HW1 rebuild, stylometry exercise) is drafted separately
> in the repo.

**Format:** online **synchronous** · 2 hrs/day × 5 days × 4 weeks ≈ **40 contact hours**
**Start:** 2026-07-06 · **Audience:** undergraduate students (lower-division), no prior coding experience
**Scope chosen:** *Drop the web-dev/portfolio half* — Python foundations + the
cultural-analytics arc (term frequency → sentiment → topic modeling), ending in a
**notebook + short essay capstone**. (The dropped HTML/CSS portfolio half overlaps
MALA 60970 "Web Authoring".)

**Why this fits 40 hrs:** F25 was ~48 contact hours (16 wks × ~3 hrs). At ~40 hrs and
the same synchronous, instructor-led model, F25's session pedagogy (concept → supported
hands-on → application) transfers almost directly; this is re-pacing + a modest trim, not
a 4:1 cut or an async rebuild.

**Daily session shape (2 hrs):** ~25 min concept/mini-lecture → ~70 min live code-along →
~25 min application + share. Homework stays light (students are in class daily).

## Reading spine — building toward Walsh independence
This course is moving to be **self-contained**: the required readings/refreshers are the
course's **own** tutorials, mini-lectures, and code-alongs — *not* assigned chapters from an
outside textbook. Melanie Walsh's *Introduction to Cultural Analytics* is credited as
**inspiration and model** (see `ACKNOWLEDGMENTS.md`), and may be offered as **optional
further reading**, but no graded work should require it.

**Port implication:** several F25 code-alongs and tutorials still open with an
"assumes you've completed Walsh Chapters 4–8" prerequisite block. As each is ported into this
repo, that dependency should be **stripped or replaced** with a pointer to our own prior
session — the same Walsh-independence treatment already applied to HW1.

---

## The 20 sessions

### Week 1 — Python foundations: "code is not neutral"
| Day | Focus | F25 assets | Critical frame |
|----|-------|-----------|----------------|
| 1 | Setup + Variables & Data Types | CA Variables/DataTypes | ML0 Humanities & Coding · ML1 Connotations & Code |
| 2 | Strings & string methods | CA StrMethods + Tutorial 1 Digital Boundaries | ML2 Boundaries |
| 3 | Comparisons, conditionals & booleans | Tutorial 2 Classification Logic (Bellevue data) | ML3 Classification Logic |
| 4 | Lists & loops | CA Lists/Loops + Tutorial 4 Collective Memory | ML5 Collective Memory |
| 5 | Functions & dictionaries + recap | CA Dictionaries/Functions | — → **assign HW1 (rebuilt, Walsh-independent)** |

### Week 2 — From text to data: ethics, pandas, AI
| Day | Focus | F25 assets | Critical frame |
|----|-------|-----------|----------------|
| 6 | HW1 debrief + "Meaningful Words" term frequency | F25 HW1 (term-freq) logic | data as evidence → **assign HW2 (term frequency)** |
| 7 | Reading & improving AI code **+ stylometry SEED (close reading)** | Tutorial 3 AI Agency + `Reading_for_the_Seams` handout + AI-voice PDF | ML4 AI Agency |
| 8 | Found data + collection ethics | CA Pandas 01 + CA Instant Data Scraper | ML6 Data Archaeology (robots.txt / AI-era) |
| 9 | Data cleaning | CA Pandas 02 | — |
| 10 | Workshop: collect & clean **your** cultural dataset | (TenCommandments CSVs as model) | — → sets up HW3 |

### Week 3 — Computational text analysis
| Day | Focus | F25 assets | Critical frame |
|----|-------|-----------|----------------|
| 11 | Sentiment with VADER | CA VADER | quantifying connotation (callback to ML1) |
| 12 | VADER deep · close vs. distant reading | CA VADER | — |
| 13 | HW3 work session (freq + sentiment on own data) | F25 HW4-1 | predictions on the record |
| 14 | Topic modeling intro (Gensim LDA) | CA Topic Modeling | ML7 NLP & Topic Modeling |
| 15 | Topic modeling deep · num_topics · limits | CA Topic Modeling | — → **assign HW4** |

### Week 4 — Integration & data-driven opinions (capstone)
| Day | Focus | F25 assets | Notes |
|----|-------|-----------|-------|
| 16 | Integration: freq + sentiment + topics **+ short stylometry demo** | F25 HW4-2 + stylometry notebook (Part A) | "measure what you close-read on Day 7" — reinforces close→distant→close |
| 17 | "Being wrong as learning" · validation · capstone framing | F25 HW4-2 reflection | frames the **stylometry capstone option** |
| 18 | Capstone work session 1 | student work | two tracks: (a) cultural dataset, or (b) **stylometry** corpus |
| 19 | Capstone work session 2 + peer review | student work | — |
| 20 | Capstone presentations + wrap | — | — |

---

## Anchor assignments (2026 numbering; F25 equivalents in the *F25 assets* column)
*Mapping: 2026 HW1 = F25 HW2 · HW2 = F25 HW1 · HW3 = F25 HW4-1 · HW4 = F25 HW4-2.*
- **HW1** — comparisons/conditionals/lists/loops (rebuilt, Walsh-independent) — end of Wk1
- **HW2** — term frequency — Wk2
- **HW3** — term frequency + sentiment — Wk3
- **HW4** — topic modeling + integration — Wk4
- **Capstone** — notebook analysis of own cultural dataset **or** stylometry corpus, + short
  data-driven-opinion essay (replaces F25's HW5–8 web portfolio)

## Stylometry placement (resolves "why Day 7?")
Only the **close-reading half** has its prerequisites met at Day 7 (zero code, rides the
AI Agency theme) — it produces a *prediction*. The **computational half** needs term
frequency + visualization + the distant-reading frame (not until Week 3) and works best as
the synthesis/capstone move — so it lands in Week 4. Day 7 = prediction; Week 4 = test.

## Cut from F25 (this scope)
HTML/CSS workshop · HW6–8 web portfolio · mini-lectures 10–12 (GitHub/HTML/CSS) ·
F25's API/JSON week. Final web portfolio → replaced by notebook + essay capstone.

## Risks / watch-items
1. **Week 1 is tightest** — 4 F25 foundation weeks → 5 days. Lean on live support + office hours; keep nightly practice short.
2. **Topic-modeling install** — the F25 HW4-2 pinned-deps + runtime-restart cell must be tested on Colab's 2026 image before Day 14.
3. **Daily homework load** — keep light; students are in live class 2 hrs/day.
4. **Dropped foundations** (dicts/functions compressed to one day; no API/JSON) — fine for this scope; revisit if a future term wants the full Python base.

## Open decisions
- Confirm scope (this draft = "drop portfolio half"; alternatives: full-arc-tightened, foundations-only).
- Whether AI Agency (Day 7) keeps its slot vs. more foundations practice.
- Capstone essay length/weight to match WRIT writing-course expectations.
