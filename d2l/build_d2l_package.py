#!/usr/bin/env python3
"""
Build an IMS Common Cartridge 1.3 package for the WRIT 20833 (Fall 2026) TCU Online shell.

The cartridge is a THIN SHELL: modules of small landing pages that frame each item and hand
the student to the real thing -- a notebook in Colab, a lecture page on the course site, a
document on GitHub. No notebook or lecture prose is copied into D2L, so editing content stays
a git commit and the LMS cannot go stale.

Sources, all read rather than retyped:
  COURSE_SCHEDULE_2026.md  weeks, days, what is linked and due (via build_schedule_html.parse)
  build_index.py           the site's card titles, blurbs and lecture thumbnails
  SYLLABUS_2026.md         the four discussion prompts
  the notebooks            each notebook's own title

Submission folders are NOT here -- see build_assignments.py. Grade items, the grade scheme,
and discussion dates are hand-wired; see WIRING_CHECKLIST.md.

Usage, from anywhere:
    python3 d2l/build_d2l_package.py
    python3 d2l/build_d2l_package.py --modules 3,4

D2L imports are ADDITIVE -- re-importing a full package onto a live shell duplicates every
module. --modules builds a partial cartridge so a mid-term fix is: permanently delete that
module in D2L, build just that module, import. Selectors: start, 1-8, homework, discussions, all.
"""
import argparse
import os
import re
import shutil
import zipfile
from xml.sax.saxutils import escape

import d2l_common as c

OUT = os.path.join(c.REPO_ROOT, "d2l", "WRIT20833_Fall2026_D2L")

CC = "http://www.imsglobal.org/xsd/imsccv1p3/imscp_v1p1"
DT = "http://www.imsglobal.org/xsd/imsccv1p3/imsdt_v1p3"
LOMM = "http://ltsc.ieee.org/xsd/imsccv1p3/LOM/manifest"
LOMR = "http://ltsc.ieee.org/xsd/imsccv1p3/LOM/resource"
XSI = "http://www.w3.org/2001/XMLSchema-instance"


# ------------------------------------------------------------- cartridge

