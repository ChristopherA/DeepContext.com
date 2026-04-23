---
created: 2026-04-19
tagline: A node and an atomic concept stand in one-to-one correspondence; compound nodes still name one concept
brief_summary: A commitment that every node in the graph names exactly one atomic concept — an atomic file or a compound folder with a designated lead, with sub-files serving as supporting material for the one concept the compound names. The correspondence is load-bearing for every downstream mechanism that reads or traverses the graph: wikilink resolution, typed-edge endpoints, supersession chains, and the filename-carries-form patterns all presuppose the one-concept-per-node bijection. Violations are split, not disambiguated in prose.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Adopt Node Atomicity

One node names one concept, and one concept has one node. A file — or, when the concept has supporting material substantial enough to warrant sub-files, a folder with a designated lead — stands in one-to-one correspondence with a single atomic concept in the graph. The commitment is to split files that carry two concepts rather than disambiguate them in prose; to promote a sub-file to its own node rather than let a compound grow a second identity; to reach for the supersession chain rather than rewrite a node whose commitment has been revised.

## Why

The commitment provides **unambiguous traversal of the graph's edges**. Every typed predicate in the vocabulary (`conforms_to::`, `grounded_in::`, `informs_downstream::`, `supersedes::`) is written assuming a single concept at the endpoint. Wikilinks resolve by filename, and each filename is one name; if a single file elaborated two concepts, a wikilink referencing the file would pick up both while the predicate on the wikilink traversed as if there were one. Atomicity at the vertex is what keeps the spine's semantics coherent — the alternative is predicates whose meaning depends on which concept in a file the reader chose to foreground.

Supersession works concept by concept. When a commitment is revised, a new Decision replaces the old and `supersedes::` carries the relation. If an old node held two commitments and only one was revised, supersession breaks — the new node cannot cleanly supersede the old because the old also carried the unchanged commitment. Atomic revision requires atomic nodes; the supersession machinery the Decision Form Contract specifies presupposes this commitment without stating it.

Readers find nodes by concept. A contributor searching for the gloss of one term opens a file whose filename names that concept. If the file also held the gloss for a second term, the folder view, the hover preview, and the search result all mislead — the mental model the filesystem-as-graph offers fractures at the first two-concept file. The filename-carries-form patterns (commitment-phrased Decisions, `<Concept> -- <definition>` Glosses, held-stance Convictions) all rest on the commitment that the filename names one thing.

Compound nodes follow the commitment without exception. A compound names one concept; its sub-files are *supporting material* — an agenda, a transcript, an ancillary record — not sub-concepts or facets. The lead file carries the compound's identity predicates and relations; the sub-files serve the concept's elaboration. Decisions MAY bundle multiple logically-related commitments under the narrow conditions in [[Decision Form Contract]], but a bundled Decision still names ONE concept — the bundle itself, adopted as a single commitment.

## Alternatives Considered

**Multi-concept files with predicate disambiguation.** Allow a file to carry two or more concepts and let named-edge predicates name which concept they target (`conforms_to::[[File#ConceptA]]`). Rejected because it pushes the disambiguation burden onto every edge in the graph. A predicate vocabulary currently written as "one question, one endpoint" would have to grow an endpoint-disambiguation axis, and every reader or tool traversing the graph would pay the cost of resolving it. The plain-markdown floor the wikilinks-and-named-edges decision commits to does not admit of an anchor-like endpoint selector without tooling.

**Folder-as-concept with files-as-facets.** Let a folder name a concept and its contained files name sub-concepts or facets of the parent. Rejected because folders are not graph vertices — the [[Folders Serve Human Legibility, Not the Graph]] Conviction commits the project to treating folder paths as reader-facing organization rather than as part of the graph the predicates traverse. Promoting folders to concept-carriers would collapse the boundary that Conviction draws and would make every predicate reference ambiguous between folder-level and file-level targets.

**Loose atomicity with curation-time splitting.** Tolerate two-concept files during authorship and split them during a later curation pass. Rejected because the cost of an ambiguous period in the graph is not local to the unsplit file. Every edge landed against the two-concept file during the tolerant window carries the ambiguity forward; the curation pass has to audit not just the file but every citing node. The commitment-level discipline is cheaper than the cleanup.

## What Would Change It

Two classes of condition would prompt revisit, both distant.

**Wikilink resolution changes mechanism.** If canonical resolution ceased to be by filename — if a wiki layer grew robust fragment addressing, named endpoints per file, or structural-selector resolution with tool-independent semantics — the commitment's central load-bearing requirement would weaken. Predicates could then target a concept inside a multi-concept file without ambiguity. No plausible candidate at the plain-markdown floor exists today; pipe-form wikilinks address display, not endpoint disambiguation.

**Named-edge predicates absorb endpoint disambiguation.** If the predicate vocabulary grew a standard way to name which concept in a two-concept file an edge targets, atomicity would become a convention rather than a structural necessity. This would require the local-dialect predicate vocabulary to grow a disambiguation axis globally — every predicate, every citing node. The ergonomic and cognitive cost is high enough that the single-concept-per-node commitment dominates at current scale; a concrete proposal with demonstrated tooling support would be the trigger for revisit.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The wikilink-by-filename and named-edge infrastructure assumes atomic endpoints. Every edge in the vocabulary — `conforms_to::`, `grounded_in::`, `informs_downstream::`, `supersedes::` — presupposes that the target is a single concept. This Decision is the standing commitment that makes that presupposition coherent; without it, the edge vocabulary would carry silent ambiguity on every traversal.

- grounded_in::[[Adopt Predicate Atomicity]]
  - The parallel atomicity commitment at the edge level. Node atomicity (one concept per node) and predicate atomicity (one question per predicate) are the two faces of the same design discipline — the graph has atomicity claims both at the vertices and at the edges, and each grounds the other.

- contrasts_with::[[Folders Serve Human Legibility, Not the Graph]]
  - Both commitments name what the graph's granularity rests on. The Conviction names the filesystem/graph boundary — folder paths are reader-facing, not part of the graph. This Decision names the concept/file boundary — each node names one concept, and that correspondence is what the graph's edges traverse. Adjacent commitments defining different axes of what "the graph" actually is.

- informs_downstream::[[Markdown Node Contract]]
  - Markdown Node Contract's node-atomicity Requirement is the thin enforcement clause pointing at this Decision. The Contract carries the compliance rule; this Decision carries the reasoning and the revisit conditions.

- informs_downstream::[[Compound Node -- a folder of markdown nodes with a designated lead|Compound Node]]
  - The compound-node pattern is this Decision's answer to concepts with substantial supporting material. The compound groups a concept's supporting material under a lead; the Decision's Why is what tells the author whether a prospective sub-file is supporting material (stays compound) or an independent concept (promote to atomic).
