"""Mirror the course corpora (notebooks/data/) onto the site as plain files, at docs/data/.

So each file has a direct GitHub Pages address, no page around it, e.g.
    https://tcu-dcda.github.io/WRIT20833_2026/data/ten_commandments/tc_youtube_comments.txt
notebooks/data/ stays the source of truth; docs/data/ is rebuilt from it (README.md files skipped).

    python3 build/build_data.py
"""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "notebooks", "data")
OUT = os.path.join(ROOT, "docs", "data")
SITE = "https://tcu-dcda.github.io/WRIT20833_2026/data/"

shutil.rmtree(OUT, ignore_errors=True)        # a file dropped from notebooks/data drops off the site
for folder, _, filenames in os.walk(SOURCE):
    for name in sorted(filenames):
        if name == "README.md" or name.startswith("."):
            continue
        relative = os.path.relpath(os.path.join(folder, name), SOURCE)
        os.makedirs(os.path.dirname(os.path.join(OUT, relative)), exist_ok=True)
        shutil.copyfile(os.path.join(SOURCE, relative), os.path.join(OUT, relative))
        print(SITE + relative.replace(os.sep, "/"))
