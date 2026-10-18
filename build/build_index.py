"""Build the course site landing page (index.html) — the launchpad for everything.

Organized on the Fall-2025 site model (https://tcu-dcda.github.io/WRIT20833_2025/): a single
dashboard with a top nav and sectioned card grids, adapted to the trimmed 2026 scope. Uses the
shared "Reading Room" theme in site_theme.py. Notebook cards open in Google Colab (the same
github/blob URLs the in-notebook badges use); those resolve once the repo is public.

Run from repo root:  python3 build_index.py
"""
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))  # repo root: paths below are repo-relative
import html
import os
from site_theme import PAGE, site_header, site_footer, write_stylesheet
from build_chatbot import CHAT_API_URL  # the Code Guide card appears only once its Worker is deployed
from release_dates import gate_attrs, day_gate_attrs  # cards unlink themselves until their schedule day

OUT = "docs/index.html"
REPO = "TCU-DCDA/WRIT20833_2026"
COLAB = f"https://colab.research.google.com/github/{REPO}/blob/main/"
GH = f"https://github.com/{REPO}"
GH_BLOB = f"{GH}/blob/main/"  # renders a repo file (e.g. the syllabus .md) on github.com
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"  # direct asset URLs (images) — resolves once public
HERO = RAW + "materials/lectures/images/messy_humanities.jpg"

# --- code-alongs, grouped by week ---
CODEALONGS_BY_WEEK = [
    ("Weeks 1–2", "Python foundations", [
        ("Variables & Data Types", "How Python stores text and numbers.", "Day 1", "notebooks/codeAlongs/WRIT20833_Variables_DataTypes_2026.ipynb"),
        ("Strings & String Methods", "Slicing, cleaning, and splitting text.", "Day 2", "notebooks/codeAlongs/WRIT20833_String_Methods_2026.ipynb"),
        ("Lists, Loops & Conditionals", "Collections, iteration, and decisions.", "Days 3–4", "notebooks/codeAlongs/WRIT20833_Lists_Loops_Conditionals_2026.ipynb"),
        ("Dictionaries & Functions", "Key–value data and reusable tools.", "Day 5", "notebooks/codeAlongs/WRIT20833_Dictionaries_Functions_2026.ipynb"),
    ]),
    ("Weeks 3–4", "From text to data", [
        ("Term Frequency", "Counting words to hear what a text is about.", "Day 7", "notebooks/codeAlongs/WRIT20833_Term_Frequency_2026.ipynb"),
        ("Found Data & Pandas", "Collection ethics, then DataFrames.", "Day 10", "notebooks/codeAlongs/WRIT20833_Pandas_01_Found_Data_2026.ipynb"),
        ("Data Cleaning", "Turning messy scraped data tidy.", "Day 11", "notebooks/codeAlongs/WRIT20833_Pandas_02_Cleaning_2026.ipynb"),
        ("YouTube Comment Collector", "Collect comments from a video you choose.", "Days 10–12", "notebooks/codeAlongs/WRIT20833_YouTube_Comment_Collector_2026.ipynb"),
    ]),
    ("Weeks 5–6", "Computational text analysis", [
        ("Sentiment with VADER", "Scoring emotional tone — and judging it.", "Days 13–14", "notebooks/codeAlongs/WRIT20833_VADER_Sentiment_2026.ipynb"),
        ("Topic Modeling (Gensim)", "Discovering themes across a corpus.", "Days 16–17", "notebooks/codeAlongs/WRIT20833_Topic_Modeling_Gensim_2026.ipynb"),
    ]),
]

# --- homework ---
HOMEWORK = [
    ("HW1 · Foundations", "Python basics on real text.", "due Day 7", "notebooks/homework/WRIT20833_HW1_2026.ipynb"),
    ("HW2 · Term Frequency", "“Whose words win?” — comments vs. the Constitution.", "due Day 10", "notebooks/homework/WRIT20833_HW2_2026.ipynb"),
    ("HW3 · Sentiment", "Tone, stance, and what counting missed.", "due Day 16", "notebooks/homework/WRIT20833_HW3_2026.ipynb"),
    ("HW4 · Topic Modeling + Integration", "Themes, then all three lenses together.", "due Day 19", "notebooks/homework/WRIT20833_HW4_2026.ipynb"),
]