class Cartridge:
    def __init__(self, out_dir):
        self.out = out_dir
        self.resources = []      # (identifier, type, href)
        self.n = 0
        for sub in ("content", "discussions"):
            os.makedirs(os.path.join(out_dir, sub), exist_ok=True)

    def _id(self, prefix):
        self.n += 1
        return f"{prefix}_{self.n:04d}"

    def page(self, title, body_html):
        """An HTML topic held inside D2L."""
        ident = self._id("pg")
        rel = f"content/{ident}.html"
        doc = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
               f"<title>{escape(title)}</title>\n</head>\n<body>\n{body_html}\n</body>\n</html>\n")
        open(os.path.join(self.out, rel), "w", encoding="utf-8").write(doc)
        self.resources.append((ident, "webcontent", rel))
        return ident, title

    def discussion(self, title, body_html):
        """A CC discussion topic. Brightspace turns these into Discussions topics.

        UNVERIFIED on TCU's instance as of 2026-09-28 -- see WIRING_CHECKLIST.md §1.
        """
        ident = self._id("dt")
        rel = f"discussions/{ident}.xml"
        xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               f'<topic xmlns="{DT}" xmlns:xsi="{XSI}"\n'
               f'  xsi:schemaLocation="{DT} '
               'http://www.imsglobal.org/profile/cc/ccv1p3/ccv1p3_imsdt_v1p3.xsd">\n'
               f"  <title>{escape(title)}</title>\n"
               f'  <text texttype="text/html">{escape(body_html)}</text>\n'
               "</topic>\n")
        open(os.path.join(self.out, rel), "w", encoding="utf-8").write(xml)
        self.resources.append((ident, "imsdt_xmlv1p3", rel))
        return ident, title

    def write_manifest(self, course_title, modules):
        """modules: [(module_title, [(identifier, item_title), ...]), ...]"""
        L = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            f'<manifest identifier="WRIT20833-Fall2026" xmlns="{CC}"',
            f'  xmlns:lomimscc="{LOMM}" xmlns:lom="{LOMR}" xmlns:xsi="{XSI}"',
            f'  xsi:schemaLocation="{CC} '
            'http://www.imsglobal.org/profile/cc/ccv1p3/ccv1p3_imscp_v1p2_v1p0.xsd">',
            "  <metadata>",
            "    <schema>IMS Common Cartridge</schema>",
            "    <schemaversion>1.3.0</schemaversion>",
            "    <lomimscc:lom><lomimscc:general><lomimscc:title>",
            f"      <lomimscc:string>{escape(course_title)}</lomimscc:string>",
            "    </lomimscc:title></lomimscc:general></lomimscc:lom>",
            "  </metadata>",
            "  <organizations>",
            '    <organization identifier="org_1" structure="rooted-hierarchy">',
            '      <item identifier="root">',
        ]
        for m, (mod_title, items) in enumerate(modules, start=1):
            L.append(f'        <item identifier="mod_{m:02d}">')
            L.append(f"          <title>{escape(mod_title)}</title>")
            for i, (ident, title) in enumerate(items, start=1):
                L.append(f'          <item identifier="itm_{m:02d}_{i:03d}" identifierref="{ident}">')
                L.append(f"            <title>{escape(title)}</title>")
                L.append("          </item>")
            L.append("        </item>")
        L += ["      </item>", "    </organization>", "  </organizations>", "  <resources>"]
        for ident, rtype, href in self.resources:
            L.append(f'    <resource identifier="{ident}" type="{rtype}" href="{href}">')
            L.append(f'      <file href="{href}"/>')
            L.append("    </resource>")
        L += ["  </resources>", "</manifest>", ""]
        open(os.path.join(self.out, "imsmanifest.xml"), "w", encoding="utf-8").write("\n".join(L))


# ------------------------------------------------------------- items

BLURBS = c.blurbs()


def notebook_item(cart, rel, kind=None):
    """Landing page for a notebook: its own title, the site's blurb, an Open-in-Colab button."""
    title = c.notebook_title(rel)
    short, desc, _ = BLURBS.get(rel, (None, None, None))
    if kind is None:
        kind = "Homework notebook" if "/homework/" in rel else "Code-along notebook"
    if short and short.startswith("HW"):
        title = short.split(" · ")[0] + " · " + re.sub(r"^Homework \d+ — ", "", title)
    return cart.page(title, c.landing(
        kind, title, desc, [("Open in Colab", c.COLAB + rel)], note=c.NOTEBOOK_NOTE))


def lecture_item(cart, page):
    """Landing page for a mini-lecture: reading page plus its slide deck."""
    title, desc, img = BLURBS[page]
    deck = page.replace(".html", ".deck.html")
    return cart.page(title, c.landing(
        "Mini-lecture", title, desc,
        [("Read the lecture", f"{c.SITE}/{page}"), ("Slides", f"{c.SITE}/{deck}")], img=img))


def doc_item(cart, label, rel, desc=None, kind="Course document"):
    """Landing page for a markdown document rendered on GitHub."""
    return cart.page(label, c.landing(kind, label, desc, [("Open the document", c.GH_BLOB + rel)]))


def link_items(cart, day_cells, seen):
    """Items for every repo link in a day's coding and due cells, deduped within the week."""
    items = []
    for cell in day_cells:
        for label, href in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", cell):
            if href in seen:
                continue
            seen.add(href)
            if href.endswith(".ipynb"):
                items.append(notebook_item(cart, href))
            elif href == "CAPSTONE_2026.md":
                items.append(doc_item(cart, "Capstone assignment sheet", href,
                                      "The final evaluative exercise: your dataset, your "
                                      "question, and a short data-driven-opinion essay."))
            elif href.endswith(".md"):
                items.append(doc_item(cart, label, href, kind="Handout"))
            else:
                raise SystemExit(f"schedule links something the builder can't frame: {href}")
    return items


