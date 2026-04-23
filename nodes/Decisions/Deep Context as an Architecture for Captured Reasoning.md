---
created: 2026-03-07
tagline: Capture reasoning as typed markdown forms with named-edge predicates — not fine-tuning, RAG, databases, or tags
brief_summary: The decision to capture personal reasoning as typed markdown forms connected by predicate wikilinks rather than as fine-tuned model weights, retrieval-augmented chunks, database-backed graphs, or tag sets. Typed forms with structural contracts make reasoning traversable by agents; named-edge predicates make the connections between pieces of knowledge navigable rather than implicit; progressive disclosure via identity predicates makes the whole usable inside finite context windows.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-03-07
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Growth Stage]]
- has_curation::[[Working Draft]]

# Deep Context as an Architecture for Captured Reasoning

Capture personal reasoning as typed markdown forms connected by predicate wikilinks into a navigable knowledge graph. Each form type answers a distinct question and carries a structural contract — required sections and identity predicates that make its shape predictable for both human readers and agent traversal. The authoring layer is plain markdown in git: zero-dependency, no database, no plugin, no schema enforcement.

## Why

Personal knowledge management captures facts and documents but not the reasoning substrate — the web of values, principles, patterns, and cases that lets a person (or an agent acting on their behalf) make decisions consistent with how they actually think. An agent with access to someone's notes can retrieve information but cannot reason as that person would, because the connective tissue between pieces of knowledge is implicit, unwritten, or scattered across unstructured prose. The problem is not retrieval; it is representation.

Five requirements drove the architectural choice. Knowledge must be captured in typed forms with known internal structure so that a reader or agent can orient quickly without reading the whole body. Forms must connect via explicit, traversable typed relations so the graph is navigable by predicate rather than by similarity. The architecture must operate within small context windows through progressive disclosure — identity predicates above the H1 let an agent decide whether to read further before loading the prose. The distinction between what an agent may decide and what requires human judgment must be expressible in the graph itself, not hidden in harness configuration. And the system must learn and expand through use, with approval gates that prevent drift.

Typed forms with named-edge predicates satisfy all five simultaneously, and no less-structured alternative does. The semantic layer is agent traversal via predicate edges; the trust layer (signed exchange between graphs) remains a future phase. Form types organized across orientation, structural, action, generative, and governance categories cover the reasoning spectrum from values and convictions through patterns and cases to inquiries and scenarios — not as a schema imposed in advance but as a taxonomy that emerges from what the knowledge actually needs.

## Alternatives Considered

**Fine-tuning or RLHF.** Train a model on an author's writing to replicate voice and judgment. Rejected because it captures behavioral patterns, not reasoning. A fine-tuned model can sound like an author without being able to explain why one principle takes priority over another; the reasoning substrate is opaque inside model weights. There is no auditability, no progressive disclosure, and no human override at decision boundaries. The output is mimicry, not structure.

**Retrieval-augmented generation over existing documents.** Index documents and retrieve relevant chunks at query time. Rejected because RAG retrieves without structuring. It finds *what* someone wrote but not *how* pieces connect or *why* one principle takes priority over another. There are no typed relations, no structural contracts, and no traversable graph — only chunks retrieved by similarity. This works for information retrieval; it does not capture reasoning.

**Database-backed knowledge graph.** Store forms and relations in Neo4j, PostgreSQL, or similar. Rejected because it violates the zero-tooling floor. The knowledge becomes hostage to a running database; every edit requires a database write; retrieval requires a specific query language. Plain-text files in git survive any tool change and any reader. A database adds a dependency that the representation does not need.

**Tags-only personal knowledge management.** Classify notes with YAML tags and retrieve by tag intersection. Rejected because tags produce sets, not graphs. "Tagged with identity AND privacy" retrieves a set of notes but says nothing about *how* identity and privacy relate — whether they are in tension, whether one constrains the other, whether a specific case validates their intersection. Predicates carry semantic meaning tags cannot.

**Hybrid structured/unstructured.** Keep most content as unstructured notes with a small structured layer for key entities. Rejected because the boundary between structured and unstructured becomes its own maintenance problem. Which knowledge deserves structure? The typed-forms approach answers the boundary question with the standalone-document test: if the content produces a standalone document with a known internal structure, it is a form; if it does not, it stays prose. The test is applied per node, not as a global split.

## Consequences

