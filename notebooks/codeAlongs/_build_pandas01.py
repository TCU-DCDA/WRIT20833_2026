"""Builder for the 2026 'Found Data & Pandas Fundamentals' code-along (Day 8).

Merges the two F25 notebooks that map to Day 8 ("Found data + collection ethics") —
WRIT20833_Pandas_01_Found_Data_Fundamentals_F25 (54 cells) and
WRIT20833_Instant_Data_Scraper_Ethics_F25 (31 cells) — into ONE focused 2-hour code-along in the
2026 house style (warm cultural examples; concept -> code -> 'your turn'; Putting It All Together ->
Sneak Preview -> Playground; colab metadata; no HW-style #comments). Walsh-independent.

Design choices vs F25:
- Collection ethics FIRST (robots.txt, fair use/scale, attribution; Instant Data Scraper as the
  no-code tool), THEN pandas fundamentals on a found table. One arc, not two notebooks.
- robots.txt demo runs OFFLINE (a status-code helper) so the notebook validates anywhere; the live
  `requests` version is shown commented, "to try in class."
- Uses an inline sample of real-shaped YouTube comments on the TX Ten Commandments law (the course's
  actual corpus theme) instead of F25's museum data — so found-data fundamentals sit on the same
  table that HW3 (sentiment) and HW4 (topic modeling) will run on. Inline (not a file path) so it
  runs in Colab with no upload.
- Pandas scope held to fundamentals: read a DataFrame, head/shape/info, select columns (Series vs
  DataFrame), filter rows (boolean indexing), value_counts, basic stats, one light df.plot bar chart.
  Cleaning (.str methods, missing values) is deliberately deferred to Pandas 02 (Day 9).

Two outputs from one cell list (2026-10-06):
- WRIT20833_Pandas_01_Found_Data_2026.ipynb — the STUDENT copy. "Type along" cells are left blank
  (a one-line comment says what to write), "predict first" cells ask for a guess before running, and
  "your turn" cells carry no commented-out answer. Plumbing (imports, the sample data, the status-code
  helper, chart formatting) and each first worked example stay complete. This is the file the
  schedule, site, and D2L link to.
- WRIT20833_Pandas_01_Found_Data_2026_complete.ipynb — every blank filled in. Not linked anywhere yet.
A cell is either shared, or a pair(student, complete).

Run from repo root:  python3 notebooks/codeAlongs/_build_pandas01.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": _lines(text)}


def code(text):
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": _lines(text)}


def _lines(text):
    text = text.strip("\n")
    lines = text.split("\n")
    return [l + "\n" for l in lines[:-1]] + [lines[-1]]


def pair(student, complete):
    """A cell that differs between the student copy and the complete copy."""
    return {"student": student, "complete": complete}


STUDENT_NB = "WRIT20833_Pandas_01_Found_Data_2026.ipynb"
COMPLETE_NB = "WRIT20833_Pandas_01_Found_Data_2026_complete.ipynb"


def badge(name):
    return md('<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/'
              'notebooks/codeAlongs/' + name + '" target="_parent"><img src="https://colab.research.'
              'google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>')


# The inline sample, shared by both copies (plumbing — nobody should have to type it).
DATA = '''data = {
    "comment": [
        "The Ten Commandments belong in every classroom, period.",
        "This is a clear violation of church and state. Keep it out.",
        "Morals matter and kids today need them more than ever.",
        "Whose religion gets to decide? Not the government's job.",
        "Honestly I have no strong opinion either way.",
        "God and country, that's what built this nation.",
        "Public schools serve everyone, not just one faith.",
        "Put the Constitution in classrooms, not commandments.",
        "Finally some common sense values in our schools.",
        "Freedom of religion means freedom from it too.",
        "My kids should learn this at home, not at school.",
    ],
    "stance": ["support", "oppose", "support", "oppose", "neutral", "support",
               "oppose", "oppose", "support", "oppose", "neutral"],
    "likes": [240, 312, 88, 150, 12, 205, 176, 410, 64, 198, 33],
    "replies": [15, 42, 6, 22, 1, 18, 19, 51, 4, 27, 2],
}'''


def notebook(cells):
    return {"cells": cells, "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 0}


cells = [
    pair(badge(STUDENT_NB), badge(COMPLETE_NB)),

    md('''# WRIT 20833 — Found Data & Pandas Fundamentals

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    md('''So far we've handled text one string at a time. But cultural arguments live in **lots** of text
at once — hundreds of comments, reviews, posts. Today is the turn from *a text* to *a dataset*: where
that data comes from, how to collect it **ethically**, and how to open it up with **pandas**, the tool
the rest of this course runs on.'''),
    pair(md('''**How today works.** Some code cells are blank on purpose:
- **type along** — a comment says what to write; type it with me, then run it.
- **predict first** — write your guess in the comment *before* you run the cell.
- **your turn** — try it on your own.

If a cell gives you an error, read the message — errors are part of the work here, not something to
hide.'''),
         md('''**Complete copy.** Every blank in the class worksheet is filled in here, so you can check your
work after class. The "predict first" guesses are left for you.''')),

    # ================= PART 1: ETHICS =================
    md('''# Part 1 — Found Data & Collecting It Ethically

## Found data: culture already in data form
You won't usually run a survey to get cultural data — it already exists, **found** out in the world:
comment sections, product reviews, library catalogs, song archives, public records. "Found data" just
means a dataset that's already there, waiting to be discovered and read at scale.

That convenience comes with responsibility. When you collect text people wrote, you're handling
**other people's words**. Three pillars keep that honest:'''),
    md('''### The three pillars of ethical collection
1. **🤖 robots.txt** — most sites publish a file saying what automated tools may and may not touch.
   Check it first. (Add `/robots.txt` to a site's address, e.g. `example.com/robots.txt`.)
2. **⚖️ Fair use & scale** — collect only what your question needs, at a human pace. Don't hammer a
   server or vacuum up a whole site because you can.
3. **📚 Attribution & transparency** — record where the data came from and how you got it, and say so
   in your work. "I scraped 200 YouTube comments on July 8" is part of your method.

**The golden rule:** collect data the way you'd want someone collecting from *your* posts —
respectfully, in the open.'''),
    md('''### Reading robots.txt: what the response means
When you (or a tool) request a page, the server answers with a **status code**. A few you'll meet
when checking permissions:'''),
    code('''# A tiny helper so the codes aren't a mystery — no internet needed to learn what they mean.
status_meanings = {
    200: "OK — it loaded; read what robots.txt says and follow it",
    403: "Forbidden — the site is telling you not to access this. Respect it.",
    404: "Not Found — no robots.txt here (common). Fall back to terms of service + judgment.",
}

def interpret(code):
    return status_meanings.get(code, "Unfamiliar code — look it up before collecting anything")

for code in (200, 403, 404):
    print(code, "→", interpret(code))'''),
    md('''In class you can check a real site live. (Run this in Colab — it needs internet, so it's
left commented here.)
```python
# import requests
# r = requests.get("https://archive.org/robots.txt", timeout=5)
# print(r.status_code, "→", interpret(r.status_code))
```'''),
    md('''### Your turn: read a real robots.txt
Pick a site you might actually want to collect from — a review site, a fan wiki, a news comment
section. Open its robots.txt in a new browser tab (add `/robots.txt` to the end of its address) and
read it. It's plain text, written for machines, but you can read it.'''),
    code('''# your turn — in a sentence or two: what does this site allow, what does it block,
# and does anything about it surprise you?
#
# site:
# what it says:
'''),
    md('''## Instant Data Scraper: collecting without code
You don't need to write a scraper to gather cultural data. **Instant Data Scraper** is a free browser
extension (Chrome/Firefox) that turns a web page's table or list into a downloadable **CSV** — point,
preview, download. We use it because it's:
- **Visible** — you see exactly what you're collecting,
- **Human-paced** — it won't flood a server, and
- **Honest about scale** — good for the hundreds-of-rows datasets this course needs, not millions.

**Before you scrape anything, ask:** Does robots.txt allow it? Do I need *this much*? Will I credit
the source? If you can't answer all three, don't collect it.'''),

    # ================= PART 2: PANDAS =================
    md('''# Part 2 — Opening Found Data with Pandas

Once collected, found data arrives as a **table** — rows and columns, like a spreadsheet (a `.csv`
file). **pandas** is Python's tool for tables. The name is from "panel data," but picture a friendly
data-handling panda. By convention we import it as `pd`.'''),
    code('''import pandas as pd
import matplotlib.pyplot as plt'''),
    md('''A real CSV you'd load with `pd.read_csv("yourfile.csv")`. To keep this notebook self-contained,
here's a small **sample** of the kind of data Instant Data Scraper produces — real-shaped YouTube
comments on the Texas Ten Commandments law, the conversation this course keeps returning to.'''),
    pair(code(DATA + """

