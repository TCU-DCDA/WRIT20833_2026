# WRIT 20833 — 2026 Project Evaluation (open-state audit)

**Course:** WRIT 20833, "Intro to Coding in the Humanities" / "When Coding Meets Culture"
**2026 offering:** 8 weeks, **in person**, MWF 10:00–11:50 AM, Oct 19 – Dec 18, 2026 (TCU 8W2, 24 sessions)
**Evaluation date:** 2026-07-01 (≈15.5 weeks to Day 1)
**Repo evaluated:** `TCU-DCDA/WRIT20833_2026` at `main` = `ffe2cd1` (post-re-pacing merge, PR #31)
**Method:** three parallel audits — (1) re-pacing consistency across every student-facing surface,
(2) day-by-day content inventory vs. the 24-session schedule, (3) open-threads / planning-doc / git-state
review — with all substantive claims re-verified directly (`git ls-files`, `git ls-tree`, grep of the
generated `docs/`).

---

## TL;DR — verdict

The course is in **strong shape and on track**: the 2026-06-26 re-pacing landed **fully consistent**
across all surfaces, every one of the 24 sessions has its promised teaching artifact, and the residual
open items are the known instructor-side ones. The WORKLOG's ~90% readiness self-assessment holds up.

**But one urgent integrity problem was found:** the **HW1–4 answer keys and the solution-bearing HW
builders are back in this public repo** — reintroduced by a merge after the 2026-06-11 BFG scrub, in
exactly the two-machine failure mode the WORKLOG warns about. Fixing this requires a history rewrite on
`main` (instructor's call), so this evaluation **reports it rather than fixes it**. One small bug
(2 broken Capstone links on the live schedule page) is also documented with its one-line fix.

| Severity | Finding | Action |
|---|---|---|
| 🔴 Urgent | Answer keys + `_build_hw2/3/4.py` tracked on public `main` | Instructor: re-scrub + force-push (§1) |
| 🟠 Bug | 2 broken `CAPSTONE_2026.md` links in `docs/schedule.html` | One-line fix in `build_schedule_html.py` + regenerate (§2) |
| ✅ Pass | Re-pacing consistency (dates, due dates, day-homes, placeholders) | None (§3) |
| ✅ Pass | Content coverage — all 24 sessions have artifacts | None (§4) |
| 🟡 Minor | Doc/reality nits + intentional placeholders | Optional (§5) |

---

## §1 🔴 URGENT — answer keys are live in the public repo again

**Evidence (verified at HEAD, `git ls-files`):** the public repo currently tracks all seven
instructor-only files —
`notebooks/homework/WRIT20833_HW{1,2,3,4}_2026_ANSWER_KEY.ipynb` and
`notebooks/homework/_build_hw{2,3,4}.py` — despite the locked convention that these live **only** in the
private `TCU-DCDA/WRIT20833_2026_keys` repo, and despite `.gitignore` listing both patterns.
(`.gitignore` only blocks *new* additions; it does not untrack files already committed.)

**Root cause (forensically confirmed):** the 2026-06-11 BFG scrub did work — but merge commit
`67899e9` ("Merge branch 'main' of https://github.com/TCU-DCDA/WRIT20833_2026") merged a **stale,
pre-scrub clone back into the rewritten remote**:

- parent `67899e9^1` (local machine's history): carries **7** key/builder files;
- parent `67899e9^2` (the scrubbed remote `main`): carries **0**;
- the merge result (now ancestor of `main`): carries **7**.

This is precisely the failure documented in this WORKLOG's own "Working across two machines" section
("a plain `pull` would try to merge the old history back (and could reintroduce scrubbed files)").
The pre-scrub commits (`2b36aef`, `665d4f6`, `5b63c73`, `bceef16`, …) are reachable from `main` again,
so the *history* is re-exposed too, not just the tips.

**Why it matters:** students can read every homework's worked solutions (and the builders that generate
them) straight off the public GitHub Pages repo. It quietly defeats the whole private-keys design and
the ungrading posture that depends on students doing the struggle themselves.

**Remediation status (updated 2026-07-01, same day — partial fix applied on this branch):**

- ✅ **Divergence check:** all 7 files' last commits date to **2026-06-10, before the scrub** — no edits
  landed here that the private keys repo lacks, so removal loses nothing.
- ✅ **Tip removal:** the 7 files are `git rm`'d on `claude/open-project-evaluation-lzee77`. Once merged,
  the public repo's browsable tree no longer serves them.
- ✅ **Recurrence guard:** `.github/workflows/guard-instructor-files.yml` — CI fails any push/PR where
  `git ls-files` matches `*_ANSWER_KEY.ipynb` or `notebooks/homework/_build_hw*.py`.
- 🔴 **STILL REQUIRED (instructor — needs a force-push to `main`):** the files remain readable in **git
  history** until it is rewritten. After merging this branch:
  1. **Re-run the BFG scrub** for `*_ANSWER_KEY.ipynb` + `notebooks/homework/_build_hw*.py` and
     force-push `main` (same procedure as 2026-06-11).
  2. **Re-sync every other clone with a hard reset, not a pull** — follow the exact block in
     `planning/WORKLOG.md` § "Working across two machines" (fetch → `reset --hard origin/main` →
     `reflog expire` + `gc`). This is the step that was missed last time.
  3. Verify on a fresh clone: `git log --all --oneline -- '*_ANSWER_KEY.ipynb' 'notebooks/homework/_build_hw*.py'`
     → **expect empty**.
  4. GitHub may cache the old commits server-side until GC; contact GitHub support to purge if the SHAs
     stay reachable by URL.

---

## §2 🟠 Bug — 2 broken Capstone links on the live schedule page

`docs/schedule.html` renders the two capstone rows (proposal Fri 12/4; final Fri 12/18) with
`href="CAPSTONE_2026.md"`. Relative to `docs/`, that resolves to `docs/CAPSTONE_2026.md`, which doesn't
exist → **404 on the live GitHub Pages site**. `docs/index.html` handles the same target correctly with
the absolute URL `https://github.com/TCU-DCDA/WRIT20833_2026/blob/main/CAPSTONE_2026.md`.

**Fix — ✅ APPLIED (2026-07-01, follow-up commit):** `_abs()` in `build_schedule_html.py` now maps
root-level `.md` links (e.g. `CAPSTONE_2026.md`) to the absolute GitHub blob URL (as `build_index.py`
already does); `docs/schedule.html` regenerated — both capstone links verified absolute.

---

## §3 ✅ Re-pacing consistency — PASS (no inconsistencies found)

The 2026-06-26 format change (4-week summer → 8-week in-person fall) is **fully synchronized** across
`SYLLABUS_2026.md`, `COURSE_SCHEDULE_2026.md`, `CAPSTONE_2026.md`, `README.md`, the three generators
(`build_index.py`, `build_schedule_html.py`, `build_lectures.py`), all 8 `materials/lectures/ml*.md`
metas, and the regenerated `docs/` (index, schedule, 16 lecture pages/decks). Specifically verified:

- **Term frame:** Mon Oct 19 – Fri Dec 18, MWF, 24 sessions, 2 hrs/day; Thanksgiving gap (recess after
  Fri 11/20, resume Mon 11/30) — consistent everywhere.
- **Registrar specifics filled:** section **020**, **MWF 10:00–11:50 AM**, **Schar Hall 2003**,
  Dr. Curt Rode / Schar 2006 — present in the syllabus; no `[...]` placeholders remain there.
- **Due dates agree across syllabus + schedule + capstone sheet:** R1 Fri 10/23 · HW1 Mon 11/2 ·
  HW2 Mon 11/9 · R2 Mon 11/16 · HW3 Mon 11/30 · HW4 assigned Wed 12/2 · proposal Fri 12/4 ·
  HW4 Mon 12/7 · Capstone + R3 Fri 12/18. Discussions D1–D4 biweekly (Wks 1/3/5/7) consistent.
- **Lecture day-homes** (AI Agency D8, Data Archaeology D10, NLP & Topic Modeling D16, Going Public D19)
  match in `build_lectures.py`, `build_index.py`, every `ml*.md` meta, and every generated page/deck.
- **No stale summer text** in any student-facing surface (the README's one "originally drafted as a
  4-week summer intensive" line is deliberate historical framing). Both `PROPOSED_4WEEK_SCHEDULE.md`
  copies carry the **SUPERSEDED** banner.

---

## §4 ✅ Content coverage — PASS (all 24 sessions have their artifacts)

- **Code-alongs:** 9/9 present in `notebooks/codeAlongs/` and mapped to their days (Variables D1 ·
  Strings D2 · Lists/Loops/Conditionals D3–4 · Dicts/Functions D5 · Term Frequency D7 · Pandas 01 D10 ·
  Pandas 02 D11 · VADER D13–14 · Topic Modeling D16–17). First half re-executed clean 2026-06-21.
- **Homework:** HW1–4 student notebooks all present.
- **Lectures:** all 8 scheduled pairs (reading page + deck) built and live; all referenced lecture
  images (22 in `materials/lectures/images/` + the pipeline diagram) resolve — no broken image paths.
- **Data:** both corpora present (`tc_youtube_comments.txt` — the 123-comment thread that runs Day 8 →
  HW3/HW4 → capstone fallback — and `us_constitution.txt`), with the data `README.md`; every data path
  referenced by the homeworks exists.
- **Stylometry (capstone Track B):** `Reading_for_the_Seams.md` + the companion notebook both present,
  as linked from `CAPSTONE_2026.md`.
- Work-session / presentation days (6, 9, 12, 15, 20–24) intentionally have no standalone notebook.

---

## §5 🟡 Minor items & ambiguities (no action required; listed for the record)

1. **Days 13/14/18 lecture titles without decks.** The schedule's Lecture column names "Quantifying
   connotation," "Close vs. distant reading," and "Integration," but these are verbal framings (per the
   schedule's own notes), not built decks. Consider a typographic cue (e.g., italics or "(verbal)") so
   the column doesn't read as promising eight+ decks.
2. **Builder-coverage wording.** README/WORKLOG say each code-along "has a `_build_*.py`," but 2 of 9
   (Variables, Lists/Loops/Conditionals) are hand-authored with no builder. Cosmetic doc/reality
   mismatch — the code-along builders are not solution-bearing. (HW1 having no builder is by design.)
3. **Intentional capstone placeholders** — presentation length `[3–5]` min and the upload location —
   are the two documented instructor-decision spots; fill before publishing the sheet to students.
4. **Stale-but-labeled planning docs.** `PORT_ASSESSMENT_2026.md` (snapshot-bannered) and the
   `NEXT_SESSION.md` preamble still carry summer-era framing; both point readers to the WORKLOG, so
   this is acceptable as-is. Update `NEXT_SESSION.md` on its next touch.

---

## §6 Open-items inventory (unchanged by this evaluation)

**Development:**
- **Chatbot tutor** — MVP code-complete in private `TCU-DCDA/WRIT20833-chatbot`; **deployment pending**
  (KV namespace, secrets, prod URL/CORS, `wrangler deploy`, Pages frontend, D2L embed). Open dial:
  "confirm-my-guess" behavior. Ship-before-launch vs. observe-first remains the instructor's call.
- **One 60-sec live Colab click** to confirm the topic-modeling install cell before Day 16 (the clean-venv
  proxy test on 2026-06-21 already passed; this is the last-mile confirmation).

**Instructor-side paperwork:** AddRan Word syllabus (`WRIT20833-020_Fall2026_Rode.docx`) kept in sync by
hand; CSV/HUM work-examples trim to the vetting form; registrar double-checks flagged 🟦 in
`SYLLABUS_COMPLIANCE.md`.

**Parked (optional):** sidebar icons / nav filter, themed `syllabus.html`, `tools/` folder tidy,
palette retune, ML7 interior image slot.

---

## §7 Prioritized recommendations

| # | Priority | Action | Owner |
|---|---|---|---|
| 1 | 🔴 Now | ~~Remove keys + builders from the tip~~ ✅ done on this branch; **re-scrub history + force-push `main` + hard-reset all clones + verify on fresh clone** (§1) | Instructor |
| 2 | 🔴 Now | ~~CI guard against instructor-only files being tracked~~ ✅ done (`.github/workflows/guard-instructor-files.yml`) | — |
| 3 | 🟠 Soon | ~~Fix the Capstone link mapping in `build_schedule_html.py`; regenerate `docs/`~~ ✅ done (§2) | — |
| 4 | 🟡 Pre-launch | Fill the two capstone placeholders; the Day-16 live Colab click | Instructor |
| 5 | 🟡 Whenever | §5 doc nits; decide the chatbot deployment timing | Instructor |

**Bottom line:** teachable material is complete, consistent, and verified — the project's one real fire
is the answer-key re-exposure, and it's a git operation away from out.
