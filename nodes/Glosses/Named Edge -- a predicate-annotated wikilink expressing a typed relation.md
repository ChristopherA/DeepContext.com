---
created: 2026-04-19
tagline: A predicate-annotated wikilink expressing a typed relation — the structural unit of the graph's connection layer
brief_summary: A Named Edge is a bullet of the form `predicate::[[Target]]` — a multi-word lower_snake_case predicate followed by a double colon followed by a wikilink to another node, optionally marked with `↗` when the target lives in a different wiki. The predicate types the relation; the wikilink identifies the target; an indented sub-bullet annotation explains why the relationship matters. Named Edges are the mechanism by which a markdown file participates in a graph without leaving plain-markdown expressibility. Inline wikilinks in prose are readable cross-references, not Named Edges — a reader distinguishes them by section, not by syntax.
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Named Edge

A predicate-annotated wikilink expressing a typed relation between two nodes, written as a top-level bullet of the form `- predicate::[[Target]]` or `- predicate::[[Target]]↗`. The predicate names the kind of relation (`extends_contract::`, `composed_of::`, `grounded_in::`, `contrasts_with::`); the wikilink identifies the target node; an indented sub-bullet annotation under the edge explains why the relationship matters. Together the three pieces carry a graph claim that is parseable by an agent and scannable by a human in the same markdown document.

Named Edges appear in two places. The **identity predicate block** above the H1 carries classification edges — `conforms_to::[[X Form Contract]]`, `in_domain::[[Y]]`, `has_lifecycle::[[Z Stage]]` — that declare what the node is. The **Relations section** after the body carries semantic edges — `composed_of::`, `contends_with::`, `informs_downstream::` — that declare how the node connects to others. Both use the same syntax; their roles differ by position in the file, not by form.

The contrast is with inline wikilinks in prose, which are readable cross-references rather than structural edges. A sentence like "this draws on [[Wikilinks and Named Edges]]↗ as a starting point" contains a wikilink but no predicate — a reader follows it if they want context, an agent does not treat it as a graph claim. The predicate is what makes an edge *named*, and the bullet position is what makes it *structural*. Lose either and the construction falls back to inline reference.

## Relations

- has_component::[[Wikilink Syntax]]↗
  - The target half of a Named Edge is always a wikilink; the `[[...]]` syntax is the substrate on top of which the predicate layer runs. The wikilink resolution is Obsidian-style filename matching, not URL resolution.

- grounded_in::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The canonical specification for the convention. This gloss captures the local working definition; the gist carries the full discussion of why the convention works the way it does.

- contrasts_with::[[Inline Wikilink Reference]]
  - Inline wikilinks in prose are readable cross-references without structural weight. Named Edges are typed structural claims in the identity block or Relations section. Both use `[[...]]` but only one participates in the graph. Ghost link pending local gloss.
