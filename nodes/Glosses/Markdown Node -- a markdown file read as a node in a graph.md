---
created: 2026-04-18
tagline: "A markdown file read as a graph node — wikilinks and named edges are structure, not decoration"
brief_summary: "A Markdown Node is a plain markdown file, valid as CommonMark, that a reader treats as a node in a knowledge graph. Its wikilinks declare the node's neighbors; its named-edge predicates (predicate::[[Target]]) type the connections; its identity predicate block above the H1 declares what the node is. The file format is unchanged — the reading discipline is layered on top."
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Markdown Node

A markdown file read as a node in a graph: its wikilinks and named edges are first-class structure, not prose decoration. The file format does not change — a Markdown Node is valid CommonMark — but a reader that understands the convention parses specific constructs as typed graph edges rather than as arbitrary hyperlinks.

Three constructs carry structure. An **identity predicate block** above the H1 declares what the node IS (`conforms_to::`, `in_domain::`, `has_lifecycle::`, and so on). A **Relations section** after the body lists typed edges to other nodes, each with an optional indented annotation explaining why the edge matters. **Inline wikilinks** in prose are readable cross-references, not structural edges — a reader distinguishes them by section, not by syntax.

The contrast is with markdown-as-prose, where every `[[link]]` is just a convenient cross-reference. A Markdown Node commits to typed, annotated connection — the graph emerges from the file itself rather than from a separate index.

## Relations

- grounded_in::[[Wikilinks and Named Edges]]↗
  - The canonical reference that names markdown-with-wikilinks-and-named-edges as the underlying convention.

- built_on::[[CommonMark Markdown]]↗
  - CommonMark is the substrate file format. A Markdown Node stays valid CommonMark — the reading discipline is layered on top, not a divergent dialect.

- has_component::[[Wikilink Syntax]]↗
  - Wikilinks are the targets of the edges a Markdown Node declares.

- has_component::[[Named Edge -- a predicate-annotated wikilink expressing a typed relation|Named Edge]]
  - Named edges are the typed predicates that make a Markdown Node's links first-class structure rather than prose.

- informed_by::[[Karpathy LLM Wiki Pattern]]↗
  - Karpathy's plain-markdown-plus-LLM-curator pattern is one precedent for treating markdown files as first-class knowledge nodes.
