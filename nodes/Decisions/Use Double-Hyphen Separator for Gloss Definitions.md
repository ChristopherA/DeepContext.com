---
created: 2026-04-19
tagline: Gloss filenames follow Concept -- definition so the working definition is visible in the filesystem without opening the file
brief_summary: A commitment that Gloss nodes use the filename pattern `<Concept> -- <one-clause definition>.md` — concept, space, double hyphen, space, definition. The concept side matches the wikilink target; the definition side is a single clause, no trailing period, no internal `--`. The filename-carries-definition pattern is what makes a folder listing of Glosses readable as a first-level index of the graph's vocabulary — a reader scanning the folder reads the dictionary at a glance without opening any file.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Use Double-Hyphen Separator for Gloss Definitions

Every Gloss node's filename follows the pattern `<Concept> -- <one-clause definition>.md`. The separator is space-hyphen-hyphen-space (` -- `). The concept side matches the wikilink target other nodes use to reference the gloss; the definition side is a single clause, no trailing period, no internal `--`. The filename carries both the concept name and its working definition — opening the file produces elaboration, but the folder view produces a first-level index of the graph's vocabulary at zero reading cost.

## Why

The commitment makes the **definition visible in the filesystem without opening the file**. A contributor browsing the Glosses folder sees an alphabetized listing where each entry carries both the concept and its working definition. Scanning the folder produces a dictionary-like view — the reader reads the graph's vocabulary at a glance, without opening any file. The filesystem-as-index property is not incidental; it is the main reason Gloss filenames carry definitions at all. Without it, a reader seeking a concept would have to open each candidate file; with it, the folder view itself is the disambiguation tool.

The pattern supports contributors reading unfamiliar vocabulary. A Gloss's job is to let a reader on first encounter understand a term well enough to keep reading the citing node. If the term's Gloss requires opening the Gloss file, the reading-flow interruption costs attention; if the term's Gloss carries its definition in the filename, a quick scan of the Glosses folder (or a quick pass over a tooltip preview that shows the filename) delivers the definition inline with the citing context. The cost of reading an unfamiliar term drops from "open another file" to "read the next two words."

The separator is specifically ` -- ` (double hyphen with spaces) rather than a single hyphen, a colon, or any other punctuation. The double-hyphen comes from [[Use ASCII Dashes in Filenames]] as the canonical visual-dash substitute; the spaces around it prevent collision with hyphenated words in the concept or definition. The colon alternative fails on Windows filesystems; em-dash and en-dash alternatives fail the filename-portability commitment. The commitment's specific `--` choice inherits from the filename-portability commitment and applies it to the Gloss form's specific need for a visual separator.

The concept side matches the wikilink target other nodes use. When a citing node references the gloss, it uses pipe form (`[[Ghost Link -- a wikilink to a target that does not yet exist|Ghost Link]]` per [[Use Pipe Wikilinks for Display-Target Divergence]]) to render the concept name while targeting the full filename. The ordering — concept first, then definition — is what makes pipe form work; putting the definition first would require every citing node to know the definition to write the citation. Concept-first keeps citation light and preserves the filesystem-as-index property.

## Alternatives Considered

**Body-only definitions with filename as bare concept.** Name Gloss files with just the concept (`Ghost Link.md`) and put the definition in the body. Rejected because it loses the filesystem-as-index property entirely. A reader browsing the Glosses folder sees only concept names — no definitions — and must open each candidate file to disambiguate. The folder view becomes a list of terms rather than a dictionary; the reader's "scan and understand" path becomes "scan, open, read, close, next."

**Colon or pipe separator.** Use `<Concept>: <definition>` or `<Concept> | <definition>`. Rejected because both collide with filesystem and tooling constraints. Colons are invalid in filenames on Windows (NTFS reserves them for alternate data streams); pipes are valid but render awkwardly in shells and some wiki tools. The double-hyphen separator inherits portability from the filename-dash commitment with no new conflicts.

**Separate metadata in YAML rather than filename.** Keep the filename bare and carry the working definition in YAML frontmatter (`definition: "..."`). Rejected because it disconnects the definition from the folder view entirely. A reader scanning the filesystem sees only filenames; the definition lives in each file's frontmatter, which is not visible without opening the file. The commitment's whole purpose is the folder-view dictionary property; YAML-encoded definitions defeat it.

## What Would Change It

The commitment would be revisited under one condition.

**Tooling makes filesystem-level discoverability less important.** If wiki tools or graph browsers presented Gloss definitions inline with concept references — tooltip previews, hover cards, inline gloss rendering — at such quality and universality that folder-level browsing stopped being a primary reading path, the filename's definition-carrying benefit would weaken. Current tooling is uneven on this axis: Obsidian offers hover previews but not in all surfaces; GitHub's markdown renderer shows filenames; the shell and file browsers show filenames. Universal inline rendering would shift the reader's encounter-path away from the folder view. The revisit condition is latent — an acknowledged "if tooling changes substantially" clause, not pressure to act on now.

## Relations

- grounded_in::[[Use ASCII Dashes in Filenames]]
  - The filename-dash commitment provides the `--` separator this pattern uses. The Gloss-specific rule is a specific application of the general rule — the double hyphen is the portable-dash substitute, and the Gloss form's `<Concept> -- <definition>` pattern is the specific filename shape that substitutes into.

- grounded_in::[[Use Pipe Wikilinks for Display-Target Divergence]]
  - The pipe-wikilink Decision is what makes `<Concept> -- <definition>` filenames usable in prose. Without pipe form, every citation of a gloss would have to display the full filename; with pipe form, citations display the concept name while targeting the full filename.

- informs_downstream::[[Gloss Form Contract]]
  - Gloss Form Contract's filename pattern Requirement carries the thin enforcement clause pointing at this Decision.
