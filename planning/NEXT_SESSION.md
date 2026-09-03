# Next-session handoff prompt

> **Course starts Mon Oct 19, 2026.** Last audit: **2026-09-02** (≈7 weeks out). Verdict: **the teaching
> material is done and verified; one launch blocker remains, and it is a repo-settings/git problem, not a
> content problem.** Full detail: the 2026-09-02 entry at the top of `planning/WORKLOG.md`.

---

## The one blocker — DOWN TO ONE STEP: flip the repo public

**Status 2026-09-03: the history scrub is DONE; only the visibility flip remains, and it is now safe.**

✅ **Done — answer keys scrubbed from history** (`git-filter-repo`, force-pushed; old tip `c45502b` → new
tip `648f1e4`). Verified on a fresh clone: no commit touches `*_ANSWER_KEY.ipynb` or
`notebooks/homework/_build_hw*.py`, no key blob in any object, and the old key-bearing SHAs (`2b36aef`,
`665d4f6`, `5b63c73`, `bceef16`, `f0e8c8d`, merge `67899e9`) are unresolvable. Nothing lost — the tip tree
is byte-identical to pre-scrub `main`; the 184 → 152 commit drop was the duplicated pre-scrub lineage
collapsing (every dropped subject has a surviving copy). CI guard green.

✅ **Done — all clones re-synced.** This machine's clone was `reset --hard` (not pulled) + `reflog expire`
+ `gc`. **The OTHER machine has not been touched** — before doing anything there, follow
`planning/WORKLOG.md` § "Working across two machines": `fetch --prune` → `reset --hard origin/main` →
`reflog expire --expire=now --all` → `gc --prune=now`. **Never `pull`** — that is what undid the June scrub.

🟠 **REMAINING — flip `TCU-DCDA/WRIT20833_2026` to PUBLIC.** Deliberately left to the instructor. Until it
flips, the public Pages site still serves students **97 dead links** (all 31 "Open in Colab" links, the
syllabus, the capstone sheet, the data folder), **404s every image** (pages rewrite images to
`raw.githubusercontent.com/.../main/materials/...`), and **breaks the HW2/3/4 data-loader cells**.

**Then verify, logged out** (a private window, not your own session):
1. one Colab link opens the notebook — e.g. the Variables code-along from the dashboard;
2. one lecture-page image renders — e.g. `lectures/ml0.html`;
3. `docs/schedule.html`'s Capstone links resolve.

---

## Plan for the next working session (pick a lane)

**Lane A — clear the blocker (highest value, ~1 hr, instructor-run).** The 4 steps above. Everything else
in the course is downstream of this: until it's done, Day 1 cannot be delivered as designed.

**Lane B — author the four missing second-half lecture framings (~2–3 hrs).** The schedule's Lecture column
names four sessions that have **no built material** — they are verbal framings only:
| Day | Date | Title |
|---|---|---|
| 13 | Mon 11/16 | Quantifying connotation *(callback to Connotations & Code)* |
| 14 | Wed 11/18 | Close vs. distant reading |
| 15 | Fri 11/20 | Predictions on the record |
| 18 | Fri 12/4 | Integration (close → distant → close) |
Options: (a) author short reading pages via `build_lectures.py` like ml0–ml9; (b) write instructor-only
speaking notes into `materials/lectures/`; (c) mark them **"(verbal)"** in the schedule so the column stops
reading as a promise of eight+ decks (the 2026-07-01 audit's §5.1 suggestion — cheapest of the three).
Day 7 "Data as evidence" is already documented as a ~5-min verbal framing; these four are not.

**Lane C — instructor decisions to close (~20 min, needs your judgment, not research).**
- **Capstone placeholders** — presentation length `[3–5]` min (2 spots) and `[to: upload location]`
  in `CAPSTONE_2026.md`. Needed by **Fri 12/4** (proposal), not Day 1.
- **HW1 window** — assigned Fri 10/30, due **Mon 11/2**: one weekend for 12 exercises + Weekly
  Experiments, from students six sessions into their first Python. HW2–4 each get a full week *plus* a
  work session. Moving HW1's due date to Wed 11/4 costs nothing structurally (Day 7 is its debrief —
  that would need to move too, or the debrief stays and only the deadline slides).
- ✅ **Stale root duplicates — DELETED 2026-09-02.** The June reorg had left four tracked copies at the
  repo root; root `WORKLOG.md` and `CONCEPTUAL_FRAMEWORK_2026.md` still dated to 2026-06-10 and described
  the *4-week summer* course. All four (`WORKLOG.md`, `CONCEPTUAL_FRAMEWORK_2026.md`, `ACKNOWLEDGMENTS.md`,
  `PROPOSED_4WEEK_SCHEDULE.md`) are `git rm`'d — `planning/` is the single source, which is where README
  already pointed. Nothing linked to them and all three generators still build clean. **Root now holds only
  the four student-facing docs** (README · SYLLABUS · COURSE_SCHEDULE · CAPSTONE) + the generators.
