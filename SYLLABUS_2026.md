# WRIT 20833 — Intro to Coding in the Humanities
## "When Coding Meets Culture: Developing Data-Driven Opinions" — Summer 2026

> **DRAFT for instructor review — structured to the TCU Online Syllabus Template (rev. 9/2024).**
> Two kinds of placeholder remain: `[...]` = instructor/registrar specifics (name, contact, links,
> credit hours), and **`[paste TCU standard text …]`** = official University policy boilerplate that
> must be copied verbatim from `Syllabus-Template-Online.docx` (do **not** paraphrase official policy).
> Course-specific content is complete. Any tables/images added must meet TCU accessibility guidelines
> (https://cte.tcu.edu/resources/accessibility/).

---

## Course Information
| | |
|---|---|
| **Course Title** | Intro to Coding in the Humanities — "When Coding Meets Culture" |
| **Prefix · Number · Section** | WRIT · 20833 · `[section]` |
| **Semester & Year** | Summer 2026 |
| **Course Component Type** | `[e.g., Lecture — confirm with registrar]` |
| **Credit Hours** | `[3 — confirm]` (lower-division undergraduate) |
| **Class Meeting Days & Times** | **Monday–Friday, `[time]`–`[time]`, July 6–31, 2026** — **online synchronous** (20 live sessions; attendance at the live sessions is expected) |
| **Class Location** | Online (synchronous via Zoom) |
| **Zoom Access** | `[Zoom link + meeting ID/passcode]` |
| **Prerequisites** | None — **no prior coding experience assumed** |
| **Final Evaluative Exercise** | The **capstone** (data-driven-opinion notebook + short essay), presented and due on the final day, **Fri July 31**. There is no separate final exam. |
| **Other Important Dates** | All activity occurs within the listed daily sessions; any deviations announced on TCU Online. |

**Instructor:** `[Name]` · **Office Location:** `[N/A — online / office]` · **Office Hours:** `[days/times; virtual — access instructions]`
**Telephone:** `[number]` · **Email:** `[email]` · **Preferred Contact:** `[email via TCU Online / TCU email]`
**Response Time:** `[e.g., within 24 hours on weekdays; longer on weekends/holidays]`
**Course site & submissions:** **TCU Online** (D2L) — `[course link]`. **Code runs in:** Google Colab (free; needs a Google account).

**Student Resources & Policy Information:** `[paste TCU standard Student Resources & Policy Information block — link + QR code — from Syllabus-Template-Online.docx]`

---

## Course Description
This course is an invitation to *think with code* about culture. Over four intensive weeks you'll learn
enough Python to ask real humanistic questions of real text — social-media comments, public documents,
your own chosen corpus — and to argue from what you find. We move from **predictions** to
**computational analysis** to **data-driven insight**, always asking not just *what the code does* but
*what it assumes, what it reveals, and what it flattens.* The deeper aim: to **hear the human at scale**
— to listen to more voices than close reading alone could reach, while staying honest about what
computation flattens from view. No prior coding experience is needed; bring curiosity and a willingness
to be wrong out loud.

`[Confirm against official course-catalog description.]`

**Program & Major Connections.** Introduces computational-text-analysis and data-literacy skills that
support further work in writing, the digital humanities, and any field that reads culture from data.

### TCU Core Curriculum — Citizenship & Social Values (CSV)
This course carries **CSV** core credit. It meets the CSV student learning outcome —
**"examine the knowledge, skills, values, or motivation needed to participate or lead within diverse
communities"** — by having you form, argue, and reflect on **evidence-based opinions about a real
public-policy debate**, weighing the values and rights of the individuals and groups whose voices you
analyze. *(Evidence: the capstone essay, the four threaded discussions, and the three reflections.)*
`[Confirm the exact outcome wording against the current CSV vetting on file.]`

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

**TCU Core (CSV) outcome:** *Examine the knowledge, skills, values, or motivation needed to participate
or lead within diverse communities.* (Met via outcomes 5–6 and the capstone/discussions/reflections.)

---

## Course Materials
**Required (no textbook to buy):**
- **Google Colab** (free) — runs every notebook in your browser; no installation. Needs a Google account.
- **TCU Online (D2L)** — readings, the four threaded discussions, and all submissions.
- A laptop with a reliable internet connection for the live sessions. `[TCU loaner-laptop info if applicable.]`
- **No additional costs.** All course materials (notebooks, tutorials, data) are provided in the course.

**A self-contained course.** Everything you need is *in this course* — our own code-along notebooks,
short tutorials, and homework. Melanie Walsh's open *Introduction to Cultural Analytics* is a wonderful
model and is offered as **optional** further reading, but nothing you're evaluated on requires an
outside book.

**Supplementary resources.** `[Optional: departmental tutoring, the Koehler Center, campus support, or
extension resources for students who want to go further.]`

---

## Teaching Philosophy & Methodology
Each 2-hour live session follows the same rhythm:
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

## Course Policies and Requirements

### Assignments
Each assignment is described below and connects to the learning outcomes; you submit and view feedback
through **TCU Online**. `[Note the specific TCU Online module/tool for submissions and where grades and
feedback appear.]`

| Work | How many | What it is | Outcomes |
|---|---|---|---|
| **Homework notebooks (HW1–HW4)** | 4 | Hands-on skill practice, each with a short reflective write-up. | 1–4 |
| **Weekly Experiments** | within each HW | 2–3 small original explorations of your own — *the heart of the ungrading*. | 1–5 |
| **Self-reflections** | 3 | Where you're starting · the halfway check · the final self-evaluation. | 6 |
| **Threaded discussions (TCU Online)** | 4 | One per week, on the week's culture question — a post + replies to peers. | 4–5 |
| **Capstone (final evaluative exercise)** | 1 | A notebook analysis of your own cultural dataset (or a stylometry corpus) + a short data-driven-opinion essay, presented on the last day. Replaces a final exam. | 2–6 |

**The three self-reflections** (≈300–500 words each, submitted to TCU Online — central to ungrading):
1. **Reflection 1 — "Where I'm starting" (due Wed 7/8).** Prior experience (likely none — fine), what
   excites or worries you, and a prediction: what can and can't computers tell us about culture?
2. **Reflection 2 — "Halfway" (due Mon 7/20).** What's clicking and what's hard? Revisit your Week-1
   prediction. What will you do differently in the second half?
3. **Reflection 3 — "Final self-evaluation" (due Fri 7/31).** Review your own body of work and make an
   evidence-based case for the final grade you've earned (see *Grading*).

**The four threaded discussions** (open Monday of their week; **initial post by Wednesday, two
substantive replies by Friday**):
1. **D1 (Wk 1) — Is code neutral?** When a program sorts people or words into categories, whose judgment
   is built in?
2. **D2 (Wk 2) — Whose data?** The ethics of collecting public text, and what it means to read (and fix)
   code an AI wrote for you.
3. **D3 (Wk 3) — Close vs. distant reading.** What does counting/sentiment let you see that reading by
   hand can't — and what does it flatten?
4. **D4 (Wk 4) — What computation reveals and hides.** Share your capstone finding and one thing your
   methods get wrong. *(The course is designed for 4 discussions; D4 may be dropped to a 3-discussion
   minimum if Week-4 capstone load is heavy.)*

### Grading
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

**Grading Scale (TCU undergraduate, plus/minus):** A 94–100 · A‑ 90–93.99 · B+ 87–89.99 · B 84–86.99 ·
B‑ 80–83.99 · C+ 77–79.99 · C 74–76.99 · C‑ 70–73.99 · D+ 67–69.99 · D 64–66.99 · D‑ 60–63.99 · F below 60.
*(No individual piece carries points; these percentages describe only the final letter, set as above.)*

**Grading Concerns.** `[State how/where students raise questions about a grade or mark, and your process
for discussing it.]`

### Late Work
Because the term is short and sessions build on each other, keep up — but ungrading is about the whole
arc, not single due dates. If life happens, **talk to me**; honest communication beats a missed
deadline. **Official University Absences** will be accommodated and work missed for them may be made up,
per TCU policy. `[Paste/confirm TCU language on Official University Absences and make-up work; see Student
Absences.]` **I will not ask for or accept medical documentation** — see *University Policies* below.

### Participation, Engagement & Attendance
This is a live, fast-moving daily course; attendance and active engagement at the synchronous sessions
are expected, and your engagement is reflected throughout your marks (there is no separate points-based
participation grade). In this online course, "engaged" means showing up to the live sessions, coding
along, posting and replying in discussions on time, and documenting your thinking in your `#comments`
and reflections. If you must miss a session, let me know in advance and we'll arrange a catch-up. A
pattern of absence that endangers your standing will be reported to the Dean of Students, per TCU policy.
`[Confirm against the TCU University Attendance Policy and Official Absence Policy.]`

### Class Norms & Netiquette
`[Paste TCU standard Class Norms & Netiquette statement from Syllabus-Template-Online.docx.]`

**Course-specific note (important).** Our running dataset is real public comments about a 2025 law
placing the Ten Commandments in Texas classrooms — a genuinely contested topic touching religion and the
state. We analyze this language as **data about a public debate**, and a goal of the course is to *hear*
the people in the data — including those we disagree with — rather than flatten them. Treat classmates'
views, and the views in the data, with respect; advance disagreements with evidence and care. You're
welcome to choose a different cultural dataset for your own work. In our online spaces, respect
confidentiality and the ownership of others' words (no screenshots or re-sharing of classmates'
posts outside the course).

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

