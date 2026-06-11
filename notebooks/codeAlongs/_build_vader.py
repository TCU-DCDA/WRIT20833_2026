"""Builder for the 2026 'Sentiment Analysis with VADER' code-along (Days 11-12).

Ports F25's WRIT20833_VADER_Sentiment_Analysis_F25.ipynb (32 cells) into the 2026 code-along house
style (warm cultural examples; concept -> code -> 'your turn'; Putting It All Together -> Sneak
Preview -> Playground; colab metadata; no HW-style #comments). Walsh-independent. Spans the two
VADER sessions (Day 11 "Sentiment with VADER" + Day 12 "VADER deep dive") as one basics->deep-dive arc.

Design choices vs F25:
- CONTINUITY: scores the SAME cleaned YouTube-comments table from Days 8-9 (comment + hand-labeled
  stance), not F25's Broadway-reviews data. The payoff exercise compares VADER's emotional *tone* to
  the human *stance* label and shows they're DIFFERENT axes (an opposing comment can be warm; a
  supporting one can be angry) — the course's close-vs-distant-reading theme (Day 12 lecture) made
  concrete, and exactly the "human vs automated" check the WORKLOG flags as a strong critical exercise.
- Keeps the "honest about borrowed code" house convention: VADER is the textbook pip-installed model
  nobody writes from scratch; we run it to learn to *judge* it, including where it fails.
- Dropped F25's TextBlob detour and multi-panel viz; kept one light bar chart (mean tone by stance).
- VADER is deterministic (fixed lexicon), but scores are NOT hardcoded in prose — all printed at
  runtime — so nothing drifts across vader versions. Validated with vaderSentiment + pandas.

Run from repo root:  python3 notebooks/codeAlongs/_build_vader.py
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
    md('<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/codeAlongs/WRIT20833_VADER_Sentiment_2026.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'),

    md('''# WRIT 20833 — Sentiment Analysis with VADER

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    md('''In Week 2 you *counted* words — what a text is about. Now we ask a different question: how does
it **feel**? **Sentiment analysis** scores the emotional tone of a text, from negative to positive.
We'll use **VADER**, a tool built for exactly the kind of informal, punctuation-and-caps-heavy language
people use online. And true to this course, we won't just trust its number — we'll check it against our
own reading.'''),

    # ---- setup ----
    md('''# Setup

VADER lives in a small library we install once. (The `!pip install` line is a one-time setup command,
not Python — run it and move on.)'''),
    code('''!pip install -q vaderSentiment'''),
    code('''from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
print("VADER ready.")'''),

    # ---- basics ----
    md('''# Part 1 — How VADER Scores a Text

Hand VADER a string and it returns four numbers. The one you'll use most is **`compound`**: a single
score from **-1 (very negative)** to **+1 (very positive)**, with **0** around neutral. The other three
(`pos`, `neu`, `neg`) show the mix it found.'''),
    code('''scores = analyzer.polarity_scores("This museum exhibition was absolutely AMAZING!!!")
print(scores)
print("compound:", scores["compound"])'''),
    md('''**Predict first.** Before running the next cell, guess: which line is most positive? Most
negative? Which is mixed? Then check yourself.'''),
    code('''samples = [
    "worst law ever, complete waste of everyone's time",
    "The idea is okay, nothing special but not terrible either",
    "I love love LOVE this, so good for our kids ❤️",
    "It was good but honestly kind of pointless",
]

for text in samples:
    c = analyzer.polarity_scores(text)["compound"]
    print(f"{c:+.3f}   {text}")'''),

    md('''### Sentiment = quantifying connotation
Notice what just happened: VADER turned *feeling* into a *number*. That's it **quantifying
connotation** — the emotional coloring of words, beyond their dictionary meaning. "Inexpensive" and
"cheap" mean the same thing but feel different; VADER scores that difference. It can because it leans on
a **lexicon** — a fixed list of ~7,500 words each pre-rated for sentiment. Caps, `!!!`, and emoji nudge
the score too.'''),
    md('''> **About borrowed code.** Nobody writes a sentiment analyzer from scratch — VADER is a
> well-known tool you `pip install`, the way you'd grab one off Stack Overflow (or from an AI today).
> Borrowing it is *expected*, not cheating. We run it here so you can do the part that matters and that
> no library can do for you: **judge whether its scores are any good** on real cultural text.'''),

    # ---- apply to the dataset ----
    md('''# Part 2 — Scoring a Whole Dataset

Here's the cleaned comments table from last week — the Texas Ten Commandments comments, with the
`stance` you'd label by hand (support / oppose / neutral). Let's have VADER score the **tone** of every
comment at once.'''),
    code('''import pandas as pd

comments = [
    ("The Ten Commandments belong in every classroom, period.", "support"),
    ("This is a clear violation of church and state. Keep it out.", "oppose"),
    ("Morals matter and kids today need them more than ever.", "support"),
    ("Whose religion gets to decide? Not the government's job.", "oppose"),
    ("Honestly I have no strong opinion either way.", "neutral"),
    ("God and country, that's what built this nation.", "support"),
    ("Public schools serve everyone, not just one faith.", "oppose"),
    ("Put the Constitution in classrooms, not commandments.", "oppose"),
    ("Finally some common sense values in our schools.", "support"),
    ("Freedom of religion means freedom from it too.", "oppose"),
    ("My kids should learn this at home, not at school.", "neutral"),
]

comments_df = pd.DataFrame(comments, columns=["comment", "stance"])
comments_df'''),
    md('''Score one first, to see the move on a single row:'''),
    code('''first = comments_df["comment"].iloc[0]
print(first)
print("compound:", analyzer.polarity_scores(first)["compound"])'''),
    md('''Now scale up. `.apply()` runs a function on every row of a column — the same one-line-to-whole-
column move you used with pandas. We add the result as a new `sentiment` column.'''),
    code('''def tone(text):
    return analyzer.polarity_scores(text)["compound"]

comments_df["sentiment"] = comments_df["comment"].apply(tone)
comments_df'''),

    # ---- interpret ----
    md('''# Part 3 — Reading the Results

With a score per comment, you can ask quantitative questions of the whole crowd.'''),
    code('''print("Average tone across all comments:", round(comments_df["sentiment"].mean(), 3))

happiest = comments_df.loc[comments_df["sentiment"].idxmax()]
angriest = comments_df.loc[comments_df["sentiment"].idxmin()]
print("\\nMost positive tone:", f'{happiest["sentiment"]:+.3f}  "{happiest["comment"]}"')
print("Most negative tone:", f'{angriest["sentiment"]:+.3f}  "{angriest["comment"]}"')'''),
    md('### Your turn'),
    code('''# your turn — sort the DataFrame by sentiment and look at the order
# comments_df.sort_values("sentiment")
'''),

    # ---- the human-vs-machine payoff ----
    md('''# Part 4 — Tone Is Not the Same as Stance

Here's the critical move. We have two judgments of each comment: the **stance** *you* labeled (a
*position* — for or against the law) and the **tone** *VADER* scored (an *emotion*). It's tempting to
expect them to line up. Let's turn VADER's score into a label and put them side by side.'''),
    code('''def tone_label(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    return "neutral"

comments_df["vader_tone"] = comments_df["sentiment"].apply(tone_label)
comments_df[["comment", "stance", "vader_tone"]]'''),
    md('''Look for the **mismatches** — and notice they're not VADER "getting it wrong." Stance and tone
are *different axes*. Someone can **oppose** the law in warm, calm language, or **support** it while
sounding furious. A word like "God" or "freedom" reads positive to the lexicon no matter which side is
saying it. Distant reading (VADER's number) and close reading (your judgment) measure different things —
which is exactly why you need both.'''),
    code('''# the average TONE within each STANCE camp — do supporters "sound" more positive than opponents?
comments_df.groupby("stance")["sentiment"].mean().round(3)'''),
    code('''import matplotlib.pyplot as plt

comments_df.groupby("stance")["sentiment"].mean().plot(kind="bar", title="Average tone by stance")
plt.ylabel("mean compound sentiment")
plt.axhline(0, color="gray", linewidth=0.8)
plt.tight_layout()
plt.show()'''),

    # ---- where VADER fails ----
    md('''# Part 5 — Where VADER Breaks

VADER reads a lexicon, not a mind. It has no idea about sarcasm, irony, or context. **Predict the tone
of each line below, then run it** — and watch it miss.'''),
    code('''tricky = [
    "Oh GREAT, more religion forced on our kids.",   # sarcasm: sounds positive, isn't
    "Sure, because schools have NO other problems.",  # sarcasm
    "Honestly? Not a bad idea at all.",               # double negative = positive
    "This is beautifully, tragically un-American.",   # mixed signals
]

for text in tricky:
    c = analyzer.polarity_scores(text)["compound"]
    print(f"{c:+.3f}   {text}")'''),
    md('''Where did VADER's number disagree with your reading? Those gaps are the most interesting
findings you'll report — not failures of the tool, but the boundary where counting stops and
interpretation has to take over.'''),

    # ---- Putting it together ----
    md('''# Putting It All Together: Score, Compare, Question

The full workflow in one place — exactly what you'll run on **your own** data in HW3: score every
comment, find the extremes, and check the machine's tone against a human's stance.'''),
    code('''comments_df["sentiment"] = comments_df["comment"].apply(tone)          # score
comments_df["vader_tone"] = comments_df["sentiment"].apply(tone_label)  # label

print("Overall average tone:", round(comments_df["sentiment"].mean(), 3))
print("\\nWhere tone and stance disagree:")
mismatch = comments_df[
    ((comments_df["stance"] == "oppose") & (comments_df["vader_tone"] == "positive")) |
    ((comments_df["stance"] == "support") & (comments_df["vader_tone"] == "negative"))
]
print(mismatch[["comment", "stance", "vader_tone"]].to_string(index=False))'''),
    code('''# your turn — paste a comment of your own below and score it; does VADER agree with your read?
my_text = "Type any comment here"
print(analyzer.polarity_scores(my_text)["compound"])
'''),

    # ---- Sneak preview ----
    md('''# Sneak Preview: Where This Is Going

**In HW3** you'll do all of this on a dataset *you* collected: score it, visualize the spread, and
write up where VADER tracked your reading and where it broke. The mismatches are the point.

**Next week (Days 14–15)** brings the last technique: **topic modeling**. Sentiment asked *what
feeling?*; topic modeling asks *what is this whole pile of text even about?* — letting the computer
surface the recurring themes across hundreds of comments at once. Counting, feeling, themes: three
different ways to hear a crowd.'''),

    md('# Playground'),
    code('# use this space to experiment!\n'),
]


out = os.path.join(HERE, "WRIT20833_VADER_Sentiment_2026.ipynb")
with open(out, "w", encoding="utf-8") as f:
    json.dump(notebook(cells), f, indent=1, ensure_ascii=False)
    f.write("\n")
print("wrote", out, "(%d cells)" % len(cells))
