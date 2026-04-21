---
created: 2026-04-20
tagline: The non-overlap arc in a Venn-style predicate adjacency — what this predicate holds that its neighbor does not
brief_summary: A Crescent is the portion of one predicate's conceptual territory that lies outside an adjacent predicate's territory — the non-overlapping arc in a Venn-style diagram of the two. The `## Crescent` section in a Predicate node carries this content for a specific near-neighbor: a dedicated H3 subsection per adjacent predicate naming what this predicate holds that the neighbor does not. The asymmetry is geometric — two overlapping circles produce two crescents, each its own shape — so the Crescent on Predicate A against Predicate B is authored independently from the Crescent on B against A. An undocumented crescent is a silent invitation to merge two adjacent predicates under later convergence pressure.
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Predicate Crescent

The distinction one predicate holds against an adjacent predicate — the non-overlapping arc when the two are pictured as overlapping circles in a Venn diagram. The term names both the geometric shape and the section in a Predicate node (`## Crescent`) whose job is to carry that distinction as prose. In short-form references elsewhere in the graph, the concept may appear as simply "the crescent" or "## Crescent"; the multi-word wikilink target disambiguates from unrelated uses of "crescent."

Two overlapping circles produce three regions: the intersection, which is what the predicates share, and the two crescent-shaped arcs outside the intersection, which are what each predicate holds that the other does not. A `## Crescent` section on a Predicate node carries the content of exactly one of those arcs — this predicate's non-overlapping territory against one specific neighbor. A predicate with multiple adjacent neighbors has multiple crescents, each against a different circle, each with its own shape.

The asymmetry is geometric, not just an authoring convenience. The crescent of A against B and the crescent of B against A are different regions of the page — different shapes, different sizes — because they sit on opposite sides of the intersection. A Crescent section on Predicate A names what A holds that B does not; the mirror section on Predicate B names what B holds that A does not; neither is the inverse of the other. Two independent accounts together are the full pairing.

The metaphor presupposes adjacency. Crescents exist only where circles overlap; between two disjoint predicates there is no intersection and therefore no crescent. This is why the Predicate Form Contract requires `## Crescent` subsections only against predicates declared as near-neighbors via `contrasts_with::`, not against every predicate in the vocabulary. Adjacency is load-bearing for the form; crescents are how the adjacency's distinctions get recorded. Leaving an adjacent predicate's crescent undocumented is a silent invitation to merge the two under later convergence pressure, because nothing in the graph records what the merge would destroy.

## Relations

- informs::[[Predicate Form Contract]]
  - The Contract's `## Crescent` Requirement uses this term. The Venn-non-overlap metaphor is what gives the section its shape — per-neighbor H3 subsections, asymmetric content across adjacent nodes, scoped to predicates with declared adjacency.

- informs::[[Document Predicate Crescents Against Adjacent Predicates]]
  - The Decision that grounds the Crescent Requirement. The metaphor is the reason the Requirement takes the shape it does — per-neighbor rather than global paragraph, asymmetric rather than mirrored.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes the distinction-preservation work load-bearing. The Crescent metaphor is how the project pictures what convergence pressure destroys: the non-overlap arc is the distinction, and merging adjacent predicates flattens the crescent into the intersection.

- contrasts_with::[[Named Edge -- a predicate-annotated wikilink expressing a typed relation|Named Edge]]
  - A Named Edge is a typed relation between two nodes; a Crescent is the distinction one predicate holds against another. Named Edges are the graph's connections; Crescents are the authorial accounts of what those connections keep separate.
