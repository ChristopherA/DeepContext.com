---
created: 2026-04-23
tagline: Image embeds use Obsidian's `![[path]]` wikilink-embed syntax; attachments live in an `Attachments/` folder co-located with the referring note; the render pipeline translates to site-root-relative `<img>`
brief_summary: Images in DeepContext nodes and the landing page are embedded using Obsidian's wikilink-embed syntax `![[Attachments/name.png]]`. Attachment files live in an `Attachments/` folder co-located with the referring note — at the repository root for root-level notes (`landing.md`), and as a sibling subdirectory for compound nodes (`nodes/<Tax>/<Folder>/Attachments/`). The render pipeline translates the embed into a standard markdown image reference with a site-root-relative URL (`![alt](/Attachments/name.png)`), which python-markdown emits as an `<img>` element; the build copies every `Attachments/` tree into the output so the URLs resolve at request time. Image extensions recognized: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`. Non-image embeds pass through unchanged, reserving `![[]]` for future transclusion features. The choice composes with Adopt Wikilinks and Named Edges at the embed layer and with Adopt Scion Publication Model at the build-artifact layer: a scion inherits working image rendering on first clone without local build steps.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-23
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Embed Images via Obsidian Wikilink Syntax

Nodes and the landing page embed images using Obsidian's wikilink-embed syntax `![[Attachments/name.png]]`. An optional pipe form `![[path|alt text]]` overrides the default alt text, which otherwise comes from the filename stem. Attachment files live in an `Attachments/` folder co-located with the note that references them: at the repository root for root-level notes (`landing.md`, future README-level embeds), and as a sibling subdirectory of a compound node's folder for images embedded by a compound node (`nodes/<Tax>/<Folder>/Attachments/`). The `.scripts/linkify.py` module translates `![[path]]` to standard markdown `![alt](/path)` before python-markdown runs, and python-markdown emits a standard `<img>` element. The build copies every `Attachments/` tree into the output directory so site-root-relative URLs resolve at request time. Recognized image extensions are `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`; non-image embeds pass through the pipeline unchanged, reserving `![[]]` as the future syntax for transclusion and other non-image embeds.

## Why

The choice composes three decisions that together let images participate in the graph without bespoke rendering or asset-management machinery: source-format editability in Obsidian, render-site standard-markdown compliance, and asset colocation with the referring note.

**Source-format editability.** Obsidian is the authoring environment many DeepContext contributors are familiar with, and its native image-embed syntax is `![[path]]`. Standard markdown's `![alt](path)` also renders in Obsidian but loses Obsidian-specific features — inline image preview in the edit pane, filename-based link completion, and the uniform treatment of embeds and wikilinks as one family. Authoring in the native syntax means a contributor who edits a node in Obsidian sees the image inline while editing, with no round-trip through the render pipeline. The project's prior commitment to Obsidian-compatible wikilink syntax for text links ([[Adopt Wikilinks and Named Edges]]) carries directly to image links; the two forms are the Obsidian convention's embed-and-link halves.

**Render-site standard-markdown compliance.** GitHub Pages' renderer in this project is python-markdown, which understands standard markdown `![alt](path)` but not Obsidian's `![[path]]`. Rather than rely on a python-markdown extension that might drift from Obsidian's exact behavior, `linkify.py` translates `![[path]]` to `![alt](/path)` before python-markdown sees the text. This keeps the rendered HTML plain and lets python-markdown's standard image handling carry through — alt-text escaping, URL encoding, output formatting all follow the library's well-tested path.

**Asset colocation with the referring note.** Attachments live in an `Attachments/` folder co-located with the note that embeds them. For root-level notes, attachments live at the repository root's `Attachments/`. For compound nodes, attachments are expected to live as a sibling subdirectory of the compound-node folder. At render time, paths are resolved as site-root-relative: `![[Attachments/name.png]]` becomes `/Attachments/name.png` in the rendered HTML, so the same embed syntax works identically whether the page is the landing page (`/`) or a nested node page (`/nodes/<tax>/<slug>/`). Colocation matches how Obsidian itself organizes attachments in its default configurations.

## Alternatives Considered

**Standard markdown image syntax only.** Require every image embed to use `![alt](path)` rather than `![[path]]`. Rejected because it loses Obsidian's native embed preview in the edit pane and burdens contributors with the same kind of manual HTML-or-markdown-thinking the wikilink convention already removes for links. Adopting one half of the Obsidian convention (wikilinks) while declining the other half (embeds) would leave contributors with two authoring models for structurally similar operations; the embed convention exists precisely because linking and embedding are variations on the same idea.

