# WRIT 20833 — Intro to Coding in the Humanities
## "When Coding Meets Culture: Developing Data-Driven Opinions" — Fall 2026

> **DRAFT for instructor review — aligned to the AddRan Simplified Syllabus Template (section order and
> all) and the F25 WRIT 20833 syllabus.** Official University-policy text (Title IX, Disability/Access,
> Religious Observations, Academic Conduct, Emergency Response, Recording) is **not pasted** — per
> AddRan, it lives behind the **Student Resources & Policy Information** QR/link below; the syllabus
> carries only course-specific policies. Instructor/registrar fields are filled (section 020, meeting time,
> room, contact, etc.). **For AddRan submission:** the
> maintained Word copy is `WRIT20833-020_Fall2026_Rode.docx` (edited directly in Word — it holds the QR image + template
> formatting; mirror any later edits here into it). Tables/images must meet TCU accessibility guidelines
> (https://cte.tcu.edu/resources/accessibility/).

---

## Course Information
| | |
|---|---|
| **Course Title** | Intro to Coding in the Humanities — "When Coding Meets Culture" |
| **Prefix · Number · Section** | WRIT · 20833 · 020 |
| **Semester & Year** | Fall 2026 (second 8-week session, "8W2") |
| **Course Component Type** | LCL |
| **Credit Hours** | 3 (lower-division undergraduate) |
| **Class Meeting Days & Times** | **Monday / Wednesday / Friday, 10:00–11:50 AM (Central), October 19 – December 18, 2026** — **in person** (24 sessions; attendance is expected). No class the week of Thanksgiving (Nov 23–27). |
| **Class Location** | Schar Hall, Room 2003 |
| **Prerequisites** | None — **no prior coding experience assumed** |
| **Final Evaluative Exercise** | The **capstone** (data-driven-opinion notebook + short essay), presented and due on the final day, **Fri December 18**. There is no separate final exam. |
| **Other Important Dates** | **Thanksgiving break (no class):** Nov 23–27 (classes recess after Fri Nov 20, resume Mon Nov 30). **Final drop deadline:** Thu Nov 19. Any other deviations announced on TCU Online. |

**Instructor:** Dr. Curt Rode · **Office Location:** Schar 2006 · **Office Hours:** By appointment — https://calendly.com/c-rode/appointments
**Telephone:** 817-257-6983 · **Email:** c.rode@tcu.edu · **Preferred Contact:** Email
**Response Time:** within 24 hours on weekdays (longer on weekends and holidays)
**Course site & submissions:** **TCU Online** (D2L) — d2l.tcu.edu. **Code runs in:** Google Colab (free; needs a Google account).

*Note for students:* The syllabus is your first course reading — it orients you to the flow and
expectations of the course. Turn to it for details on assignments and policies.

### Student Resources & Policy Information
[![Student Resources & Policy Information — scan for TCU student resources and university policies](https://cte.tcu.edu/wp-content/uploads/TCU-Syllabus-Policies-Resources.png)](https://cte.tcu.edu/wp-content/uploads/TCU-Syllabus-Policies-Resources.png)

**Click or scan the QR code** for resources to support you as a TCU student. Please note especially the
sections on **Student Access and Accommodation**, **Academic Conduct & Course Materials Policies**, and
**Emergency Response & TCU Alert**. The University's official policies — including **Anti-Discrimination
& Title IX**, **Religious Observations & Holidays**, **Disability/Access**, and **Recording of Class
Sessions** — are provided there and apply to this course.

---

## Land Acknowledgment
TCU acknowledges the many benefits, responsibilities, and relationships of being in this place, which we
share with all living beings. We respectfully acknowledge all Native American peoples who have lived on
this land since time immemorial. TCU especially acknowledges and pays respect to the Wichita and
Affiliated Tribes, upon whose historical homeland our university is located.

---

## Course Description
**From the official course catalog:** *This course is designed as an introduction to coding for students in the Humanities and/or the Digital Culture and Data Analytics (DCDA) Minor. Students will be introduced to the basics of a computer programming language (such as Python or R) as they pertain to the intellectual, cultural, and creative work central to the Humanities.*

This offering of the course is an invitation to *think with code* about culture. Over eight weeks you'll learn
enough Python to ask real humanistic questions of real text — social-media comments, public documents,
your own chosen corpus — and to argue from what you find. We move from **predictions** to
**computational analysis** to **data-driven insight**, always asking not just *what the code does* but
*what it assumes, what it reveals, and what it flattens.* The deeper aim: to **hear the human at scale**
— to listen to more voices than close reading alone could reach, while staying honest about what
computation flattens from view. No prior coding experience is needed; bring curiosity and a willingness
to be wrong out loud.

**Prerequisites & Concurrent Enrollment.** None — no prior coding experience assumed.

**Program & Major Connections.** This course satisfies the coding requirement for the Digital Culture and Data Analytics major and minor. It also satisfies elective requirements for the English and Writing majors and minors.

### TCU Core Curriculum — Citizenship & Social Values (CSV) and Humanities (HUM)
This course carries **two** TCU Core Curriculum designations.

**Citizenship & Social Values (CSV).** It meets the CSV student learning outcome —
**"examine the knowledge, skills, values, or motivation needed to participate or lead within diverse
communities"** — by having you form, argue, and reflect on **evidence-based opinions about a real
public-policy debate**, weighing the values and rights of the individuals and groups whose voices you
analyze. *(Evidence: the capstone essay, the four threaded discussions, and the three reflections.)*

**Humanities (HUM).** It meets the Humanities student learning outcome — **"use humanistic modes of
inquiry to analyze human experiences and expressions across space and time"** — by teaching you to read
real human expression both closely and at scale: you interpret cultural texts (public comments, a
founding document, a corpus you choose), move between contemporary voices and historical ones, and ask at
every step what computation reveals and what it flattens. *(Evidence: the homework analyses, the capstone
notebook + essay, and the close- vs. distant-reading work.)*

---

## Course Materials
**Required (no textbook to buy):**
- **Google Colab** (free) — runs every notebook in your browser; no installation. Needs a Google account.
- **TCU Online (D2L)** — readings, the four threaded discussions, and all submissions.
- A laptop you can bring to class (any OS — everything runs in the browser via Colab).
- **No additional costs.** All course materials (notebooks, tutorials, data) are provided in the course.

**A self-contained course.** Everything you need is *in this course* — our own code-along notebooks,
short tutorials, and homework. Melanie Walsh's open *Introduction to Cultural Analytics* is a wonderful
model and is offered as **optional** further reading, but nothing you're evaluated on requires an
outside book.

---

## Teaching Philosophy & Methodology
Each 2-hour in-class session follows the same rhythm:
- **~25 min — concept / mini-lecture:** the idea and the culture question behind it.
- **~70 min — live code-along:** we build it together; you type as we go.
- **~25 min — application + share:** you apply it to real text and we compare notes.

Four threads run through the course: (1) our notebooks serve as the "textbook"; (2) a critical frame
each day (code is not neutral; classification logic; AI agency; collective memory; what counting hides);
(3) tutorials bridging concept and culture; (4) homework applying the skills to a cultural dataset —
ideally **one you choose** and carry across the whole term. The course is built around an honest
question rather than a tidy answer: every computation we run, we immediately ask *what did this flatten,
who chose this, can we trust it?* — which is why it's evaluated by **ungrading** (below).

---

## Learning Outcomes
By the end of the course you will be able to:
1. **Read and write basic Python** — variables, conditionals, loops, functions, and lists/dictionaries.
2. **Work with real data** in pandas — load, clean, and explore a text dataset you collected.
3. **Run three methods of computational text analysis** — term frequency, sentiment analysis (VADER),
   and topic modeling (LDA) — and **integrate** them into a single interpretation.
4. **Borrow and judge tools critically** — use libraries and AI-written code you didn't build, and
   evaluate whether to trust their output.
5. **Make a data-driven argument** about a cultural text, **represent the voices in your data
   responsibly** (including their disagreements), and **name the limits** of your own methods.
6. **Reflect on your learning** — assess your own growth honestly (see *Grading*).

**TCU Core outcomes.** This course carries two Core designations:
- **CSV** — *Examine the knowledge, skills, values, or motivation needed to participate or lead within
  diverse communities.* (Met via outcomes 5–6 and the capstone/discussions/reflections.)
- **HUM** — *Use humanistic modes of inquiry to analyze human experiences and expressions across space
  and time.* (Met via outcomes 2–3 and 5 and the homework analyses + capstone.)

---

## Course Requirements

### Assignments
Each assignment is described below and connects to the learning outcomes; you submit and view feedback
through **TCU Online**: submit homework notebooks and reflections in the **Assignments** area and post to the weekly **Discussions**; your marks and my feedback appear in **Grades**.

| Work | How many | What it is | Course outcomes | Core (CSV · HUM) |
|---|---|---|---|---|
| **Homework notebooks (HW1–HW4)** | 4 | Hands-on skill practice, each with a short reflective write-up. | 1–4 | HUM |
| **Weekly Experiments** | within each HW | 2–3 small original explorations of your own — *the heart of the ungrading*. | 1–5 | HUM |
| **Self-reflections** | 3 | Where you're starting · the halfway check · the final self-evaluation. | 6 | CSV |
| **Threaded discussions (TCU Online)** | 4 | One every other week (Weeks 1, 3, 5, 7), on a culture question — a post + replies to peers. | 4–5 | CSV |
| **Capstone (final evaluative exercise)** | 1 | A notebook analysis of your own cultural dataset (or a stylometry corpus) + a short data-driven-opinion essay, presented on the last day (full sheet: `CAPSTONE_2026.md`). Replaces a final exam. | 2–6 | CSV · HUM |

*(Outcome mapping per AddRan: every learning outcome is exercised by an assignment above. The **CSV** core
outcome is met by the discussions, reflections, and capstone; the **HUM** core outcome by the homework
analyses and the capstone — the forms of evidence each core submission cites.)*

**The three self-reflections** (≈300–500 words each, submitted to TCU Online — central to ungrading):
1. **Reflection 1 — "Where I'm starting" (due Fri 10/23).** Prior experience (likely none — fine), what
   excites or worries you, and a prediction: what can and can't computers tell us about culture?
2. **Reflection 2 — "Halfway" (due Mon 11/16).** What's clicking and what's hard? Revisit your early
   prediction. What will you do differently in the second half?
3. **Reflection 3 — "Final self-evaluation" (due Fri 12/18).** Review your own body of work and make an
   evidence-based case for the final grade you've earned (see *Grading Scale*).

**The four threaded discussions** (open Monday of their week; **initial post by Wednesday, two
substantive replies by Friday**):
1. **D1 (Wk 1) — Is code neutral?** When a program sorts people or words into categories, whose judgment
   is built in?
2. **D2 (Wk 3) — Whose data?** The ethics of collecting public text, and what it means to read (and fix)
   code an AI wrote for you.
3. **D3 (Wk 5) — Close vs. distant reading.** What does counting/sentiment let you see that reading by
   hand can't — and what does it flatten?
4. **D4 (Wk 7) — What computation reveals and hides.** Share your capstone finding and one thing your
   methods get wrong. *(The course is designed for 4 discussions; D4 may be dropped to a 3-discussion
   minimum if end-of-term capstone load is heavy.)*

### Grading Philosophy (ungrading)
This course uses **ungrading**. Through the term your work is **not** scored with points; each piece is
marked on a simple **3-point scale**, and my feedback focuses on your engagement, reflection, and growth
— not on whether your code or analysis was "right." *(Documenting a failure and what you learned counts
as meeting expectations.)* The goal is **earned insight over clean code.**

**Per-piece marks:**
- **3 — Exceeds expectations:** goes beyond the ask — depth, insight, intellectual risk-taking.
- **2 — Meets expectations:** does the work with genuine, honest engagement. *This is success and the
  expected standard.*
- **1 — Does not yet meet:** missing, incomplete, or minimal. The "not yet" is an invitation to revise
  where time allows.

### Late Work
Because sessions build on each other, keep up — but ungrading is about the whole
arc, not single due dates. If life happens, **talk to me**; honest communication beats a missed
deadline, and we'll find a reasonable way for you to complete the work. **Official University Absences**
are always accommodated (see *Attendance & Engagement*, next).

### Attendance & Engagement
This is a fast-moving course that meets three days a week and builds session to session; attendance and
active engagement in class are expected, and your engagement is reflected throughout your marks (there is
no separate points-based participation grade). In this course, "engaged" means showing up to class, coding
along, posting and replying in discussions on time, and documenting your thinking in your `#comments`
and reflections. If you must miss a session, let me know in advance and we'll arrange a catch-up.

**Official University Absences** are those described in the Official University Absence Policy and
include Title IX–related issues, military leave, holy days, and university-related absences. Students
entitled to such absences may work with me to complete missed work within a reasonable time after the
absence.

**Medical privacy.** Because it is considered an infringement on student privacy for me to have access
to student medical records, I cannot accept medical documentation to justify absences. If you have a
legitimate reason for an absence and want to provide verification, please use the **Absence
Documentation Form** through the **Dean of Students Office**.

### Course Assignments & Final Grade
Because this course uses **ungrading**, individual assignments carry **no point values** — the column a
conventional syllabus fills with points is replaced here by the 3-point engagement scale, and the final
letter is set from the *pattern* of those marks (below), not from a points total.

| Component | How many | How it's evaluated | Role in the final grade |
|---|---|---|---|
| **Homework notebooks (HW1–HW4)** | 4 | 3-point scale — engagement + reflection | Core of the body-of-work floor |
| **Weekly Experiments** (within each HW) | 2–3 per HW | 3-point, as part of each homework | The heart of the ungrading |
| **Threaded discussions (D1–D4)** | 4 | 3-point — initial post + two replies | Part of the floor |
| **Self-reflections (R1–R3)** | 3 | 3-point; **R3** is the final self-evaluation | R3 sets the plus/minus |
| **Capstone** (final evaluative exercise) | 1 | 3-point; presented Fri 12/18 | Weighted most heavily in the holistic judgment |

*(The capstone is the course's Final Evaluative Exercise — there is no separate final exam.)*

TCU requires a final letter grade. Here is exactly how it is set — no mystery:

**1. Your pattern of marks sets a whole-letter floor.** The "body of work" = the four homeworks (with
Weekly Experiments), the three reflections, the four discussions, and the capstone.

| Marks across the body of work | Grade floor |
|---|---|
| All **2s and 3s** (everything meets; several exceed) | **A** band |
| Mostly **2s**, a few **1s** | **B** band |
| Several **1s** (multiple pieces not yet meeting) | **C** band |
| Many **1s** / large portions missing | **D / F** range |

"Engaged" means real effort and honest documentation of your process — *not* polish. Something that
doesn't fully work, paired with a clear account of what you tried and learned, **meets expectations.**

**2. Your final self-evaluation (Reflection 3) sets the plus/minus.** You make an evidence-based case for
the precise grade you've earned: consistent **3s** argue toward the top of your band (A, B+, C+);
**mostly 2s** sit at the mid-to-minus (A‑, B/B‑, C/C‑). The floor is a guarantee you can count on; the
self-evaluation is where you make your case for more. I confirm or adjust.

### Grading Scale
**Grading Scale (TCU undergraduate, plus/minus):** A 94–100 · A‑ 90–93.99 · B+ 87–89.99 · B 84–86.99 ·
B‑ 80–83.99 · C+ 77–79.99 · C 74–76.99 · C‑ 70–73.99 · D+ 67–69.99 · D 64–66.99 · D‑ 60–63.99 · F below 60.
*(No individual piece carries points; these percentages describe only the final letter, set as above.)*

**Grading Concerns.** Because the course is ungraded, there's nothing to "dispute" point-by-point — but my
feedback is always open to conversation. If a comment doesn't sit right, email me at
c.rode@tcu.edu and we'll talk it through: since each piece is evaluated on engagement and reflection rather than a
right answer, the conversation is about what the work shows and how to strengthen it moving forward. The
final letter grade isn't handed down unilaterally — you make an evidence-based case for it in your final
self-evaluation (Reflection 3), and I confirm or adjust. For the University's formal grade-appeal
procedure, see the **Student Resources & Policy Information** link above.

---

## Course Policies
*University policies — **Anti-Discrimination & Title IX**, **Disability/Access**, **Religious
Observations**, **Academic Conduct**, **Recording of Class Sessions**, and **Emergency Response & TCU
Alert** — are provided through the **Student Resources & Policy Information** QR/link in *Course
Information* above, and apply to this course. (The University-Absence and Medical-Privacy statements are
under *Attendance & Engagement*.) Below are the course-specific policies.*

### Class Norms
**Course-specific note (important).** Our running dataset is real public comments about a 2025 law
placing the Ten Commandments in Texas classrooms — a genuinely contested topic touching religion and the
state. We analyze this language as **data about a public debate**, and a goal of the course is to *hear*
the people in the data — including those we disagree with — rather than flatten them. Treat classmates'
views, and the views in the data, with respect; advance disagreements with evidence and care. You're
welcome to choose a different cultural dataset for your own work. In class and in our TCU Online
discussion spaces, respect confidentiality and the ownership of others' words (no screenshots or
re-sharing of classmates' posts outside the course).

### Artificial Intelligence (AI / LLM) Use Policy
You **may** use AI tools (ChatGPT, Claude, Copilot, etc.) — this course literally teaches you to read and
improve AI-written code. The rule is **understanding, not avoidance**, and it differs by *what* you're
borrowing:
- **Code — borrowing is expected.** Using a library, Stack Overflow, or an AI to help write code is
  normal practice. You must be able to **explain any code you submit**, and you should **note in your
  `#comments` where you used AI** and what you changed. Passing off code you can't explain is not allowed.
- **Writing — develop your own voice.** Your reflections, discussion posts, `#comments`, and the capstone
  essay are where you *become a writer.* A unique voice is forged through the difficulty of finding your
  own words; letting AI generate your writing forfeits that. **Use AI for feedback if you like, but the
  writing itself must be yours.** When in doubt, ask.

### Technology & Recording
- **Technology.** Bring a laptop that can run a web browser — all code runs in **Google Colab**, so
  there's nothing to install. If your device fails in class, let me know and pair with a classmate; you
  can also reach me on TCU Online to catch up on anything you miss.
- **Recording of class sessions.** This is an in-person course and class sessions are not routinely
  recorded. The University's official **Recording of Class Sessions** policy is in *Student Resources &
  Policy Information* above; if you have an accommodation to make your own recordings, see *Student Access
  and Accommodation* there.

### Academic Conduct
The University's academic-conduct policy is in *Student Resources & Policy Information* above (under
**Academic Conduct & Course Materials Policies**). In this course specifically: **borrowing code is
expected; submitting work (code or writing) you cannot explain, or that isn't yours, is not.** Cite your
sources, including AI.

---

## Course Schedule (24 sessions)
*Each row is one class day. "Due" items are due by the start of class that day unless noted; discussion
threads open Monday of their week. **No class the week of Thanksgiving (Nov 23–27).** The schedule may be
adjusted to the class's pace; changes are announced on TCU Online. A standalone version is in
`COURSE_SCHEDULE_2026.md`.*

### Python skills map — what's taught when
*Each skill is introduced in a class code-along, then practiced in the linked homework. Nothing is
assessed before it's taught.*

| Skill | First taught | Practiced in |
|---|---|---|
| Variables & data types | Day 1 (Mon 10/19) | HW1 · all later work |
| Strings & string methods | Day 2 (Wed 10/21) | HW1, HW2 |
| Comparisons & conditionals | Day 3 (Fri 10/23) | HW1 |
| Lists & loops | Day 4 (Mon 10/26) | HW1, HW2 |
| Functions & dictionaries | Day 5 (Wed 10/28) | HW1 · every HW |
| Counting & term frequency | Day 7 (Mon 11/2) | HW2 |
| pandas DataFrames | Day 10 (Mon 11/9) | HW3, HW4, capstone |
| Cleaning & `.apply()` | Day 11 (Wed 11/11) | HW3, HW4 |
| Sentiment (VADER) | Day 13 (Mon 11/16) | HW3 |
| Grouping & charts | Days 11–17 | HW3, HW4 |
| Topic modeling (Gensim LDA) | Day 16 (Mon 11/30) | HW4, capstone |

### Week 1 (Oct 19–23) — Python foundations: "code is not neutral"
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 10/19** (1) | Humanities & Coding · Connotations & Code | Setup + Variables & data types | D1 opens |
| **Wed 10/21** (2) | — | Strings & string methods | D1 post |
| **Fri 10/23** (3) | Classification Logic | Comparisons, conditionals & booleans | **R1 due** · D1 replies |

### Week 2 (Oct 26–30) — Python foundations: collections & reusable tools
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 10/26** (4) | Collective Memory | Lists & loops | — |
| **Wed 10/28** (5) | — | Functions & dictionaries | — |
| **Fri 10/30** (6) | — (recap) | Foundations recap + practice | **HW1 assigned** |

### Week 3 (Nov 2–6) — From text to data: term frequency & AI
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 11/2** (7) | Data as evidence *(brief framing)* | Term frequency + HW1 debrief | **HW1 due** · **HW2 assigned** · D2 opens |
| **Wed 11/4** (8) | AI Agency | Reading & improving AI code + stylometry seed | D2 post |
| **Fri 11/6** (9) | — | HW2 work session (term frequency on your data) | D2 replies |

### Week 4 (Nov 9–13) — Found data, ethics & pandas
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 11/9** (10) | Data Archaeology | Found data + collection ethics (pandas 01 + scraping) | **HW2 due** |
| **Wed 11/11** (11) | — | Data cleaning (pandas 02) | — |
| **Fri 11/13** (12) | — (workshop) | Workshop: collect & clean **your** dataset | — |

### Week 5 (Nov 16–20) — Computational text analysis: sentiment
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 11/16** (13) | Quantifying connotation | Sentiment with VADER | **R2 due (midterm)** · **HW3 assigned** · D3 opens |
| **Wed 11/18** (14) | Close vs. distant reading | VADER deep dive | D3 post |
| **Fri 11/20** (15) | Predictions on the record | HW3 work session (freq + sentiment on your data) | D3 replies |

*— Thanksgiving break: no class Nov 23–27 (resume Mon Nov 30) —*

### Week 6 (Nov 30 – Dec 4) — Topic modeling & integration
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 11/30** (16) | NLP & Topic Modeling | Topic modeling intro (Gensim LDA) | **HW3 due** |
| **Wed 12/2** (17) | — | Topic modeling deep · `num_topics` · limits | **HW4 assigned** |
| **Fri 12/4** (18) | Integration (close → distant → close) | Freq + sentiment + topics + stylometry demo | **Capstone proposal due** |

### Week 7 (Dec 7–11) — Going public & capstone development
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 12/7** (19) | Going Public | Validation · "being wrong as learning" · capstone framing | **HW4 due** · D4 opens |
| **Wed 12/9** (20) | — | Capstone work session 1 | D4 post |
| **Fri 12/11** (21) | — | Capstone work session 2 | D4 replies |

### Week 8 (Dec 14–18) — Capstone
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 12/14** (22) | — | Capstone work session 3 + peer review | — |
| **Wed 12/16** (23) | — | Capstone polish + presentation dry-run | — |
| **Fri 12/18** (24) | — (wrap) | **Capstone presentations + wrap** | **Capstone due** · **R3 (final self-evaluation) due** |

*Lecture "—" = recap / workshop / work-session days (Day 2 included — "Sacred Boundaries" was cut, its
material folded into the Day-10 and Day-1 lectures). "Going Public" anchors Day 19 (analysis → public
argument → the capstone); "Code as Rhetoric" was folded into the Day-1 and Day-19 lectures. See
`planning/CONCEPTUAL_FRAMEWORK_2026.md`.*

---

> *This syllabus is a working plan and may be adjusted to fit the class's pace; changes will be announced
> in class and on TCU Online.*
