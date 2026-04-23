---
created: 2026-04-21
tagline: Bare wikilinks render with `[[brackets]]` preserved; pipe wikilinks drop them
brief_summary: A rendering decision for the DeepContext.com pipeline. A bare `[[Target]]` becomes an HTML anchor whose visible text is `[[Target]]` with the brackets preserved, so readers see the source convention on the rendered page. A piped `[[Target|Display]]` becomes an anchor whose visible text is `Display` with brackets dropped, so the alias reads naturally in prose. Ghost and external markers already keep their brackets via the span styling that distinguishes them. The convention is provisional -- revisit if readers find the brackets noisy, if screen-reader rendering suffers, or if the source pattern's visibility no longer serves newcomers.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-21
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Render Bare Wikilinks with Visible Brackets

A bare `[[Target]]` in source renders on the site as a working anchor whose visible text is `[[Target]]` -- brackets preserved. A piped `[[Target|Display]]` renders as `Display` with brackets dropped. The choice splits by wikilink form: bare wikilinks keep the source pattern legible to readers; piped wikilinks let the author's alias read naturally in prose without typographic noise.

Ghost links and external markers already keep their brackets through distinct styling (`.ghost-link` and `.external-ref` spans), so the visible-brackets discipline for bare wikilinks is consistent with how unresolved and cross-graph references have always rendered. The new rule aligns resolved bare wikilinks with the same visible-brackets treatment.

## Why

The decision serves a specific commitment this graph holds: the source pattern should be legible on the rendered surface. A newcomer encountering the site should be able to see, without reading documentation, that `[[Compound Node]]` is a wikilink that could be authored the same way anywhere else in the corpus. Stripping the brackets at render time hides the author-declared structure behind an ordinary-looking hyperlink, and the convention becomes something a reader has to be told about rather than something they can infer from the page.

Preserving brackets also distinguishes wikilinks from plain external hyperlinks visually, so a reader scanning a paragraph can tell at a glance which links stay inside the graph and which leave it -- without relying on color, hover-behavior, or URL-bar inspection. This is a small legibility gain per link, but the graph already carries many links per node, so the gain compounds.

The split by form -- bare keeps brackets, pipe drops them -- respects the different jobs the two forms do. A bare wikilink typically cites a concept name directly (e.g., `[[Atomic Node]]` as a reference to the Gloss). Brackets make the reference structure visible. A piped wikilink specifically exists to let an author use an alias when the filename stem is too long or formal for the prose context (`[[Compound Node -- a folder of markdown nodes with a designated lead|Compound Node]]`). The whole point of the pipe is to let the display text read as prose, which brackets would undercut.

## Alternatives Considered

**Strip all brackets, render as standard links.** This is the conventional wiki behavior -- wikilinks become ordinary anchors. Rejected because it hides the graph's structural layer from readers. A page full of `<a href="...">Target</a>` is visually indistinguishable from a page of ordinary web links; the wikilink discipline becomes invisible on the rendered surface.

**Render brackets via CSS `::before` and `::after` pseudo-elements.** Emit the anchor text without brackets and inject them in the stylesheet. Rejected because the content then lives only in the CSS, not the HTML. Screen readers and stylesheet-disabled readers lose the bracket content; copy-paste strips the brackets; and the layer that makes the source pattern visible becomes fragile to styling changes.

**Preserve brackets on both bare and piped wikilinks.** Uniform rule, no form-splitting. Rejected because the pipe form's whole purpose is to let the display text read as prose; brackets around an alias like `[[atomic]]` would re-introduce the very noise the pipe was adopted to remove.

**Preserve brackets only on specific-context wikilinks (e.g., inside named edges).** Keep brackets in `predicate::[[Target]]` but strip elsewhere. Rejected as a half-measure -- the legibility argument for brackets applies to inline references in body prose too, not only to structured named-edge bullets.

## What Would Change It

The decision is provisional and tied to tested assumptions about reader response that the project has not yet tested at real-reader scale.

**Brackets become noisy at information density.** If body prose accumulates enough wikilinks per paragraph that the brackets obscure reading rather than aiding it, the split could shift -- for instance, stripping brackets from bare wikilinks inside prose but preserving them in structured contexts (Relations sections, identity blocks). The visible-scaffolding goal would survive in the structured contexts where pattern recognition matters most.

**Accessibility feedback shifts the tradeoff.** If screen-reader users report that "open bracket open bracket Target close bracket close bracket" is disruptive, CSS-based rendering becomes more attractive despite its fragility trade-offs, or an ARIA-label approach could mask the brackets for assistive tech while keeping them visually.

**The corpus grows large enough that the visibility argument stops mattering.** If readers arrive already knowing the convention -- which would happen if the practice spreads and the wikilink pattern becomes widely recognized -- the bracket-as-affordance argument weakens. Pages full of ordinary links would be fine for a reader who knows what to expect.

**A competing legibility mechanism emerges.** If a different visual treatment (distinct color, icon, tooltip convention) carries the same "this is a wikilink inside the graph" signal more readably than brackets, the visible-brackets rule loses its load-bearing reason.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The substrate Decision the wikilink-and-named-edge convention sits on. This rendering rule is a downstream implementation choice: given that the source carries `[[brackets]]`, what visible form should the rendered page present? The substrate Decision does not specify the rendering; this Decision does, and either rendering would leave the substrate Decision intact. The dependency runs one direction -- changing how pages render wouldn't invalidate the source convention, but changing the source convention (e.g., away from `[[brackets]]`) would obviate this Decision.

- informs_downstream::[[Markdown Node Contract]]
  - Markdown Node Contract specifies the source form (`[[Target]]`, `[[Target|Display]]`, `[[Target]]↗`); this Decision specifies one rendering of that source form. A different rendering pipeline could implement the Contract differently, but the Contract does not prescribe a single rendering.

- informs_downstream::[[Embed Images via Obsidian Wikilink Syntax]]
  - The sibling Decision at the image-embed layer. Both Decisions specify how a source-layer convention survives the render pass: bracket-preserving wikilinks for text, Obsidian-embed syntax translated to standard markdown images for embeds. Both live inside the same render-pipeline responsibility; the embed Decision composes with this one rather than repeating its reasoning.