### Technology Policies, Email & Recording
- **Technology.** `[State expectations for hardware/connection, and what to do if tech fails during a
  live session.]`
- **Email.** `[Paste TCU standard Email policy; state your preferred channel and response time.]`
- **Recording of Class Sessions.** `[Paste TCU standard Recording-of-Class-Sessions statement.]`

### Academic Misconduct
`[Paste TCU standard Academic Misconduct statement from Syllabus-Template-Online.docx.]` In this course:
**borrowing code is expected; submitting work (code or writing) you cannot explain or that isn't yours is
not.** Cite your sources, including AI.

---

## Course Schedule (20 sessions)
*Each row is one live class day. "Due" items are due by the start of class that day unless noted;
discussion threads open Monday of their week. The schedule may be adjusted to the class's pace; changes
are announced on TCU Online. A standalone version is in `COURSE_SCHEDULE_2026.md`.*

### Python skills map — what's taught when
*Each skill is introduced in a live code-along, then practiced in the linked homework. Nothing is
assessed before it's taught.*

| Skill | First taught | Practiced in |
|---|---|---|
| Variables & data types | Day 1 (Mon 7/6) | HW1 · all later work |
| Strings & string methods | Day 2 (Tue 7/7) | HW1, HW2 |
| Comparisons & conditionals | Day 3 (Wed 7/8) | HW1 |
| Lists & loops | Day 4 (Thu 7/9) | HW1, HW2 |
| Functions & dictionaries | Day 5 (Fri 7/10) | HW1 · every HW |
| Counting & term frequency | Day 6 (Mon 7/13) | HW2 |
| pandas DataFrames | Day 8 (Wed 7/15) | HW3, HW4, capstone |
| Cleaning & `.apply()` | Day 9 (Thu 7/16) | HW3, HW4 |
| Sentiment (VADER) | Day 11 (Mon 7/20) | HW3 |
| Grouping & charts | Days 9–13 | HW3, HW4 |
| Topic modeling (Gensim LDA) | Day 14 (Thu 7/23) | HW4, capstone |

