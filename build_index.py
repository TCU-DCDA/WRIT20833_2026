"""Build the course site landing page (index.html) — the launchpad for everything.

Organized on the Fall-2025 site model (https://tcu-dcda.github.io/WRIT20833_2025/): a single
dashboard with a top nav and sectioned card grids, adapted to the trimmed 2026 scope. Uses the
shared "Reading Room" theme in site_theme.py. Notebook cards open in Google Colab (the same
github/blob URLs the in-notebook badges use); those resolve once the repo is public.

Run from repo root:  python3 build_index.py
"""
import html
import os
from site_theme import PAGE, sidebar, shell, write_stylesheet

OUT = "docs/index.html"
REPO = "TCU-DCDA/WRIT20833_2026"
COLAB = f"https://colab.research.google.com/github/{REPO}/blob/main/"
GH = f"https://github.com/{REPO}"
GH_BLOB = f"{GH}/blob/main/"  # renders a repo file (e.g. the syllabus .md) on github.com

# --- code-alongs, grouped by week ---
CODEALONGS_BY_WEEK = [
    ("Week 1", "Python foundations", [
        ("Variables & Data Types", "How Python stores text and numbers.", "Day 1", "notebooks/codeAlongs/WRIT20833_Variables_DataTypes_2026.ipynb"),
        ("Strings & String Methods", "Slicing, cleaning, and splitting text.", "Day 2", "notebooks/codeAlongs/WRIT20833_String_Methods_2026.ipynb"),
        ("Lists, Loops & Conditionals", "Collections, iteration, and decisions.", "Days 3–4", "notebooks/codeAlongs/WRIT20833_Lists_Loops_Conditionals_2026.ipynb"),
        ("Dictionaries & Functions", "Key–value data and reusable tools.", "Day 5", "notebooks/codeAlongs/WRIT20833_Dictionaries_Functions_2026.ipynb"),
    ]),
    ("Week 2", "From text to data", [
        ("Term Frequency", "Counting words to hear what a text is about.", "Day 6", "notebooks/codeAlongs/WRIT20833_Term_Frequency_2026.ipynb"),
        ("Found Data & Pandas", "Collection ethics, then DataFrames.", "Day 8", "notebooks/codeAlongs/WRIT20833_Pandas_01_Found_Data_2026.ipynb"),
        ("Data Cleaning", "Turning messy scraped data tidy.", "Day 9", "notebooks/codeAlongs/WRIT20833_Pandas_02_Cleaning_2026.ipynb"),
    ]),
    ("Week 3", "Computational text analysis", [
        ("Sentiment with VADER", "Scoring emotional tone — and judging it.", "Days 11–12", "notebooks/codeAlongs/WRIT20833_VADER_Sentiment_2026.ipynb"),
        ("Topic Modeling (Gensim)", "Discovering themes across a corpus.", "Days 14–15", "notebooks/codeAlongs/WRIT20833_Topic_Modeling_Gensim_2026.ipynb"),
    ]),
]

# --- homework ---
HOMEWORK = [
    ("HW1 · Foundations", "Python basics on real text.", "due Day 6", "notebooks/homework/WRIT20833_HW1_2026.ipynb"),
    ("HW2 · Term Frequency", "“Whose words win?” — comments vs. the Constitution.", "due Day 10", "notebooks/homework/WRIT20833_HW2_2026.ipynb"),
    ("HW3 · Sentiment", "Support, opposition, and what counting missed.", "due Day 15", "notebooks/homework/WRIT20833_HW3_2026.ipynb"),
    ("HW4 · Topic Modeling + Integration", "Themes, then all three lenses together.", "due Day 17", "notebooks/homework/WRIT20833_HW4_2026.ipynb"),
]

# --- mini-lectures (the ~25-min conceptual frames) — not yet built as pages ---
# ML0-7 map cleanly to 2026; ML2 and ML9 are under review (WORKLOG thread #9); ML10-12 (web) cut.
# (title, desc, when, page) — page is a docs-relative URL when the lecture has an authored
# reading page (built by build_lectures.py); None keeps it a "soon" placeholder card.
LECTURES = [
    ("ML0 · Humanities & Coding", "Why a humanist learns to code.", "Day 1", "lectures/ml0.html"),
    ("ML1 · Connotations & Code", "Code is not neutral.", "Day 1", "lectures/ml1.html"),
    ("ML2 · Sacred Boundaries", "Privacy & the limits of analysis. (under review)", "Day 2", None),
    ("ML3 · Classification Logic", "Whose categories? Sorting as judgment.", "Day 3", "lectures/ml3.html"),
    ("ML5 · Collective Memory", "What a culture keeps and forgets.", "Day 4", "lectures/ml5.html"),
    ("ML4 · AI Agency", "Reading & judging machine-written code.", "Day 7", None),
    ("ML6 · Data Archaeology", "Where found data comes from.", "Day 8", None),
    ("ML7 · NLP & Topic Modeling", "Teaching machines to read culture.", "Day 14", None),
    ("ML9 · Going Public", "Analysis → public argument. (under review)", "Day 17", None),
]

RESOURCES = [
    ("Tools", "Google Colab", "https://colab.research.google.com/", "runs every notebook — no install"),
    ("Tools", "Course GitHub repo", GH, "all notebooks, data, and docs"),
    ("Data", "Course corpus", f"{GH}/tree/main/notebooks/data", "123 YouTube comments · the U.S. Constitution"),
    ("Reference", "Python docs", "https://docs.python.org/3/", "the language reference"),
    ("Reference", "pandas", "https://pandas.pydata.org/docs/", "DataFrames & data wrangling"),
    ("Reference", "VADER sentiment", "https://github.com/cjhutto/vaderSentiment", "the sentiment lexicon we use"),
    ("Reference", "Gensim LDA", "https://radimrehurek.com/gensim/", "topic modeling"),
    ("Further reading", "Melanie Walsh, Cultural Analytics", "https://melaniewalsh.github.io/Intro-Cultural-Analytics/", "optional model & inspiration"),
]


