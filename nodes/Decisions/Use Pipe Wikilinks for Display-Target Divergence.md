---
created: 2026-04-19
tagline: Pipe wikilinks let authors choose link phrasing that fits the prose while the graph edge still resolves to the canonical target
brief_summary: The pipe form `[[Full Filename|Display Text]]` is the graph-participating mechanism for letting the author choose how a link reads inline. The target on the left names the resolved node; the display on the right is the phrasing the author wants the reader to see. The forcing case is the Gloss Form's ` -- <definition>` filename pattern — bare `[[Concept]]` produces a spurious ghost link because partial-filename resolution is not standard — but the broader use is author discretion over prose phrasing: a shorter surface form, a grammatical variant, an in-context synonym, any phrasing that reads more naturally than the canonical filename. Preferred over Obsidian's `aliases:` frontmatter, which is graph-non-participating by prior decision.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Use Pipe Wikilinks for Display-Target Divergence

Pipe form `[[Full Filename|Display Text]]` is the canonical way to write a wikilink when the author wants the link to read in prose differently from how the target file is named. The target on the left is the canonical filename the graph edge resolves to; the display on the right is the phrasing the reader sees. The edge stays graph-participating — typed-edge traversal uses the target, not the display — while prose reads the way the author wants it to read.

## Why

The primary rationale is **author phrasing flexibility**. A writer working in running prose wants each link to fit its sentence: a shorter surface form, a grammatical variant ("resolving" rather than "Display-Target Divergence"), an in-context synonym, or simply the concept name rather than the canonical filename. Pipe form lets the author choose that phrasing without abandoning graph participation — the edge still resolves to the canonical target; only the rendered text changes. The author is not forced to choose between prose that reads naturally and edges that resolve correctly; pipe form gives both.

The forcing case is the Gloss Form's ` -- <definition>` filename pattern. A gloss named `Ghost Link -- a wikilink to a target that does not yet exist.md` carries its concept name ("Ghost Link") on the left of the separator and its working definition on the right. Prose referring to the concept wants to write "Ghost Link," not the full filename — but a bare `[[Ghost Link]]` resolves only if a file named `Ghost Link.md` exists. In vanilla wiki tooling and Obsidian's default configuration, no partial-filename resolution happens; `[[Ghost Link]]` becomes a ghost link even though the gloss is sitting right next to it. Pipe form — `[[Ghost Link -- a wikilink to a target that does not yet exist|Ghost Link]]` — names the target explicitly while rendering the concept name the reader expects. This is the case where pipe form is not optional but required; the convention's broader use is author-discretionary.

The same mechanism applies wherever display and target diverge for any reason: a long commitment-phrased Decision filename that reads poorly in running prose, a node whose canonical filename includes disambiguation the inline context does not need, a reference to an existing node under a synonym that carries shorter grammar, or any other prose-fit choice. The Gloss case is the loudest because the ghost link is a visible failure; author-phrasing use is quieter but no less legitimate. The convention is one mechanism serving both.

## Alternatives Considered

**Obsidian `aliases:` frontmatter.** Rejected because aliases are graph-non-participating by prior decision in the Markdown Node Contract. An alias lets Obsidian's autocomplete offer "Ghost Link" when the user types the concept name, but writing `[[Ghost Link]]` in source still produces a ghost link unless Obsidian-specific alias resolution is active. Aliases break the plain-markdown-expressibility floor — the graph's meaning depends on Obsidian-resolved aliases rather than on filename-only resolution.

**Gloss stub files.** Rejected because they violate one-file-one-concept. Creating `Ghost Link.md` as a stub that redirects to `Ghost Link -- a wikilink to a target that does not yet exist.md` doubles the maintenance surface (two files per gloss), and the stub has no content of its own. The redirect mechanism itself requires tool support, violating the zero-tooling floor.

**Bare full filename in prose.** Rejected because it breaks prose readability. Writing "The `[[Ghost Link -- a wikilink to a target that does not yet exist]]` convention signals an intentional future node" is functionally correct but unreadable. Prose that strings the full gloss filename into running text makes bodies harder to scan and reveals implementation detail the reader does not need.

**Drop the filename-carries-definition gloss convention.** Rejected because the convention is load-bearing. A contributor browsing the gloss folder reads the dictionary at a glance; opening files or hovering for tooltips defeats the purpose. The filename-in-folder view as readable index is a first-class feature of the Gloss Form Contract, not an incidental property.

## What Would Change It

Three signals would prompt revisit.

**Author friction overwhelms the convention.** If contributors consistently forget the full filename and revert to bare wikilinks, ghost links accumulate and the decision has failed at the adoption layer. A lightweight author aid — a template snippet or a seed script that emits pipe-form references — could arrive as a refinement; if even that does not move the practice, the convention is not viable.

**Display/target drift becomes a maintenance problem.** The pipe form decouples what the reader sees from what the graph traverses. If glosses rename (definition refined) and pipe-form references do not update, display text continues reading correctly while the target breaks silently — the cheap-to-write form becomes the expensive-to-maintain form. A link-check hook would detect the first wave of drift; if drift keeps outpacing detection, the convention is not sustainable.

**A graph-participating alias mechanism emerges.** Standard wiki tooling could add first-class alias-as-target resolution (Obsidian's `aliases:` reaching into wikilink resolution, or a similar feature at the CommonMark level). A graph-participating alias would let `[[Ghost Link]]` resolve directly to the gloss file without pipe syntax. We would prefer the bare form if it became viable — pipe syntax is overhead the author pays to restore the intuition a bare wikilink ought to carry.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The wikilinks-and-named-edges convention commits the graph to plain-markdown expressibility and author-declared edges. Pipe form is the same convention's answer to display-target divergence: an author-declared target and an author-declared display, no tooling between them.

- informs::[[Markdown Node Contract]]
  - The Markdown Node Contract's wikilink syntax inherits this decision. The contract's description of how bare wikilinks resolve must note that gloss filenames (and any ` -- ` filename) do not resolve from the concept side alone; pipe form is the canonical way to reference such nodes from prose or named edges.

- informs::[[Gloss Form Contract]]
  - The Gloss Form Contract establishes the filename-carries-definition pattern. Pipe form is the mechanism that makes the pattern usable in prose: contributors reference the gloss by its concept name without the definition flooding the reader's view.