The architecture is exercised at estate scale: a running instance carries on the order of ninety typed nodes across most of the form taxonomy, connected by several thousand named-edge predicates. Progressive disclosure works in practice — agents load nodes on demand via identity predicates and named-edge traversal rather than reading full bodies up front. The zero-tooling floor holds: shell one-liners serve as the query layer; no specialized tools are required.

Authoring effort runs higher than unstructured notes. Writing a principle with grounding and structural consequences takes more work than capturing a thought, and the predicate vocabulary depends on author discipline rather than schema enforcement. A handful of form types remain uninstantiated at any given time — either premature or awaiting use cases that produce them. Ghost links accumulate as nodes reference concepts not yet written; manageable, but requires periodic tending.

External validation has arrived independently. Multiple agent memory systems (ClawVault, QMD, MIE) have converged on plain markdown plus YAML frontmatter plus typed metadata as the storage format for agent knowledge; benchmarks show this outperforms purpose-built infrastructure for the reasoning-capture use case. Research on agent context files finds they "behave more like dynamic configurations than static text," validating the architecture's treatment of living documents as first-class engineering artifacts.

## What Would Change It

Nothing plausible. The architecture rests on four requirements that each rule out a broad class of alternatives: typed forms rule out any purely unstructured approach; plain markdown in git rules out tool-hostage storage; progressive disclosure rules out any design that requires full-graph loading; expressible agent-versus-human authority boundaries rule out fully autonomous approaches. A revisit would require all four rule-outs to fail simultaneously — or the discovery of a substrate more plain-markdown-expressible than markdown itself, which has no plausible candidate.

The `has_commitment::[[Firm Commitment]]` predicate marks this decision as expensive to change, not irreversible. Concrete within-architecture decisions — which predicates, which form contracts, which folder layout — are provisional and are recorded in their own Decision nodes with their own revisit criteria. The architecture itself is the substrate on which those decisions operate; revising it would invalidate the graph of decisions built on top.

## Sources

- Allen, Christopher. "The Path to Self-Sovereign Identity," 2016 — values-to-principles chain as structural exemplar for typed forms carrying reasoning.
- Alexander, Christopher. *A Pattern Language*. Oxford University Press, 1977 — Alexandrian pattern form as template for structured-reasoning artifacts with context, problem, solution, and consequences.
- Matuschak, Andy. "Taxonomy of note types" — note type spectrum as input to form taxonomy.

## Relations

- grounded_in::[[Capture Reasoning, Not Just Knowledge]]
  - The Conviction that makes this architecture load-bearing. Capturing how contributors actually reason — values, patterns, alternatives, grounds — is what the form contracts and the named-edge convention implement at the structural layer. A Decision that records only the choice is a fact; this architecture exists so Decisions carry their reasoning.

- grounded_in::[[Knowledge Outlives Its Tools]]
  - The Conviction that makes plain markdown, git, and the zero-tooling floor load-bearing rather than aesthetic. The captured reasoning must survive tool changes; the architecture's durability commitments are how it meets that requirement.

- informs_downstream::[[Adopt Wikilinks and Named Edges]]
  - The wikilinks-and-named-edges decision commits this graph's semantic layer to author-declared named edges. Taking the architecture decision seriously requires committing to the mechanism that makes predicate traversal expressible; the gist-level decision is that mechanism's concrete form.

- informs_downstream::[[Markdown Node Contract]]
  - The contract encodes the file-form half of "typed forms with known internal structure" — identity block, Relations section, named-edge syntax, filename discipline. A downstream concretization of the architecture's first requirement.

- informed_by::[[Hybrid Bootstrapping for Garden Migration]]↗
  - A case study in transforming a corpus of source files into typed garden nodes at scale. The estate's node holds the methodology and its observed results; this Decision draws on that evidence for the claim that the architecture works in practice.

- informed_by::[[Wikis Without Curation Drift Toward Write-Only]]
  - The Observation names the failure mode this architecture is designed to counter — shared wikis that accumulate contribution but stall in navigability, ontology arbitration, and onboarding. The architectural moves (typed forms, progressive disclosure, named edges, structural contracts) are specifically responses to that failure mode.

- informs_downstream::[[The Second Cycle of Contribution Happens]]
  - The second-cycle Aspiration is the directional target this architecture serves across cycles. The architecture is the structural substrate; the Aspiration is the practice-level target the substrate makes reachable.
