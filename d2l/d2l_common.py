"""Shared pieces for the two TCU Online (D2L) generators in this directory.

Nothing here restates course content. Dates come from COURSE_SCHEDULE_2026.md (through
build_schedule_html.parse, the same parser the site uses); discussion and reflection prompts
come from SYLLABUS_2026.md; card blurbs and lecture thumbnails come from build_index.py. A
schedule or syllabus edit plus a rebuild keeps D2L in agreement with the site.

Adapted from WRIT 40363's d2l/ generators, with one deliberate difference: every local time
goes through zoneinfo. This term crosses the end of daylight saving (Sun Nov 1, 2026), so a
fixed UTC offset would put every deadline after that an hour early.
"""
import datetime
import html
import json
import os
import re
import sys
from zoneinfo import ZoneInfo

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The site generators use repo-relative paths, so import them from the repo root.
os.chdir(REPO_ROOT)
sys.path.insert(0, REPO_ROOT)
import build_schedule_html as sched  # noqa: E402
import build_index as index  # noqa: E402

SITE = "https://tcu-dcda.github.io/WRIT20833_2026"
COLAB = sched.COLAB
GH_BLOB = sched.GH_BLOB
RAW = index.RAW
YEAR = 2026
TZ = ZoneInfo("America/Chicago")
CLASS_START = (10, 0)   # syllabus: "due by the start of class that day unless noted"

# House palette, from site_theme.THEME_CSS ("Reading Room").
GREEN, INK, MUTED, RULE, SOFT, CLAY = (
    "#1e3b2f", "#262a20", "#696e5e", "#dcd8c9", "#eef2ec", "#8c6338")


# ------------------------------------------------------------------ schedule

def plain(md):
    """Markdown cell text -> plain text (links keep their label)."""
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    t = re.sub(r"[*`]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def schedule_days():
    """Every class day, in order: week, num, date, lecture, coding, due tokens."""
    _, _, weeks, _ = sched.parse()
    days = []
    for w, week in enumerate(weeks, start=1):
        for cells in week["rows"]:
            date_cell, lecture, coding, due = (cells + ["", "", "", ""])[:4]
            m = re.match(r"\*\*(\w{3}) (\d+)/(\d+)\*\*\s*\((\d+)\)", date_cell)
            if not m:
                raise SystemExit(f"unparseable schedule date cell: {date_cell!r}")
            wd, mo, dd, num = m.groups()
            days.append({
                "week": w, "week_head": week["head"], "num": int(num),
                "date": datetime.date(YEAR, int(mo), int(dd)),
                "label": f"{wd} {int(mo)}/{int(dd)}",
                "lecture": lecture, "coding": coding, "due": due,
                "tokens": [plain(t) for t in re.split(r"\s*·\s*", due) if plain(t) not in ("", "—")],
            })
    return days


def week_heads():
    _, _, weeks, _ = sched.parse()
    return [w["head"] for w in weeks]


def events(days=None):
    """Due-column tokens -> {key: day}. Keys: HW1_assigned, HW1_due, R1_due, D1_opens,
    D1_post, D1_replies, proposal_due, capstone_due."""
    ev = {}
    for d in days or schedule_days():
        for tok in d["tokens"]:
            for pat, key in [
                (r"^(HW\d) (assigned|due)$", lambda m: f"{m[1]}_{m[2]}"),
                (r"^(R\d) due\b", lambda m: f"{m[1]}_due"),
                (r"^(D\d) (opens|post|replies)$", lambda m: f"{m[1]}_{m[2]}"),
                (r"^Capstone proposal due$", lambda m: "proposal_due"),
                (r"^Capstone due$", lambda m: "capstone_due"),
            ]:
                m = re.match(pat, tok)
                if m:
                    key = key(m)
                    if key in ev:
                        raise SystemExit(f"schedule lists {key} twice")
                    ev[key] = d
    return ev


def utc(date, hour, minute, second=0):
    """Central local time -> the naive-UTC string Brightspace packages store."""
    local = datetime.datetime(date.year, date.month, date.day, hour, minute, second, tzinfo=TZ)
    return local.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")


def when(day, hour=CLASS_START[0], minute=CLASS_START[1]):
    """'Mon 11/2, 10:00 a.m.' for student-facing text."""
    t = datetime.time(hour, minute).strftime("%-I:%M %p").lower().replace("am", "a.m.").replace("pm", "p.m.")
    return f"{day['label']}, {t}"


# ------------------------------------------------------------------ syllabus

def _numbered_block(lead):
    """The numbered list that follows a bold lead-in line in SYLLABUS_2026.md."""
    lines = open("SYLLABUS_2026.md", encoding="utf-8").read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith(lead))
    items, cur = [], None
    for l in lines[start + 1:]:
        if re.match(r"^\d+\. ", l):
            cur = l.split(" ", 1)[1]
            items.append(cur)
        elif l.startswith("   ") and items:
            items[-1] += " " + l.strip()
        elif l.strip() == "" and items:
            break
    return items


