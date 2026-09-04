# Next-session handoff prompt

> **Course starts Mon Oct 19, 2026.** Status as of **2026-09-05**: 🚀 **the launch blocker is CLEARED —
> the repo is public, the site is live, and the answer keys are unreachable from it.** A **continuity
> audit** (2026-09-05) then read the code-alongs against the homework they build toward and fixed the
> mechanical defects — day numbers, a wrong corpus count, a dead guard in HW4 — in both the course repo
> (`0821ee6`, pushed) and the keys builders (`4fa8490`, **committed not pushed**). What remains is
> polish and instructor decisions, none of it blocking Days 1–12. Full detail: the 2026-09-05 and
> 2026-09-04 entries at the top of `planning/WORKLOG.md`.
>
> ⏩ **One loose end:** `git push` the keys repo (`../WRIT20833_2026_keys`, one commit ahead).

---

## ⚠️ First, know which repo you are in

**`TCU-DCDA/WRIT20833_2026` was recreated on 2026-09-04.** Same owner, same name, same URL, same 153-commit
history — but a **new repository**. The old one (which kept serving the answer keys from unreachable
objects even after the history rewrite) was renamed to the **private `TCU-DCDA/WRIT20833_2026_archive`**
and must never be made public.

- **SHAs cited in WORKLOG entries before 2026-09-04 and in `PROJECT_EVALUATION_2026-07-01.md` do not
  resolve here.** The prose is still accurate; only the hashes are dead.
- **The other machine's clone points at the old repo and still holds the pre-scrub history.**
  **Re-clone it fresh** — do not pull, and do not push from it.
- A full safety copy exists at **`~/WRIT20833_2026_scrubbed.bundle`** (verified restorable; 153 commits).
  Keep a copy off that machine — right now it is the only backup.

## ✅ Launch blocker — CLEARED 2026-09-04

Verified **anonymously**, which is what a student actually gets: index · schedule · all 8 lecture pages +
decks → 200; **43/43** repo-pointing links pass (every Colab link, every image); both HW corpora load.
And the other half: all 4 answer keys → 404 on `main`, the builders → 404, **the keys at the old
pre-scrub SHAs → 404 on both `raw.githubusercontent.com` and `github.com/.../blob/<sha>/`**, archive → 404.

**The site is deliverable end-to-end. Days 1–12 need nothing further.**

---

## Plan for the next working session (pick a lane)

**~~Lane A — clear the blocker~~ ✅ DONE 2026-09-04.** Scrub → rename → republish → public → verified.
Nothing here is outstanding. *(If a similar exposure ever recurs: a history rewrite alone is NOT enough —
GitHub keeps serving unreachable objects until it GCs. Either open a support ticket from the org, which is
on a Team plan, or repeat the rename-and-republish, which needs no one's permission and preserves the URL.)*

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

**Lane E — the six judgment calls the 2026-09-05 audit left open (needs your voice, not mechanics).**
The mechanical fixes shipped; these change what the assignments *say*, so they were not applied
unilaterally. In priority order:
1. **HW3 conflates tone with stance.** The VADER code-along's Part 4 is titled "Tone Is Not the Same as
   Stance" — then HW3 opens "use sentiment to hear the **stance**," subtitles C1 "now split by stance"
   while splitting on VADER's label, and B4 asks "does this crowd **support or oppose**" from sentiment
   alone. HW3's corpus has no hand-labeled stance column, so the two-axis comparison the code-along
   builds cannot be reproduced there. **The homework teaches against its own code-along** — this is the
   one worth fixing before Day 13.
2. **Day 3 / Day 4 split fights the notebook.** Both schedule and syllabus assign Day 3 = conditionals,
   Day 4 = lists & loops, but `Lists_Loops_Conditionals` runs Lists → Conditionals → Loops and the
   conditionals section depends on `platforms` from the Lists section. Reorder the notebook (it has no
   builder — edit directly) or swap the two days. **Bites on Day 3**, so it is the most urgent by date.
3. **Topic Modeling Part 1's "clear example" isn't clear** on gensim 4.4.0 / `random_state=42`: 3 of the
   5 music docs land in the sports or food topic and "song" sits in the sports topic's top 6, while the
   narration promises "a comment or two" misfiled. The k=4 run in Part 2 separates cleanly. Re-tune the
   toy corpus or the seed.
4. **Term Frequency's "distinctive words" cell** computes `comment_top - official_top` (top-8 minus
   top-8). The lists are fully disjoint, so nothing is ever subtracted and the point is invisible. HW2
   **B3** does it correctly against the full vocabulary — make the code-along match.
