"""Rewrite wikilinks in source markdown.

Transforms (in-memory; callers write to .build/ via render.py):
    [[Target]]              -> [Target](/nodes/<tax>/<slug>/)           if resolved
    [[Target|Display]]      -> [Display](/nodes/<tax>/<slug>/)          if resolved
    [[Target]]              -> <span class="ghost-link">[[Target]]</span>
    [[Target]]\u2197          -> <span class="external-ref">[[Target]]\u2197</span>

Fenced code blocks and inline code spans are protected during the rewrite.
"""

from __future__ import annotations

import re
from pathlib import Path

# Match [[...]] optionally followed by an external arrow.
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\](\u2197?)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")


def linkify_text(text: str, slug_table: dict[str, dict]) -> str:
    placeholders: list[str] = []

    def _save_fence(m: re.Match[str]) -> str:
        placeholders.append(m.group(0))
        return f"\x00FENCE{len(placeholders) - 1}\x00"

    text = FENCE_RE.sub(_save_fence, text)
    text = INLINE_CODE_RE.sub(_save_fence, text)

    def _replace(m: re.Match[str]) -> str:
        raw_target = m.group(1)
        arrow = m.group(2) or ""

        if arrow:
            # External marker: preserve verbatim, styled via span.
            return f'<span class="external-ref">[[{raw_target}]]\u2197</span>'

        if "|" in raw_target:
            target, display = raw_target.split("|", 1)
        else:
            target, display = raw_target, None

        target_stripped = target.strip()
        entry = slug_table.get(target_stripped)

        if entry is None:
            # Unresolved: render as ghost link span.
            return f'<span class="ghost-link">[[{raw_target}]]</span>'

        link_text = (display if display is not None else target).strip()
        return f"[{link_text}]({entry['url']})"

    text = WIKILINK_RE.sub(_replace, text)

    for i, fence in enumerate(placeholders):
        text = text.replace(f"\x00FENCE{i}\x00", fence)

    return text


def linkify_file(path: Path, slug_table: dict[str, dict]) -> str:
    return linkify_text(path.read_text(encoding="utf-8"), slug_table)