- **Chatbot tutor** — untouched since 2026-06-18, still code-complete/undeployed in the private
  `TCU-DCDA/WRIT20833-chatbot`. Ship before launch, or observe first and skip this term? Deployment =
  KV namespace, secrets, prod `API_URL` + CORS, `wrangler deploy`, Pages frontend, D2L embed.

**Lane D — pre-launch checks not in this repo.** TCU Online (D2L) shell built: 4 discussion topics
(D1 Wk1 · D2 Wk3 · D3 Wk5 · D4 Wk7), 3 reflection dropboxes, 4 HW dropboxes, capstone dropbox; the
AddRan Word syllabus (`SYLLABUS_2026.docx`, added 2026-08-27) synced to `SYLLABUS_2026.md`; the 🟦
registrar wording double-checks in `planning/SYLLABUS_COMPLIANCE.md`; one 60-sec live Colab click on the
Day-16 gensim install cell. **Not a task:** the CSV/HUM vetting-form trim — the course already carries
both designations and nothing is pending (closed 2026-06-26; WORKLOG item #10). `CSV_HUM_WORK_EXAMPLES.md`
is reference only.

---

## What is already verified — do not re-do

Re-verified by execution on **2026-09-02** (not read from the log):
- **All 9 code-along notebooks + the stylometry notebook execute clean** — 165 code cells; the only error
  is the *intentional* "read the error message" `TypeError` in Variables. Stack: pandas 2.3.3 / numpy
  2.0.2 / gensim 4.4.0 / vaderSentiment. **The Day 16–17 gensim LDA notebook ran clean** (the standing
  risk item). ⚠️ **Toolchain note:** `/opt/anaconda3/bin/python` (the path this WORKLOG cites) does **not
  exist on the `/Users/crode/...` machine** — plain `python3` there has the full stack.
- **Site is in sync** — re-running `build_index.py`, `build_schedule_html.py`, `build_lectures.py`
  reproduces the committed `docs/` **byte-identically**. Don't hand-edit `docs/`.
- **Syllabus complete** — zero `[...]` placeholders; section 020 · MWF 10:00–11:50 AM · Schar Hall 2003;
  all D1–D4 + R1–R3 prompts written; dates agree across syllabus, schedule, and capstone sheet.
- **Lecture day-homes correct** post-repacing: ml0+ml1 D1 · ml3 D3 · ml5 D4 · ml4 D8 · ml6 D10 · ml7 D16 ·
  ml9 D19. All 8 reading pages + decks live.
- **Readiness:** Day 1 = content 100% · Week 1 = 100% · first half (Days 1–12) = ~99% · second half = ~90%
  (Lanes B + C). **All of it gated on the blocker above.**

---

## Resume prompt (paste into a fresh thread)

```
WRIT 20833 (2026) course port — resuming work.

Repo (this machine): /Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026
  (an older clone lives at /Users/curtrode/Code/Teaching/WRIT/... on the other machine)
Course: 8 weeks, IN PERSON, MWF 10:00–11:50 AM, Oct 19 – Dec 18 2026, TCU 8W2, section 020,
Schar Hall 2003, 24 sessions, enrollment ≤ 20. No class Thanksgiving week (Nov 23–27).

READ FIRST: planning/NEXT_SESSION.md (the blocker + the lane you're picking), then
planning/WORKLOG.md (decision log). planning/PROJECT_EVALUATION_2026-07-01.md is the last
full audit; the 2026-09-02 WORKLOG entry is the most recent verification.

REPO STATE: main is at origin/main; repo is currently PRIVATE and the public Pages site is
therefore broken for students (see NEXT_SESSION.md). Solo maintainer → commit straight to
`main`, no per-task branches/PRs. After any history rewrite, re-sync clones with
`reset --hard`, NEVER `pull`.

Answer keys + the solution-bearing _build_hw2/3/4.py live ONLY in the private
TCU-DCDA/WRIT20833_2026_keys. A CI guard (.github/workflows/guard-instructor-files.yml)
fails any push that tracks them here. To change HW2–4: edit the builder THERE, run it, copy
the regenerated STUDENT notebook back. HW1 has no builder (edit directly).

Conventions: ungrading voice ("errors are learning"; #comments "frequent & meaningful");
house style for notebooks; the TX Ten Commandments corpus threads Day 8 → 10 → 13–14 → 16–17
and HW3/HW4. Validate notebooks with `python3`. Regenerate docs/ after any content edit
(build_index / build_schedule_html / build_lectures) — the generators enforce WCAG AA and
≥12px type via site_theme.assert_accessible(), and fail loudly on a regression.

Ask before anything outward-facing (force-push, visibility flip, publishing to students).
```
