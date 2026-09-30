# Next-session handoff prompt

> **Course starts Mon Oct 19, 2026.** Status as of **2026-09-28**: the repo is public, the site is live,
> and the answer keys are unreachable from it. **Lane E is closed.** All six judgment calls from the
> 2026-09-05 continuity audit were fixed and pushed on 2026-09-28: the HW3 tone/stance framing, the
> Day 3/4 notebook order, the Topic Modeling toy corpus, Term Frequency's distinctive-words cell, the
> false provenance claims, and the smaller items. The Lane C decision on the HW1 window is also made
> (Day 6 = start HW1 in class). Both repos are in sync with `origin/main`. Every builder reproduces
> what is committed (re-verified 2026-09-28).
>
> ⏩ **Next up:** Lane C (the capstone placeholders; the chatbot is launch-ready, deploy steps below) → Lane B (four lecture
> framings) → Lane D (both D2L packages imported 2026-09-28; confirm the discussions + DST dates, then hand-wire the shell per `d2l/WIRING_CHECKLIST.md` §3–6, plus the checks outside this repo).
> ✍️ **Hand edits pending (Word syllabus `WRIT20833-020_Fall2026_Rode.docx`):** (1) the 2026-09-28 Day 6 and
> Day 9 label changes; (2) the two 2026-09-30 Code Guide paragraphs now in `SYLLABUS_2026.md` (after the
> reflections list, and at the end of the AI Use Policy). Then **re-upload the syllabus PDF to D2L**
> (`d2l/WIRING_CHECKLIST.md` → *Updating a live shell*).

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
- ✅ **HW1 window — DECIDED 2026-09-28.** The due date stays Mon 11/2. The Day 6 work session is relabeled
  "foundations recap + **start HW1 in class**" in the schedule and syllabus, so the window is one class
  session plus a weekend, about the same as HW4. ⚠️ Mirror this into the Word syllabus
  (`WRIT20833-020_Fall2026_Rode.docx`).
- ✅ **Stale root duplicates — DELETED 2026-09-02.** The June reorg had left four tracked copies at the
  repo root; root `WORKLOG.md` and `CONCEPTUAL_FRAMEWORK_2026.md` still dated to 2026-06-10 and described
  the *4-week summer* course. All four (`WORKLOG.md`, `CONCEPTUAL_FRAMEWORK_2026.md`, `ACKNOWLEDGMENTS.md`,
  `PROPOSED_4WEEK_SCHEDULE.md`) are `git rm`'d — `planning/` is the single source, which is where README
  already pointed. Nothing linked to them and all three generators still build clean. **Root now holds only
  the four student-facing docs** (README · SYLLABUS · COURSE_SCHEDULE · CAPSTONE) + the generators.
