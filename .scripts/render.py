"""Render a linkified markdown string to HTML using python-markdown."""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import quote

import markdown

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

MD_EXTENSIONS = ["tables", "fenced_code", "attr_list", "sane_lists"]

BULLET_RE = re.compile(r"^( {0,4})([*+\-]|\d+[.)]) ")

# GitHub source link for the "Edit on GitHub" footer widget. Forks should set
# GITHUB_REPO_URL to their own repo or to an empty string to suppress the link.
GITHUB_REPO_URL = "https://github.com/ChristopherA/DeepContext.com"
GITHUB_BRANCH = "main"


def normalize_list_indents(text: str) -> str:
    """Convert 2-space bullet-indent under a list item to 4-space (python-markdown nesting).

    The graph's convention puts annotation bullets directly below a predicate bullet
    at 2-space indent; python-markdown needs 4-space indent to nest lists. We promote
    only the 2-space case — anything already at 4+ is left untouched.
    """
    out: list[str] = []
    in_list = False

    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        m = BULLET_RE.match(stripped)
        if m:
            indent = len(m.group(1))
            if indent == 2 and in_list:
                out.append("    " + stripped[2:] + "\n")
            else:
                in_list = True
                out.append(line)
        else:
            # Continuation lines inside a list item: keep current in_list state.
            # A fully blank line ends the list.
            if stripped.strip() == "":
                in_list = False
            out.append(line)

    return "".join(out)


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    body = text[m.end():]
    raw = m.group(1)
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        if value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        meta[key] = value
    return meta, body


def render_html(
    markdown_body: str,
    *,
    title: str,
    taxonomy_name: str | None,
    taxonomy_url: str | None,
    source_rel_path: str | None = None,
    style_href: str = "/style.css",
    is_home: bool = False,
) -> str:
    normalized = normalize_list_indents(markdown_body)
    html_body = markdown.markdown(normalized, extensions=MD_EXTENSIONS)

    crumb = ""
    if not is_home:
        segments = ['<a href="/">DeepContext</a>']
        if taxonomy_name and taxonomy_url:
            segments.append(
                f'<a href="{html.escape(taxonomy_url)}">{html.escape(taxonomy_name)}</a>'
            )
        crumb = '<nav class="crumb">' + " / ".join(segments) + "</nav>"

    source_link = ""
    if source_rel_path and GITHUB_REPO_URL:
        encoded = quote(source_rel_path, safe="/")
        source_url = f"{GITHUB_REPO_URL}/blob/{GITHUB_BRANCH}/{encoded}"
        source_link = (
            f'<a class="source-link" href="{html.escape(source_url)}">'
            "Edit on GitHub</a>"
        )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{html.escape(style_href)}">
</head>
<body>
<header>{crumb}</header>
<main>
{html_body}
</main>
<footer><a href="/">DeepContext</a>{source_link}</footer>
</body>
</html>
"""


def render_file(
    source_path: Path,
    linkified_text: str,
    *,
    title: str,
    taxonomy_name: str | None,
    taxonomy_url: str | None,
    source_rel_path: str | None = None,
) -> str:
    _, body = strip_frontmatter(linkified_text)
    return render_html(
        body,
        title=title,
        taxonomy_name=taxonomy_name,
        taxonomy_url=taxonomy_url,
        source_rel_path=source_rel_path,
    )