5. **False provenance.** Term Frequency's setup claims "the same tools from Day 5 and HW1: a
   `split_into_words` helper, the long `stopwords` skip-list"; HW2 repeats it. Day 5 has neither and
   HW1 A6's list is five words, explicitly a preview — both are new on Day 7. Relatedly HW2's prep list
   never cites the Day-5 code-along though A5 and `Counter` come from it, and the syllabus maps Day 5 →
   HW1 while HW1 has no `def`, no `{}`, no `Counter`.
6. **Smaller:** list comprehensions appear in Term Frequency's given code and HW2 A3's hint but are
   never taught; HW2's own-data exercise is *optional* while Day 9 is a scheduled "term frequency on
   your data" work session; HW4's capstone bridge (C2) is due Day 19, a day **after** the capstone
   proposal it should inform (Day 18). Cosmetic: Term Frequency's prose word order, and the VADER
   "predict first" cell whose intended *mixed* line scores **+0.714** (higher than the lukewarm one)
   while 5 of its 11 demo comments score exactly 0.0000.

⚠️ **Any HW2–4 change goes through `_build_hw2/3/4.py` in `../WRIT20833_2026_keys`, never the `.ipynb`.**
See the new root `CLAUDE.md` §1.

**Lane D — pre-launch checks not in this repo.** TCU Online (D2L) shell built: 4 discussion topics
(D1 Wk1 · D2 Wk3 · D3 Wk5 · D4 Wk7), 3 reflection dropboxes, 4 HW dropboxes, capstone dropbox; the
AddRan Word syllabus (`SYLLABUS_2026.docx`, added 2026-08-27) synced to `SYLLABUS_2026.md`; the 🟦
registrar wording double-checks in `planning/SYLLABUS_COMPLIANCE.md`; one 60-sec live Colab click on the
Day-16 gensim install cell. **Not a task:** the CSV/HUM vetting-form trim — the course already carries
both designations and nothing is pending (closed 2026-06-26; WORKLOG item #10). `CSV_HUM_WORK_EXAMPLES.md`
is reference only.

---

## What is already verified — do not re-do

Re-verified by execution on **2026-09-05** (not read from the log):
- **All 7 code-along builders and all 3 HW builders emit byte-identical output** to what is committed
  in each repo — no drift anywhere as of `0821ee6` / keys `4fa8490`.
- **All 3 answer keys execute top-to-bottom with zero errors**, including HW4 with the corrected `-1`
  guard (B2 now reports 2 fragment rows).
- **The Colab/raw fallback is live on `main`** — both corpora and both notebook paths return HTTP 200
  anonymously, so `load_text()`'s download path works for students out of the box.

Re-verified by execution on **2026-09-02**:
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

READ FIRST: CLAUDE.md (which files are generated — HW2-4 come from builders in the
private keys repo, NOT from the .ipynb), then planning/NEXT_SESSION.md (the lane you're
picking; Lane E holds the six open judgment calls from the 2026-09-05 continuity audit), then
planning/WORKLOG.md (decision log). planning/PROJECT_EVALUATION_2026-07-01.md is the last
full audit; the 2026-09-02 WORKLOG entry is the most recent verification.

REPO STATE: PUBLIC, site live and verified working for students. NOTE: this repo was
RECREATED 2026-09-04 (the compromised one is the private WRIT20833_2026_archive — never
make it public). Same URL and history, new object store; pre-2026-09-04 SHAs in the docs
do not resolve. The other machine's clone points at the old repo — re-clone it fresh, do
not pull or push from it. Backup: ~/WRIT20833_2026_scrubbed.bundle. Solo maintainer →
commit straight to `main`, no per-task branches/PRs.

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
