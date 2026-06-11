"""Builder for the 2026 'Data Cleaning with Pandas' code-along (Day 9).

Ports F25's WRIT20833_Pandas_02_Data_Cleaning_Analysis_Pandas_F25.ipynb (57 cells, a sprawling
literary-publications dataset + advanced groupby/regex/viz) into a focused 2-hour Day-9 code-along
in the 2026 house style (warm cultural examples; concept -> code -> 'your turn'; Putting It All
Together -> Sneak Preview -> Playground; colab metadata; no HW-style #comments). Walsh-independent.

Design choices vs F25:
- Held to the CLEANING core (the point of Day 9): diagnose mess (isnull/unique/duplicated),
  handle missing values (fillna + the ethics of filling), standardize text (.str.strip/.lower/
  .title/.replace + map variants), drop duplicates. F25's heavy multi-agg groupby, bubble-chart
  viz, and regex author-origin guessing are dropped as too much for one session.
- CONTINUITY: cleans a *messy version of the same YouTube-comments table from Pandas 01 (Day 8)* —
  inconsistent stance labels, whitespace/newlines, a missing likes value, an exact duplicate row —
  and turns it back into the tidy table students already met. Reinforces that real scraped data is
  messy, and keeps the course corpus (TX Ten Commandments) the throughline into HW3/HW4.
- One light payoff at the end (value_counts + groupby on the CLEAN data) shows cleaning changes the
  picture; Sneak Preview points at the Day-10 'clean YOUR data' workshop and Week-3 sentiment.

All values are computed, not asserted in prose, so nothing drifts. Validated with pandas.

Run from repo root:  python3 notebooks/codeAlongs/_build_pandas02.py
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
    md('''# WRIT 20833 — Data Cleaning with Pandas

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    md('''Last class the data was *tidy*. Real found data almost never is. Scraped comments show up with
stray spaces, line breaks in the middle of text, the same category spelled five different ways, blank
cells, and duplicate rows. Before you can analyze anything, you have to **clean** it. Today you'll take
a messy version of the same comments table from last class and turn it back into something trustworthy —
and notice that every cleaning choice is also an *interpretive* choice.'''),

    # ---- the mess ----
    md('''# A Realistically Messy Dataset

Here's what those tidy YouTube comments might actually look like fresh out of a scraper. Same columns
as last time — `comment`, `stance`, `likes`, `replies` — but full of real-world junk.'''),
    code('''import pandas as pd
import numpy as np

data = {
    "comment": [
        "  The Ten Commandments belong in every classroom, period.  ",
        "This is a clear violation of church and state.\\nKeep it out.",
        "Morals matter and kids today need them more than ever.",
        "Whose religion gets to decide? Not the government's job.",
        "Honestly I have no strong opinion either way.",
        "God and country, that's what built this nation.",
        "Public schools serve everyone, not just one faith.  ",
        "Put the Constitution in classrooms, not commandments.",
        "Finally some common sense values in our schools.",
        "Freedom of religion means freedom from it too.",
        "My kids should learn this at home, not at school.",
        "  The Ten Commandments belong in every classroom, period.  ",
    ],
    "stance": ["support", "Oppose", "SUPPORT", "against", "Neutral", "for",
               "oppose ", "OPPOSE", "support", "Against", "neutral", "support"],
    "likes": [240, 312, 88, 150, np.nan, 205, 176, 410, 64, 198, 33, 240],
    "replies": [15, 42, 6, 22, 1, 18, 19, 51, 4, 27, 2, 15],
}

messy_df = pd.DataFrame(data)
messy_df'''),

    # ---- diagnose ----
    md('''# Step 1: Diagnose Before You Touch Anything

Good cleaning starts with *looking*. Three quick questions tell you most of what's wrong:
**What's missing? What's inconsistent? What's duplicated?**'''),
    code('''# what's missing?
print("Missing values per column:")
print(messy_df.isnull().sum())'''),
    code('''# what's inconsistent? .unique() shows every distinct value in a column
print("Stance labels as found:")
print(messy_df["stance"].unique())'''),
    code('''# what's duplicated? (a whole row repeated)
print("Duplicate rows:", messy_df.duplicated().sum())'''),
    md('''So: one missing `likes` value, a `stance` column that means three things but is spelled eight
ways, and one repeated comment. Let's fix them one at a time on a **copy** (never destroy your raw
data — you may need to go back).'''),
    code('''clean_df = messy_df.copy()'''),

    # ---- text cleaning ----
    md('''# Step 2: Clean the Text Fields

Pandas applies a string method to a *whole column* at once through the `.str` accessor — it's the
column-wide version of the string methods you already know. Strip the whitespace, drop the stray
newline.'''),
    code('''clean_df["comment"] = clean_df["comment"].str.strip().str.replace("\\n", " ", regex=False)
clean_df["comment"].tolist()'''),

    # ---- standardize categories ----
    md('''# Step 3: Standardize the Categories

`stance` is the worst offender. First flatten the casing and spacing, then **map** the synonyms
("for" → support, "against" → oppose) onto a clean set of three labels.'''),
    code('''# lowercase + trim so "OPPOSE", "Oppose", "oppose " all become "oppose"
clean_df["stance"] = clean_df["stance"].str.strip().str.lower()
print("After casing fix:", clean_df["stance"].unique())'''),
    code('''# map the synonyms onto canonical labels
clean_df["stance"] = clean_df["stance"].replace({"for": "support", "against": "oppose"})
print("Canonical labels:", clean_df["stance"].unique())'''),
    md('### Your turn'),
    code('''# your turn — run .value_counts() on the cleaned stance column to see the three-way split
# clean_df["stance"].value_counts()
'''),

    # ---- missing data ----
    md('''# Step 4: Handle the Missing Value

One comment has no `likes` count. You have choices, and **none are neutral**:
- **Drop** the row (`.dropna()`) — but you lose a real comment.
- **Fill** it (`.fillna()`) with an estimate — but you're inventing data.

Here we fill with the **median** (the middle value, less skewed by that 410-like outlier than the
mean). Whatever you choose, *say so* in your writeup — it's part of your method.'''),
    code('''median_likes = clean_df["likes"].median()
clean_df["likes"] = clean_df["likes"].fillna(median_likes)

print("Filled the missing likes with the median:", median_likes)
print("Any missing left?", clean_df["likes"].isnull().sum())'''),

    # ---- duplicates ----
    md('''# Step 5: Drop the Duplicate

Now that the text is trimmed, the repeated comment is an *exact* duplicate. `.drop_duplicates()`
keeps the first and removes the rest.'''),
    code('''before = len(clean_df)
clean_df = clean_df.drop_duplicates().reset_index(drop=True)
print(f"Rows: {before} -> {len(clean_df)}")
clean_df'''),

    # ---- Putting it together ----
    md('''# Putting It All Together: Clean Data Tells a Truer Story

The whole point of cleaning is that the analysis you couldn't trust before, you can trust now. With
the labels standardized and the duplicate gone, the counts finally mean something.'''),
    code('''print("Stance breakdown (clean):")
print(clean_df["stance"].value_counts())

print("\\nAverage likes by stance:")
print(clean_df.groupby("stance")["likes"].mean().round(1))'''),
    md('''Before cleaning, `.value_counts()` on `stance` would have shown *eight* fake categories and a
double-counted comment — a garbage picture. Same data, cleaned, and the crowd's split comes through.
You can also now reliably search the text — the `.str` accessor again, this time to *filter*:'''),
    code('''# which comments invoke "religion" directly?
religion = clean_df[clean_df["comment"].str.lower().str.contains("religion")]
religion[["comment", "stance"]]'''),
    code('''# your turn — filter to comments mentioning "schools" (or another word) and see who's on which side
'''),

    # ---- Sneak preview ----
    md('''# Sneak Preview: Where This Is Going

**This Friday's workshop** is you doing exactly this — to a dataset *you* collected. Diagnose it,
standardize it, drop the junk, until it's analysis-ready. Cleaning is unglamorous, but it's where
honest analysis begins: every choice you make here (what to fill, what to drop, how to label) quietly
shapes the conclusions you'll draw later.

And next week the payoff arrives: with a clean `comment` column, **VADER** will read each comment's
*sentiment* — turning "support / oppose / neutral" from something you labeled by hand into something
the computer scores. Clean data in, real analysis out.'''),
    code('''# a peek at next week: clean text is what sentiment scoring needs
clean_df[["comment", "stance"]].head()'''),

    md('# Playground'),
    code('# use this space to experiment!\n'),
]


out = os.path.join(HERE, "WRIT20833_Pandas_02_Cleaning_2026.ipynb")
with open(out, "w", encoding="utf-8") as f:
    json.dump(notebook(cells), f, indent=1, ensure_ascii=False)
    f.write("\n")
print("wrote", out, "(%d cells)" % len(cells))
