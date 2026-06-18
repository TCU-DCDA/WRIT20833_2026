# WRIT 20833 — Course Schedule (Summer 2026)

**Mon Jul 6 – Fri Jul 31, 2026 · Monday–Friday · 2 hours/day · online synchronous**

A day-at-a-glance schedule derived from `SYLLABUS_2026.md` (see the syllabus for full assignment
descriptions, the ungrading policy, and the three reflection / four discussion prompts). Each day:
**Lecture** = the ~25-min concept / critical frame · **Coding** = the ~70-min hands-on block, labeled by
mode and linked to its notebook where one exists.

*Coding modes:* **Code-along** = instructor-led, live-typed notebook · **Lab** = guided hands-on with a
handout/demo · **Workshop** = students build with their own data · **Work session** = independent
homework/capstone time with support · **Presentations** = student showcase.

*Key:* **HW** = homework · **R** = self-reflection · **D** = D2L threaded discussion · ML = mini-lecture.
Notebook links are relative paths into this repo (`notebooks/codeAlongs/`, `notebooks/homework/`,
`materials/stylometry/`).

---

### Week 1 (Jul 6–10) — Python foundations: "code is not neutral"
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 7/6** (1) | Humanities & Coding · Connotations & Code | **Code-along** → [Setup + Variables & data types](notebooks/codeAlongs/WRIT20833_Variables_DataTypes_2026.ipynb) | D1 opens |
| **Tue 7/7** (2) | — | **Code-along** → [Strings & string methods](notebooks/codeAlongs/WRIT20833_String_Methods_2026.ipynb) | — |
| **Wed 7/8** (3) | Classification Logic | **Code-along** → [Comparisons, conditionals & booleans](notebooks/codeAlongs/WRIT20833_Lists_Loops_Conditionals_2026.ipynb) | **R1 due** · D1 post |
| **Thu 7/9** (4) | Collective Memory | **Code-along** → [Lists & loops](notebooks/codeAlongs/WRIT20833_Lists_Loops_Conditionals_2026.ipynb) | — |
| **Fri 7/10** (5) | — (recap) | **Code-along** → [Functions & dictionaries](notebooks/codeAlongs/WRIT20833_Dictionaries_Functions_2026.ipynb) + recap | **HW1 assigned** · D1 replies |

### Week 2 (Jul 13–17) — From text to data: ethics, pandas, AI
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 7/13** (6) | Data as evidence | **Code-along** → [Term frequency ("Meaningful Words")](notebooks/codeAlongs/WRIT20833_Term_Frequency_2026.ipynb) + HW1 debrief | **HW1 due** · **HW2 assigned** · D2 opens |
| **Tue 7/14** (7) | AI Agency | **Lab** → Reading & improving AI code + stylometry seed: [Reading for the Seams](materials/stylometry/Reading_for_the_Seams.md) (close reading) | — |
| **Wed 7/15** (8) | Data Archaeology | **Code-along** → [Found data + collection ethics (pandas 01 + scraping)](notebooks/codeAlongs/WRIT20833_Pandas_01_Found_Data_2026.ipynb) | D2 post |
| **Thu 7/16** (9) | — | **Code-along** → [Data cleaning (pandas 02)](notebooks/codeAlongs/WRIT20833_Pandas_02_Cleaning_2026.ipynb) | — |
| **Fri 7/17** (10) | — | **Workshop** → collect & clean **your** cultural dataset (apply Pandas 01–02) | **HW2 due** · D2 replies |

### Week 3 (Jul 20–24) — Computational text analysis
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 7/20** (11) | Quantifying connotation (callback to Connotations & Code) | **Code-along** → [Sentiment with VADER](notebooks/codeAlongs/WRIT20833_VADER_Sentiment_2026.ipynb) | **R2 due (midterm)** · D3 opens |
| **Tue 7/21** (12) | Close vs. distant reading | **Code-along** → [VADER deep dive](notebooks/codeAlongs/WRIT20833_VADER_Sentiment_2026.ipynb) (same notebook, Part 4–5) | **HW3 assigned** |
| **Wed 7/22** (13) | Predictions on the record | **Work session** → HW3 (frequency + sentiment on your data) | D3 post |
| **Thu 7/23** (14) | NLP & Topic Modeling | **Code-along** → [Topic modeling intro (Gensim LDA)](notebooks/codeAlongs/WRIT20833_Topic_Modeling_Gensim_2026.ipynb) | — |
| **Fri 7/24** (15) | — | **Code-along** → [Topic modeling deep · `num_topics` · limits](notebooks/codeAlongs/WRIT20833_Topic_Modeling_Gensim_2026.ipynb) (same notebook, Part 2–3) | **HW3 due** · **HW4 assigned** · D3 replies |

### Week 4 (Jul 27–31) — Integration & data-driven opinions (capstone)
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 7/27** (16) | Integration (close → distant → close) | **Lab** → Integration demo (frequency + sentiment + topics) via the [HW4 notebook](notebooks/homework/WRIT20833_HW4_2026.ipynb) + short [stylometry demo](materials/stylometry/WRIT20833_Stylometry_Reading_Seams_2026.ipynb) | **[Capstone](CAPSTONE_2026.md) proposal due** · D4 opens |
| **Tue 7/28** (17) | Going Public | **Work session** → Validation · "being wrong as learning" · capstone framing | **HW4 due** · D4 post |
| **Wed 7/29** (18) | — | **Work session** → Capstone work session 1 (cultural dataset **or** stylometry) | — |
| **Thu 7/30** (19) | — | **Work session** → Capstone work session 2 + peer review | D4 replies |
| **Fri 7/31** (20) | — (wrap) | **Presentations** → Capstone presentations + wrap | **[Capstone](CAPSTONE_2026.md) due** · **R3 due (final self-evaluation)** |

---

*Notes on the notebooks:* one code-along can span two sessions — **Days 3–4** share the
[Lists, Loops & Conditionals](notebooks/codeAlongs/WRIT20833_Lists_Loops_Conditionals_2026.ipynb) notebook,
**Days 11–12** the [VADER](notebooks/codeAlongs/WRIT20833_VADER_Sentiment_2026.ipynb) notebook, and
**Days 14–15** the [Topic Modeling](notebooks/codeAlongs/WRIT20833_Topic_Modeling_Gensim_2026.ipynb)
notebook. Every coding day now links a real notebook — the term-frequency code-along (Day 6) was
authored fresh (no F25 source existed) and leads directly into HW2.

*Notes on lectures:* "—" in **Lecture** marks recap / workshop / work-session days with no formal
mini-lecture (Day 2 included — **"Sacred Boundaries" was cut**: its privacy/collection-ethics core
lives in the Day-8 Data Archaeology lecture, and its noumena-limit point in the Day-1 opener.
The **"Going Public"** lecture now anchors **Day 17** (analysis → public argument → the capstone);
**"Code as Rhetoric"** was harvested into the Connotations & Code (Day 1) and Going Public lectures rather
than built as its own deck (its HTML/CSS half belongs to the cut web-dev arc). The schedule will be
adjusted to the class's pace; changes announced in class and on D2L.
