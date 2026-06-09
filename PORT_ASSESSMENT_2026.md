# WRIT 20833 — 2026 Readiness & Port Assessment

**Course:** WRIT 20833, "Intro to Coding in the Humanities" / "When Coding Meets Culture"
**2026 offering:** 4 weeks, async, **start date 2026-07-06**
**Assessment date:** 2026-06-09 (27 days to start)
**Repo assessed:** `TCU-DCDA/WRIT20833_2026` (this repo)
**Reference offering:** Fall 2025 (`TCU-DCDA/WRIT20833_2025`), **16-week** semester

> **Sourcing note:** This revision incorporates the authoritative `WRIT20833_2025`
> repository README (fetched via raw.githubusercontent.com on 2026-06-09), which
> corrects several facts from the first draft (course is **16 weeks**, full asset
> inventory, and resolution of the HW2 / data-scraper gaps).

---

## TL;DR

The 2026 repo looks nearly empty (one notebook), but the course is **not** being built
from scratch. A mature, classroom-tested **16-week** Fall 2025 offering exists in
sibling repos. The 2026 work is therefore **scope-selection + port**, not content
creation.

- **Content creation:** essentially done, and far more extensive than first thought.
- **The binding constraint is curricular, not technical:** fitting a 16-week course
  into 4 weeks is a **4:1 compression** — roughly one of the four semester phases fits,
  or a heavily-thinned through-line. This is an instructor design decision and remains open.
- **Mechanical port is easy and quick.** Achievable for 2026-07-06 — *once the scope is chosen.*

> ⚠️ Assessment only. No porting, content changes, or scheduling decisions have been made.

---

## What exists today

### This repo (`WRIT20833_2026`)
- `notebooks/codeAlongs/WRIT20833_Variables_DataTypes_2026.ipynb` — the only ported unit
  so far (the F25 "Variables & Data Types" worksheet). Polished, executable.

### Sibling repos in `TCU-DCDA`
| Repo | Purpose | State |
|---|---|---|
| `WRIT20833_2025` | Fall 2025 offering (full 16-week course) | Archived, public |
| `WRIT20833` | Course-page website (`gh-pages`) | Active, public |
| `writ20833-textbook` | Course textbook | Active, private |
| `WRIT20833-portfolio-template` | Student portfolio starter | Active, public |
| `WRIT20833-chatbot` | Course chatbot | Active, private |
| `WRIT20833_alt` | "alt 20833 syllabus" | Archived |
| `writ20833_f25-intro-to-github-...` | GitHub Classroom starter | Archived |

---

## F25 course (full 16-week structure, per repo README)

- **Weeks 1–4 — Python Foundations:** variables, data types, string methods, conditionals,
  loops, dictionaries, functions
- **Weeks 5–8 — Text Analysis & Cultural Data:** pandas, ethical data collection,
  sentiment analysis (VADER), topic modeling (Gensim LDA)
- **Weeks 9–12 — Web Development & Portfolio:** HTML/CSS workshop, HW6–8, GitHub Pages
- **Weeks 13–16 — Final Projects & Public Presentation**

**Pedagogy:** four-strand design — (1) Melanie Walsh's *Intro to Cultural Analytics*
(external OER, Python backbone); (2) a 13-part mini-lecture series (critical theory);
(3) tutorials bridging concept↔theme; (4) homework applying skills to student-chosen
cultural datasets. Analytical arc: predictions → computational analysis → data-driven
insight → public portfolio. Ungrading philosophy ("earned insight over clean code").

### Full asset inventory

**Code-alongs (9, `notebooks/codeAlongs/`):**
1. Variables & Data Types — *ported to 2026*
2. String Methods / Conditionals / Loops
3. Lists & Loops (Complete)
4. Dictionaries & Functions
5. Pandas 01 — Found Data Fundamentals
6. Pandas 02 — Data Cleaning & Analysis
7. Instant Data Scraper & Ethics
8. VADER Sentiment Analysis
9. Topic Modeling (Gensim) — *the combined version is the F25-canonical one*

**Exercises (1):** Conditionals (9-5-25)

**Tutorials (4, paired to mini-lectures 1–4):** Digital Boundaries · Classification Logic ·
AI Agency · Collective Memory

**Homework:** HW1 (term frequency) · HW4-1 (term freq + sentiment) ·
HW4-2 (topic modeling + integration) · HW5 (final project proposal) ·
HW6 (HTML portfolio structure) · HW7 (CSS portfolio styling) · HW8 (portfolio deployment)
— *Note: there is **no HW2 or HW3**; numbering jumps 1 → 4. The "HW3-1/3-2 Pandas"
files are code-along practice notebooks, not graded homework.*

