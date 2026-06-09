# WRIT 20833 — 2026 Readiness & Port Assessment

**Course:** WRIT 20833, "Intro to Coding in the Humanities" (a.k.a. "When Coding Meets Culture")
**2026 offering:** 4 weeks, async, **start date 2026-07-06**
**Assessment date:** 2026-06-09 (27 days to start)
**Repo assessed:** `TCU-DCDA/WRIT20833_2026` (this repo)
**Reference offering:** Fall 2025, semester-length (~15 weeks), spread across sibling repos

---

## TL;DR

The 2026 repo looks nearly empty (one notebook), but **the course is not being built from scratch.** A mature, classroom-tested Fall 2025 offering already exists across sibling repos. The 2026 work is a **port + compression**, not content creation.

- **Content creation:** essentially done. High quality, scaffolded, classroom-tested.
- **Real remaining work:** (1) a mechanical port into this repo, and (2) a *pedagogical decision* about how to compress ~15 weeks of material into 4.
- **Achievable for 2026-07-06** if the port starts soon. The binding constraint is the compression decision, not missing assets.

> ⚠️ This report is an assessment only. No porting, content changes, or scheduling decisions have been made. Compression of the semester into 4 weeks is an instructor decision that remains open.

---

## What exists today

### This repo (`WRIT20833_2026`)
- `notebooks/codeAlongs/WRIT20833_Variables_DataTypes_2026.ipynb` — the only ported unit so far. Polished, executable. Maps to the F25 "Variables & Data Types" worksheet.

### Sibling repos in the `TCU-DCDA` org (prior/supporting material)
| Repo | Purpose | State |
|---|---|---|
| `WRIT20833_2025` | The Fall 2025 offering (direct predecessor) | Archived, public |
| `WRIT20833` | Course-page website (`gh-pages`) | Active, public |
| `writ20833-textbook` | Course textbook | Active, private |
| `WRIT20833-portfolio-template` | Student portfolio starter | Active, public |
| `WRIT20833-chatbot` | Course chatbot | Active, private |
| `WRIT20833_alt` | "alt 20833 syllabus" | Archived |
| `writ20833_f25-intro-to-github-...` | GitHub Classroom starter | Archived |

> Note: `WRIT20833_2025` could not be read directly from this session (out of scope; archived so not in code search). The analysis below is based on 11 F25 notebooks provided manually.

---

## F25 course architecture (four intertwined strands)

1. **Melanie Walsh, *Intro to Cultural Analytics*** — external OER textbook providing the Python backbone (Ch 4–10: variables → data types → strings → conditionals → lists & loops). Not ours to maintain.
2. **Mini-lecture video series** — the humanities/critical-theory spine: Sacred Boundaries → Classification → Agentic Coding → Collective Memory.
3. **Tutorials** — bridge concept to theme; explicitly week-labeled and tracking Walsh chapters.
4. **Homework** — applies skills to student-chosen cultural datasets.

### Notebooks reviewed (11)

**Code-alongs (`notebooks/codeAlongs/`):**
- Variables & Data Types (worksheet) — *ported to 2026*
- VADER Sentiment Analysis
- Topic Modeling Part 1: Introduction
- Topic Modeling Part 2: Research Application
- Topic Modeling Gensim (older **combined** version — predecessor to the Part 1/Part 2 split; likely redundant)

**Homework (`notebooks/homework/`):**
- HW1 — Term Frequency / "Meaningful Words" (uses provided F22 text files)
- HW3-1 — Pandas: Found Data + collection ethics (robots.txt, AI-era)
- HW3-2 — Pandas: Data Cleaning (continues HW3-1 dataset)
- HW4-1 — Term Frequency + Sentiment ("Midterm Part 1")
- HW4-2 — Topic Modeling + Integration ("Midterm Part 2")

**Tutorials (paired with mini-lectures):**
- Tutorial 1: Digital Boundaries (strings, conditionals)
- Tutorial 2: Classification Logic (booleans + Bellevue Almshouse dataset)
- Tutorial 3: AI Agency — **Week 3** (reading/improving AI-generated code)
- Tutorial 4: Collective Memory — **Week 4** (lists & loops)

**Analytical arc:** term frequency → sentiment (VADER) → topic modeling (Gensim LDA), with critical-theory integration (Shrout's Bellevue Almshouse, Noble, O'Neil) and explicit AI-literacy content.

---

## Port status

**✅ Carry-over-ready (high quality, minimal change):**
- Variables & Data Types (done)
- VADER code-along
- Topic Modeling Part 1 & Part 2
- HW1, HW3-1, HW3-2, HW4-1, HW4-2
- Tutorials 1–4

**⚠️ Decisions needed before porting:**
- **Duplicate topic-modeling notebooks** — choose canonical: standalone "Gensim" vs. the Part 1/Part 2 split. Don't port both.
- **Hard-coded F25 dates** — HW4-1 "due Oct 5", HW4-2 "Oct 17" vs "Oct 13" (internally inconsistent). All need 2026 dates.
- **F25/-2025 Colab badge links** — every notebook's "Open in Colab" badge points at `WRIT20833`/`WRIT20833-2025` paths; must be repointed to `WRIT20833_2026`.
- **HW4-2 dependency-pinning cell** — pins `numpy==1.26.4`, `pandas==2.2.2`, `scipy==1.13.1`, `gensim==4.3.3` and requires a mandatory Colab runtime restart. Verify against Colab's 2026 default image before students hit it.

---

## The central open question: semester → 4 weeks

F25 was ~15 weeks; 2026 is 4. The conceptual spine compresses cleanly (Tutorials/Mini-Lectures 1–4 are already a 4-unit, week-labeled sequence). **The risk is workload, not missing content:** 5 homeworks + 4 code-alongs + 4 tutorials + 4 mini-lectures in 4 async weeks — for grad students with *no prior coding experience*, over summer — is heavy. Compression will require dropping, merging, or making-optional some components.

This is a pedagogical decision and has been left open intentionally.

---

## Known gaps in this assessment

- **No syllabus/schedule reviewed** — total unit count and official sequencing unconfirmed.
- **HW2 not located** — there is a numbering gap between HW1 and HW3-1.
- **"Instant Data Scraper" lesson not located** — referenced as the data-collection step feeding HW3/HW4.
- **`WRIT20833_2025` not directly accessible** from this session (would confirm the above).

---

## Comparison context: WRIT 20833 vs. MALA 60970

Both are 4-week summer 2026 courses with strong, near-complete source material; the difference is *where* the 2026 work currently lives.

| | MALA 60970 (Web Authoring) | WRIT 20833 (Coding in Humanities) |
|---|---|---|
| Underlying course | Mature planning repo (~85% ready) | Mature, fully built & taught (F25) |
| 2026 repo state | 2026 content authored in-repo | Nearly empty — port not started |
| Real remaining work | Polish + D2L build (IT-blocked) | Port + compress semester → 4 weeks |
| Risk profile | Low (execution only) | Medium (port scope + compression) |

Neither course needs content *invented*. MALA's 2026 deliverable is more assembled in-repo; WRIT's underlying course is more battle-tested (actually delivered).

---

## Suggested next steps (when ready)

1. Decide the 4-week compression (week-by-week mapping; what to cut/merge/make optional).
2. Mechanical port of carry-over-ready notebooks into this repo.
3. Global fixes: dates, Colab links, dedup topic-modeling, dependency-cell verification.
4. Confirm/locate HW2, the data-scraper lesson, and the syllabus.