# --- mini-lectures (the ~25-min conceptual frames) — not yet built as pages ---
# ML0-7 map cleanly to 2026; ML2 cut (folded into ML6 + ML0); ML9 "Going Public" homed at Day 19;
# ML8 "Code as Rhetoric" harvested into ML1 + ML9 (no deck); ML10-12 (web) cut.
# (title, desc, when, page, thumb) — page is a docs-relative URL when the lecture has an authored
# reading page (None keeps it a "soon" placeholder card); thumb is the title-image path under the repo
# (None → a proportion-matched placeholder box, to be filled when that lecture's art is generated).
LECTURES = [
    ("Humanities & Coding", "Why a humanist learns to code.", "Day 1", "lectures/ml0.html", "materials/lectures/images/humanities_coding_script_to_structure.jpg"),
    ("Connotations & Code", "Code is not neutral.", "Day 1", "lectures/ml1.html", "materials/lectures/images/ml1_title.jpg"),
    ("Classification Logic", "Whose categories? Sorting as judgment.", "Day 3", "lectures/ml3.html", "materials/lectures/images/ml3_title.jpg"),
    ("Collective Memory", "What a culture keeps and forgets.", "Day 4", "lectures/ml5.html", "materials/lectures/images/ml5_title.jpg"),
    ("AI Agency", "Reading & judging machine-written code.", "Day 8", "lectures/ml4.html", "materials/lectures/images/ml4_title.jpg"),
    ("Data Archaeology", "Where found data comes from.", "Day 10", "lectures/ml6.html", "materials/lectures/images/ml6_title.jpg"),
    ("NLP & Topic Modeling", "Teaching machines to read culture.", "Day 16", "lectures/ml7.html", "materials/lectures/images/ml7_title.jpg"),
    ("Going Public", "Analysis → public argument.", "Day 19", "lectures/ml9.html", "materials/lectures/images/ml9_title.jpg"),
]

RESOURCES = [
    ("Tools", "Google Colab", "https://colab.research.google.com/", "runs every notebook — no install"),
    ("Tools", "Course GitHub repo", GH, "all notebooks, data, and docs"),
    ("Data", "Course corpus", f"{GH}/tree/main/notebooks/data", "93 YouTube comments (123 rows) · the U.S. Constitution"),
    ("Reference", "Python docs", "https://docs.python.org/3/", "the language reference"),
    ("Reference", "pandas", "https://pandas.pydata.org/docs/", "DataFrames & data wrangling"),
    ("Reference", "VADER sentiment", "https://github.com/cjhutto/vaderSentiment", "the sentiment lexicon we use"),
    ("Reference", "Gensim LDA", "https://radimrehurek.com/gensim/", "topic modeling"),
    ("Further reading", "Melanie Walsh, Cultural Analytics", "https://melaniewalsh.github.io/Intro-Cultural-Analytics/", "optional model & inspiration"),
]


def card(label, title, desc, when, href, soon=False, img=None, thumb=False, alt=None, opens=""):
    """alt=(label, href) adds a second link; the card is then a <div> whose title link stretches
    over the whole card (links can't nest), so clicking anywhere still opens `href`."""
    cls = "card soon" if soon else "card"
    when_html = f'<span class="when">{html.escape(when)}</span>' if when else ""
    if alt and href:
        cls += " linked"
        when_html += f'<a class="alt" href="{alt[1]}">{html.escape(alt[0])}</a>'
        title = f'<a class="stretch" href="{href}">{title}</a>'
    body = (f'<span class="lbl">{html.escape(label)}</span>'
            f'<h3>{title}</h3><p>{html.escape(desc)}</p>{when_html}')
    if thumb:
        # thumbnail card: real image if we have one, else a proportion-matched placeholder box
        cls += " has-thumb"
        thumb_html = (f'<span class="thumb"><img src="{img}" alt=""></span>' if img
                      else '<span class="thumb ph" aria-hidden="true"></span>')
        inner = f'{thumb_html}<span class="card-body">{body}</span>'
    else:
        inner = body
    if href and not alt:
        return f'<a class="{cls}" href="{href}"{opens}>{inner}</a>'
    return f'<div class="{cls}"{opens}>{inner}</div>'


