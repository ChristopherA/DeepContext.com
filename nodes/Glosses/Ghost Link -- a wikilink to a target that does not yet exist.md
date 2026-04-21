---
created: 2026-04-19
tagline: A wikilink to a target that does not yet exist — a planning signal carried inside the graph itself
brief_summary: A Ghost Link is a wikilink whose target node has not yet been authored. It is written with the same `[[Multi Word Target]]` syntax as any other wikilink; what marks it as a ghost is that no file with that name exists in the graph. Ghost Links are a feature, not a defect — they let a contributor declare intent ("this concept deserves a node eventually") without requiring creation-first discipline. A curation pass later reads the accumulated ghost links as a backlog of candidate nodes, prioritized by how many other nodes already depend on each one. The convention distinguishes ghost links from broken links (where a target was renamed or removed) and from cross-wiki references (where `↗` signals the target lives in a different wiki).
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Ghost Link

A wikilink whose target does not yet exist as a file in the graph. Ghost Links are written with the ordinary `[[Multi Word Target]]` syntax and are indistinguishable in source from resolved wikilinks; what marks them as ghosts is the absence of a target file, not any special notation. A contributor writes a ghost link when they want to declare that a concept deserves a node without writing that node now — and the graph remembers the intent.

Ghost Links carry planning signal in two directions. A contributor scanning their own draft sees which concepts they have named but not yet elaborated — each ghost link is a reminder that the term is in use and wants a home. A curation pass across the whole graph aggregates ghost links into a backlog of candidate nodes, weighted by how many other nodes already reference each one: a term that appears as a ghost in five places has earned a seed, while a term that appears once may be a one-off the contributor no longer intends to elaborate. Ghost links turn the act of writing into an implicit vote for what deserves attention next, without any separate tracking mechanism.

The convention distinguishes Ghost Links from two adjacent constructions. A **broken link** points to a target that used to exist and was renamed or removed; the fix is to rename, repoint, or delete the link. A **cross-wiki reference** marked with `↗` points to a target that lives in a different wiki or an external tradition and is not expected to resolve locally; the `↗` is the signal that absence-of-file is intentional. A Ghost Link is neither — it is a pending intent inside this graph, waiting to be fulfilled.

## Relations

- has_component::[[Wikilink Syntax]]↗
  - A Ghost Link uses ordinary wikilink syntax; the only thing that makes it a ghost is the absence of a target file. Tools that detect and report ghost links do so by cross-referencing wikilinks against the filename index.

- contrasts_with::[[Broken Link]]
  - A broken link points to a target that was renamed or removed and needs a repair; a ghost link points to a target that was never written and signals intent. A curation pass distinguishes them by history — broken links have a prior resolution; ghost links do not. Ghost link pending local gloss.

- contrasts_with::[[Cross Wiki Reference]]
  - A cross-wiki reference marked with `↗` signals that the target deliberately lives in a different wiki or external tradition; a ghost link signals a target intended to live here but not yet written. The `↗` marker is the disambiguator. Ghost link pending local gloss.

- grounded_in::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The gist specifies ghost-links-as-planning-signal as one of the convention's intentional features.
