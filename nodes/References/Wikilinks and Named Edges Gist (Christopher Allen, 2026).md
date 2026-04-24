---
created: 2026-04-19
tagline: The gist specifying wikilinks plus named edges plus indented annotations as a plain-markdown graph convention
brief_summary: Christopher Allen's gist is the primary convention source Deep Context builds on. It specifies author-declared wikilinks (`[[Multi Word Target]]`), named-edge predicates (`predicate::[[Target]]`), and indented sub-bullet annotations as the three-piece machinery for expressing a typed graph in plain markdown — with companion moves (↗ for external provenance, `conforms_to::` over `is_a::`, unconflation as discipline, translation over convergence) that constitute the rest of the convention layer. Deep Context adopts it in full as the starting point; local dialect choices (which predicates, which form contracts, which folder layout) are carried by the graph's own Predicate nodes, Contract nodes, and the folder structure itself rather than in a separate conventions document.
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Primary Convention Source]]
- under_license::[[CC-BY 4.0]]↗
- authored_by::[[Christopher Allen]]↗
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Wikilinks and Named Edges Gist (Christopher Allen, 2026)

URL: <https://gist.github.com/ChristopherA/151aefa6a6bde1ce4fa6b1182656cebe>

The gist Christopher Allen published as an agent-reference guide for a plain-markdown convention combining wikilinks, named-edge predicates, and indented annotations. Deep Context treats it as the root of this project's convention layer: the filesystem-as-graph primitives, the progressive-disclosure discipline of annotated edges, the classification pattern using `conforms_to::[[X Form Contract]]` rather than `is_a::[[X]]`, and the vocabulary-sovereignty stance that lets diverse contributors keep their local dialects while a facilitating agent translates across them.

### Adopted

- **The three-piece convention** — `[[Multi Word Wikilink]]` plus `predicate::[[Target]]` named edges plus indented sub-bullet annotations — as the primary machinery every node uses.
- **`↗` as external-referent marker** — a trailing arrow on a wikilink whose target lives in a different wiki or external tradition, signaling "not a broken link, not a ghost link, a cross-wiki reference."
- **`conforms_to::` over `is_a::`** for classification — conformance is pluralizable; identity forces premature commitment.
- **Predicate axis refactoring** — predicates that smuggle more than one question into a single value get split into single-axis predicates before they ossify. The prototype names this as a recurring craft move in [[Refactor the Predicate's Axes]], paired with the predicate-atomicity Requirement in [[Markdown Node Contract]] as its standing structural rule.
- **Translation, not convergence** — when two contributors use different vocabulary for overlapping territory, both edges land in the graph as distinct claims and an agent translates between them rather than normalizing to a canonical form.
- **Progressive disclosure for finite context** — identity predicates above the H1 let a reader or agent orient before any prose is read, spending a finite context budget deliberately on the nodes and edges most worth traversing. The prototype names this as a recurring authoring move in [[Progressive Summary Before Substance]], paired with the layered-structure Requirement in [[Markdown Node Contract]] as its standing structural rule.

### Not adopted (yet)

- **`Renditions/` and `Archives/` convention** — adopted in principle for later sessions, but no sources yet warrant the folder layout. The decision to adopt it is deferred until the first source wants it.
- **Full vocabulary breadth** — the gist surveys a richer predicate family than Deep Context has introduced. Predicates are added locally only when 2–3 nodes actually want them; the gist's full catalog is reference material, not a checklist.

### Key moves to remember

- Annotated predicates (indented sub-bullet under the edge) are the mechanism that keeps the graph readable to a contributor scanning it, not just to an agent traversing it.
- Ghost links (wikilinks to targets that do not yet exist) are a planning signal, not a bug — they declare intended future nodes without requiring creation-first discipline.
- The convention is plain-markdown expressible without tooling: no database, no schema layer, no editor lock-in. Any markdown file is a graph node; any `predicate::[[Target]]` line is a typed edge.

## Relations

- informs_downstream::[[Markdown Node Contract]]
  - Markdown Node Contract encodes the gist's wikilinks-and-named-edges specification as file-form requirements — identity block above H1, `- predicate::[[Target]]` bullets, `↗` for external provenance, no scalar mirrors of graph predicates.

- informs_downstream::[[Adopt Wikilinks and Named Edges]]
  - The Decision that commits this graph to wikilinks plus named edges plus contributor-vocabulary plurality. This Reference is the source the Decision is `informed_by::`.

- informs_downstream::[[Contract Form Contract]]
  - Contract Form Contract specializes the gist's `conforms_to::[[X Form Contract]]` move into the self-conformance and inheritance patterns that Contract nodes use.
