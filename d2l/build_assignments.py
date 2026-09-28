#!/usr/bin/env python3
"""Generate a Brightspace-native import package holding every WRIT 20833 submission folder.

Format copied from a real export of WRIT 40363's Fall 2026 shell (imsmanifest.xml +
dropbox_d2l.xml; see that repo's d2l/build_p1_assignments.py). Common Cartridge cannot
express submission folders, which is why this is a second package.

Folders (9), in three categories:
  Homework          HW1-HW4             opens the day it is assigned, due at the start of class
  Self-Reflections  Reflection 1-3      due at the start of class
  Capstone          Proposal, Capstone  due at the start of class

Every date comes from COURSE_SCHEDULE_2026.md's Due column; reflection prompts come from
SYLLABUS_2026.md, the proposal prompt from CAPSTONE_2026.md. The build fails if the
syllabus's printed reflection dates disagree with the schedule.

Folders get a due date and NO end date: the syllabus's late-work policy is "talk to me," so a
late upload should land (flagged late), not bounce off a closed folder.

Local times go through zoneinfo, not a fixed offset: this term crosses the end of daylight
saving (Sun Nov 1, 2026).

Usage:
    python3 d2l/build_assignments.py

Writes d2l/WRIT20833_Fall2026_Assignments/ and .zip (gitignored build products). Import via
Course Admin > Import/Export/Copy Components, selecting only Assignments. Imports are
additive: importing twice makes two of every folder.
"""
import json
import xml.etree.ElementTree as ET
import os
import re
import zipfile
from xml.sax.saxutils import escape as x

import d2l_common as c

OUT_DIR = os.path.join(c.REPO_ROOT, "d2l", "WRIT20833_Fall2026_Assignments")
OUT_ZIP = OUT_DIR + ".zip"

# Attribute set copied from the exported 40363 folders. submission_type 0 = file upload,
# files_per_submission 0 = unlimited, folder_type 2 = individual.
FOLDER_ATTRS = ('submission_type="0" completion_type="0" allowable_file_type="0" '
                'folder_type="2" sort_order="{sort}" add_to_schedule="true" '
                'folder_is_retricted="false" files_per_submission="0" submissions="2" '
                'ai_human_origin="0" resource_code="{code}" is_hidden="false" '
                'is_anonymous="false"')

MANIFEST = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="WRIT20833_F26_DROP" xmlns:d2l_2p0="http://desire2learn.com/xsd/d2lcp_v2p0" xmlns:scorm_1p2="http://www.adlnet.org/xsd/adlcp_rootv1p2" xmlns:imsmd="http://www.imsglobal.org/xsd/imsmd_rootv1p2p1" xmlns="http://www.imsglobal.org/xsd/imscp_v1p1">
    <metadata>
        <imsmd:lom>
            <imsmd:general>
                <imsmd:title>
                    <imsmd:langstring xml:lang="en-us">WRIT 20833 Fall 2026 assignment folders</imsmd:langstring>
                </imsmd:title>
                <imsmd:language>en-us</imsmd:language>
            </imsmd:general>
        </imsmd:lom>
    </metadata>
    <resources>
        <resource identifier="res_dropbox" type="webcontent" d2l_2p0:material_type="d2ldropbox" d2l_2p0:link_target="" href="dropbox_d2l.xml" title="" />
    </resources>
