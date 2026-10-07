# Plan: make `TCU-DCDA/WRIT20833_2026` private without breaking the course site

**Status:** proposal, 2026-10-07. Nothing done. **The visibility flip is the instructor's call** (CLAUDE.md §7).

## What survives a private repo, and what doesn't

The org is on GitHub **Team**, which serves Pages from a private repo, and the site stays publicly readable.
So `https://tcu-dcda.github.io/WRIT20833_2026/` (the dashboard, schedule, lecture pages, slides, Code Guide
page) keeps loading. The Code Guide Worker is unaffected: it checks the page's origin, not the repo.

What breaks is everything that reaches **into the repo** instead of into `docs/` (measured 2026-10-07):

| Breaks | Count | Used by |
|---|---|---|
| Images loaded from `raw.githubusercontent.com/...` | 26 URLs | lecture pages, slides, dashboard thumbnails (`build_lectures.RAW`, `build_index`) |
| "Open in Colab" links (`colab.research.google.com/github/...`) | 14 on the site; badges in 15 notebooks | dashboard, schedule, D2L, each notebook's first cell |
| `github.com/.../blob` or `/tree` links | 5 | syllabus, capstone sheet, stylometry handout, `notebooks/data` |
| Notebook data loaders' download fallback (`raw.githubusercontent.com/.../notebooks/data/`) | HW2, HW3, HW4 | Colab, where the data file isn't local |
| The live D2L shell | ~45 URLs | imported 2026-09-28 from `d2l/build_d2l_package.py`; widget |

**Colab is the hard constraint.** It opens GitHub notebooks only from repos the student can read, so the
notebooks need a public home somewhere.

## First, the question that picks the option

**What should stop being public?** If it's the instructor-side material (`planning/`, the WORKLOG, review
notes, `d2l/` tooling), Option A is far cheaper. If it's the whole repo, history included, it's Option B.
Note: Option A does **not** remove what is already in the public history.

### Option A — keep this repo public; move instructor material out (≈1 hr, nothing breaks)

1. Move `planning/`, `d2l/` (the generators and checklist) and any instructor notes to a private repo (the keys
   repo, or a new private `WRIT20833_2026_ops`). Keep the student-facing files and the generators that build
   `docs/` here.
2. Update `CLAUDE.md`, `README.md` and the guard workflow to match.
3. If old history must also go, that's a history rewrite, which has failed here before (2026-09-03/04: GitHub
   kept serving unreachable objects). It would need the rename-and-republish route again. Avoid unless necessary.

### Option B — make this repo private; give students a public mirror (≈4–6 hrs + D2L time)

**Phase 1 — make `docs/` self-contained** (no student link into the repo):
- Generators copy the images (`materials/lectures/images/`, `materials/images/`) into `docs/assets/` and link
  them relatively; `RAW` goes away. Keep `site_theme.assert_accessible()` passing.
- Render `SYLLABUS_2026.md`, `CAPSTONE_2026.md` and the stylometry handout as pages in `docs/` with the lecture
  renderer; repoint the five `GH_BLOB` links. (The Word/PDF syllabus in D2L stays the official copy.)
- Copy `notebooks/data/*.txt` to `docs/data/`; replace the `notebooks/data` tree link with a small data page.

**Phase 2 — notebooks get a public home**:
- Create a public mirror, e.g. `TCU-DCDA/WRIT20833_2026_notebooks`, holding **only** the student notebooks and
  the data. A sync script here copies them over and pushes; the mirror gets the same guard workflow (no
  `*_ANSWER_KEY*`, no builders). Never sync the `_complete` copies unless intended.
- Repoint every Colab link and badge to the mirror, and the HW2–4 download fallback to
  `https://tcu-dcda.github.io/WRIT20833_2026/data/` (served by Pages, no repo access needed). Edit the
  code-along builders here, HW1 directly, and `_build_hw2/3/4.py` in the keys repo; rebuild and copy back.
- Students' already-saved Colab copies keep working; only fresh opens use the new links.

**Phase 3 — D2L**: rebuild the packages so they point only at Pages and the mirror. D2L imports are additive,
so follow `d2l/WIRING_CHECKLIST.md` → *Updating a live shell* (hand-edit links, or delete and re-import the
affected modules); re-paste the homepage widget.

**Phase 4 — verify before the flip, while the repo is still public**: an anonymous link check of every URL in
`docs/` and the D2L packages must show **zero** links into `TCU-DCDA/WRIT20833_2026` (raw, blob, tree or
Colab). Open three notebooks from the mirror in Colab in a private window.

**Phase 5 — flip** (ask first). Settings → Visibility → Private; then confirm Pages still reports
`public: true` (`gh api repos/TCU-DCDA/WRIT20833_2026/pages`). Re-run the anonymous check. **Rollback:** flip
back to public; nothing else needs undoing.

## Timing

Option B touches every student entry point 12 days before Day 1 (Oct 19), plus the live D2L shell. If B is
chosen, the safest windows are (1) right now, before D2L hand-wiring makes the shell's links more work to
change, or (2) after the term ends Dec 18. Mid-term, avoid it.
