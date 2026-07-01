"""Render COURSE_SCHEDULE_2026.md into a polished, self-contained HTML view.

Uses the shared course design system in `site_theme.py` (the "Reading Room" theme) so the schedule
matches the rest of the course site. The markdown stays the single source of truth; this only
produces a more readable COURSE_SCHEDULE_2026.html. Relative notebook links are preserved, so they
resolve when the HTML sits at repo root.

Run from repo root:  python3 build_schedule_html.py
"""
import re, html, os
from site_theme import PAGE, sidebar, shell, write_stylesheet

SRC = "COURSE_SCHEDULE_2026.md"
OUT = "docs/schedule.html"

# the published site lives in docs/, so repo-relative links must go absolute
REPO = "TCU-DCDA/WRIT20833_2026"
COLAB = f"https://colab.research.google.com/github/{REPO}/blob/main/"
GH_BLOB = f"https://github.com/{REPO}/blob/main/"


def _abs(href):
    """Rewrite a repo-relative link to an absolute one the published /docs site can reach."""
    if href.startswith(("http", "#", "schedule.html", "index.html")):
        return href
    if href.endswith(".ipynb"):
        return COLAB + href
    if href.startswith(("notebooks/", "materials/", "planning/", "reference/", "docs/")):
        return GH_BLOB + href
    if href.endswith(".md"):  # root-level docs (e.g. CAPSTONE_2026.md) aren't copied into /docs
        return GH_BLOB + href
    return href

# greens deepening across the term (8 instructional weeks; extends --wk1..4 in site_theme.py)
WEEK_COLORS = ["#3a6b54", "#356450", "#305d49", "#2b5643",
               "#26503e", "#214a39", "#1c4333", "#1e3b2f"]
MODE_CLASS = {
    "Code-along": "m-codealong", "Lab": "m-lab", "Workshop": "m-workshop",
    "Work session": "m-worksession", "Presentations": "m-present",
}


def md_inline(t):
    """Minimal markdown inline -> HTML (escape, then links/bold/italic/code)."""
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
               lambda m: f'<a href="{_abs(m.group(2))}">{m.group(1)}</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t


def parse():
    lines = open(SRC, encoding="utf-8").read().splitlines()
    title = lines[0].lstrip("# ").strip()
    subtitle = next((l.strip().strip("*") for l in lines if l.startswith("**Mon")), "")
    weeks, cur, notes_start = [], None, None
    for idx, l in enumerate(lines):
        if l.startswith("### Week"):
            cur = {"head": l[4:].strip(), "rows": []}
            weeks.append(cur); continue
        if l.startswith("|") and cur is not None:
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if cells[0] == "Date" or set("".join(cells)) <= set("-: "):
                continue
            cur["rows"].append(cells)
            continue
        if l.startswith("*Notes") and notes_start is None:
            notes_start = idx
    notes = []
    if notes_start is not None:
        para = []
        for l in lines[notes_start:]:
            if l.strip() == "":
                if para: notes.append(" ".join(para)); para = []
            else:
                para.append(l)
        if para: notes.append(" ".join(para))
    return title, subtitle, weeks, notes


def render_day(cell):
    m = re.match(r'\*\*(.+?)\*\*\s*\((\d+)\)', cell)
    if not m:
        return f'<div class="day">{md_inline(cell)}</div>'
    label, num = m.group(1), m.group(2)
    parts = label.split(" ", 1)
    wd = parts[0]
    dt = parts[1] if len(parts) > 1 else ""
    return (f'<div class="day">'
            f'<span class="wd">{html.escape(wd)}</span>'
            f'<span class="dt">{html.escape(dt)}</span>'
            f'<span class="num">day {num}</span></div>')


def render_coding(cell):
    m = re.match(r'\*\*(.+?)\*\*\s*→\s*(.*)', cell)
    if not m:
        return md_inline(cell)
    mode, rest = m.group(1), m.group(2)
    cls = MODE_CLASS.get(mode, "m-other")
    return f'<span class="mode {cls}">{html.escape(mode)}</span> {md_inline(rest)}'


def render_due(cell):
    cell = cell.strip()
    if cell in ("—", ""):
        return '<span class="due-none">—</span>'
    chips = []
    for part in re.split(r'\s*·\s*', cell):
        part = part.strip()
        if not part:
            continue
        cls = "chip chip-key" if "**" in part else "chip"
        chips.append(f'<span class="{cls}">{md_inline(part)}</span>')
    return " ".join(chips)


def render():
    title, subtitle, weeks, notes = parse()
    legend = "".join(
        f'<span class="mode {cls}">{name}</span>' for name, cls in MODE_CLASS.items()
    )
    week_html = []
    for i, w in enumerate(weeks):
        color = WEEK_COLORS[i % len(WEEK_COLORS)]
        rows = []
        for cells in w["rows"]:
            date, lecture, coding, due = (cells + ["", "", "", ""])[:4]
            rows.append(
                "<tr>"
                f'<td class="c-day">{render_day(date)}</td>'
                f'<td class="c-lec">{md_inline(lecture)}</td>'
                f'<td class="c-code">{render_coding(coding)}</td>'
                f'<td class="c-due">{render_due(due)}</td>'
                "</tr>"
            )
        week_html.append(
            f'<section class="week" id="week-{i+1}" style="--wk:{color}">'
            f'<h2>{md_inline(w["head"])}</h2>'
            '<table><thead><tr>'
            '<th class="c-day">Day</th><th class="c-lec">Lecture</th>'
            '<th class="c-code">Coding</th><th class="c-due">Due</th>'
            '</tr></thead><tbody>' + "".join(rows) + "</tbody></table></section>"
        )
    notes_html = "".join(f"<p>{md_inline(n)}</p>" for n in notes)

    nav_items = ([("index.html", "← Dashboard", None)]
                 + [(f"#week-{i+1}", f"Week {i+1}", f"0{i+1}") for i in range(len(weeks))]
                 + [(GH_BLOB + "SYLLABUS_2026.md", "Syllabus", None)])
    side = sidebar(
        "WRIT 20833 · Fall 2026", "Course Schedule",
        nav_items,
        [(f"https://github.com/{REPO}", "GitHub ↗"), ("https://colab.research.google.com/", "Colab ↗")],
    )

    main = (
        '<header class="masthead">'
        '<div class="kicker">WRIT 20833 · When Coding Meets Culture</div>'
        '<h1>Course Schedule</h1>'
        f'<p class="sub">{md_inline(subtitle)}</p>'
        '<p class="meta">Fall 2026 · a day-at-a-glance companion to the syllabus '
        '(full assignment descriptions, the ungrading policy, and the reflection / discussion prompts '
        'live there). Generated from <code>COURSE_SCHEDULE_2026.md</code>.</p>'
        f'<div class="legend"><span class="lbl">Coding modes</span>{legend}</div>'
        '</header>'
        + "".join(week_html)
        + f'<div class="notes">{notes_html}</div>'
        + '<footer>WRIT 20833 · Fall 2026 · a working plan, adjusted to the class’s pace</footer>'
    )
    return PAGE(html.escape(title), shell(side, main), wrap=False)


if __name__ == "__main__":
    css = write_stylesheet(os.path.dirname(OUT) or ".")
    out = render()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes) + {css} ({os.path.getsize(css)} bytes)")