def discussions():
    """[(code 'D1', week, title, prompt_md), ...] from the syllabus."""
    out = []
    for item in _numbered_block("**The four threaded discussions**"):
        m = re.match(r"\*\*(D\d) \(Wk (\d)\) — (.+?)\*\*\s*(.*)", item)
        if not m:
            raise SystemExit(f"unparseable discussion prompt: {item[:60]!r}")
        out.append((m[1], int(m[2]), m[3], m[4]))
    return out


def reflections():
    """[(n, title, syllabus_due_text, prompt_md), ...] from the syllabus."""
    out = []
    for item in _numbered_block("**The three self-reflections**"):
        m = re.match(r'\*\*Reflection (\d) — "(.+?)" \(due (.+?)\)\.\*\*\s*(.*)', item)
        if not m:
            raise SystemExit(f"unparseable reflection prompt: {item[:60]!r}")
        out.append((int(m[1]), m[2], m[3], m[4]))
    return out


def md_html(md):
    """Inline markdown -> HTML, links absolute and opening in a new tab."""
    return sched.md_inline(md).replace("<a href=", '<a target="_blank" rel="noopener" href=')


def capstone_section(heading):
    """Body of one '### ' section of CAPSTONE_2026.md, as simple HTML."""
    lines = open("CAPSTONE_2026.md", encoding="utf-8").read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith(f"### {heading}"))
    paras, bullets, out = [], [], []
    for l in lines[start + 1:]:
        if l.startswith("#") or l.startswith("---"):
            break
        if l.startswith("- "):
            bullets.append(l[2:])
        elif l.startswith("  ") and bullets:
            bullets[-1] += " " + l.strip()
        elif l.strip():
            if bullets:
                out.append("<ul>" + "".join(f"<li>{md_html(b)}</li>" for b in bullets) + "</ul>")
                bullets = []
            paras.append(l.strip())
        else:
            if paras:
                out.append(f"<p>{md_html(' '.join(paras))}</p>")
                paras = []
    if bullets:
        out.append("<ul>" + "".join(f"<li>{md_html(b)}</li>" for b in bullets) + "</ul>")
    if paras:
        out.append(f"<p>{md_html(' '.join(paras))}</p>")
    return "\n".join(out)


# ------------------------------------------------------------------ notebooks

def notebook_title(rel):
    """The notebook's own '# ' title, without the course-code prefix."""
    nb = json.load(open(rel, encoding="utf-8"))
    for c in nb["cells"]:
        if c["cell_type"] != "markdown":
            continue
        for line in "".join(c["source"]).splitlines():
            if line.startswith("# "):
                return re.sub(r"^WRIT 20833 — ", "", line[2:].strip())
    raise SystemExit(f"{rel}: no '# ' title in its markdown cells")


def blurbs():
    """repo path or site page -> (short title, one-line blurb, thumb URL or None), from build_index."""
    out = {}
    for _, _, items in index.CODEALONGS_BY_WEEK:
        for title, desc, _, path in items:
            out[path] = (title, desc, None)
    for title, desc, _, path in index.HOMEWORK:
        out[path] = (title, desc, None)
    for title, desc, _, page, thumb in index.LECTURES:
        out[page] = (title, desc, RAW + thumb if thumb else None)
    return out


