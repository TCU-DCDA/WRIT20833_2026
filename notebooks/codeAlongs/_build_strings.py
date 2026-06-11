"""Builder for the 2026 'Strings & String Methods' code-along (Day 2).

Ports the string half of F25's WRIT20833_StrMethods_Conditionals_Loops_F25.ipynb into the
existing 2026 code-along house style (warm cultural examples; concept -> code -> 'your turn';
Putting It All Together -> Sneak Preview -> Playground; colab metadata; no HW-style #comments).
Walsh-independent and Drive-mount-independent (F25 read Kafka off Google Drive; here the text is
inline so the notebook runs anywhere).

The F25 source bundled strings + comparisons + conditionals + lists + loops in one notebook. In
2026 those latter topics already live in WRIT20833_Lists_Loops_Conditionals_2026 (Days 3-4), so
this Day-2 notebook is strings-ONLY. It goes deeper than the quick string section in the Day-1
Variables notebook (index/slice/concat/lower/count/split/f-string) by adding replace, strip,
membership, join, startswith/endswith, and a 'clean a real comment' routine that seeds Week-2
term frequency.

Run from repo root:  python3 notebooks/codeAlongs/_build_strings.py
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
    # match the existing 2026 code-alongs' metadata exactly
    return {"cells": cells, "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 0}


cells = [
    md('<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/codeAlongs/WRIT20833_String_Methods_2026.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'),

    md('''# WRIT 20833 — Strings & String Methods

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    md('''Yesterday you met the **string** — Python's data type for text. Almost all the cultural data
we'll analyze in this course *is* text: comments, lyrics, headlines, speeches. So before we can study
it, we need to get comfortable handling it. A string isn't just one blob — it's an ordered **sequence
of characters**, and Python gives us a toolbox of **string methods** for reaching into it, measuring
it, and reshaping it.'''),

    # ---- A real text to work with ----
    md('''# A Text to Work With

Let's start with a single real-sounding comment — the kind of thing people actually post about a
public-policy debate. We'll spend this lesson taking it apart.'''),
    code('''comment = "Honestly the Ten Commandments belong in our schools. They taught morals for thousands of years and God made this country great."

print(comment)
print("Characters:", len(comment))'''),
    md('`len()` counts **every character**, including spaces and punctuation — not words. We\'ll get to words soon.'),

    # ---- Index ----
    md('''# Index: One Character at a Time

Every character has a position, or **index**, starting at **0**. Square brackets pull out the
character at a position. Negative numbers count from the *end*.'''),
    code('''print(comment[0])    # the very first character
print(comment[7])    # the eighth character
print(comment[-1])   # the last character (the period)'''),

    # ---- Slice ----
    md('''# Slice: A Range of Characters

A **slice** grabs a span. The syntax is `text[start : stop]` — it starts at `start` and stops *just
before* `stop`. Leave a side blank to mean "the beginning" or "the end."'''),
    code('''print(comment[:9])     # from the start, up to (not including) index 9
print(comment[10:25])  # a middle chunk
print(comment[-13:])   # the last 13 characters'''),
    md('You can save a slice to a variable, just like any other value:'),
    code('''opening = comment[:9]
print(opening, "...")'''),
    md('### Your turn'),
    code('''# your turn — slice out the first 25 characters of this lyric
lyric = "I'm beginning to feel like a Rap God, Rap God"

# print(lyric[ ... ])
'''),

    # ---- Upper / lower (and why it matters) ----
    md('''# Uppercase & Lowercase

`.upper()` and `.lower()` return a **new** string in that case. This is not just cosmetic. When a
computer compares text, `"God"` and `"god"` are *different* strings. Lowercasing everything first is
how we make them count as the **same word** — a move you'll rely on the moment you start counting
words.'''),
    code('''print(comment.upper())
print(comment.lower())'''),
    code('''# "God" and "god" are not equal — until you lowercase
print("God" == "god")
print("God".lower() == "god".lower())'''),

    # ---- Replace ----
    md('''# Replace: Swap One Substring for Another

`.replace(old, new)` hands back a copy with every match swapped. The original string is unchanged —
string methods never edit in place; they **return a new string**. Have a little fun with it first:'''),
    code('''print(comment.replace("schools", "group chats"))
print(comment.replace(" ", " 🐸 "))'''),
    md('''The serious use is **cleaning**. Real text is full of stray newline characters (`\\n`) and
junk you want gone before analysis. Replace turns messy text into tidy text.'''),
    code('''messy = "God\\nand\\ncountry"
print(messy)                       # the \\n's break it across lines
print("---")
print(messy.replace("\\n", " "))   # one clean line'''),
    md('### Your turn'),
    code('''# your turn — replace "great" with a word of your choosing, then print it
# remember: replace returns a NEW string, so print the result (or save it to a variable)
'''),

    # ---- Strip ----
    md('''# Strip: Trim the Edges

Text copied from the web often arrives wrapped in extra spaces or newlines. `.strip()` removes
whitespace from **both ends** (not the middle) — small but essential cleaning.'''),
    code('''raw = "   too much space here   "
print("[" + raw + "]")
print("[" + raw.strip() + "]")'''),

    # ---- count & membership ----
    md('''# Count & Membership: Asking Questions of the Text

Two quick ways to interrogate a string. `.count()` tells you **how many times** something appears;
the `in` keyword answers **yes or no** — is this substring present?'''),
    code('''text = comment.lower()                 # lowercase first, so case can't fool us
print(text.count("o"))                 # how many letter o's
print(text.count("god"))               # how many times the letters "god" appear
print("commandments" in text)          # is it mentioned at all? -> True / False
print("freedom" in text)'''),
    md('''Heads up: `.count()` matches **characters**, not whole words — `count("god")` would also catch
the "god" hidden inside *"goddess"* or *"godless."* (Counting real **words** needs `.split()`, coming up
next.) And notice we lowercased **once** at the top and reused it — a habit worth keeping: clean the
text, then ask your questions of the clean version.'''),

    # ---- Split (the bridge) ----
    md('''# Split: From One String to a List of Words

This is the most important method in the course. `.split()` breaks a string into a **list** of
pieces. With no argument it splits on whitespace — turning a sentence into its **words**.'''),
    code('''words = comment.split()
print(words)
print("Word count:", len(words))'''),
    md('''Now `len()` counts **words**, not characters, because `words` is a list. Splitting is the
hinge between "a text" and "data you can count" — it's where cultural analytics begins.

You can also split on a specific delimiter by passing it in:'''),
    code('''csv_row = "god,country,schools,morals"
print(csv_row.split(","))   # split on commas instead of spaces'''),
    md('### Your turn'),
    code('''# your turn — split this comment into words and print how many there are
your_comment = "Keep religion out of public schools please"

# words = your_comment.split()
# print(words)
# print(len(words))
'''),

    # ---- Join ----
    md('''# Join: From a List Back to a String

`.join()` is split's mirror image: it glues a list of strings back together with a separator of your
choice. The string you call it on *is* the glue.'''),
    code('''words = ["God", "and", "country"]
print(" ".join(words))     # glue with spaces
print("-".join(words))     # glue with hyphens'''),

    # ---- startswith / endswith ----
    md('''# Startswith & Endswith

Two handy yes/no checks — useful later for filtering (e.g. keep only comments that start with a
hashtag, or files that end in `.txt`).'''),
    code('''print(comment.startswith("Honestly"))
print(comment.endswith("?"))'''),

    # ---- Putting it together ----
    md('''# Putting It All Together: Clean, Then Inspect

Here's the real workflow. Take a messy comment, **clean** it (lowercase, drop newlines, trim), then
**inspect** it (split into words, count them, check for a keyword). Every method below you just
learned — chained into one small routine.'''),
    code('''raw_comment = "  The Ten Commandments\\nDON'T belong in schools.  "

clean = raw_comment.lower().replace("\\n", " ").strip()
words = clean.split()

print("Cleaned:", clean)
print("Words:", words)
print("Word count:", len(words))
print("Mentions schools?", "schools" in clean)'''),
    md('''Read that middle line again: `raw_comment.lower().replace("\\n", " ").strip()`. We
**chained** three methods — each returns a new string, which the next one acts on, left to right.
That one line is a preview of how you'll prep real data all term.'''),
    code('''# your turn — clean and inspect this one the same way
mine = "   GOD bless\\nthis great nation   "

# clean = mine.lower().replace("\\n", " ").strip()
# print(clean.split())
'''),

    # ---- Sneak preview ----
    md('''# Sneak Preview: Where This Is Going

`.split()` just handed you a **list** of words. Tomorrow we learn to **loop** over lists — visiting
every word, one at a time — and to ask **conditional** questions about each (*is this an
interesting word, or just "the" and "and"?*). Put those together and you can do this:'''),
    code('''comment = "god god country schools god morals freedom god"
words = comment.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)'''),
    md('''Don't worry about every line yet — that's the next two lessons. But notice the shape of it:
**split a text into words, then count them.** That single idea, scaled up to thousands of real
comments, is **term frequency** — the first real analysis you'll run in Week 2, and the start of
hearing what a crowd is actually saying.'''),

    md('# Playground'),
    code('# use this space to experiment!\n'),
]


out = os.path.join(HERE, "WRIT20833_String_Methods_2026.ipynb")
with open(out, "w", encoding="utf-8") as f:
    json.dump(notebook(cells), f, indent=1, ensure_ascii=False)
    f.write("\n")
print("wrote", out, "(%d cells)" % len(cells))