def grid(cards):
    return '<div class="grid">' + "".join(cards) + "</div>"


def section(anchor, n, title, lede, body):
    return (f'<section class="sec" id="{anchor}">'
            f'<h2><span class="n">{n}</span>{html.escape(title)}</h2>'
            f'<p class="lede">{lede}</p>{body}</section>')


def render():
    masthead = (
        '<header class="masthead">'
        f'<figure class="mast-banner"><img src="{HERO}" alt="A warm painting of the humanities — a bust, '
        'a seated thinker, a portrait on an easel, a guitar, a theatre mask, and scattered manuscripts">'
        '</figure>'
        '<div class="kicker">WRIT 20833 · Fall 2026 · TCU</div>'
        '<h1>When Coding Meets Culture</h1>'
        '<p class="sub">Developing data-driven opinions — an eight-week introduction to coding in the '
        'humanities.</p>'
        '<p class="meta">Learn just enough Python to ask humanistic questions of real text — term '
        'frequency, sentiment, topic modeling — and to argue from what you find, while staying honest '
        'about what computation reveals and flattens. No prior coding experience needed. '
        'Everything launches from this page.</p>'
        '</header>'
    )

    start_cards = [
        card("Schedule", "Course Schedule", "Day-by-day: lecture, coding, and what's due.",
             "24 sessions", "schedule.html"),
        card("Syllabus", "Syllabus", "Outcomes, the ungrading policy, AI-use policy, and dates.",
             "Fall 2026", GH_BLOB + "SYLLABUS_2026.md"),
    ]
    if CHAT_API_URL:
        start_cards.append(card("Tutor", "Code Guide", "An after-hours tutor for your homework and capstone.",
                                "optional", "chatbot.html"))
    start = section(
        "start", "00", "Start here",
        "The documents that frame the course." if CHAT_API_URL else "The two documents that frame the course.",
        grid(start_cards))

    ca_body = "".join(
        '<div class="wkgroup"><h3><span class="wkn">' + html.escape(wk) + '</span>'
        + html.escape(theme) + '</h3>'
        + grid([card("Code-along", t, d, w, COLAB + p, opens=gate_attrs(p)) for (t, d, w, p) in items])
        + '</div>'
        for (wk, theme, items) in CODEALONGS_BY_WEEK)
    codealongs = section(
        "codealongs", "02", "Code-alongs",
        "Instructor-led notebooks we build together in class — one per coding day, grouped by week. "
        "Each opens in Colab on the morning of its class day.",
        ca_body)

    # Homework and the capstone share one section (the "Assignments" pill); the old #homework and
    # #capstone anchors survive on the two groups.
    homework = grid([card("Homework", t, d, w, COLAB + p, opens=gate_attrs(p)) for (t, d, w, p) in HOMEWORK])
    capstone = grid([
            card("Capstone", "Data-Driven Opinion", "Notebook analysis + short essay, presented Wed 12/16 or Fri 12/18.",
                 "Week 8", GH_BLOB + "CAPSTONE_2026.md"),
            card("Worksheet", "Checking the Machine", "A one-page routine for testing a result by hand: HW3, HW4, and the capstone.",
                 "Day 19 · Week 7", GH_BLOB + "materials/Checking_the_Machine.md"),
            card("Exercise", "Reading for the Seams", "Stylometry close-reading: hearing a human (or AI) voice.",
                 "Day 8 · Week 3", GH_BLOB + "materials/stylometry/Reading_for_the_Seams.md"),
            card("Notebook", "Stylometry (computational)", "The computational half of the stylometry exercise.",
                 "Day 18 · Week 6", COLAB + "materials/stylometry/WRIT20833_Stylometry_Reading_Seams_2026.ipynb",
                 opens=gate_attrs("materials/stylometry/WRIT20833_Stylometry_Reading_Seams_2026.ipynb")),
        ])
    assignments = section(
        "assignments", "03", "Assignments",
        "The four homework notebooks and the capstone, the course's final evaluative exercise. Turn in "
        "everything through <strong>TCU Online → Assignments</strong>.",
        '<div class="wkgroup" id="homework"><h3>Homework</h3>'
        '<p class="lede">Four notebooks where you apply the skills to a cultural dataset — ideally one you '
        'choose. Each opens on the day it is assigned. (Due dates are confirmed in the syllabus.)</p>'
        + homework + '</div>'
        '<div class="wkgroup" id="reflections"><h3>Self-reflections</h3>'
        + grid([card("Reflections", "Self-Reflections", "Three short reflections that build your case for your final grade.",
                     "R1 due Fri 10/23", "guides/reflections.html")]) + '</div>'
        '<div class="wkgroup" id="capstone"><h3>Capstone &amp; stylometry</h3>'
        '<p class="lede">The final evaluative exercise integrates all three methods on data you choose; '
        'the stylometry track is an alternative path.</p>'
        + capstone + '</div>')

    lectures = section(
        "lectures", "01", "Lectures",
        "The short conceptual frames that open each day — the “code is not neutral” throughline, "
        "from Humanities &amp; Coding on Day 1 to Going Public on Day 19. Each opens as a slide deck on the day it is taught; the full text is linked on every card.",
        grid([card("Mini-lecture", t, d, w, p and p.replace(".html", ".deck.html"), soon=(p is None),
                   img=(RAW + im if im else None), thumb=True, alt=p and ("Full text", p),
                   opens=day_gate_attrs(w) if p else "")
              for (t, d, w, p, im) in LECTURES]))

    res_items = "".join(
        f'<li><span class="k">{html.escape(k)}</span>'
        f'<a href="{href}">{html.escape(name)}</a> — <span class="muted">{html.escape(note)}</span></li>'
        for (k, name, href, note) in RESOURCES)
    res_cards = [
        card("Guide", "Working in Colab", "Set up, save your copy, come back to it, and submit homework.",
             "start here · Day 1", "guides/working-in-colab.html"),
        card("Guide", "YouTube API Key", "One-time setup for the YouTube Comment Collector.",
             "Day 10 · by Fri 11/13", "guides/youtube-api-key.html"),
    ]
    if CHAT_API_URL:
        res_cards.append(card("Tutor", "Code Guide", "An after-hours tutor for your homework and capstone.",
                              "optional", "chatbot.html"))
    res_cards.append(card("Policy", "Syllabus", "Outcomes, the ungrading policy, AI-use policy, and dates.",
                          "Fall 2026", GH_BLOB + "SYLLABUS_2026.md"))
    resources = (f'<section class="sec" id="resources"><h2><span class="n">04</span>Resources</h2>'
                 f'<p class="lede">How-to guides, the tutor, the syllabus, and tools and references for going further.</p>'
                 f'{grid(res_cards)}'
                 f'<div class="wkgroup"><h3>Tools &amp; references</h3>'
                 f'<ul class="reslist">{res_items}</ul></div></section>')

    main = masthead + start + lectures + codealongs + assignments + resources
    return PAGE("WRIT 20833 — When Coding Meets Culture", main,
                header=site_header(chat=bool(CHAT_API_URL)),
                footer=site_footer("WRIT 20833 · Fall 2026 · “hear the human at scale” · "
                                   "a working draft, adjusted to the class’s pace"))


if __name__ == "__main__":
    css = write_stylesheet(os.path.dirname(OUT) or ".")
    out = render()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes) + {css} ({os.path.getsize(css)} bytes)")
