# WRIT 20833 — Intro to Coding in the Humanities
## "When Coding Meets Culture" — Summer 2026 Syllabus

> **DRAFT for instructor review.** Bracketed `[...]` fields are placeholders to fill in
> (instructor name, contact, office hours, TCU policy boilerplate, D2L links). Schedule and
> assignment placements follow the repo's `PROPOSED_4WEEK_SCHEDULE.md`; due dates are proposals.

**Term:** Summer 2026 · **Dates:** Monday **July 6 – Friday July 31, 2026** (4 weeks)
**Meetings:** **Monday–Friday, 2 hours/day** (20 live sessions), **online synchronous** via `[Zoom/Webex link]`
**Modality:** Live online (this is the *synchronous* section; the MALA 60970 web-authoring course is async)
**Credit:** Graduate · **Prerequisites:** none — **no prior coding experience assumed**

**Instructor:** `[Name]` · **Email:** `[email]` · **Office hours:** `[days/times + link]`
**Course site / submissions:** TCU **D2L** (`[course link]`) · **Code runs in:** Google Colab (free; needs a Google account)

---

## Course description
This course is an invitation to *think with code* about culture. Over four intensive weeks you'll
learn enough Python to ask real humanistic questions of real text — social-media comments, public
documents, your own chosen corpus — and to argue from what you find. We move from **predictions** to
**computational analysis** to **data-driven insight**, always asking not just *what the code does* but
*what it assumes, what it reveals, and what it flattens.* No prior coding experience is needed; bring
curiosity and a willingness to be wrong out loud.

## What you'll be able to do (learning outcomes)
By the end of the course you will be able to:
1. **Read and write basic Python** — variables, conditionals, loops, functions, and lists/dictionaries.
2. **Work with real data** in pandas — load, clean, and explore a text dataset you collected.
3. **Run three methods of computational text analysis** — term frequency, sentiment analysis (VADER),
   and topic modeling (LDA) — and **integrate** them into a single interpretation.
4. **Borrow and judge tools critically** — use libraries and AI-written code you didn't build, and
   evaluate whether to trust their output.
5. **Make a data-driven argument** about a cultural text and **name the limits** of your own methods.
6. **Reflect on your learning** — assess your own growth honestly (see *Ungrading*, below).

## A self-contained course (no textbook to buy)
Everything you need is **in this course**: our own code-along notebooks, short tutorials, and
homework. Melanie Walsh's open *Introduction to Cultural Analytics* is a wonderful model and is
offered as **optional** further reading, but **nothing you're graded on requires an outside book.**

## Technology
- **Google Colab** (free) — runs all notebooks in your browser; no installation. Bring a Google account.
- **TCU D2L** — readings, the four threaded discussions, and all submissions (Dropbox).
- A laptop with a reliable connection for the live sessions. `[TCU loaner info if applicable.]`

---

## How a day works
Each 2-hour session follows the same rhythm:
- **~25 min — concept / mini-lecture:** the idea and the culture question behind it.
- **~70 min — live code-along:** we build it together; you type as we go.
- **~25 min — application + share:** you apply it to real text and we compare notes.

Four threads run through the course: (1) our notebooks as the "textbook"; (2) a critical frame each
day (code is not neutral; classification logic; AI agency; collective memory; what counting hides);
(3) tutorials bridging concept and culture; (4) homework applying skills to a cultural dataset —
ideally **one you choose** and carry across the whole term.

---

## How you'll be evaluated — *ungrading*
This course uses **ungrading**: the goal is **earned insight, not clean code**. You are evaluated on
**engagement, reflection, and labor** — the thinking you show — not on getting every number "right."
Concretely:

- **Every code cell carries `#comments`** explaining what you tried and what you learned (or what
  confused you). *Documenting a failure and what it taught you is worth as much as working code.*
- **There are no points or letter grades on individual assignments.** Instead, you keep a steady
  record of doing the work — homeworks, weekly experiments, discussions, and three reflections.
- **You assess your own learning.** Three **self-reflections** (below) build toward a **final
  self-evaluation** in which you make the case, with evidence from your own work, for what you
  learned and the course grade you've earned. `[Instructor sets the final grade per TCU requirements,
  in dialogue with your self-evaluation.]`
- **"Complete" means honest effort + reflection**, not perfection. Something that doesn't run, paired
  with a clear account of what you tried, still counts as engaged work.

### What you'll produce
| Work | How many | What it is |
|---|---|---|
| **Homework notebooks (HW1–HW4)** | 4 | Hands-on skill practice, each with a short reflective write-up. |
| **Weekly Experiments** | in each HW | 2–3 small original explorations of your own — *the heart of the ungrading*. |
| **Self-reflections** | 3 | Where you're starting · the halfway check · the final self-evaluation. |
| **Threaded discussions (D2L)** | 4 | One per week, on the week's culture question — a post + replies to peers. |
| **Capstone** | 1 | A notebook analysis of your own cultural dataset (or a stylometry corpus) + a short data-driven-opinion essay. Replaces a final exam. |

### AI / LLM use policy
You **may** use AI tools (ChatGPT, Claude, Copilot, etc.) — this course literally teaches you to
read and improve AI-written code. The rule is **understanding, not avoidance**: you must be able to
**explain any code you submit**, and you should **note in your `#comments` where you used AI** and what
you changed. Borrowing code — from a library, Stack Overflow, or an AI — is normal professional
practice; passing off code you can't explain is not. When in doubt, ask.

---

## Schedule (20 sessions)
*Times are class days; "Due" items are due by the start of class that day unless noted. D2L discussion
posts open Monday of their week.*