### Week 1 (Jul 6–10) — Python foundations: "code is not neutral"
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 7/6** (1) | Humanities & Coding · Connotations & Code | Setup + Variables & data types | D1 opens |
| **Tue 7/7** (2) | Sacred Boundaries / digital privacy | Strings & string methods | — |
| **Wed 7/8** (3) | Classification Logic | Comparisons, conditionals & booleans | **R1 due** · D1 post |
| **Thu 7/9** (4) | Collective Memory | Lists & loops | — |
| **Fri 7/10** (5) | — (recap) | Functions & dictionaries + recap | **HW1 assigned** · D1 replies |

### Week 2 (Jul 13–17) — From text to data: ethics, pandas, AI
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 7/13** (6) | Data as evidence | Term frequency + HW1 debrief | **HW1 due** · **HW2 assigned** · D2 opens |
| **Tue 7/14** (7) | AI Agency | Reading & improving AI code + stylometry seed | — |
| **Wed 7/15** (8) | Data Archaeology | Found data + collection ethics (pandas 01 + scraping) | D2 post |
| **Thu 7/16** (9) | — | Data cleaning (pandas 02) | — |
| **Fri 7/17** (10) | — (workshop) | Workshop: collect & clean **your** dataset | **HW2 due** · D2 replies |

### Week 3 (Jul 20–24) — Computational text analysis
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 7/20** (11) | Quantifying connotation | Sentiment with VADER | **R2 due (midterm)** · D3 opens |
| **Tue 7/21** (12) | Close vs. distant reading | VADER deep dive | **HW3 assigned** |
| **Wed 7/22** (13) | Predictions on the record | HW3 work session (freq + sentiment on your data) | D3 post |
| **Thu 7/23** (14) | NLP & Topic Modeling | Topic modeling intro (Gensim LDA) | — |
| **Fri 7/24** (15) | — | Topic modeling deep · `num_topics` · limits | **HW3 due** · **HW4 assigned** · D3 replies |

