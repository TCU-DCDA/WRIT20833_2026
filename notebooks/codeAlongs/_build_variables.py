"""Builder for the 2026 'Variables & Data Types' code-along (Day 1).

Until 2026-10-15 this notebook had no builder and every one of its 24 concept cells was already
filled in, so a "code-along" had nothing left to type. This builder keeps the Day-1 content and
order (variables -> reassignment -> the four data types -> type() -> a first pass at strings ->
arithmetic -> the intentional TypeError -> Sneak Preview -> Playground) and opens up the room:

Two outputs from one cell list (same approach as _build_pandas01.py / _build_strings.py):
- WRIT20833_Variables_DataTypes_2026.ipynb — the STUDENT copy. The first worked example of each
  idea stays complete so students see the shape; the *next* move is a "type along" cell left
  blank (a one-line comment says what to write). "Predict first" cells ask for a guess before
  running; "your turn" cells carry no answer. This is the file the schedule, site, and D2L link to.
- WRIT20833_Variables_DataTypes_2026_complete.ipynb — every blank filled in. Not linked anywhere yet.
A cell is either shared, or a pair(student, complete).

The intentional TypeError ("read the error message carefully") is still here and is the only
expected error in any notebook in the repo. Nothing after a blank depends on it: skipping a
type-along cell never breaks a later complete cell.

Run from repo root:  python3 notebooks/codeAlongs/_build_variables.py
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


STUDENT_NB = "WRIT20833_Variables_DataTypes_2026.ipynb"
COMPLETE_NB = "WRIT20833_Variables_DataTypes_2026_complete.ipynb"


def badge(name):
    return md('<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/'
              'notebooks/codeAlongs/' + name + '" target="_parent"><img src="https://colab.research.'
              'google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>')


def notebook(cells):
    # match the existing 2026 code-alongs' metadata exactly
    return {"cells": cells, "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 0}


cells = [
    pair(badge(STUDENT_NB), badge(COMPLETE_NB)),

    md('''# WRIT 20833 — Variables & Data Types

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    pair(md('''**How today works.** Some code cells are blank on purpose:
- **type along** — a comment says what to write; type it with me, then run it.
- **predict first** — write your guess in the comment *before* you run the cell.
- **your turn** — try it on your own.

If a cell gives you an error, read the message — errors are part of the work here, not something to
hide. (One cell today is *supposed* to error. You'll know it when you see it.)'''),
         md('''**Complete copy.** Every blank in the class worksheet is filled in here, so you can check your
work after class. The "predict first" guesses are left for you.''')),

    # ================= VARIABLES =================
    md('''# Variables

A variable is a **label** we apply to a stored data point.

- The data exists at a specific memory location with its own address
- The variable is just a human-friendly name that points to that location
- The data and the variable name are separate things'''),

    md('''# Variable Names

### Good variable names
- **Descriptive**: `song_title` is better than `x`
- **snake_case**: words separated by underscores (`comment_count`, not `commentCount`)
- **Lowercase**: capital letters are reserved for special things in Python

### Off-limits names
Python has reserved words you can't use as variable names. If you accidentally use one, things break quietly:
- `type`, `print`, `list`, `str`, `int` — these are built-in functions
- `for`, `if`, `while`, `class`, `return` — these are language keywords'''),

    pair(code('''# type along — store a first name in a variable called `name`, then print it
'''),
         code('''name = "Curt"

print(name)''')),

    md('''# Re-Assigning Variables

A variable only ever points at one value. Assign something new and the old value is simply gone.'''),
    pair(code('''# type along — assign a different name to `name`, then print it again. Where did the first one go?
'''),
         code('''name = "Brad"

print(name)''')),

    # ================= DATA TYPES =================
    md('''# Data Types

Four to know today:

* Strings — text, in quotes
* Integers — whole numbers
* Floats — numbers with a decimal point
* Booleans — `True` or `False`'''),

    code('''# Strings — anything in quotes is text, even if it looks like a number

happiest_students = "TCU"
happiest_number_of_students = "40"

print(happiest_students)
print(happiest_number_of_students)'''),
    md('''**Predict first.** `type()` tells you what kind of value a variable holds. Is `"40"` a number here?
Write your guess in the comment, then run the cell.'''),
    code('''# my guess:
type(happiest_number_of_students)'''),

    pair(code('''# type along — assign the number 40 (no quotes) to `happiest_number_of_students`, then check its type
'''),
         code('''# Integers

happiest_number_of_students = 40

type(happiest_number_of_students)''')),

    code('''# Floats — the decimal point is what makes it a float

pi = 3.14

type(pi)'''),

    code('''# Booleans — a comparison with == asks a yes/no question and answers True or False

old_friend = "Brad"
new_friend = "Selina"

"Selina" == old_friend'''),
    md('### Your turn'),
    pair(code('''# your turn — write a comparison of your own that comes out True
'''),
         code('''# your turn — write a comparison of your own that comes out True
"Selina" == new_friend''')),

    md('''# Check Data Types

Four variables, four types. `type()` on each one:'''),
    code('''# Check the type of each variable we've created

print(type(happiest_students))
print(type(happiest_number_of_students))
print(type(pi))
print(type(old_friend == new_friend))'''),

    # ================= STRINGS =================
    md('''# Strings and String Methods

A quick first pass — Wednesday's whole session is strings, so today is just a taste.'''),
    code('''# index — every character has a numbered position, starting at 0

beyonce = "a famous and very rich artist"

len(beyonce)'''),
    md('**Predict first.** Count along the string: which character is at position 14? (Spaces count.)'),
    code('''# my guess:
beyonce[14]'''),

    pair(code('''# type along — slice from index 14 up to (but not including) index 20
'''),
         code('''# slice

beyonce[14:20]''')),

    code('''# add (concatenate) — + glues two strings together

name = "TJ"
action = " is sitting"

print(name + action)'''),

    pair(code('''# type along — set `name` to "Curt" and `moniker` to "curt"; lowercase `name` with .lower(), then compare the two with ==
'''),
         code('''# lowercase

name = "Curt"
moniker = "curt"

name2 = name.lower()

name2 == moniker''')),

    pair(code('''# type along — count how many times the letter "a" appears in `beyonce` with .count()
'''),
         code('''# count — how many times does a character or word appear?

beyonce.count("a")''')),

    code('''# split — break a string into a list of words

words = beyonce.split()

print(words)
print(len(words))'''),

    code('''# f-string — embed variables directly inside a string

artist = "Beyoncé"
album_count = 8

print(f"{artist} has released {album_count} studio albums.")
print(f"That's roughly one album every {30 // album_count} years.")'''),
    md('### Your turn'),
    pair(code('''# your turn — write an f-string about an artist, show, or team you follow, using at least one variable
'''),
         code('''# your turn — write an f-string about an artist, show, or team you follow, using at least one variable
team = "TCU"
wins = 11

print(f"{team} won {wins} games last season.")''')),

    # ================= NUMBERS =================
    md('''# Integers & Floats and Operations

When we're dealing with actual numbers (whole numbers and decimal points), we can use basic mathematical operations that should be pretty familiar:

 * x + y
 * x - y
 * x * y
 * x / y
 * -x
 * x**y (x to the y power)

Some operations that are helpful but less obvious would be:

*  x // y (floored quotient of x and y)
*  x % y (remainder of x/y)'''),

    code('''# x**y — exponentiation

followers = 1000
annual_growth = 2

# if followers doubled every year for 5 years
followers * annual_growth**5'''),

    pair(code('''# type along — 23 songs, 2 per side of a record: how many are left over? use % (modulo)
'''),
         code('''# x % y — modulo (remainder)

total_songs = 23
songs_per_side = 2

# how many songs left over after filling both sides?
total_songs % songs_per_side''')),

    # ================= TYPE ERRORS =================
    md('''# Type Errors

Python will not quietly guess what you meant when you mix types. It stops and tells you.'''),
    code('''# What happens when you mix types?

greeting = "hello"
number = 5

# this will cause a TypeError — read the error message carefully
greeting + number'''),
    md('''Read the last line of that message. It names the two types that didn't fit together. There are two
ways to fix it, depending on what you want:'''),
    pair(code('''# type along — fix it two ways: (1) turn `number` into a string with str() and use +; (2) use an f-string
'''),
         code('''# Two ways to fix it — depends on what you want

# Option 1: convert the number to a string (concatenation)
print(greeting + str(number))

# Option 2: use an f-string (usually cleaner)
print(f"{greeting} {number}")''')),

    # ================= SNEAK PREVIEW =================
    md('''# Sneak Preview: Where This Is Going

Everything we just learned — variables, strings, `.split()`, f-strings — is the foundation for analyzing real cultural data. Here's a taste of what we'll be doing in a few weeks.'''),
    code('''# A real headline about the Ten Commandments in public schools
headline = "Louisiana law requiring Ten Commandments in classrooms blocked by federal judge"

# Use .split() to count words
word_count = len(headline.split())

# Use `in` to check for a keyword
mentions_law = "law" in headline

# Use an f-string to report what we found
print(f"Headline: {headline}")
print(f"Word count: {word_count}")
print(f"Mentions 'law': {mentions_law}")'''),

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