</manifest>'''


class Ids:
    """Categories and folders share one id space in the exported XML."""
    def __init__(self):
        self.n = 0

    def next(self):
        self.n += 1
        return self.n


def folder(ids, sort, code, name, instructions_html, due_day, open_day=None):
    parts = [f'<folder name="{x(name)}" id="{ids.next()}" '
             + FOLDER_ATTRS.format(sort=sort, code=code) + '>',
             '<blti xmlns="asset_processors" />',
             f'<instructions text_type="text/html"><text>{x(instructions_html)}</text></instructions>']
    if open_day:
        parts.append(f'<availability_start><availability_date>{c.utc(open_day["date"], 0, 1)}'
                     f'</availability_date><availability_type>2</availability_type></availability_start>')
    parts.append(f'<date_due>{c.utc(due_day["date"], *c.CLASS_START)}</date_due>')
    parts.append('</folder>')
    return "".join(parts)


def due_line(day, extra=""):
    return (f'<p style="margin:0 0 10px"><strong>Due by the start of class, {c.when(day)}</strong> '
            f'(Day {day["num"]}).{extra} Late? Talk to me &mdash; the folder stays open.</p>')


def upload_name(rel):
    """The filename the notebook itself asks for ('Upload as: LASTNAME_HW1.ipynb')."""
    nb = json.load(open(rel, encoding="utf-8"))
    for cell in nb["cells"]:
        m = re.search(r"\*\*Upload as:\*\*\s*`([^`]+)`", "".join(cell["source"]))
        if m:
            return m[1]
    raise SystemExit(f"{rel}: no 'Upload as:' line")


def homework_folders(ids, ev):
    out = []
    for n, (short, desc, _, rel) in enumerate(c.index.HOMEWORK, start=1):
        code = short.split(" · ")[0]
        title = f"{code} · " + re.sub(r"^Homework \d+ — ", "", c.notebook_title(rel))
        body = (due_line(ev[f"{code}_due"])
                + '<p style="margin:0 0 6px"><strong>To turn it in:</strong></p><ol style="margin:0 0 10px">'
                  '<li>In Colab, <strong>File &rarr; Download &rarr; Download .ipynb</strong>.</li>'
                  f'<li>Name the file <code>{c.esc(upload_name(rel))}</code>, as the notebook asks.</li>'
                  '<li>Upload it here.</li></ol>'
                  '<p style="margin:0">Run every cell before you download. Where something still '
                  'breaks, leave a <code>#comment</code> about what you tried &mdash; errors are part '
                  'of the work here, not something to hide.</p>')
        html = c.landing("Homework", title, desc, [("Open in Colab", c.COLAB + rel)], body_html=body)
        out.append(folder(ids, n, f"writ20833-f26-{code.lower()}", title, html,
                          ev[f"{code}_due"], ev[f"{code}_assigned"]))
    return out


def reflection_folders(ids, ev):
    lead = next(l for l in open("SYLLABUS_2026.md", encoding="utf-8")
                if l.startswith("**The three self-reflections**"))
    length = re.search(r"\((≈[^,]+?) each", lead)[1]
    out = []
    for n, title, syl_due, prompt in c.reflections():
        day = ev[f"R{n}_due"]
        if syl_due != day["label"]:
            raise SystemExit(f"Reflection {n}: syllabus says due {syl_due}, "
                             f"schedule says {day['label']} -- fix one before building")
        name = f"Reflection {n} · {title}"
        body = (due_line(day)
                + f'<p style="margin:0 0 10px">{c.md_html(prompt)}</p>'
                + f'<p style="margin:0">About {c.esc(length)}. Upload your reflection here.</p>')
        html = c.landing("Self-reflection", name, None,
                         [("Open the syllabus", c.GH_BLOB + "SYLLABUS_2026.md#assignments")], body_html=body)
        out.append(folder(ids, n, f"writ20833-f26-r{n}", name, html, day))
    return out


def capstone_folders(ids, ev):
    sheet = c.GH_BLOB + "CAPSTONE_2026.md"
    prop_day, cap_day = ev["proposal_due"], ev["capstone_due"]
    proposal = c.landing(
        "Capstone", "Capstone proposal", None, [("Open the capstone sheet", sheet)],
        body_html=due_line(prop_day) + c.capstone_section("The proposal"))
    capstone = c.landing(
        "Capstone", "Capstone: notebook + essay",
        "The final evaluative exercise: a notebook analysis of your own cultural dataset (or a "
        "stylometry corpus) and a short data-driven-opinion essay.",
        [("Open the capstone sheet", sheet),
         ("Submit checklist", sheet + "#submit-checklist")],
        body_html=due_line(cap_day, " You present in class that day.")
        + '<p style="margin:0">Upload <strong>both</strong> files: the notebook '
          '(<strong>File &rarr; Download &rarr; Download .ipynb</strong> in Colab) and your essay. '
          'Go through the submit checklist first.</p>')
    return [folder(ids, 1, "writ20833-f26-proposal", "Capstone proposal", proposal, prop_day),
            folder(ids, 2, "writ20833-f26-capstone", "Capstone: notebook + essay", capstone, cap_day)]


def main():
    ev = c.events()
    ids = Ids()
    # Category ids are drawn before their folders', matching the exported order.
    cats = []
    for name, sort, make in [("Homework", 1, homework_folders),
                             ("Self-Reflections", 2, reflection_folders),
                             ("Capstone", 3, capstone_folders)]:
        cat_id = ids.next()
        body = "".join(make(ids, ev))
        cats.append(f'<category name="{x(name)}" sort_order="{sort}" id="{cat_id}">{body}</category>')
    dropbox = ('<dropbox xmlns:d2l_2p0="http://desire2learn.com/xsd/d2lcp_v2p0">'
               + "".join(cats) + '</dropbox>')

    os.makedirs(OUT_DIR, exist_ok=True)
    open(os.path.join(OUT_DIR, "imsmanifest.xml"), "w", encoding="utf-8").write(MANIFEST)
    open(os.path.join(OUT_DIR, "dropbox_d2l.xml"), "w", encoding="utf-8").write(dropbox)
    with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for name in ("imsmanifest.xml", "dropbox_d2l.xml"):
            z.write(os.path.join(OUT_DIR, name), name)

    folders = ET.fromstring(dropbox).iter("folder")
    rows = [(f.get("name"), f.findtext("availability_start/availability_date"), f.findtext("date_due"))
            for f in folders]
    print(f"wrote {OUT_ZIP} ({len(rows)} folders)")
    for name, opens, due in rows:
        print(f"  {name:<72} opens {opens or '—':<19}  due {due} UTC")

    # Discussion dates can't ride in a package; print them for hand-setting.
    print("\nDiscussion dates to set by hand (Central time):")
    for code, week, title, _ in c.discussions():
        print(f"  {code} {title.rstrip('.'):<38} opens {ev[code + '_opens']['label']:<10}"
              f"post by {c.when(ev[code + '_post'])}   replies by {c.when(ev[code + '_replies'])}")


if __name__ == "__main__":
    main()
