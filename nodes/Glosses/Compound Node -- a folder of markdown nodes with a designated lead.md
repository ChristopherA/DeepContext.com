---
created: 2026-04-18
tagline: "A folder with a designated lead where the concept has supporting material; the folder resolves to the lead, and sub-files serve that one concept"
brief_summary: "A Compound Node names one concept — the same as an atomic node — and groups the concept's supporting material under a folder whose lead file carries the identity predicates, body, and relations. Sub-files are supporting material for the lead's concept, not sub-concepts or facets of a partitioned whole; if a sub-file begins to read as a concept in its own right (cited by other nodes under its own name, carrying its own outgoing edges), that is the signal the compound should be split. Folder-notes plugins make the folder directly addressable; without one, the lead is the canonical resolution and the folder is a grouping device."
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Compound Node

A folder with a designated lead, where the concept the compound names has supporting material substantial enough to warrant its own sub-files. The folder resolves to a graph node via the lead file, which carries the concept's identity predicates, body, and outgoing edges. The sub-files inside the folder are supporting material for that one concept — not sub-concepts, facets, or parts of a partitioned whole.

The **lead file** carries the compound's identity and elaboration; its filename matches the folder's wikilink target. **Sub-files** are siblings of the lead, serving the lead's concept (a meeting's agenda and transcript; a gloss's longer exegesis; a decision's ancillary records). A reader resolving `[[Compound]]` lands on the lead; sub-files are accessed through the lead's navigation, not typically cited from elsewhere in the graph under their own names.

Tool compatibility is the main gotcha. With a folder-notes plugin (Obsidian, Foam), the folder is directly addressable. Without one, the lead is just another file and the folder is a grouping device — the graph resolves identically, but navigation through the folder entry differs. The contract makes no plugin assumption: the lead file is canonical; folder-notes is a convenience layer on top.

The compound is a structural answer to concepts with substantial supporting material; it is not an exception to the one-node-one-concept rule. If a sub-file begins to accrue citations under its own name from other nodes, or starts carrying its own identity predicates and its own outgoing semantic edges, that is the signal that the sub-file was always a second concept sharing a folder with the first, and the compound should be split — see the node-atomicity Requirement in [[Markdown Node Contract]].

## Relations

- composed_of::[[Markdown Node -- a markdown file read as a node in a graph|Markdown Node]]
  - A Compound Node is a folder of Markdown Nodes. The lead and its supporting sub-files are each Markdown Nodes at the file-form level; the folder groups them for filesystem navigation. The compound as a whole names one concept.

- contrasts_with::[[Atomic Node -- a single markdown file resolving to a wikilink target|Atomic Node]]
  - An Atomic Node is a single markdown file; a Compound Node is a folder with a lead plus supporting material. Both name exactly one concept — the contrast is filesystem layout (single file vs folder with sub-files), not the count of concepts named.

- grounded_in::[[Adopt Node Atomicity]]
  - The Decision that commits the project to one-node-one-concept correspondence applies uniformly to atomic and compound nodes. A compound names one concept; its sub-files are supporting material, not additional concepts. The Decision's split criterion — a sub-file cited by other nodes under its own name, or carrying its own outgoing edges — defines when a compound must be split.

- grounded_in::[[Markdown Node Contract]]
  - The node-atomicity Requirement in the Markdown Node Contract is the thin enforcement clause for Adopt Node Atomicity. The compound-node pattern is the structural answer for concepts with substantial supporting material under that Requirement.

- grounded_in::[[Wikilinks and Named Edges]]↗
  - The wikilinks-and-named-edges convention specifies that a wikilink target resolves to either a single file or a folder whose lead file carries the same name.