**Mini-lectures (13, numbered 0–12):**
0 Humanities & Coding · 1 Connotations & Code · 2 Boundaries · 3 Classification Logic ·
4 AI Agency · 5 Collective Memory · 6 Data Archaeology · 7 NLP & Topic Modeling ·
8 Code as Rhetoric · 9 Public Arguments · 10 GitHub Infrastructure · 11 HTML as Structure ·
12 CSS as Rhetoric

**Final project:** 3 deliverables — research essay + Python notebooks + web portfolio
(HTML/CSS). Proposal (HW5) → Requirements doc → portfolio (HW6–8).

**Also present:** `datasets/`, HTML/CSS workshop (`docs/html_training/`),
"Editing Digital Essay" guide, 100+ lecture images, `_development/` materials.

---

## The central decision: 16 weeks → 4 weeks (4:1)

This is the crux and it is **not** a porting problem — it's curriculum design. Options
the instructor will need to choose among (illustrative, not prescriptive):

- **Foundations-only:** deliver Weeks 1–4 (Python basics) as the whole 4-week course.
  Cleanest fit; drops the text-analysis, web-dev, and portfolio halves.
- **Text-analysis track:** assume minimal Python and run the cultural-analytics arc
  (term frequency → sentiment → topic modeling, HW1/HW4-1/HW4-2). Matches the 2026
  Variables notebook's "When Coding Meets Culture" framing.
- **Thinned through-line:** one compressed week per semester-phase; very aggressive cuts,
  highest workload risk for no-prior-experience grad students in summer.

Whatever the choice, note the **summer async + no-coding-experience** audience makes
workload the dominant risk. The F25 homework load alone (HW1–HW8) cannot fit in 4 weeks.

---

## Port status (once scope is chosen)

**✅ Carry-over-ready (high quality, minimal change):** all 9 code-alongs, 4 tutorials,
HW1/HW4-1/HW4-2, and (if web-dev is in scope) HW5–8 + HTML/CSS workshop.

**⚠️ Mechanical fixes needed before porting:**
- **De-duplicate topic modeling** — F25 canonical is the combined "Gensim" notebook;
  the Part 1 / Part 2 split (provided separately) is a reorganization. Pick one.
- **Hard-coded F25 dates** — e.g., HW4-1 "due Oct 5", HW4-2 "Oct 17" vs "Oct 13"
  (internally inconsistent). All need 2026 dates.
- **Colab badge links** — every notebook points at `WRIT20833`/`WRIT20833-2025`/
  `WRIT20833_2025` paths; repoint to `WRIT20833_2026`. (Note F25 itself mixes hyphen
  and underscore repo names — standardize during port.)
- **HW4-2 dependency-pinning cell** — pins numpy/pandas/scipy/gensim and forces a Colab
  runtime restart; verify against Colab's 2026 default image.

---

## Gaps now CLOSED (vs. first draft)
- ✅ Total unit count: **16 weeks**, 4 phases (was unknown).
- ✅ "HW2 / HW3" mystery: no such graded homework; numbering jumps 1 → 4.
- ✅ Instant Data Scraper lesson: exists (`..._Instant_Data_Scraper_Ethics_F25.ipynb`).
- ✅ Final project / post-HW4 content: HW5 proposal + HW6–8 portfolio + requirements doc.

## Gaps still open
- Official **2026 4-week syllabus/schedule** — does not yet exist; depends on the scope decision above.
- Direct read access to `WRIT20833_2025` from this session (worked around via raw GitHub).

---

## Comparison context: WRIT 20833 vs. MALA 60970

| | MALA 60970 (Web Authoring) | WRIT 20833 (Coding in Humanities) |
|---|---|---|
| Underlying course | Mature planning repo (~85% ready) | Mature, fully built & taught (16-wk F25) |
| 2026 repo state | 2026 content authored in-repo | Nearly empty — port not started |
| Real remaining work | Polish + D2L build (IT-blocked) | **Choose 4-week scope** + port |
| Risk profile | Low (execution only) | Medium–High (4:1 compression decision) |

Neither needs content *invented*. MALA's 2026 deliverable is more assembled in-repo and
already scoped to 4 weeks; WRIT has vastly more battle-tested material but a much larger
compression decision still to make. **Thematic overlap:** WRIT Weeks 9–16 (HTML/CSS
portfolios) parallel MALA's "Web Authoring" subject matter.

---

## Suggested next steps (when ready)
1. **Decide the 4-week scope** (which phase[s], which assignments, what to cut). This unblocks everything else.
2. Mechanical port of the chosen carry-over-ready notebooks into this repo.
3. Global fixes: dates, Colab links, dedup topic modeling, dependency-cell verification.
4. Author a 2026 4-week syllabus/schedule to match the chosen scope.