def lecture_pages_by_day():
    """Schedule day number -> [lecture page, ...], from build_index.LECTURES' 'Day N'."""
    out = {}
    for _, _, when, page, _ in c.index.LECTURES:
        if page:
            out.setdefault(int(when.split()[1]), []).append(page)
    return out


# ------------------------------------------------------------- pages

STYLE = (f'style="font-family:Arial,Helvetica,sans-serif;line-height:1.55;'
         f'max-width:44rem;color:{c.INK}"')
H = f'style="color:{c.GREEN}"'


def orientation_page():
    intro = f"""<h2 style="color:{c.GREEN};margin-top:0">How this course works</h2>
<p>The course lives in three places, and each does one job:</p>
<ul style="padding-left:1.1rem">
  <li><strong>The <a href="{c.SITE}/" target="_blank">course site</a></strong> &mdash;
      the schedule, the mini-lectures, and a card for every notebook.</li>
  <li><strong>Google Colab</strong> &mdash; where the code runs. Every notebook opens there;
      you need a Google account and nothing installed.</li>
  <li><strong>TCU Online</strong> (here) &mdash; the weekly modules, the four discussions,
      and the Assignments folders where you turn work in.</li>
</ul>
<p>Follow the weekly modules here and they will send you to the right place.</p>"""
    return f"""<div style="font-family:Arial,Helvetica,sans-serif;line-height:1.55;max-width:50rem;color:{c.INK}">
{c.two_col(c.index.HERO, intro, img_basis="260px", img_max="340px")}

<h3 {H}>Opening a notebook</h3>
<p>{c.NOTEBOOK_NOTE} To hand in a homework notebook, use <strong>File &rarr; Download
&rarr; Download .ipynb</strong> in Colab and upload that file to its folder under
Assignments.</p>

<h3 {H}>Ungrading</h3>
<p>This course uses ungrading. Your work is answered with feedback on your engagement,
reflection, and growth &mdash; not on whether your code was &ldquo;right.&rdquo; Errors are
part of the work here, not something to hide. Three times during the term you will write a
self-reflection, and in the last one you make the case for your own final grade.</p>

<p>Full policies are in the <a href="{c.GH_BLOB}SYLLABUS_2026.md" target="_blank">syllabus</a>.</p>
</div>"""


def week_page(head, days):
    rows = []
    for d in days:
        lec = "" if d["lecture"].startswith("—") else f'<br>Lecture: {c.md_html(d["lecture"])}'
        coding = c.md_html(d["coding"])
        due = "" if d["due"].strip() in ("", "—") else f'<br><em>Due / opens: {c.md_html(d["due"])}</em>'
        rows.append(f'<li style="margin-bottom:.9rem"><strong>Day {d["num"]} &mdash; {d["label"]}</strong>'
                    f'{lec}<br>{coding}{due}</li>')
    return f"""<div {STYLE}>
<h2 {H}>{c.md_html(head)}</h2>
<ul style="padding-left:1.1rem">
{chr(10).join(rows)}
</ul>
<p>Due items are due by the start of class that day unless noted.
<a href="{c.SITE}/schedule.html" target="_blank">Full course schedule</a></p>
</div>"""


def discussion_body(code, title, prompt, ev):
    opens, post, replies = ev[f"{code}_opens"], ev[f"{code}_post"], ev[f"{code}_replies"]
    return (f'<div {STYLE}>'
            f'<p style="font-size:17px"><strong>{c.esc(title)}</strong> {c.md_html(prompt)}</p>'
            f'<p><strong>Initial post</strong> by the start of class {post["label"]} &middot; '
            f'<strong>two substantive replies</strong> to classmates by the start of class '
            f'{replies["label"]}. (Opens {opens["label"]}.)</p>'
            f'</div>')


# ------------------------------------------------------------- build

