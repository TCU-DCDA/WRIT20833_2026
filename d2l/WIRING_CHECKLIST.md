# WRIT 20833 Fall 2026 — TCU Online (D2L) shell wiring checklist

Instructor-only. Adapted from WRIT 40363's `d2l/WIRING_CHECKLIST.md`, which was tested
against a live Fall 2026 shell. Where this course differs, it says so.

> **Status, Fall 2026 shell:** §1 and §2 imported 2026-09-28 (both packages). **Not yet confirmed:**
> the discussion topics (§1 ⚠️) and the Nov 1 date spot-check (§2). Start Here + Weeks + Homework were
> re-imported once (uncropped images). §6 widget is live. §3–§5 not started. Resume point:
> `planning/NEXT_SESSION.md` → Lane D.

Two generators, two packages, one widget:

| Build | Carries | Import as |
|---|---|---|
| `python3 d2l/build_d2l_package.py` → `WRIT20833_Fall2026_D2L.imscc` | Start Here, Weeks 1–8, Homework and Capstone, the 4 discussion topics | Import Components → all |
| `python3 d2l/build_assignments.py` → `WRIT20833_Fall2026_Assignments.zip` | 9 submission folders in 3 categories, with dates | Import Components → **Assignments only** |
| (the first build also writes) `WRIT20833_Fall2026_D2L-homepage-widget.html` | the course homepage card | paste by hand (§6) |

Every item is a small landing page (a title, the site's one-line blurb, a button out to Colab,
the course site, or GitHub), not a copy of the content. Dates, titles and prompts are read
from `COURSE_SCHEDULE_2026.md`, `SYLLABUS_2026.md`, `CAPSTONE_2026.md`, `build_index.py`
and the notebooks themselves, so a source edit plus a rebuild keeps D2L in agreement. The
packages are gitignored build products; the generators and this file are what's tracked.

**Not carried, and hand-wired below:** discussion dates, the grade scheme, grade items, the
syllabus file, and the homepage.

## 1. Import the cartridge

Course Admin → **Import/Export/Copy Components** → **Import Components** → upload the
`.imscc` → import all.

Verify:

- Content shows **Start Here**, **Week 1 · …** through **Week 8 · …**, **Homework and
  Capstone**, and **Discussions**.
- Open any week overview; it should render the day list, not raw HTML.
- Open one notebook item (say *Term Frequency*, Week 3). You should see a titled page, a
  one-line description, a green **Open in Colab** button, and the "Save a copy in Drive" note.
- Open a mini-lecture (say *Humanities & Coding*, Week 1): the image, **Read the lecture**,
  and **Slides**. Images load from the public GitHub repo, so a broken image means the repo
  is unreachable, not that the package is wrong.

**⚠️ Unverified: the discussions.** WRIT 40363 had no discussions, so the Common Cartridge
discussion topics (`imsdt_xmlv1p3`) have never been imported on TCU's instance. Check:

- Under **Communication → Discussions** there should be four topics, *D1 (Week 1) · Is code
  neutral?* through *D4 (Week 7) · What computation reveals and hides*, each with its
  prompt and the post/reply deadlines in the text. Brightspace picks the forum name itself;
  rename it if it's unhelpful.
- **If they don't appear, or appear as broken Content items:** delete whatever landed, create the
  4 topics by hand, and paste each topic's text from
  `d2l/WRIT20833_Fall2026_D2L/discussions/dt_*.xml`. Then say so in this file, so the next term
  builds with `--modules start,1,2,3,4,5,6,7,8,homework` instead.
- **If they work:** delete this warning.

If topics import as downloadable files instead of rendering inline, the CC version handling
differs on this instance; the package can be rebuilt at CC 1.2.

## 2. Import the submission folders

Import Components → upload the `.zip` → select **only Assignments**.

This shell starts empty, so the categories are created by the package. That sidesteps
40363's category problem: Brightspace matches categories by an internal id, so importing
into a shell that already has a "Homework" category makes a second one.

Verify under **Assignments**:

| Category | Folders | Opens | Due |
|---|---|---|---|
| Homework | HW1 – HW4 | 12:01 a.m. on the day it's assigned | start of class (10:00 a.m.) on its due day |
| Self-Reflections | Reflection 1 – 3 | always | start of class |
| Capstone | Capstone proposal · Capstone: notebook + essay | always | start of class |

`python3 d2l/build_assignments.py` prints the exact dates. **Spot-check one date on each side
of Nov 1** (end of daylight saving): Reflection 1 (Fri 10/23) and HW2 (Mon 11/9) should both
show **10:00 AM**. If HW2 shows 9:00 or 11:00, the shell's time zone isn't Central; fix the
shell setting rather than the generator.

**No end dates, on purpose.** The late-work policy is "talk to me," so a late upload should
land flagged late, not bounce off a closed folder. Don't add end dates.

**The Capstone proposal folder is extra.** The original Lane D list named one capstone folder.
The proposal is a dated deliverable on the schedule (Fri 12/4), so it gets its own folder, but it
isn't in the body of work the final grade is read from. Don't give it a grade item (§4). Hide it
if you'd rather take proposals in class.

## 3. Discussion dates (by hand)