def card(label, title, desc, when, href, soon=False):
    cls = "card soon" if soon else "card"
    when_html = f'<span class="when">{html.escape(when)}</span>' if when else ""
    inner = (f'<span class="lbl">{html.escape(label)}</span>'
             f'<h3>{title}</h3><p>{html.escape(desc)}</p>{when_html}')
    if href:
        return f'<a class="{cls}" href="{href}">{inner}</a>'
    return f'<div class="{cls}">{inner}</div>'


def grid(cards):
    return '<div class="grid">' + "".join(cards) + "</div>"


def section(anchor, n, title, lede, body):
    return (f'<section class="sec" id="{anchor}">'
            f'<h2><span class="n">{n}</span>{html.escape(title)}</h2>'
            f'<p class="lede">{lede}</p>{body}</section>')


def render():
    side = sidebar(
        "WRIT 20833 · Summer 2026",
        "When Coding Meets Culture",
        [("#start", "Start here", "00"),
         ("#codealongs", "Code-alongs", "01"),
         ("#homework", "Homework", "02"),
         ("#capstone", "Capstone", "03"),
         ("#lectures", "Lectures", "04"),
         ("#resources", "Resources", "05")],
        [(GH, "GitHub ↗"), ("https://colab.research.google.com/", "Colab ↗")],
    )

    masthead = (
        '<header class="masthead">'
        '<div class="kicker">WRIT 20833 · Summer 2026 · TCU</div>'
        '<h1>When Coding Meets Culture</h1>'
        '<p class="sub">Developing data-driven opinions — a four-week introduction to coding in the '
        'humanities.</p>'
        '<p class="meta">Learn just enough Python to ask humanistic questions of real text — term '
        'frequency, sentiment, topic modeling — and to argue from what you find, while staying honest '
        'about what computation reveals and flattens. No prior coding experience needed. '
        'Everything launches from this page.</p>'
        '</header>'
    )

    start = section(
        "start", "00", "Start here",
        "The two documents that frame the course.",
        grid([
            card("Schedule", "Course Schedule", "Day-by-day: lecture, coding, and what's due.",
                 "20 sessions", "schedule.html"),
            card("Syllabus", "Syllabus", "Outcomes, the ungrading policy, AI-use policy, and dates.",
                 "draft", GH_BLOB + "SYLLABUS_2026.md"),
        ]))

    ca_body = "".join(
        '<div class="wkgroup"><h3><span class="wkn">' + html.escape(wk) + '</span>'
        + html.escape(theme) + '</h3>'
        + grid([card("Code-along", t, d, w, COLAB + p) for (t, d, w, p) in items])
        + '</div>'
        for (wk, theme, items) in CODEALONGS_BY_WEEK)
    codealongs = section(
        "codealongs", "01", "Code-alongs",
        "Instructor-led notebooks we build together in class — one per coding day, grouped by week. "
        "Each opens in Colab.",
        ca_body)

    homework = section(
        "homework", "02", "Homework",
        "Four notebooks where you apply the skills to a cultural dataset — ideally one you choose. "
        "(Due dates are confirmed in the syllabus.)",
        grid([card("Homework", t, d, w, COLAB + p) for (t, d, w, p) in HOMEWORK]))

    capstone = section(
        "capstone", "03", "Capstone & stylometry",
        "The final evaluative exercise integrates all three methods on data you choose; the stylometry "
        "track is an alternative path.",
        grid([
            card("Capstone", "Data-Driven Opinion", "Notebook analysis + short essay, presented Fri 7/31.",
                 "Week 4", GH_BLOB + "CAPSTONE_2026.md"),
            card("Exercise", "Reading for the Seams", "Stylometry close-reading: hearing a human (or AI) voice.",
                 "Day 7 · Week 4", GH_BLOB + "materials/stylometry/Reading_for_the_Seams.md"),
            card("Notebook", "Stylometry (computational)", "The computational half of the stylometry exercise.",
                 "Week 4", COLAB + "materials/stylometry/WRIT20833_Stylometry_Reading_Seams_2026.ipynb"),
        ]))

    lectures = section(
        "lectures", "04", "Lectures",
        "The short conceptual frames that open each day — the “code is not neutral” throughline. "
        "ML0 is live as a reading page; the rest are in development. ML2 and ML9 are under review.",
        grid([card("Mini-lecture", t, d, w, p, soon=(p is None)) for (t, d, w, p) in LECTURES]))

    res_items = "".join(
        f'<li><span class="k">{html.escape(k)}</span>'
        f'<a href="{href}">{html.escape(name)}</a> — <span class="muted">{html.escape(note)}</span></li>'
        for (k, name, href, note) in RESOURCES)
    resources = (f'<section class="sec" id="resources"><h2><span class="n">05</span>Resources</h2>'
                 f'<p class="lede">Tools, the course data, and references for going further.</p>'
                 f'<ul class="reslist">{res_items}</ul></section>')

    main = (masthead + start + codealongs + homework + capstone + lectures + resources +
            '<footer>WRIT 20833 · Summer 2026 · “hear the human at scale” · '
            'a working draft, adjusted to the class’s pace</footer>')
    return PAGE("WRIT 20833 — When Coding Meets Culture", shell(side, main), wrap=False)


if __name__ == "__main__":
    css = write_stylesheet(os.path.dirname(OUT) or ".")
    out = render()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes) + {css} ({os.path.getsize(css)} bytes)")
