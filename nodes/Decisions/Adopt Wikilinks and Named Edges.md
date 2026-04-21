---
created: 2026-04-18
tagline: Author-declared wikilinks and named edges are the convention spine
brief_summary: The graph's structural claims travel through `[[wikilinks]]` and `predicate::[[Target]]` named edges with indented annotations — plain-markdown expressible, author-declared rather than agent-inferred, and designed to let contributor vocabulary stay local-dialect and emergent rather than convergent on a fixed ontology. Wikilinks without named edges produce an unindexed pile of terms; named edges without wikilinks collapse into tag spaghetti with no canonical target. The two pieces co-specify and are adopted together.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-18
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Adopt Wikilinks and Named Edges

The spine of the graph is author-declared wikilinks with named-edge predicates and indented annotations. Every relational claim takes the form `- predicate::[[Target]]` or `- predicate::[[Target]]↗`, expressed as a top-level bullet in the identity block above the H1 or under a node's Relations section. Classification rides the same rails: `conforms_to::[[X Form Contract]]` over `is_a::[[X Form]]`. Unconflation is a discipline — predicates that smuggle more than one question into a single value get split into single-axis predicates before they ossify. We keep structural claims off prose, off YAML, and off tags entirely: if a named edge can carry it, a named edge carries it.

## Why

We face the vocabulary-sovereignty problem that kills shared wikis in diverse-contributor settings. When contributors bring different naming traditions, a system that forces convergence on one ontology destroys the meaning each tradition preserved, and a system with no discipline produces a pile of terms no one can navigate. We want a third option: each contributor's vocabulary stays local-dialect and emergent, but the graph an agent reads remains coherent — because the author names each edge rather than an agent inferring it.

The hinge is **author-declared edges** rather than agent-inferred edges. When one contributor writes `- critiques::[[X]]` on a contested-concept node and another writes `- challenges::[[X]]` on their own, both edges land in the graph as distinct claims; a facilitating agent reading the graph later translates between the vocabularies rather than collapsing them into a normalized `disagrees_with::`. Wikilinks and named-edge predicates are the plain-markdown mechanism that makes this expressible without tooling — no database, no schema, no editor lock-in. Any markdown file becomes a graph node; any `predicate::[[Target]]` line becomes a typed edge; any external reference (`[[Target]]↗`) signals a node in another wiki rather than a broken or ghost link.

Classification through `conforms_to::[[X Form Contract]]` rather than `is_a::[[X Form]]` is not cosmetic: a node conforms to a specification rather than being identical to one, which lets it pluralize (a node can conform to multiple contracts from different traditions) and stay revisable. Unconflation is the same principle applied to single-value predicates — a predicate carrying two axes (lifecycle and curation, say, under one status name) splits into two single-axis predicates, so a predicate answering two questions doesn't smuggle a decision past deliberation. Progressive disclosure for agents is the practical payoff: classification predicates above the H1 orient a reader or agent to the node's type, domain, and maturity before any prose is read, and a finite reading budget gets spent deliberately on the edges most worth traversing.

## Alternatives Considered

A successor to the wikilink-and-named-edge bundle would need to preserve plain-markdown expressibility, author-declared edges, and contributor-vocabulary plurality simultaneously. Every alternative considered violates at least one.

**Tool-dependent query layers (Dataview, Logseq properties).** Rejected because they break plain-markdown expressibility. The graph becomes hostage to the tool — the same notes read elsewhere lose their structure, and any reader that does not run the tool sees only prose and unprocessed metadata.

**RDF-in-frontmatter.** Rejected because it is unreadable in raw markdown and pushes toward ontological imposition. RDF requires committing to a schema before the predicates stabilize, which forecloses the local-dialect-and-emergent property the convention is specifically designed to preserve.

**LLM-inferred edge layers.** Rejected because they violate the author-declared property. When an agent infers relations from prose rather than transcribing relations the author declared, contributors become subjects of the system's extraction rather than participants in its naming — the precise failure mode that drove the design toward author-declared edges.

**Fixed global vocabulary.** Rejected because it breaks contributor-vocabulary plurality. Forcing convergence on one ontology destroys the meaning each naming tradition preserved; the system we want is one where contributor vocabularies stay local-dialect and a facilitating agent translates across them, not one where a single agreed vocabulary papers over the underlying differences.

## What Would Change It

This decision bundles two tightly-coupled commitments; the revisit conditions split by part.

**Wikilink spine.** We'd revisit if plain-markdown expressibility broke down — if tooling became required to follow links at usable scale, if authors could no longer rely on ghost links as planning signals because target discoverability demanded pre-existing files, or if broken-link accumulation outpaced seed velocity. None of these look plausible at current scale; the convention assumes a human-readable graph and nothing so far has contradicted that.

**Named-edge vocabulary.** We'd revisit if contributors cannot produce annotations reliably — if the discipline overhead outweighs the curation payoff, if single-word predicates reappear by default, if `relates_to::` becomes the lazy catch-all, or if vocabulary drift outpaces consolidation. The unconflation decisions already in play are preventative; if they prove insufficient, we'd move to tighter predicate gatekeeping. A switch to a fixed global vocabulary would break the local-dialect property that made the convention viable for diverse contributors in the first place, so we'd treat that as an expensive revisit, not a cheap one.

We'll revisit the whole bundle after the first seed-and-run cycle produces 15-30 nodes that exercise the full predicate family.

## Relations

- grounded_in::[[Founding Conversation]]
  - The exploration that grounds this Decision — what was considered, what was rejected, what became provisionally committed. The Founding Conversation is a context-folder record rather than a first-class node; the edge points at that record so the reasoning remains traversable.

- informs::[[Markdown Node Contract]]
  - Markdown Node Contract encodes the wikilink and named-edge mechanics as file-form requirements (identity block above H1, `- predicate::[[Target]]` bullets, `↗` for external provenance, no scalar mirrors of graph predicates). The wikilink-and-named-edge decision is the upstream substrate; Markdown Node Contract is the first concrete downstream implementation.
