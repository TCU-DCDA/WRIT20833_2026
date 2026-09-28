# CLAUDE.md — working rules for this repo

WRIT 20833, "When Coding Meets Culture" (TCU, Fall 2026). A **public, student-facing**
course repo: syllabus, schedule, capstone sheet, 9 code-along notebooks, 4 homework
notebooks, mini-lecture pages, and a generated GitHub Pages site.

Orientation: `README.md` (what's here) · `planning/NEXT_SESSION.md` (what to do next) ·
`planning/WORKLOG.md` (decision log, newest entry on top) ·
`planning/CONCEPTUAL_FRAMEWORK_2026.md` (why the course is shaped this way).

---

## 1. Generated files — know what you are allowed to edit

Most of this repo is emitted from a generator. **Editing the output directly creates drift
that the next rebuild silently reverts.** This has already happened twice (HW3 on 2026-09-04,
HW2–HW4 on 2026-09-05); both were caught and closed, but only because someone went looking.
Check the table below *before* you open a notebook.

| You want to change… | Edit this | Then |
|---|---|---|
| A **code-along** notebook (`notebooks/codeAlongs/*.ipynb`) | its `_build_*.py` **in the same directory** | `python3 _build_<name>.py`, commit both |
| **HW2 / HW3 / HW4** (`notebooks/homework/*.ipynb`) | `_build_hw2/3/4.py` in the **private `TCU-DCDA/WRIT20833_2026_keys`** | run it there, copy the regenerated *student* notebook back, commit here |
| **HW1** | the `.ipynb` directly | — it has no builder |
| The **TCU Online (D2L)** shell | the source (schedule, syllabus, `build_index.py`, notebooks), or `d2l/build_d2l_package.py` / `d2l/build_assignments.py` | rebuild, then follow `d2l/WIRING_CHECKLIST.md` → *Updating a live shell*. D2L imports are **additive**; never re-import a full package onto a live shell |
| Anything in **`docs/`** | the markdown/lecture source + `build_index.py`, `build_schedule_html.py`, `build_lectures.py` | re-run the generators; never hand-edit `docs/` |

Two code-alongs (`Variables_DataTypes`, `Lists_Loops_Conditionals`) have **no builder** —
edit those `.ipynb` directly.

Check for drift before trusting a notebook: copy the builders to a scratch dir, run them
there, and `diff` against the committed notebooks. As of 2026-09-28 all seven code-along
builders and all three HW builders emit byte-identical output to what is committed (student
notebooks here *and* answer keys in the keys repo). The keys repo tracks only the keys and the
builders; the student notebooks it generates are untracked there.

The keys repo is cloned at `../WRIT20833_2026_keys`. Its builders write **both** the student
notebook and the answer key into the keys repo; only the *student* notebook is copied back
here. Never copy a `*_ANSWER_KEY.ipynb` into this repo — see §2.

## 2. Answer keys must never land here

Keys and the solution-bearing `_build_hw*.py` live **only** in the private
`TCU-DCDA/WRIT20833_2026_keys`. `.github/workflows/guard-instructor-files.yml` fails any
push that tracks them. It also fails on raw D2L exports (`D2LExport_*`, which carry the
course's org-unit id) and on built D2L packages (`*.imscc`, `d2l/WRIT20833_Fall2026_*`). A pull after a history rewrite reintroduced them once (2026-06) and
a public-visibility flip nearly shipped them (2026-09-03/04) — treat this as load-bearing,
not hygiene.

Related: this repo was **recreated on 2026-09-04**. Same owner, name, URL, and 153-commit
history, new object store. SHAs cited in WORKLOG entries before that date do not resolve.
The pre-scrub history survives only in the private `WRIT20833_2026_archive` — never make it
public.

## 3. Validating notebooks

Use plain `python3` on this machine (`/opt/anaconda3/bin/python`, cited in older WORKLOG
entries, does not exist here). The full stack is present: pandas 2.3.3 · numpy 2.0.2 ·
gensim 4.4.0 · vaderSentiment · matplotlib 3.9.4.

Executing a notebook top-to-bottom is not enough on its own — homework cells are mostly
`TODO` stubs, so they pass while teaching nothing. When you touch homework logic, **simulate
a completed student solution against the real corpora in `notebooks/data/`** and check that
the narrative claims (counts, "most positive," topic labels, which bar appears) actually
hold. The 2026-09-05 audit found several that did not.

The only expected error in any notebook is the intentional `TypeError` in
`Variables_DataTypes` ("read the error message carefully").

`jupyter`/`nbconvert` are **not installed**. To execute a notebook, `exec` its code cells in
order in one namespace, skipping `!pip` lines and using `matplotlib.use("Agg")`.

LDA output depends on the seed and on the gensim version. If you change a topic-modeling example,
check it at `random_state=42` *and* across many seeds; don't stop at "it looks fine once." Prose
must not promise a specific split.

## 4. Cross-references are a standing hazard

Notebooks cite each other and the calendar constantly — "Day 8," "next week," "the same
tools from HW1," "123 comments." These were ported from a 16-week course and re-paced to 8
weeks, so day numbers drift silently. **`COURSE_SCHEDULE_2026.md` is the source of truth**
for day numbers; `notebooks/data/README.md` for corpus facts. Any edit to
`SYLLABUS_2026.md` must also be made **by hand** in the Word syllabus
(`WRIT20833-020_Fall2026_Rode.docx`), which holds the AddRan template formatting. Grep for `Day \d`, `Week \d`,
and bare counts after any re-paced edit.

## 5. Voice and house style

- **Ungrading** — evaluate engagement, reflection, and labor, not correctness. No
  grade/points framing. "Errors are part of the work here, not something to hide."
- **Walsh-independent** — required work never depends on an outside textbook. Prep lists
  cite *our own* materials by their real titles.
- **Honest about borrowed code** — setup cells are "plumbing" (run it, don't read every
  line); students build a routine by hand once so they can *read and judge* the prefab or
  AI-written version later.
- **Structure** — homeworks: Part A/B/C + Weekly Experiments + Submit checklist.
  Code-alongs: warm cultural example → concept → code → "your turn" → Playground →
  "Sneak Preview: Where This Is Going."
- Every technique lands on the same humanistic question: *what did this flatten, who chose
  it, can you trust it?*

## 6. Site accessibility is enforced at build time

`site_theme.assert_accessible()` holds all UI text ≥ 12px and the muted tokens at WCAG AA
4.5:1. The generators **fail loudly** on a regression — retune the `THEME_CSS` palette
within those limits rather than working around the assertion.

## 7. Git

Solo maintainer: commit straight to `main`, no per-task branches or PRs. Regenerate `docs/`
after any content edit and commit the result alongside it.

**Ask before anything outward-facing** — force-push, visibility flips, publishing to
students, or touching the archive repo.
