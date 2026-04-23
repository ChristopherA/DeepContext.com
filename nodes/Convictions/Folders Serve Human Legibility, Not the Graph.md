---
created: 2026-04-19
tagline: Folders exist for contributors scanning the filesystem; the graph lives in named edges, not in directory paths
brief_summary: A held stance that folder placement in a Deep Context prototype is a reader-facing convenience and plays no part in the graph layer. Wikilinks resolve by filename, not by path; named-edge predicates carry the semantic connections between nodes; filesystem adjacency encodes nothing the graph traverses. Folders may be reorganized at any time — by form, by domain, by lifecycle stage, by any scheme that serves human legibility — without touching any edge or any predicate. A tool reading the graph ignores folders entirely; a contributor scanning the filesystem relies on them. The stance drifts when any graph mechanism (a predicate, a convention, a resolver, a tooling assumption) starts depending on a folder path.
---

- conforms_to::[[Conviction Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Folders Serve Human Legibility, Not the Graph

In a Deep Context prototype, folder paths exist for the human reader scanning the filesystem — they let a contributor open a directory and recognize at a glance what kind of node lives there. The graph itself lives in the named edges between files; the project holds that moving a node from one folder to another changes no edge, no predicate, and no relation the graph traverses.

## Why It Is Held

Three mechanisms make the stance warranted.

Wikilinks resolve by filename. In CommonMark wiki extensions and Obsidian's default configuration, `[[Ghost Link -- a wikilink to a target that does not yet exist]]` resolves to the file with that name regardless of which directory it sits in. The resolver does not consult folder paths; it consults the filesystem for a file whose name matches. A gloss placed in `Glosses/` and a gloss placed at the top of `prototype/nodes/` resolve identically from any prose reference.

Named edges carry graph semantics. The connection between two nodes is expressed by a predicate — `conforms_to::`, `grounded_in::`, `informs_downstream::` — attached to a wikilink. That predicate is author-declared and readable as plain markdown. No predicate in this prototype says "is in the same folder as" or derives meaning from filesystem adjacency; two nodes colocated in `Contracts/` are no more related by the graph than two nodes in different folders.

Committing filesystem paths to the graph would conflate two orthogonal concerns. Folders serve scanning: which directory should I open to find contracts? Edges serve traversal: which node does this one conform to, and where does that one derive its authority? Binding the graph to paths would make every reorganization destructive — renaming a folder would require rewriting every edge — and would force one organization scheme to carry both reader-facing and graph-facing load. Separating the two leaves folders free to change as reader needs evolve while the graph's meaning stays stable.

## What It Asks

Folders MAY be reorganized at any time without touching any edge. A contributor who decides that form-based grouping is less useful than domain-based grouping — or who introduces a stage-based view, or flattens everything and relies on filename prefixes — can move files freely. The stance, taken seriously, means the graph survives the move.

A contributor scanning `Glosses/` understands the form-type of what lives there from the folder name. That understanding is not encoded in the graph; the nodes themselves carry `conforms_to::[[Gloss Form Contract]]` as an edge, which is what a tool reading the graph relies on. The folder is a reader convenience that parallels the edge without substituting for it.

Tools reading the graph ignore folder paths entirely. They parse identity predicates, body structure, and relation edges; they do not consult the directory tree. If a future agent needs to find all Decisions, it searches for `conforms_to::[[Decision Form Contract]]` across files — not for files under a `Decisions/` path. A folder-blind tool and a folder-using reader see the same graph, and the project commits to keeping it that way.

Folder schemes may be layered or adapted without coordinating with the graph layer. A prototype might group by form today and by domain tomorrow; a derived publication might flatten everything into a single directory; an Obsidian vault view might hide folders and expose tags. All four views show the same graph, because the graph is not in the folders.

## Drift Recognition

The stance has drifted when a graph mechanism depends on folder paths. A predicate that encodes a folder name — something like `in_folder::[[Glosses]]` carrying semantic weight — is drift, because folder membership would then be part of what the graph asserts. A convention that forbade moving a file between folders because edges would break is drift, because it would reveal that edges silently depend on paths. A resolver that refused to dereference `[[Ghost Link -- ...]]` unless the target sat in a specific directory is drift, because it would have made the graph folder-dependent at the tool layer.

A lint check that surfaces a file whose form-predicate disagrees with its folder — `conforms_to::[[Gloss Form Contract]]` but placed in `Contracts/` — is not drift. That check serves the reader (a mislabelled drawer) by noticing the disagreement, without making the graph's meaning depend on the folder. The distinction is whether the folder carries graph-relevant authority or whether the check treats the folder as a reader-facing cue the author may have gotten wrong.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The commitment to filename-resolving wikilinks and author-declared predicates is what makes the folder-independence stance structurally viable. Because the graph's spine is wikilinks-by-filename and author-declared typed edges — neither of which consults filesystem paths — folder placement never becomes load-bearing. A graph spine built on path-based references would force filesystem placement into the graph layer and make the stance unattainable.

- contrasts_with::[[Adopt Node Atomicity]]
  - Both commitments define what the graph's granularity rests on, along different axes. Adopt Node Atomicity names the concept/file boundary — each node names one concept, and that correspondence is what the graph's edges traverse. This Conviction names the filesystem/graph boundary — folder paths are reader-facing, not part of the graph. Adjacent commitments defining different axes of what "the graph" actually is.

- informs_downstream::[[Markdown Node Contract]]
  - The Markdown Node Contract specifies the file-level form (identity block, H1, body, Relations) without constraining folder placement. This Conviction is the held stance that explains the silence: the contract is silent on folders because folders are not part of the graph the contract describes.

- informs_downstream::[[Gloss Form Contract]]
  - The Gloss Form Contract's filename pattern (`<Concept> -- <definition>.md`) encodes enough information for a contributor to recognize the form from the filename alone. Folder placement in `Glosses/` is a parallel reader convenience that reinforces the filename signal; the contract does not require it, because requiring it would bind the form to a filesystem scheme rather than to the file's own content.

- grounded_in::[[Human Authority Over Augmentation Systems]]
  - The Human Authority Conviction names the authorship locus — the graph's meaning rests on human-declared structure, not on tool-inferred patterns. This Conviction specializes that stance at the filesystem boundary: the graph's meaning rests on named edges a human authors, not on directory paths the filesystem imposes. The broader stance is held at the authorship layer; this one is held at the folder layer.
