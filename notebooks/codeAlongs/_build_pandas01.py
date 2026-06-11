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


def notebook(cells):
    return {"cells": cells, "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 0}


cells = [
    md('<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/codeAlongs/WRIT20833_Pandas_01_Found_Data_2026.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'),

    md('''# WRIT 20833 — Found Data & Pandas Fundamentals

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    md('''So far we've handled text one string at a time. But cultural arguments live in **lots** of text
at once — hundreds of comments, reviews, posts. Today is the turn from *a text* to *a dataset*: where
that data comes from, how to collect it **ethically**, and how to open it up with **pandas**, the tool
the rest of this course runs on.'''),

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
    code('''data = {
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
}

comments_df = pd.DataFrame(data)
comments_df'''),

    md('''## Always explore first
Before analyzing found data, get to know it. What's its shape? What are the columns? What does a row
look like?'''),
    code('''comments_df.head()        # the first few rows'''),
    code('''print("Shape:", comments_df.shape)
print(f"{comments_df.shape[0]} rows (comments) and {comments_df.shape[1]} columns (fields)")'''),
    code('''comments_df.info()        # column names, types, and how many values are present'''),

    md('''## Selecting columns
Grab one column with `df["name"]` (a **Series** — a single labeled column). Grab several with a
*list* of names inside the brackets (a smaller **DataFrame**).'''),
    code('''stances = comments_df["stance"]      # one column -> a Series
print(type(stances))
print(stances)'''),
    code('''comments_df[["comment", "likes"]]    # two columns -> a DataFrame'''),
    md('### Your turn'),
    code('''# your turn — select just the "comment" and "stance" columns
# comments_df[[ ... ]]
'''),

    md('''## Filtering rows (boolean indexing)
This is where analysis starts. Put a **condition** inside the brackets and pandas keeps only the rows
where it's true. Read it as "give me the rows *where*..."'''),
    code('''# comments that struck a nerve — more than 150 likes
popular = comments_df[comments_df["likes"] > 150]
print(f"{len(popular)} comments with >150 likes")
popular[["comment", "stance", "likes"]]'''),
    code('''# only the opposing comments
opposed = comments_df[comments_df["stance"] == "oppose"]
print(f"{len(opposed)} opposing comments")
opposed[["comment", "likes"]]'''),
    md('### Your turn'),
    code('''# your turn — keep only the "support" comments and print how many there are
# supported = comments_df[comments_df["stance"] == "support"]
# print(len(supported))
'''),

    md('''## Counting patterns
`.value_counts()` tallies how often each value appears in a column — the fastest way to see the shape
of an opinion.'''),
    code('''comments_df["stance"].value_counts()'''),
    md('And numeric columns answer quantitative questions directly:'),
    code('''print("Average likes:", round(comments_df["likes"].mean(), 1))
print("Most-liked comment got:", comments_df["likes"].max(), "likes")
print("Total replies across all comments:", comments_df["replies"].sum())'''),

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
the opposing camp and pull out the comment that landed hardest.'''),
    code('''opposed = comments_df[comments_df["stance"] == "oppose"]      # filter
print("Opposing comments:", len(opposed))                     # count
print("Their average likes:", round(opposed["likes"].mean(), 1))

# the single most-liked opposing comment
top = opposed.sort_values("likes", ascending=False).iloc[0]   # surface one row
print("\\nLoudest opposing voice:")
print(f'  "{top["comment"]}"  ({top["likes"]} likes)')'''),
    code('''# your turn — do the same for the "support" camp: filter, count, find its most-liked comment
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


out = os.path.join(HERE, "WRIT20833_Pandas_01_Found_Data_2026.ipynb")
with open(out, "w", encoding="utf-8") as f:
    json.dump(notebook(cells), f, indent=1, ensure_ascii=False)
    f.write("\n")
print("wrote", out, "(%d cells)" % len(cells))