# type along — turn `data` into a DataFrame named comments_df, then show it
"""),
         code(DATA + """

comments_df = pd.DataFrame(data)
comments_df""")),

    md('''## Always explore first
Before analyzing found data, get to know it. What's its shape? What are the columns? What does a row
look like?'''),
    pair(code('''# type along — show the first few rows with .head()
'''),
         code('''comments_df.head()        # the first few rows''')),
    md('''**Predict first.** Count from the table above: how many rows? How many columns? Write your guess in
the comment, then run the cell.'''),
    code('''# my guess:    rows,    columns
print("Shape:", comments_df.shape)
print(f"{comments_df.shape[0]} rows (comments) and {comments_df.shape[1]} columns (fields)")'''),
    code('''comments_df.info()        # column names, types, and how many values are present'''),

    md('''## Selecting columns
Grab one column with `df["name"]` (a **Series** — a single labeled column). Grab several with a
*list* of names inside the brackets (a smaller **DataFrame**).'''),
    pair(code('''# type along — grab the "stance" column, save it as `stances`, then print its type and the column
'''),
         code('''stances = comments_df["stance"]      # one column -> a Series
print(type(stances))
print(stances)''')),
    code('''comments_df[["comment", "likes"]]    # two columns -> a DataFrame'''),
    md('### Your turn'),
    pair(code('''# your turn — select just the "comment" and "stance" columns
# comments_df[[ ... ]]
'''),
         code('''# your turn — select just the "comment" and "stance" columns
comments_df[["comment", "stance"]]''')),

    md('''## Filtering rows (boolean indexing)
This is where analysis starts. Put a **condition** inside the brackets and pandas keeps only the rows
where it's true. Read it as "give me the rows *where*..."

**Predict first.** Scan the `likes` column: how many comments have more than 150 likes?'''),
    code('''# my guess:
# comments that struck a nerve — more than 150 likes
popular = comments_df[comments_df["likes"] > 150]
print(f"{len(popular)} comments with >150 likes")
popular[["comment", "stance", "likes"]]'''),
    pair(code('''# type along — keep only the rows where stance is "oppose" and save them as `opposed`;
# print how many there are, then show their comment and likes columns
'''),
         code('''# only the opposing comments
opposed = comments_df[comments_df["stance"] == "oppose"]
print(f"{len(opposed)} opposing comments")
opposed[["comment", "likes"]]''')),
    md('### Your turn'),
    pair(code('''# your turn — keep only the comments with fewer than 50 likes.
# How many are there, and which stance do they come from?
'''),
         code('''# your turn — keep only the comments with fewer than 50 likes.
# How many are there, and which stance do they come from?
quiet = comments_df[comments_df["likes"] < 50]
print(f"{len(quiet)} comments with fewer than 50 likes")
quiet[["comment", "stance", "likes"]]''')),

    md('''## Counting patterns
`.value_counts()` tallies how often each value appears in a column — the fastest way to see the shape
of an opinion.

**Predict first.** Count the stances by hand from the table: how many support, oppose, neutral?'''),
    pair(code('''# my guess: support    oppose    neutral
# type along — tally the "stance" column with .value_counts()
'''),
         code('''# my guess: support    oppose    neutral
comments_df["stance"].value_counts()''')),
    md('And numeric columns answer quantitative questions directly:'),
    pair(code('''print("Average likes:", round(comments_df["likes"].mean(), 1))

# type along — following the line above, print the most likes any comment got (.max())
# and the total number of replies across all comments (.sum())
'''),
         code('''print("Average likes:", round(comments_df["likes"].mean(), 1))
print("Most-liked comment got:", comments_df["likes"].max(), "likes")
print("Total replies across all comments:", comments_df["replies"].sum())''')),

    md('''## One quick picture
A chart is just another way to *see* a count. pandas can plot a Series directly — `value_counts()`
straight into a bar chart, one line.'''),
    code('''comments_df["stance"].value_counts().plot(kind="bar", title="Comments by stance")
plt.xlabel("stance")
plt.ylabel("number of comments")
plt.tight_layout()
plt.show()'''),

    # ---- Putting it together ----
    md('''# Putting It All Together: Read a Found Dataset

The whole Part-2 workflow in one pass: **explore → filter → count → surface a row.** Here we zero in on
the opposing camp and pull out the comment that landed hardest.

**Predict first.** The two camps are close in size — 5 opposing comments, 4 supporting. Which camp do
you think averages more likes? Write your guess, then run the next two cells.'''),
    code('''# my guess:
opposed = comments_df[comments_df["stance"] == "oppose"]      # filter
print("Opposing comments:", len(opposed))                     # count
print("Their average likes:", round(opposed["likes"].mean(), 1))

# the single most-liked opposing comment
top = opposed.sort_values("likes", ascending=False).iloc[0]   # surface one row
print("\\nLoudest opposing voice:")
print(f'  "{top["comment"]}"  ({top["likes"]} likes)')'''),
    pair(code('''# your turn — do the same for the "support" camp: filter, count, find its most-liked comment
'''),
         code('''# your turn — do the same for the "support" camp: filter, count, find its most-liked comment
supported = comments_df[comments_df["stance"] == "support"]
print("Supporting comments:", len(supported))
print("Their average likes:", round(supported["likes"].mean(), 1))

top = supported.sort_values("likes", ascending=False).iloc[0]
print("\\nLoudest supporting voice:")
print(f'  "{top["comment"]}"  ({top["likes"]} likes)')''')),
    md('''**Was your guess right?** Now the harder question: what is a like count actually measuring — how
many people agree, or how loud and visible a comment got? Who decided that likes were the thing to
count? Answer in a `#comment` below.'''),
    code('''# what do likes measure?
'''),

    # ---- Sneak preview ----
    md('''# Sneak Preview: Where This Is Going

Real scraped data is never this tidy — it shows up with blank cells, stray whitespace, duplicate rows,
and numbers stored as text. **Next class (Pandas 02)** is all about *cleaning* a messy real dataset so
it's ready to analyze.

And this `comments_df` is exactly the shape your later work runs on: in **HW3** you'll score each
comment's **sentiment** and add it as a new column; in **HW4** you'll discover the **topics** the crowd
is really arguing about. Today you learned to open the table — soon you'll make it talk.'''),
    code('''# a glimpse of what's coming: counts split by stance, the start of every comparison you'll make
comments_df.groupby("stance")["likes"].mean()'''),

    md('# Playground'),
    code('# use this space to experiment!\n'),
]


for name, version in ((STUDENT_NB, "student"), (COMPLETE_NB, "complete")):
    picked = [c[version] if "student" in c else c for c in cells]
    out = os.path.join(HERE, name)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(notebook(picked), f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("wrote", out, "(%d cells)" % len(picked))
