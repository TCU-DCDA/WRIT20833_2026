"""Builder for the 2026 'Lists, Loops & Conditionals' code-along (Days 3-4).

Until 2026-10-15 this notebook had no builder and 28 of its 31 code cells were already filled in.
This builder keeps the content, order, and the "Day 3 stops here" marker, and opens up the room
to type. House rule: the *first* worked example of each idea stays complete so students see the
shape; the *next* one is a "type along" blank (a one-line comment says what to write). Data lines
stay in the student cell so the blank is only the logic.

Two outputs from one cell list (same approach as _build_variables.py / _build_strings.py /
_build_pandas01.py):
- WRIT20833_Lists_Loops_Conditionals_2026.ipynb — the STUDENT copy. 12 type-along blanks,
  3 "predict first" guesses, and the "your turn" cells carry no answer (the podcast-hosts exercise
  used to ship its whole solution). This is the file the schedule, site, and D2L link to.
- WRIT20833_Lists_Loops_Conditionals_2026_complete.ipynb — every blank filled in. Not linked yet.
A cell is either shared, or a pair(student, complete).

No complete cell depends on a name that only a blank defines, so skipping a type-along never
strands a student later. Expected errors: none (the bad-index demo stays commented out).

Run from repo root:  python3 notebooks/codeAlongs/_build_lists.py
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


STUDENT_NB = "WRIT20833_Lists_Loops_Conditionals_2026.ipynb"
COMPLETE_NB = "WRIT20833_Lists_Loops_Conditionals_2026_complete.ipynb"


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

    md('''# WRIT 20833 — Lists, Loops & Conditionals

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    pair(md('''**How this notebook works.** It covers two class days (Friday and Monday). Some code cells are blank on purpose:
- **type along** — a comment says what to write; type it with me, then run it.
- **predict first** — write your guess in the comment *before* you run the cell.
- **your turn** — try it on your own.

If a cell gives you an error, read the message — errors are part of the work here, not something to
hide.'''),
         md('''**Complete copy.** Every blank in the class worksheet is filled in here, so you can check your
work after class. The "predict first" guesses are left for you.''')),

    # ================= DAY 3: COMPARISONS & CONDITIONALS =================
    md('''# Comparisons & Conditionals

Before we start storing whole collections of data, we need a way to make decisions. Conditionals let the computer ask yes/no questions about data.

### Comparison operators
| Operator | Meaning |
|----------|---------|
| `==` | equal to |
| `!=` | not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |
| `in` | is this inside a string? (on Monday: a list) |

**Predict first.** Each line below prints `True` or `False`. Write your three guesses in the comment, then run it.'''),
    code('''# my guess:
print(10 > 5)
print("TCU" == "tcu")       # case matters!
print("Frogs" in "TCU Horned Frogs")   # `in` from Day 2, now as a yes/no question'''),

    md('''### `if` / `elif` / `else`

An `if` statement runs code only when a condition is `True`. Add `elif` (else if) for additional checks, and `else` as a catch-all.

Notice the pattern: condition ends with a **colon** `:`, and the code underneath is **indented**.'''),
    code('''tcu_score = 34
smu_score = 31

if tcu_score > smu_score:
    print("TCU wins!")
elif tcu_score == smu_score:
    print("Headed to overtime")
else:
    print("Better luck next year")'''),

    md('Two conditions can be joined with `and` (both must be true) or `or` (either one will do).'),
    pair(code('''# type along — print "You can vote!" only if age >= 18 AND has_id is True; otherwise "Not yet eligible"
age = 20
has_id = True
'''),
         code('''# combining conditions with `and` / `or`

age = 20
has_id = True

if age >= 18 and has_id:
    print("You can vote!")
else:
    print("Not yet eligible")''')),

    md('`in` works inside a condition too. Here is a bio and a platform to look for:'),
    code('''bio = "Film student. Coffee addict. Posting mostly on TikTok and Letterboxd."
favorite = "YouTube"'''),
    pair(code('''# type along — if `favorite` is in `bio`, print that it is; otherwise print that it isn't (use an f-string)
'''),
         code('''# using `in` with conditionals

if favorite in bio:
    print(f"{favorite} is in this bio")
else:
    print(f"{favorite} is not in this bio")''')),

    md('### Your turn'),
    code('''# your turn — write an if / elif / else that sorts something into categories
# (a score, a year, a word in a caption — your choice)

'''),

    md('''---

### 🛑 Day 3 stops here

On Monday we pick up with **lists** — and `in` will work on them exactly the way it works on strings. Then we'll combine lists with the conditionals you just wrote to build **loops** that sort whole collections at once.'''),

    # ================= DAY 4: LISTS =================
    md('''# Lists

A **list** is an ordered collection of items — like a column in a spreadsheet.

So far we've stored single values in variables. But real data comes in groups: a playlist of songs, a set of hashtags, a roster of names. Lists let us work with all of them at once.

- Created with square brackets `[]`
- Items separated by commas
- Can hold any data type (strings, numbers, booleans)
- Order is preserved — first item stays first'''),
    code('''# a list of strings
platforms = ["TikTok", "Instagram", "YouTube", "Threads", "X"]

print(platforms)'''),
    pair(code('''# type along — make a list of five numbers called `follower_counts`, then print it
'''),
         code('''# a list of numbers
follower_counts = [12000, 8500, 45000, 3200, 27000]

print(follower_counts)''')),
    pair(code('''# type along — how many platforms are in the list? len() works on lists just like strings
'''),
         code('''# len() works on lists just like it works on strings
print(len(platforms))''')),
    code('''# your turn — create a list of your favorite shows, artists, or podcasts
my_favorites = []  # replace with your own items

print(my_favorites)'''),

    md('''# Indexing

Each item in a list has a position number called an **index**.

Python starts counting at **0**, not 1. Think of it like floors in a building where the ground floor is 0.

| Index | 0 | 1 | 2 | 3 | 4 |
|-------|---|---|---|---|---|
| Item | TikTok | Instagram | YouTube | Threads | X |

**Predict first.** Which platform prints on each line? Write your guesses, then run.'''),
    code('''# my guess: [0] =    [2] =    [-1] =
print(platforms[0])   # first item
print(platforms[2])   # third item
print(platforms[-1])  # last item (negative counts from the end)'''),
    code('''# what happens when you try an index that doesn't exist?
# uncomment the line below and run it — read the error message

# platforms[10]'''),

    md('''# Slicing

Slicing pulls out a portion of a list. The syntax is `list[start:stop]` — it includes the start position but stops *before* the stop position.

Think of it as "from here, up to but not including there." You did this with strings on Days 1 and 2; lists slice the same way.'''),
    pair(code('''# type along — print the first three platforms; then from index 2 to the end; then the last two
'''),
         code('''print(platforms[0:3])   # first three items
print(platforms[:3])    # same thing — blank start means "from the beginning"
print(platforms[2:])    # from index 2 to the end
print(platforms[-2:])   # last two items''')),

    md('''# List Methods

Methods are actions you can perform on a list. They use dot notation: `list.method()`'''),
    md('### Adding items — `.append()` and `.extend()`'),
    code('''# .append() adds one item to the end
artists = ["Beyoncé", "Bad Bunny", "Tyler the Creator"]
artists.append("SZA")

print(artists)'''),
    pair(code('''# type along — make new_artists = ["Kendrick Lamar", "Olivia Rodrigo"], add them all at once with .extend(), print
'''),
         code('''# .extend() adds multiple items from another list
new_artists = ["Kendrick Lamar", "Olivia Rodrigo"]
artists.extend(new_artists)

print(artists)''')),
    md('### Removing items — `.remove()`'),
    pair(code('''# type along — remove "Bad Bunny" from `artists` with .remove(), then print the list
'''),
         code('''artists.remove("Bad Bunny")

print(artists)''')),
    md('### Organizing — `.sort()` and `.reverse()`'),
    code('''artists.sort()
print("Sorted:", artists)

artists.reverse()
print("Reversed:", artists)'''),
    md('''### Counting and finding — `.count()` and `.index()`

**Predict first.** How many times does `#TCU` appear? What index is `#FortWorth` at?'''),
    code('''# my guess: count =    index =
tags = ["#TCU", "#GoFrogs", "#TCU", "#FortWorth", "#TCU"]

print(tags.count("#TCU"))       # how many times does #TCU appear?
print(tags.index("#FortWorth"))  # what position is #FortWorth at?'''),
    code('''# your turn — build a list, then try .append(), .sort(), and .count()
my_list = []

# add some items

# sort it

# count something

print(my_list)'''),

    # ================= FOR LOOPS =================
    md('''# For Loops

A **for loop** repeats an action for every item in a list. This is where coding gets powerful — instead of writing the same code over and over, you write it once and the loop handles the rest.

The structure:
```python
for item in my_list:
    do something with item
```

- `item` is a temporary variable that takes on each value in the list, one at a time
- The indented code runs once per item
- You can name `item` whatever makes sense (`name`, `tag`, `year`, etc.)'''),
    code('''# loop through our platforms list
for platform in platforms:
    print(f"Checking: {platform}")'''),
    pair(code('''# type along — loop over `prices`; for each one, multiply by 1.0825 (Texas sales tax) and print both numbers
prices = [9.99, 14.99, 4.99, 19.99]
'''),
         code('''# loop with numbers — calculate something for each item
prices = [9.99, 14.99, 4.99, 19.99]

for price in prices:
    with_tax = price * 1.0825  # Texas sales tax
    print(f"${price} → ${with_tax:.2f} with tax")''')),

    md('''### Loops + Conditionals

The real power shows up when you combine loops with `if` statements — now you can process a list *and* make decisions about each item.'''),
    code('''# filter: which platforms have short names?
for platform in platforms:
    if len(platform) <= 5:
        print(f"{platform} — short name ({len(platform)} chars)")
    else:
        print(f"{platform} — longer name ({len(platform)} chars)")'''),
    pair(code('''# type along — for each year print its generation: <= 1964 Boomer, <= 1980 Gen X, <= 1996 Millennial, else Gen Z
years = [1966, 1985, 1997, 2003, 1961, 1995]
'''),
         code('''# a more realistic example — classifying birth years by generation
years = [1966, 1985, 1997, 2003, 1961, 1995]

for year in years:
    if year <= 1964:
        print(f"{year}: Boomer")
    elif year <= 1980:
        print(f"{year}: Gen X")
    elif year <= 1996:
        print(f"{year}: Millennial")
    else:
        print(f"{year}: Gen Z")''')),

    md('''### Counting with loops

A common pattern: start a counter at 0, then add to it inside a loop.'''),
    code('''# count how many hashtags mention TCU
tags = ["#TCU", "#GoFrogs", "#FortWorth", "#TCU", "#BigXII", "#TCU"]

tcu_count = 0

for tag in tags:
    if tag == "#TCU":
        tcu_count = tcu_count + 1

print(f"TCU was mentioned {tcu_count} times out of {len(tags)} total tags")'''),

    md('''### Building new lists from old ones

Another essential pattern: start with an empty list, loop through a source list, and `.append()` items that meet your criteria.

This is like going through a library catalog and pulling only the books that match your research topic.'''),
    code('''# pull out only the short platform names
short_names = []

for platform in platforms:
    if len(platform) <= 5:
        short_names.append(platform)

print("Short platform names:", short_names)'''),
    pair(code('''# type along — build `clean_authors`: only the names that do NOT contain "(?)"; then print raw and clean
raw_authors = ["Toni Morrison", "Unknown (?)", "James Baldwin", "N.K. Jemisin", "Anonymous (?)"]
'''),
         code('''# clean messy data — remove items with question marks
raw_authors = ["Toni Morrison", "Unknown (?)", "James Baldwin", "N.K. Jemisin", "Anonymous (?)"]

clean_authors = []

for author in raw_authors:
    if "(?)" not in author:
        clean_authors.append(author)

print("Raw:", raw_authors)
print("Clean:", clean_authors)''')),

    md('''### Using `enumerate()` — tracking position

Sometimes you need to know both the item *and* its position. `enumerate()` gives you both.'''),
    code('''# create a numbered playlist
playlist = ["Not Like Us", "Espresso", "Birds of a Feather", "APT.", "Die With a Smile"]

for position, song in enumerate(playlist, 1):  # start counting at 1
    print(f"{position}. {song}")'''),

    # ================= PUTTING IT ALL TOGETHER =================
    md('''# Putting It All Together

Let's combine everything — lists, methods, loops, and conditionals — to do something that actually looks like digital humanities work.'''),
    code('''# analyze hashtag frequency from a mock social media dataset
social_tags = ["#climate", "#action", "#justice", "#climate", "#equality",
               "#justice", "#climate", "#activism", "#equality", "#climate"]

# find unique tags and count each one
analyzed = []

print("Hashtag Frequency Analysis")
print("-" * 30)

for tag in social_tags:
    if tag not in analyzed:
        count = social_tags.count(tag)
        print(f"{tag}: {count} times")
        analyzed.append(tag)

print(f"\\nTotal tags: {len(social_tags)}")
print(f"Unique tags: {len(analyzed)}")'''),
    md('### Your turn'),
    pair(code('''# your turn — how many podcasts are hosted on each platform?
# Use the counting pattern: start a counter at 0 for each platform, loop, add one when it matches.
# Then print each count. Bonus: print each one as a percentage of the total.
podcast_hosts = ["Spotify", "Apple", "Spotify", "YouTube", "Spotify", "Apple", "YouTube", "Spotify"]
'''),
         code('''# your turn — how many podcasts are hosted on each platform?
podcast_hosts = ["Spotify", "Apple", "Spotify", "YouTube", "Spotify", "Apple", "YouTube", "Spotify"]

# count how many are on each platform
spotify_count = 0
apple_count = 0
youtube_count = 0

for host in podcast_hosts:
    if host == "Spotify":
        spotify_count = spotify_count + 1
    elif host == "Apple":
        apple_count = apple_count + 1
    elif host == "YouTube":
        youtube_count = youtube_count + 1

total = len(podcast_hosts)
print(f"Spotify: {spotify_count} ({spotify_count/total*100:.0f}%)")
print(f"Apple: {apple_count} ({apple_count/total*100:.0f}%)")
print(f"YouTube: {youtube_count} ({youtube_count/total*100:.0f}%)")''')),

    # ================= SNEAK PREVIEW =================
    md('''# Sneak Preview: Where This Is Going

Now that you can work with lists and loops, you're ready for the next level. Dictionaries let you pair **keys** with **values** — like a contact list where each name has a phone number. Functions let you package your code into reusable tools.

Here's a taste of what's coming:'''),
    code('''# dictionaries — pair keys with values (next lesson)
album = {
    "title": "Renaissance",
    "artist": "Beyoncé",
    "year": 2022,
    "tracks": 16
}

print(f"{album['title']} by {album['artist']} ({album['year']})")
print(f"{album['tracks']} tracks")'''),
    code('''# functions — reusable code blocks (next lesson)
def classify_year(year):
    if year <= 1964:
        return "Boomer"
    elif year <= 1980:
        return "Gen X"
    elif year <= 1996:
        return "Millennial"
    else:
        return "Gen Z"

# now we can use it in a loop
family = [1962, 1985, 1997, 2004]

for year in family:
    generation = classify_year(year)
    print(f"{year} → {generation}")'''),

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
