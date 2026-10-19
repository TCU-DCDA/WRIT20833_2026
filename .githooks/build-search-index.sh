#!/bin/sh
# Rebuilds the course site's search index (docs/pagefind/) from the pages in docs/.
# Run by hand after regenerating docs/, or let the pre-commit hook run it.
# Pinned so every machine writes the same index format. See build/build_search.py.
cd "$(git rev-parse --show-toplevel)" || exit 1
echo "[search] Rebuilding docs/pagefind/ ..."
# Pagefind does not delete index fragments that a content change makes
# obsolete, so build into an empty folder and swap it in only on success;
# a failed build leaves the old index in place.
tmp="$(mktemp -d)" || exit 1
if npx --yes pagefind@1.5.2 --site docs --output-path "$tmp/pagefind" --silent; then
  rm -rf docs/pagefind && mv "$tmp/pagefind" docs/pagefind
  rm -rf "$tmp"
  echo "[search] Done."
else
  rm -rf "$tmp"
  echo "[search] Pagefind failed; the old search index was left in place." >&2
  exit 1
fi