### Week 4 (Jul 27–31) — Integration & data-driven opinions (capstone)
| Date | Lecture | Coding | Due |
|---|---|---|---|
| **Mon 7/27** (16) | Integration (close → distant → close) | Freq + sentiment + topics + stylometry demo | **Capstone proposal due** · D4 opens |
| **Tue 7/28** (17) | "Being wrong as learning" · capstone framing | Validation + capstone framing | **HW4 due** · D4 post |
| **Wed 7/29** (18) | — | Capstone work session 1 | — |
| **Thu 7/30** (19) | — | Capstone work session 2 + peer review | D4 replies |
| **Fri 7/31** (20) | — (wrap) | **Capstone presentations + wrap** | **Capstone due** · **R3 (final self-evaluation) due** |

*Lecture "—" = recap / workshop / work-session days. Three lecture slots are under review (ML2 "Sacred
Boundaries," a possible ML9 "Going Public" at Day 17, and a noumena framing at Day 1); see
`CONCEPTUAL_FRAMEWORK_2026.md`.*

---

## TCU Online: Our Learning Management System
`[Paste the TCU Online section from Syllabus-Template-Online.docx — Getting Started, Getting Help,
Personal Settings & Notifications, and Student Success Tools.]`

## University Policies & Student Resources
*Official University policy statements — paste the current text from `Syllabus-Template-Online.docx`; do
not paraphrase.*
- **Anti-Discrimination & Title IX Information** — `[paste TCU standard statement]`
- **TCU Policy for Religious Observations & Holidays** — `[paste TCU standard statement]`
- **Disability / Access (Student Access & Accommodation)** — `[paste TCU standard statement]`
- **Medical Documentation** — Faculty will **not** seek or accept medical documentation; students upload
  any documentation to verify absences via the **Dean of Students Office** website. `[paste TCU standard
  statement]`
- **Audio Recording Notification** — `[paste TCU standard statement]`
- **Emergency Response Information** — `[paste TCU standard statement]`
- **Student Resources & Policy Information** — link + QR `[paste TCU standard block]`

> *This syllabus is a working plan and may be adjusted to fit the class's pace; changes will be announced
> in class and on TCU Online.*