A package can't set discussion dates. Take them from the table at the end of
`python3 d2l/build_assignments.py`'s output. For each topic, set **start date** = its opens
day and **end date** none (same late-work reasoning). The post and reply deadlines are in each
topic's text.

> **Decision to confirm:** the text says the initial post is due by the **start of class**
> Wednesday and replies by the **start of class** Friday. That applies the syllabus's
> "due by the start of class unless noted" rule; the syllabus itself only says "by Wednesday
> / by Friday." If you mean end of day, change `discussion_body()` in
> `build_d2l_package.py` and rebuild just that module (see *Updating a live shell*).

## 4. Grade book

The syllabus (*Course Assignments & Final Grade*) says each piece gets a 3-point mark, the
marks show in **Grades**, and the final letter comes from the *pattern* of marks plus
Reflection 3's argument, not from a points total. So:

**Grade scheme:** Grades → Schemes → New. Name it *Ungrading (3-point)*:

| Symbol | Start % | Meaning |
|---|---|---|
| 1 — Not yet | 0 | Does not yet meet |
| 2 — Meets | 50 | Meets expectations (the expected standard) |
| 3 — Exceeds | 84 | Exceeds expectations |

(Out of 3, a 1 is 33%, a 2 is 67% and a 3 is 100%, so each lands in its own band.)

**Grade items (12):** Numeric, max 3, the scheme above, displayed as the **scheme symbol**,
not points. Put them in categories that match the syllabus's body of work:

- Homework: HW1, HW2, HW3, HW4 (Weekly Experiments are part of each HW's mark)
- Discussions: D1, D2, D3, D4
- Self-Reflections: R1, R2, R3
- Capstone: Capstone

Then link each assignment folder and discussion topic to its grade item (Edit → Evaluation
& Feedback → Grade Item). **Exclude every item from the final grade calculation**: no
points-based total should be visible, because none exists.

**Final grade:** release a manually entered **Final Adjusted Grade** only at term end, set by
the floor-plus-R3 procedure in the syllabus.

Check the student view (View as Student → Grades) once. It should show symbols like "2 —
Meets" and no percentage or points total. 40363 found that "not in the final grade" and
"the student sees the mark" are separate settings; confirm the second is on.

## 5. Syllabus file

Start Here links to `SYLLABUS_2026.md` rendered on GitHub, which is always current. The
AddRan Word syllabus (`SYLLABUS_2026.docx`) is a separate Lane D task: sync it to the
markdown, export a PDF, and upload the PDF to Start Here by hand. A rebuild never touches
an uploaded file, so re-upload after any syllabus edit.

## 6. Homepage widget

Course Admin → Homepages → Widgets → Create Widget → Content (source view) → paste
`WRIT20833_Fall2026_D2L-homepage-widget.html` → add the widget to the course homepage.
A cartridge can't set the homepage.

## 7. Announcements

The shell's org-unit id (`ou=`) is in the address bar of any course page. For a deadline, link
the assignments list rather than one folder:

```
https://tcu.brightspace.com/d2l/lms/dropbox/user/folders_list.d2l?ou=<OU>
```

Folder ids (`db=`) change every term and after a re-import; the list URL doesn't. Keep
announcement drafts out of this public repo if they carry the `ou`. 40363 keeps its drafts in
`course_admin/d2l_announcements/`, which is fine there because that repo is private.

## 8. Known gaps carried in from the repo

- **Days 13, 14, 15 and 18 have no lecture pages** (Lane B). Week 5 has no mini-lecture item,
  and Week 6 has only *NLP & Topic Modeling*. When a page is built and added to
  `build_index.LECTURES`, rebuild that week's module.
- **The stylometry notebook says "DRAFT exercise for review"** in its header and calls its
  handout the "Day-7" handout. The schedule puts that handout on Day 8. It's linked from Week 6
  and from Homework and Capstone.
- **`CAPSTONE_2026.md` still has `[to: upload location / TCU Online]`** (Lane C). Once §2 is done,
  the answer is "the *Capstone: notebook + essay* folder under Assignments in TCU Online."

## Updating a live shell

**D2L imports are additive.** There is no replace mode: importing the full cartridge again
duplicates every module, and importing the assignments zip again duplicates every folder.

| You changed | What to do |
|---|---|
| A notebook, lecture, or the capstone sheet's body | **Nothing.** The items link to the live copy. |
| A card blurb, a notebook's title, or a lecture thumbnail | Rebuild that module and re-import it (below). |
| The schedule: something moved days, or a lecture page was added | Rebuild the affected week module(s) and re-import. |
| A due date | Edit the folder's date **by hand in D2L** (and fix the schedule, the source of truth). Don't re-import the assignments zip. |
| A discussion prompt | Hand-edit the topic in D2L, or delete it and rebuild `--modules discussions`. |
| The syllabus | Re-upload the PDF (§5). |

### Partial re-import

```
# rebuild just week 5 after a schedule change
python3 d2l/build_d2l_package.py --modules 5 --out d2l/WRIT20833_Fall2026_week5
```

Selectors: `start`, `1`–`8`, `homework`, `discussions`, `all` (the default). Comma-separate to
combine: `--modules 3,4`.

In D2L, delete that module first, choosing **permanent** deletion (not "remove from
Content", or the old topics linger in Manage Files), then import the small package.
Delete first, then import, or you get the duplicates you were avoiding.
