---
created: 2026-04-19
tagline: A single markdown file resolving to a wikilink target — the default node shape the graph uses
brief_summary: An Atomic Node is a single markdown file whose filename matches a wikilink target. It is the default node shape and the one a reader should expect unless a node's concept has supporting material substantial enough to warrant its own sub-files. An Atomic Node contrasts with a Compound Node (a folder with a designated lead and supporting sub-files); both resolve to wikilink targets identically and both name exactly one concept — the Compound pattern is reserved for cases where supporting material warrants its own files. Choosing atomic over compound is a default; choosing compound over atomic is a deliberate move.
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Atomic Node

A single markdown file whose filename matches a wikilink target — `[[Atomic Node]]` resolves to `Atomic Node.md` (or `Atomic Node -- <definition>.md` for a Gloss). Atomic is the default node shape: a node is atomic unless a specific reason pushes it toward the compound pattern. A reader scanning the graph expects most nodes to be atomic files and only a handful to be folders with lead files.

The atomic shape keeps the filesystem layout and the graph layout aligned in the simplest possible way. One file is one node; the node's content lives inside the file; the file's name is the node's identifier. Wikilinks resolve by filename lookup with no folder traversal. Moving an atomic node is one file operation; renaming is one filename change.

The contrast is with a [[Compound Node -- a folder of markdown nodes with a designated lead|Compound Node]], which groups a concept's supporting material into a folder with a designated lead file. Compound is chosen when the concept has supporting material substantial enough to warrant its own sub-files — a meeting has an agenda and a transcript; a decision has ancillary records; a gloss has a longer exegesis. The compound still names one concept; the sub-files serve it. If a node has only grown long, the correct move is usually to split it into multiple atomic nodes (each naming its own concept) with `contrasts_with::` or `composed_of::` edges between them, not to reshape it as compound. Compound nodes earn their compound-ness by having genuine supporting material, not by having large bodies.

## Relations

- contrasts_with::[[Compound Node -- a folder of markdown nodes with a designated lead|Compound Node]]
  - An Atomic Node is a single file; a Compound Node is a folder with a lead file plus supporting material. Both resolve to wikilink targets identically and both name exactly one concept. The choice is driven by whether the concept has supporting material substantial enough to warrant its own sub-files, not by file size.

- grounded_in::[[Markdown Node Contract]]
  - Markdown Node Contract specifies the file-form requirements an Atomic Node satisfies directly — filename matching the wikilink target, identity predicate block above the H1, optional YAML, Relations section. The atomic shape is the contract's default case.