# ---------------------------------------------------------------- landing HTML

def esc(s):
    return html.escape(s, quote=True)


def two_col(img, text_html, img_basis="220px", img_max="300px", gap="28px"):
    """Image beside text, wrapping to image-above-text on narrow screens.

    D2L strips <style> blocks, so there are no media queries: a wrapping flex row does
    the job. The image column is about a third of the width and the image is never
    cropped (the course's images are 16:9, 3:2, square and portrait).
    """
    return (f'<div style="display:flex;flex-wrap:wrap;gap:{gap};align-items:flex-start;'
            f'margin-bottom:22px">'
            f'<div style="flex:1 1 {img_basis};max-width:{img_max}">'
            f'<img src="{esc(img)}" alt="" style="display:block;width:100%;height:auto;'
            f'border-radius:12px;border:1px solid {RULE}"></div>'
            f'<div style="flex:2 1 300px;min-width:0">{text_html}</div></div>')


def landing(kind, title, desc=None, buttons=(), img=None, note=None, body_html=None):
    """A small page inside D2L that frames an item and hands the student onward.

    Inline styles only: D2L's editor strips <style> blocks. `buttons` is
    [(label, url), ...]; the first is primary, the rest are outlined. With an image,
    the head (kicker, title, blurb, buttons) sits beside it so it lands above the fold.
    """
    head = [f'<p style="margin:0 0 6px;font-size:13px;letter-spacing:.08em;'
            f'text-transform:uppercase;color:{MUTED}">{esc(kind)}</p>',
            f'<h2 style="margin:0 0 14px;color:{GREEN};font-size:26px;line-height:1.2">'
            f'{esc(title)}</h2>']
    if desc:
        head.append(f'<p style="margin:0 0 20px;font-size:16px">{esc(desc)}</p>')
    btn_html = ""
    if buttons:
        btns = []
        for i, (label, url) in enumerate(buttons):
            look = (f"background:{GREEN};color:#ffffff;border:2px solid {GREEN}" if i == 0
                    else f"background:#ffffff;color:{GREEN};border:2px solid {GREEN}")
            btns.append(f'<a href="{esc(url)}" target="_blank" rel="noopener" '
                        f'style="display:inline-block;{look};text-decoration:none;'
                        f'font-weight:bold;font-size:16px;padding:11px 22px;border-radius:8px;'
                        f'margin:0 10px 10px 0">{esc(label)} &rarr;</a>')
        btn_html = f'<p style="margin:0 0 12px">{"".join(btns)}</p>'

    rest = []
    if body_html:
        rest.append(f'<div style="margin:0 0 22px;font-size:16px">{body_html}</div>')
    if note:
        rest.append(f'<p style="margin:0 0 22px;background:{SOFT};border-left:4px solid {GREEN};'
                    f'border-radius:0 8px 8px 0;padding:12px 16px;font-size:15px">{note}</p>')

    p = [f'<div style="font-family:Arial,Helvetica,sans-serif;line-height:1.55;'
         f'color:{INK};max-width:{"50rem" if img else "44rem"}">']
    if img:
        # Buttons ride in the side column only when nothing sits between them and the head.
        side = "".join(head) + (btn_html if not rest else "")
        p.append(two_col(img, side))
        p += rest
        if rest:
            p.append(btn_html)
    else:
        p += head + rest + [btn_html]
    if buttons:
        p.append(f'<p style="margin:0;padding-top:14px;border-top:1px solid {RULE};'
                 f'font-size:14px;color:{MUTED}">Opens in a new tab, so this page stays here '
                 f'if you need to find your way back.</p>')
    p.append("</div>")
    return "\n".join(p)


NOTEBOOK_NOTE = ("Colab opens a read-only copy. Choose <strong>File &rarr; Save a copy in "
                 "Drive</strong> before you start typing, or your work will not be kept.")