- **Chatbot tutor ("Code Guide")** — **code-ready and reviewed; deployment pending.** Real deadline: HW1 is
  assigned Fri 10/30. Worker, prompt, and assignment blocks: private `TCU-DCDA/WRIT20833-chatbot` (its
  `CLAUDE.md` + `DEPLOY.md` are current). Chat page: this repo (`chatbot/chatbot.js` + `chatbot/render.js` +
  `build_chatbot.py` → `docs/chatbot.html`), live but **unlinked** until `CHAT_API_URL` is set.
  - **2026-09-30:** two independent reviews (`COURSE_CONTEXT_REVIEW_*` / `COURSE_REVIEW_EXPANDED_*` in the
    chatbot repo, with replies recording Dr. Rode's six decisions). Work order done: permitted-help prompt
    revision (explain supplied + AI-written code; homework-writing feedback; concepts; no due dates; Track B
    context); page fixes (verbatim code rendering, per-request state, clean rollback; `node --test
    chatbot/render.test.js` + `chatbot/browser-check.mjs`); worker (Sonnet 5.5 at low effort, refusal/error
    stream endings, access gate before a 60/min + 800/day per-network limit that fails open); HW2 checklist
    (C2 optional) + HW3 B3 own-data sentence via the keys-repo builders; syllabus + page privacy wording;
    live acceptance probe run 1: 12/12 pass (`worker/retest/RESULTS.md`).
  - **Remaining, in order:** (1) deploy per the chatbot repo's `DEPLOY.md`: KV namespace, `ANTHROPIC_API_KEY`
    + `ACCESS_CODE` secrets, Anthropic spend cap, confirm Analytics Engine on the plan, `npm test`, `npx
    wrangler deploy`; (2) set `CHAT_API_URL` in `build_chatbot.py`, run it + `build_index.py`, push (the
    home-page card appears); (3) re-run `worker/retest/acceptance-probe.mjs` against the deployed Worker and
    read the transcripts; (4) the Word syllabus + D2L PDF hand steps above.
  - **Open decisions:** the "confirm-my-guess" dial (seen live in probe A10: "the loop line you wrote is built
    correctly"); and review of the stylometry handout + notebook (`materials/stylometry/`), still marked
    "DRAFT" with pre-re-pacing "Day 7" / "Week 4" references (Track B context maps them to Day 8 / capstone
    weeks). Watch reply length with real students (~250–450 words in the probe).

**Lane E — the six judgment calls the 2026-09-05 audit left open (needs your voice, not mechanics).**
The mechanical fixes shipped; these change what the assignments *say*, so they were not applied
unilaterally. In priority order:
1. ✅ **HW3 tone vs. stance — FIXED 2026-09-28.** HW3 is reframed around **tone** (title, intro, Part B
   heading, B4, C1). **B3** now has students hand-label the stance of the 5 warmest and 5 coldest
   comments, which reproduces the code-along's Part 4 on real data. On the course corpus the warmest 5
   are 4 oppose / 0 support. The key's "sentiment disentangles support and opposition" claim is gone.
   HW4's two support/oppose lines were fixed to match. Keys commit carries the builders.
2. ✅ **Day 3 / Day 4 split — FIXED 2026-09-28.** `Lists_Loops_Conditionals` reordered to
   Conditionals → Lists → Loops so it matches the calendar (the calendar was kept because the lecture
   pairing — ml3 "Classification Logic" / ml5 "Collective Memory" — belongs with the days). The two
   `platforms`-dependent `in` checks now use strings (a Day-2 callback); added a Day-3 "your turn" and a
   "🛑 Day 3 stops here" marker. Filename unchanged, so Colab links still resolve.
3. ✅ **Topic Modeling toy corpus — FIXED 2026-09-28.** The 15 toy comments were rewritten so the three
   themes share no vocabulary. Seed 42 on gensim 4.4.0 now files all 15 correctly (it was 12/15); across
   seeds, 54/100 are clean (it was 15/100). A corpus this size tops out around 75%. The prose now says the
   split depends on the seed, and explains why.
4. ✅ **Term Frequency "distinctive words" — FIXED 2026-09-28.** The cell now checks the comments' top 8
   against the official text's *full* vocabulary, using a loop with `if` (no set comprehension). Output:
   7 distinctive, 1 shared (**religion**). A new sentence names that shared word as where the two voices meet.
5. ✅ **False provenance — FIXED 2026-09-28.** Term Frequency's setup now says `split_into_words` and
   the long `stopwords` list are **new on Day 7** (HW1 A6 previewed five words), and that `Counter` is
   from the end of Day 5. HW2's setup, tool list, and A5 header were corrected to match. HW2's prep list
   now cites the Term Frequency and Dictionaries & Functions code-alongs. HW3's "you built in HW2" is now
   "you used". The syllabus maps Day 5 → "HW2 · every HW after" (HW1 has no `def`).
6. ✅ **Smaller items — FIXED 2026-09-28.** List comprehensions are taught once in Term Frequency,
   next to the Day-4 loop version. Day 9 is relabeled "HW2 (+ optional C2: text of your own)"; students
   don't collect their own data until Day 12. HW4 C2 now revisits the Day-18 proposal instead of planning
   it, and the capstone sheet was fixed to match. Cosmetic fixes: Term Frequency's word order now matches
   its output; VADER has notes on why the "mixed" line scores high (*pointless* is not in the lexicon,
   *honestly* is rated positive) and why four demo comments score 0.000 ("no evidence," not "no opinion").

**Lane E is closed.**

⚠️ **Any HW2–4 change goes through `_build_hw2/3/4.py` in `../WRIT20833_2026_keys`, never the `.ipynb`.**
See the new root `CLAUDE.md` §1.

**Lane D — pre-launch checks not in this repo.** **D2L tooling BUILT and both packages IMPORTED 2026-09-28** (`.imscc` + assignments `.zip`); hand-wiring not done.
**▶ Resume here (D2L, left mid-task 2026-09-28):**
1. **Layout decision pending.** The shell holds the *second* import (single-column pages, images uncropped).
   Commit `85e193e` switched pages + widget to a two-column layout (image beside title/buttons). Choose:
   (a) re-paste the widget only (`d2l/WRIT20833_Fall2026_D2L-homepage-widget.html`, via Widgets → Course
   Welcome → Content → `</>`); (b) also swap *How this course works* by hand (source:
   `d2l/WRIT20833_Fall2026_D2L/content/pg_0001.html`); or (c) third import — permanently delete Start Here,
   Weeks 1–8, Homework and Capstone; import `python3 d2l/build_d2l_package.py --modules
   start,1,2,3,4,5,6,7,8,homework --out d2l/WRIT20833_Fall2026_D2L_replace`; drag Discussions to the bottom.
   Build products are gitignored — rebuild them first on a fresh clone.
2. **Widget:** created and active on a copied homepage; default D2L banner still above it (remove via its ⋯
   menu, or keep). "New here?" line not yet a Quicklink (and any Quicklink breaks if Start Here is re-imported).
3. **Still unconfirmed:** discussion topics landed in Discussions (checklist §1); Nov 1 date spot-check (§2).
4. **Then checklist §3–5:** discussion dates, 3-point grade scheme + 12 grade items, syllabus PDF.
`d2l/build_d2l_package.py` (cartridge: Start Here, Weeks 1–8, Homework and Capstone, the 4 discussion
topics) and `d2l/build_assignments.py` (9 folders: HW1–4, R1–3, capstone proposal, capstone) are
adapted from WRIT 40363's `d2l/` and read every date and prompt from the schedule and syllabus. Next:
hand-wire the grade scheme, 12 grade items, discussion dates,
syllabus PDF and homepage widget per **`d2l/WIRING_CHECKLIST.md`**. ⚠️ The CC discussion topics are
**unverified** on TCU's instance (checklist §1 has the fallback). Two calls to confirm there: discussion
deadlines = start of class, and the extra capstone-proposal folder. Remaining Lane D items: the
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
picking; Lane E, the 2026-09-05 continuity audit's judgment calls, is closed as of 2026-09-28), then
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