def parse_selectors(raw, week_count):
    if not raw or raw.strip().lower() == "all":
        return None
    keys = set()
    for token in (t.strip().lower() for t in raw.split(",")):
        if token in ("start", "homework", "discussions"):
            keys.add(token)
        elif token.isdigit() and 1 <= int(token) <= week_count:
            keys.add(f"week{int(token)}")
        elif token:
            raise SystemExit(f"unrecognized selector {token!r} "
                             f"(use: start, 1-{week_count}, homework, discussions, all)")
    return keys


def build(out_dir, selectors=None):
    days = c.schedule_days()
    ev = c.events(days)
    heads = c.week_heads()
    cart = Cartridge(out_dir)
    modules = []
    wanted = lambda k: selectors is None or k in selectors

    if wanted("start"):
        modules.append(("Start Here", [
            cart.page("How this course works", orientation_page()),
            cart.page("Course site", c.landing(
                "Course site", "WRIT 20833 — When Coding Meets Culture",
                "The dashboard: every notebook, every mini-lecture, and the schedule.",
                [("Open the course site", f"{c.SITE}/")], img=c.index.HERO)),
            cart.page("Schedule", c.landing(
                "Course site", "Course schedule",
                "All 24 class days: the lecture, the coding block, and what is due.",
                [("Open the schedule", f"{c.SITE}/schedule.html")])),
            doc_item(cart, "Syllabus", "SYLLABUS_2026.md",
                     "Policies, the ungrading approach, and every assignment prompt."),
            doc_item(cart, "Capstone assignment sheet", "CAPSTONE_2026.md",
                     "The final evaluative exercise, due on the last day of class."),
        ]))

    lectures = lecture_pages_by_day()
    for w, head in enumerate(heads, start=1):
        if not wanted(f"week{w}"):
            continue
        wdays = [d for d in days if d["week"] == w]
        label = f"Week {w}"
        items = [cart.page(f"{label} overview", week_page(head, wdays))]
        seen = set()
        for d in wdays:
            for page in lectures.get(d["num"], []):
                items.append(lecture_item(cart, page))
            items += link_items(cart, [d["coding"], d["due"]], seen)
            # Homework notebooks enter the week they are assigned, where the schedule
            # names them but does not link them.
            for tok in d["tokens"]:
                m = re.match(r"^HW(\d) assigned$", tok)
                if m:
                    rel = f"notebooks/homework/WRIT20833_HW{m[1]}_2026.ipynb"
                    if rel not in seen:
                        seen.add(rel)
                        items.append(notebook_item(cart, rel))
        # "Week 6 (Nov 30 – Dec 4) — Topic modeling … (classes resume …)" -> "Week 6 · Topic modeling …";
        # the dates and asides stay on the overview page.
        topic = re.sub(r"^Week \d+ \([^)]*\) — ", "", c.plain(head))
        modules.append((f"{label} · " + re.sub(r"\s*\([^)]*\)$", "", topic), items))

    if wanted("homework"):
        hw = [notebook_item(cart, p) for _, _, _, p in c.index.HOMEWORK]
        hw.append(doc_item(cart, "Capstone assignment sheet", "CAPSTONE_2026.md",
                           "The final evaluative exercise, due on the last day of class."))
        hw.append(notebook_item(cart, "materials/stylometry/WRIT20833_Stylometry_Reading_Seams_2026.ipynb",
                                kind="Capstone option: stylometry"))
        modules.append(("Homework and Capstone", hw))

    if wanted("discussions"):
        topics = []
        for code, week, title, prompt in c.discussions():
            title = title.rstrip(".")
            if ev[f"{code}_opens"]["week"] != week:
                raise SystemExit(f"{code}: syllabus says Week {week}, schedule opens it in "
                                 f"Week {ev[f'{code}_opens']['week']}")
            topics.append(cart.discussion(f"{code} (Week {week}) · {title}",
                                          discussion_body(code, title, prompt, ev)))
        modules.append(("Discussions", topics))

    if not modules:
        raise SystemExit("selection matched no modules -- nothing to build")
    cart.write_manifest("WRIT 20833: When Coding Meets Culture (Fall 2026)", modules)
    return modules


