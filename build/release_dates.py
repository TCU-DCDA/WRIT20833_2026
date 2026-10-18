"""When does each notebook become clickable on the course site?

Single source of truth: COURSE_SCHEDULE_2026.md. A notebook is released on the first day the
schedule's table links it; a homework notebook is released on the day its row says
"**HWn assigned**" (or the first day it is linked, whichever is earlier). Notebooks the schedule
never dates (none at the moment) are never gated.

The gate itself is client-side: `build_index.py` and `build_schedule_html.py` stamp every notebook
link with ``data-opens="YYYY-MM-DD"`` and ``data-opens-label="Fri 10/23"``, and the small
``GATE_JS`` in `site_theme.PAGE` turns links whose date is still ahead into plain text (with
"opens Fri 10/23"). The site is static and only rebuilt on commits, so this is the one way the
links can open on the right morning without a daily rebuild.

Two honest limits: (1) the viewer's own clock decides, at local midnight; (2) the repo is public, so
anyone who looks on GitHub can still find every notebook. This paces what students see on the site;
it does not hide the files. ``?all=1`` on any site page shows everything (for the instructor).

    python3 release_dates.py        # prints the table
"""
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))  # repo root: paths below are repo-relative
import re
from datetime import date

SRC = "COURSE_SCHEDULE_2026.md"
_ROW_DATE = re.compile(r'^\|\s*\*\*([A-Z][a-z]{2}) (\d{1,2})/(\d{1,2})\*\*\s*\((\d+)\)')
_LINK = re.compile(r'\[[^\]]*\]\(([^)]+\.ipynb)\)')
_HW_ASSIGNED = re.compile(r'\*\*HW(\d)\s+assigned\*\*')
_HW_PATH = "notebooks/homework/WRIT20833_HW{n}_2026.ipynb"


def _year(lines):
    for l in lines[:6]:
        m = re.search(r'\b(20\d\d)\b', l)
        if m:
            return int(m.group(1))
    raise ValueError("release_dates: no year found in the schedule header")


def release_table(src=SRC):
    """{repo-relative notebook path: (date, 'Fri 10/23', day_number)} — earliest date wins."""
    lines = open(src, encoding="utf-8").read().splitlines()
    year = _year(lines)
    table = {}

    def note(path, d, label, day):
        cur = table.get(path)
        if cur is None or d < cur[0]:
            table[path] = (d, label, day)

    for l in lines:
        m = _ROW_DATE.match(l)
        if not m:
            continue
        wd, mo, dd, day = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
        d = date(year, mo, dd)
        label = f"{wd} {mo}/{dd}"
        for path in _LINK.findall(l):
            note(path, d, label, day)
        for n in _HW_ASSIGNED.findall(l):
            note(_HW_PATH.format(n=n), d, label, day)
    return table


_TABLE = None


def release(path):
    """(iso_date, label) for a repo-relative notebook path, or None if the schedule never dates it."""
    global _TABLE
    if _TABLE is None:
        _TABLE = release_table()
    hit = _TABLE.get(path)
    return (hit[0].isoformat(), hit[1]) if hit else None


def day_table(src=SRC):
    """{day_number: (date, 'Fri 10/23')} for every dated row of the schedule."""
    lines = open(src, encoding="utf-8").read().splitlines()
    year = _year(lines)
    out = {}
    for l in lines:
        m = _ROW_DATE.match(l)
        if m:
            wd, mo, dd, day = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))
            out.setdefault(day, (date(year, mo, dd), f"{wd} {mo}/{dd}"))
    return out


def day_gate_attrs(day):
    """data- attributes that open a link on schedule day `day` (an int, or a "Day 8" string)."""
    if isinstance(day, str):
        day = int(re.search(r'\d+', day).group(0))
    d, label = day_table()[day]
    return f' data-opens="{d.isoformat()}" data-opens-label="{label}"'


def gate_attrs(path):
    """The two data- attributes a notebook link carries (empty string if the path isn't gated)."""
    r = release(path)
    return f' data-opens="{r[0]}" data-opens-label="{r[1]}"' if r else ""


if __name__ == "__main__":
    for path, (d, label, day) in sorted(release_table().items(), key=lambda kv: kv[1][0]):
        print(f"{d}  day {day:2d}  {label:10s} {path}")
