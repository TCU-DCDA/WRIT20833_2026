# WRIT 20833 — 2026 Readiness & Port Assessment

**Course:** WRIT 20833, "Intro to Coding in the Humanities" / "When Coding Meets Culture"
**2026 offering:** 4 weeks, **online synchronous** (2 hrs/day × 5 days/wk), **start date 2026-07-06**
*(Sibling course MALA 60970 "Web Authoring" is online **async**; WRIT 20833 is online **live**.)*
**Assessment date:** 2026-06-09 (27 days to start)
**Repo assessed:** `TCU-DCDA/WRIT20833_2026` (this repo)
**Reference offering:** Fall 2025 (`TCU-DCDA/WRIT20833_2025`), **16-week** semester

> **Sourcing note:** This revision incorporates the authoritative `WRIT20833_2025`
> repository — first its README, then a **full clone** (284 files) inspected on
> 2026-06-09 via the allowlisted `github.com`. Corrects several facts from the first
> draft (course is **16 weeks**, full asset inventory, resolution of the HW2 /
> data-scraper gaps) and adds the findings in "Direct repo inspection" below.

---

## TL;DR

The 2026 repo looks nearly empty (one notebook), but the course is **not** being built
from scratch. A mature, classroom-tested **16-week** Fall 2025 offering exists in
sibling repos. The 2026 work is therefore **format redesign + port**, not content creation.

- **Content creation:** essentially done, and far more extensive than first thought.
- **The hour budget is comparable, not a cliff.** 2026 = 4 wks × 5 days × 2 hrs ≈ **40
  contact hours** vs. F25's ~48 (16 wks × ~3 hrs). So ~83% of F25's teaching time —
  the challenge is **intensity + scope trim**, not a 4:1 content cut.
- **Live online preserves F25's pedagogy.** Because WRIT is synchronous (not async), F25's
  instructor-supported in-person model — Hour 1 concept → Hour 2 supported hands-on → Hour 3
  application — transfers almost directly to live online sessions. This removes the largest
  risk a self-paced format would have carried.
- **The real lifts are:** (1) pacing the arc into ~20 daily 2-hr live sessions for
  *no-prior-experience* grad students; (2) a modest scope trim (likely lightening/cutting the
  web-dev + portfolio back half, which also overlaps MALA 60970); (3) a from-scratch syllabus.
- **Mechanical port is easy and quick.** Achievable for 2026-07-06 — *once scope is chosen.*

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

## The central decision: scope trim within a comparable hour budget

**2026 format:** 4 weeks × 5 days × 2 hrs/day ≈ **40 contact hours**, **online synchronous**.
**F25:** 16 weeks × ~3 hrs/week in-person ≈ **48 hours**, synchronous.

The budgets are close (~83%) **and both are synchronous & instructor-led**, so F25's session
pedagogy transfers with minimal change (in-person → live online). This is **not** a drastic
content cut, nor an async rebuild — it's mainly **re-pacing + a modest scope trim**. Scope
options (illustrative):

- **Full arc, tightened (recommended to evaluate first):** keep Python → text-analysis →
  portfolio → project, trimming depth. ~40 hrs is plausibly enough; risk is pace for beginners.
- **Drop the web-dev/portfolio back half:** run Python foundations + the cultural-analytics
  arc (HW1/HW4-1/HW4-2) as the spine, ending in a notebook-based project instead of an
  HTML/CSS portfolio. Frees the most time; note the dropped half overlaps **MALA 60970
  "Web Authoring"** anyway.
- **Foundations-only:** Weeks 1–4 Python basics as the whole course. Safest for true
  beginners; omits the cultural-analytics payoff that defines the course's identity.

**Dominant risk is pacing, not hours.** A daily 2-hr intensive for no-prior-experience grad
students leaves little recovery time when someone falls behind — though live sessions let the
instructor catch and unblock students in real time (an advantage the async sibling lacks). The
F25 HW1–HW8 load still must be thinned and re-sequenced to a ~20-session rhythm regardless of scope.

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
- Official **2026 4-week syllabus/schedule** — must be authored from scratch (see below: even
  F25 never had a written syllabus), and depends on the scope decision above.

## Direct repo inspection (full clone, 2026-06-09)
Additional facts confirmed by cloning `WRIT20833_2025`:
- **No syllabus exists, even for F25.** `docs/syllabus/index.md` is empty. A 2026 syllabus
  will be authored from scratch regardless of scope chosen.
- **Datasets are in-repo and reusable:** `datasets/TenCommandmentsTX/` holds real F25 YouTube
  comment CSVs (CBS1, CBS2, CNN, Talarico) — the cultural data behind the 2026 Variables
  notebook's "Ten Commandments" example. Portable as-is.
- **Dual-purpose repo:** F25 doubles as the source for a *"When Coding Meets Culture"* textbook
  (Jupyter Book, **publication target Aug 2026**); `_development/textbook/provisionalTOC.md`
  holds an 18-chapter structure. Explains the heavy `_development/` scaffolding.
- **Schedule cadence:** the weekly outline assumes 3-hour in-person sessions; the 2026 live
  online format (2-hr daily sessions) preserves the synchronous, instructor-supported model,
  so this is a re-pacing into shorter daily blocks rather than an async rebuild.
- **Internal week-numbering drift:** README phases (1–4/5–8/9–12/13–16) and the dev outline
  (which references a 16-week plan aligned to the ~18–19-ch TOC) differ slightly; treat the
  README phase grouping as the working map.

---

## Comparison context: WRIT 20833 vs. MALA 60970

| | MALA 60970 (Web Authoring) | WRIT 20833 (Coding in Humanities) |
|---|---|---|
| 2026 format | Online **async** | Online **synchronous** (2 hr/day × 5) |
| Underlying course | Mature planning repo (~85% ready) | Mature, fully built & taught (16-wk F25) |
| 2026 repo state | 2026 content authored in-repo | Nearly empty — port not started |
| Real remaining work | Polish + D2L build (IT-blocked) | **Scope trim + re-pace** + port |
| Teaching-hour budget | 4-wk summer | ~40 hrs (vs F25 ~48) — comparable |
| Risk profile | Low (execution only) | Low–Medium (pacing + scope trim) |

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