### Week 1 (Jul 6–10) — Python foundations: "code is not neutral"
| Date | Day | In class | Due / assigned |
|---|---|---|---|
| **Mon 7/6** | 1 | Setup + Variables & Data Types · *Humanities & Coding; Connotations & Code* | **Discussion 1 opens** |
| **Tue 7/7** | 2 | Strings & string methods · *Digital Boundaries* | |
| **Wed 7/8** | 3 | Comparisons, conditionals & booleans · *Classification Logic* | **Reflection 1 due** · **D1 post due** |
| **Thu 7/9** | 4 | Lists & loops · *Collective Memory* | |
| **Fri 7/10** | 5 | Functions & dictionaries + recap | **D1 replies due** · **HW1 assigned** |

### Week 2 (Jul 13–17) — From text to data: ethics, pandas, AI
| Date | Day | In class | Due / assigned |
|---|---|---|---|
| **Mon 7/13** | 6 | HW1 debrief + "Meaningful Words": term frequency | **HW1 due** · **HW2 assigned** · **Discussion 2 opens** |
| **Tue 7/14** | 7 | Reading & improving AI code + stylometry seed (close reading) · *AI Agency* | |
| **Wed 7/15** | 8 | Found data + collection ethics (pandas 01 + scraping) · *Data Archaeology* | **D2 post due** |
| **Thu 7/16** | 9 | Data cleaning (pandas 02) | |
| **Fri 7/17** | 10 | **Workshop:** collect & clean *your* cultural dataset | **HW2 due** · **D2 replies due** |

### Week 3 (Jul 20–24) — Computational text analysis
| Date | Day | In class | Due / assigned |
|---|---|---|---|
| **Mon 7/20** | 11 | Sentiment with VADER · *quantifying connotation* | **Reflection 2 due (midterm)** · **Discussion 3 opens** |
| **Tue 7/21** | 12 | VADER deep · close vs. distant reading | **HW3 assigned** |
| **Wed 7/22** | 13 | HW3 work session (frequency + sentiment on your data) | **D3 post due** |
| **Thu 7/23** | 14 | Topic modeling intro (Gensim LDA) · *NLP & Topic Modeling* | |
| **Fri 7/24** | 15 | Topic modeling deep · choosing `num_topics` · limits | **HW3 due** · **HW4 assigned** · **D3 replies due** |

### Week 4 (Jul 27–31) — Integration & data-driven opinions (capstone)
| Date | Day | In class | Due / assigned |
|---|---|---|---|
| **Mon 7/27** | 16 | Integration: frequency + sentiment + topics + short stylometry demo | **Capstone proposal due** · **Discussion 4 opens** |
| **Tue 7/28** | 17 | "Being wrong as learning" · validation · capstone framing | **HW4 due** · **D4 post due** |
| **Wed 7/29** | 18 | Capstone work session 1 (cultural dataset **or** stylometry track) | |
| **Thu 7/30** | 19 | Capstone work session 2 + peer review | **D4 replies due** |
| **Fri 7/31** | 20 | Capstone presentations + wrap | **Capstone due** · **Reflection 3 (final self-evaluation) due** |

---

## The three self-reflections
Short (≈300–500 words each), submitted to D2L. These are central to ungrading — write honestly.
1. **Reflection 1 — "Where I'm starting" (due Wed 7/8).** Your prior experience (likely
   none — that's fine), what excites or worries you, and a prediction: what do you expect computers
   can and can't tell us about culture?
2. **Reflection 2 — "Halfway" (due Mon 7/20).** What's clicking and what's hard? Revisit your Week-1
   prediction. What will you do differently in the second half?
3. **Reflection 3 — "Final self-evaluation" (due Fri 7/31).** Make the case, with specific evidence
   from your notebooks, experiments, and capstone, for what you learned and the grade you've earned.

## The four threaded discussions (D2L)
Each opens Monday of its week; **initial post by Wednesday, two substantive replies by Friday.**
1. **D1 (Wk 1) — Is code neutral?** After Classification Logic: when a program sorts people or words
   into categories, whose judgment is built in?
2. **D2 (Wk 2) — Whose data?** Ethics of collecting public text, and what it means to read (and fix)
   code an AI wrote for you.
3. **D3 (Wk 3) — Close vs. distant reading.** What does counting/sentiment let you see that reading by
   hand can't — and what does it flatten?
4. **D4 (Wk 4) — What computation reveals and hides.** Share your capstone finding and one thing your
   methods get wrong.

*(Scope note: the course is designed for **4** discussions, one per week; drop D4 to land on the
3-discussion minimum if Week 4's capstone load is too heavy.)*

---

## Course policies
- **Attendance & participation.** This is a live, fast-moving daily course; sessions build on each
  other, so attendance matters. Let me know in advance if you must miss a session and we'll arrange a
  catch-up. `[TCU attendance policy boilerplate.]`
- **Late / missing work.** Because the term is short, keep up — but ungrading is about the whole arc,
  not single due dates. If life happens, **talk to me**; honest communication beats a missed deadline.
- **A note on our main dataset.** Our running example is real public comments about a 2025 law placing
  the Ten Commandments in Texas classrooms — a genuinely contested topic touching religion and the
  state. We analyze this language as *data about a public debate*; treat classmates' views with respect.
  You're welcome to choose a different cultural dataset for your own work.
- **Accessibility.** TCU is committed to access. If you need accommodations, contact `[Student Access
  & Accommodation / instructor]` early and we'll make it work.
- **Academic integrity.** `[TCU academic-conduct boilerplate.]` In this course: borrowing code is
  expected; **submitting code you cannot explain is not.** Cite your sources, including AI.
- **Communication.** `[Email response window, preferred channel, etc.]`

> *This syllabus is a working plan and may be adjusted to fit the class's pace; changes will be
> announced in class and on D2L.*