def homepage_widget():
    """HTML for a D2L Custom Widget; a cartridge cannot set the course homepage."""
    links = [
        ("Course site", "/", "Every notebook and mini-lecture"),
        ("Schedule", "/schedule.html", "All 24 days, and what is due"),
        ("Syllabus", None, "Policies and assignment prompts"),
        ("Google Colab", "colab", "Where the code runs"),
    ]
    cards = []
    for title, path, blurb in links:
        url = (c.GH_BLOB + "SYLLABUS_2026.md" if path is None else
               "https://colab.research.google.com/" if path == "colab" else c.SITE + path)
        cards.append(
            f'<a href="{url}" target="_blank" rel="noopener" style="display:block;'
            f'text-decoration:none;border:1px solid {c.RULE};border-left:3px solid {c.GREEN};'
            f'border-radius:8px;padding:12px 14px;background:#ffffff">'
            f'<span style="display:block;color:{c.GREEN};font-weight:bold;font-size:16px;'
            f'margin-bottom:3px">{title} &rarr;</span>'
            f'<span style="display:block;color:{c.MUTED};font-size:13px">{blurb}</span></a>')
    head = (f'<h2 style="margin:0 0 6px;color:{c.GREEN};font-size:24px">When Coding Meets Culture</h2>'
            f'<p style="margin:0 0 14px;font-size:14px;color:{c.MUTED}">WRIT 20833 &middot; Fall 2026 '
            f'&middot; MWF 10:00&ndash;11:50 &middot; Schar Hall 2003</p>'
            f'<p style="margin:0;font-size:16px">Notebooks run in Google Colab and the lectures live '
            f'on the course site. Use the weekly modules here to find them, to post to the '
            f'discussions, and to turn work in under Assignments.</p>')
    return f"""<!-- Paste into a D2L Custom Widget: Course Admin -> Homepages -> Widgets ->
     Create Widget -> Content (source view). Then add the widget to the course homepage.
     Images load from the public GitHub repo. -->
<div style="font-family:Arial,Helvetica,sans-serif;color:{c.INK};line-height:1.55;
  max-width:56rem;margin:0 auto;padding:8px 32px 16px">
  {c.two_col(c.index.HERO, head, img_basis="260px", img_max="380px")}
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px">
    {"".join(cards)}</div>
  <p style="margin:20px 0 0;padding-top:14px;border-top:1px solid {c.RULE};font-size:14px;
    color:{c.MUTED}">New here? Start with <strong>Start Here &rarr; How this course
    works</strong>.</p>
</div>
"""


def zip_package(out_dir, zip_path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(out_dir):
            for name in sorted(files):
                full = os.path.join(root, name)
                z.write(full, os.path.relpath(full, out_dir))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("Usage")[0].strip())
    ap.add_argument("--modules", default="all",
                    help="comma-separated: start, 1-8, homework, discussions, all (default)")
    ap.add_argument("--out", default=OUT, help=f"output directory (default: {OUT})")
    a = ap.parse_args()

    selectors = parse_selectors(a.modules, len(c.week_heads()))
    if os.path.exists(a.out):
        shutil.rmtree(a.out)
    os.makedirs(a.out)
    mods = build(a.out, selectors)
    zip_package(a.out, a.out.rstrip("/") + ".imscc")
    open(a.out.rstrip("/") + "-homepage-widget.html", "w", encoding="utf-8").write(homepage_widget())

    scope = "full package" if selectors is None else f"partial: {a.modules}"
    print(f"wrote {a.out}.imscc -- modules: {len(mods)}, items: {sum(len(i) for _, i in mods)} ({scope})")
    for title, items in mods:
        print(f"  {title}: {len(items)}")
