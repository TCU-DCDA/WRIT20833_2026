"""Render COURSE_SCHEDULE_2026.md into a polished, self-contained HTML view.

Single source of truth stays the markdown; this just produces a more readable
COURSE_SCHEDULE_2026.html (inline CSS, no external assets, opens in any browser).
Relative notebook links are preserved, so they resolve when the HTML sits at repo root.

Run from repo root:  python3 build_schedule_html.py
"""
import re, html, os

SRC = "COURSE_SCHEDULE_2026.md"
OUT = "COURSE_SCHEDULE_2026.html"

WEEK_COLORS = ["#2563eb", "#0d9488", "#7c3aed", "#db2777"]  # blue, teal, violet, pink
MODE_CLASS = {
    "Code-along": "m-codealong", "Lab": "m-lab", "Workshop": "m-workshop",
    "Work session": "m-worksession", "Presentations": "m-present",
}


def md_inline(t):
    """Minimal markdown inline -> HTML (escape, then links/bold/italic/code)."""
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
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
    # notes = trailing italic paragraphs
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
    return (f'<div class="day"><span class="num">{num}</span>'
            f'<span class="wd">{html.escape(wd)}</span>'
            f'<span class="dt">{html.escape(dt)}</span></div>')


def render_coding(cell):
    m = re.match(r'\*\*(.+?)\*\*\s*→\s*(.*)', cell)
    if not m:
        return md_inline(cell)
    mode, rest = m.group(1), m.group(2)
    cls = MODE_CLASS.get(mode, "m-other")
    return f'<span class="mode {cls}">{html.escape(mode)}</span> {md_inline(rest)}'


def render_due(cell):
    cell = cell.strip()
    if cell == "—" or cell == "":
        return '<span class="due-none">—</span>'
    chips = []
    for part in re.split(r'\s*·\s*', cell):
        part = part.strip()
        if not part:
            continue
        important = "**" in part
        cls = "chip chip-key" if important else "chip"
        chips.append(f'<span class="{cls}">{md_inline(part)}</span>')
    return " ".join(chips)


def render():
    title, subtitle, weeks, notes = parse()
    legend = "".join(
        f'<span class="mode {cls}">{name}</span>'
        for name, cls in MODE_CLASS.items()
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
            f'<section class="week" style="--wk:{color}">'
            f'<h2>{md_inline(w["head"])}</h2>'
            '<table><thead><tr>'
            '<th class="c-day">Day</th><th class="c-lec">Lecture</th>'
            '<th class="c-code">Coding</th><th class="c-due">Due</th>'
            '</tr></thead><tbody>' + "".join(rows) + "</tbody></table></section>"
        )
    notes_html = "".join(f"<p>{md_inline(n)}</p>" for n in notes)

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
:root {{ --ink:#1f2330; --muted:#6b7280; --line:#e6e8ee; --bg:#f4f5f8; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink);
  font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }}
.wrap {{ max-width:1080px; margin:32px auto; padding:0 18px; }}
header.top {{ background:#fff; border:1px solid var(--line); border-radius:14px;
  padding:24px 26px; box-shadow:0 1px 3px rgba(20,20,40,.05); }}
header.top h1 {{ margin:0 0 6px; font-size:26px; letter-spacing:-.01em; }}
.sub {{ font-weight:600; color:#374151; margin:0 0 14px; }}
.meta {{ color:var(--muted); font-size:14px; margin:0; }}
.legend {{ display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 2px; }}
.legend .lbl {{ color:var(--muted); font-size:13px; align-self:center; margin-right:4px; }}
.mode {{ display:inline-block; font-size:12px; font-weight:700; line-height:1;
  padding:5px 9px; border-radius:999px; color:#fff; white-space:nowrap; }}
.m-codealong {{ background:#2563eb; }} .m-lab {{ background:#7c3aed; }}
.m-workshop {{ background:#0d9488; }} .m-worksession {{ background:#d97706; }}
.m-present {{ background:#db2777; }} .m-other {{ background:#6b7280; }}
.week {{ background:#fff; border:1px solid var(--line); border-left:5px solid var(--wk);
  border-radius:14px; margin:20px 0; overflow:hidden; box-shadow:0 1px 3px rgba(20,20,40,.05); }}
.week h2 {{ margin:0; padding:14px 20px; font-size:17px; color:var(--wk);
  border-bottom:1px solid var(--line); background:color-mix(in srgb, var(--wk) 7%, #fff); }}
table {{ width:100%; border-collapse:collapse; }}
th, td {{ text-align:left; padding:11px 14px; vertical-align:top; border-top:1px solid var(--line); }}
thead th {{ border-top:none; font-size:12px; text-transform:uppercase; letter-spacing:.04em;
  color:var(--muted); font-weight:700; }}
tbody tr:nth-child(even) {{ background:#fafbfc; }}
.c-day {{ width:74px; }} .c-lec {{ width:26%; }} .c-due {{ width:24%; }}
.day {{ position:relative; padding-left:30px; min-height:34px; }}
.day .num {{ position:absolute; left:0; top:1px; width:22px; height:22px; border-radius:50%;
  background:var(--ink); color:#fff; font-size:12px; font-weight:700;
  display:flex; align-items:center; justify-content:center; }}
.day .wd {{ display:block; font-weight:700; font-size:13px; }}
.day .dt {{ display:block; color:var(--muted); font-size:13px; }}
.c-lec {{ color:#374151; font-size:14.5px; }}
.c-code {{ font-size:14.5px; }}
.c-code .mode {{ margin-right:4px; vertical-align:baseline; }}
a {{ color:#1d4ed8; text-decoration:none; }} a:hover {{ text-decoration:underline; }}
code {{ background:#eef0f4; padding:1px 5px; border-radius:5px; font-size:.9em; }}
.chip {{ display:inline-block; font-size:12px; padding:3px 8px; border-radius:7px;
  background:#eef1f6; color:#475569; margin:1px 0; }}
.chip-key {{ background:#fef3c7; color:#92400e; font-weight:600; }}
.chip-key strong {{ font-weight:700; }}
.due-none {{ color:#c2c7d0; }}
.notes {{ background:#fff; border:1px solid var(--line); border-radius:14px;
  padding:14px 22px; margin:22px 0; color:#4b5563; font-size:13.5px; }}
.notes p {{ margin:9px 0; }}
footer {{ color:var(--muted); font-size:12px; text-align:center; margin:24px 0 8px; }}
@media (max-width:720px) {{ .c-lec,.c-due {{ width:auto; }} body {{ font-size:15px; }} }}
@media print {{ body {{ background:#fff; }} .week,.notes,header.top {{ box-shadow:none; }} }}
</style></head>
<body><div class="wrap">
<header class="top">
<h1>{md_inline(title)}</h1>
<p class="sub">{md_inline(subtitle)}</p>
<p class="meta">Generated from <code>COURSE_SCHEDULE_2026.md</code> — see the syllabus for full
assignment descriptions, the ungrading policy, and the reflection / discussion prompts.</p>
<div class="legend"><span class="lbl">Coding modes:</span>{legend}</div>
</header>
{''.join(week_html)}
<div class="notes">{notes_html}</div>
<footer>WRIT 20833 · Summer 2026 · this is a working plan and may shift to the class's pace.</footer>
</div></body></html>
"""


if __name__ == "__main__":
    out = render()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote {OUT} ({len(out)} bytes, {os.path.getsize(OUT)} on disk)")