**Central assets directory at the repository root only.** Require every image to live in `/assets/` or `/images/` at the repository root regardless of which node references it. Rejected because it breaks co-location — a compound node's author-faced layout would have images in a distant directory rather than next to the note that references them, making Obsidian's file tree harder to reason about and decoupling image management from node authorship. The co-located convention matches how Obsidian itself organizes attachments and keeps a node's author-faced footprint (node + its images + its sub-files) in one folder.

**Inline base64-encoded images.** Embed image bytes directly in the markdown source as base64 data URIs. Rejected because it bloats markdown files dramatically (a 10MB image becomes a ~13MB base64 string embedded in source), breaks git diff usability, and defeats image caching at the browser layer. Markdown files stay text-only; image binaries stay in dedicated attachment files committed alongside.

**Emit bespoke HTML rather than translating to standard markdown image.** Have `linkify.py` produce `<img ... class="embed-image">` HTML directly, bypassing python-markdown's image handling. Rejected because it duplicates python-markdown's existing image pipeline (alt-text escaping, URL encoding, output formatting) with project-specific code that would drift. Translating to standard markdown and letting python-markdown produce the `<img>` keeps the rendering path narrow and consistent with how the pipeline handles other markdown constructs.

**Host images externally and reference via URL.** Store images on a CDN or external host and reference them via `![alt](https://example.com/image.png)`. Rejected because it introduces an external-service dependency that [[Adopt Scion Publication Model]]'s self-containment commitment specifically rejects. A scion cloned tomorrow should render images without contacting any service the template-owner controls; committing attachments alongside the content is what makes that property hold.

## What Would Change It

**A contributor's Obsidian configuration places attachments somewhere other than `Attachments/`.** Obsidian's "Default location for new attachments" setting can be configured per-vault; if a contributor's setting produces `./assets/`, `./Media/`, or similar, their embeds would reference a path the build does not copy. The revisit would either expand the copy-attachments step to walk multiple candidate folder names, ship a project-level `.obsidian/app.json` that enforces the `Attachments/` location, or require contributors to normalize on `Attachments/` via explicit onboarding documentation.

**A compound-node image embed surfaces the per-node Attachments gap.** The current build copies only the repository-root `Attachments/`. If a compound node embeds an image from its own sibling `Attachments/`, the build does not yet copy that folder. The first such embed forces the extension — a walk over `nodes/` looking for `Attachments/` siblings and copying each to the corresponding build-output location. The revisit would add that walk to `copy_attachments`.

**A renderer gains native `![[]]` embed support.** If python-markdown, a replacement renderer, or a sufficiently stable extension handles Obsidian-style embeds reliably, `linkify.py`'s embed-translation step becomes redundant. The revisit would remove the `EMBED_RE` pass and let the renderer handle the syntax directly; the convention stays, the translation layer drops.

**Image scale pushes the repository beyond a practical size.** Scions inherit the full repository including attachments. A single scion with a 100MB attachments directory is workable; scions with GB-scale media are not. The revisit would introduce git-LFS for large attachments, factor attachments into a separate repository the build references, or tighten file-size policies on what can be committed. The current landing header image alone is not a concern; accumulation across many nodes might be.

**Non-image embeds (transclusion, markdown includes) become load-bearing.** The current implementation reserves `![[]]` for image embeds by checking file extension; non-image embeds pass through unchanged. If transclusion of markdown fragments or of other media types becomes a project commitment, this Decision narrows to "image embeds use this syntax" and a new Decision specifies the transclusion story. The syntax is the same; the pipeline's per-case translation is what grows.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The upstream Decision that adopted Obsidian-compatible wikilink syntax for the graph's text edges. This Decision extends the same syntax choice to images: `![[path]]` is the embed counterpart of `[[target]]`. Adopting one implies adopting the other to the extent the project treats the Obsidian-family of conventions as a coherent authoring surface.

- grounded_in::[[Adopt Scion Publication Model]]
  - The scion commitment requires every scion to get working image rendering on first clone with no additional configuration. Committing the `Attachments/` directory alongside the content, and making the copy-attachments step part of the build, is what keeps the property holding. A scion cloning the template inherits working attachments and a working build.

- informs_downstream::[[Markdown Node Contract]]
  - The Contract carries a thin image-embed Requirement pointing at this Decision. The Contract states the rule (use `![[path]]` embed syntax; attachments live in `Attachments/`); this Decision records the reasoning and revisit conditions.

- informed_by::[[Render Bare Wikilinks with Visible Brackets]]
  - The sibling Decision at the text-wikilink layer. Both Decisions specify how a source-layer convention survives the render pass: bracket-preserving wikilinks for text, Obsidian-embed syntax for images. The embed Decision composes with the bracket Decision rather than repeating its reasoning; both live inside the same render-pipeline responsibility.
