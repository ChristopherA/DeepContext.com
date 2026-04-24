---
created: 2026-04-19
tagline: The relates_to:: predicate is prohibited; contributors choose a specific predicate or add one to the local vocabulary
brief_summary: A commitment that the generic `relates_to::` predicate is not permitted anywhere in the graph. When an author wants to assert that two nodes are connected, they MUST pick a specific predicate from the local vocabulary — `grounded_in::`, `informs_downstream::`, `contrasts_with::`, `built_on::`, `informed_by::`, or similar — or add a new predicate to the vocabulary. The commitment protects the query sharpness the named-edge spine promises by forbidding the one predicate that would absorb every unspecific connection and collapse the vocabulary's distinctions.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# No Generic relates_to Predicate

The `relates_to::` predicate MUST NOT be used anywhere in the graph. When an author wants to assert a connection between two nodes, the author picks a specific predicate from the local vocabulary — `grounded_in::`, `informs_downstream::`, `contrasts_with::`, `built_on::`, `informed_by::`, `contends_with::`, `composes_with::`, or any other typed edge in use — or adds a new predicate to the vocabulary when none of the existing family members fits. The commitment forecloses the path of least resistance: "these two things are related, let's just say so." That path collapses the query vocabulary into a single undifferentiated edge.

## Why

The commitment preserves **what the relationship IS, not just that it exists**. Specific predicates carry semantic weight: `grounded_in::[[X]]` says this node rests on X as substrate; `informs_downstream::[[X]]` says this node shapes X; `contrasts_with::[[X]]` says this node and X are adjacent on a load-bearing boundary; `contends_with::[[X]]` says there is a live tension between them. A query filtering on `grounded_in::` returns substrate relationships specifically, not informing, contrasting, or contending ones. The predicate vocabulary IS the semantic distinction — it is not metadata decorating a relation; it is the relation.

`relates_to::` is the predicate that makes every query imprecise. When the graph allows `relates_to::[[X]]` as a valid assertion, contributors reach for it whenever naming the specific relationship feels uncertain or effortful. The resulting graph carries a mass of connections whose type is "related in some way," and every query that wants substrate, contrast, or tension has to fall back to reading each node's body to reconstruct what the author actually meant. The query vocabulary's sharpness degrades with each generic edge added; once `relates_to::` becomes available, it out-competes specific predicates by offering lower authoring cost, and the graph drifts toward tag-spaghetti semantics under a wikilink surface.

The commitment is the edge-level expression of the same discipline that drives [[Adopt Predicate Atomicity]]: predicates answer one question, and the question is specific. `relates_to::` is the degenerate limit of overloaded predicate design — a predicate whose question is "is there any connection at all?" — and the answer it returns carries no information the rest of the graph's traversable structure does not already carry (the absence of a predicate-path between two nodes is itself a statement, differently informative). Prohibiting `relates_to::` rules out the limit case; predicate atomicity governs all the middle cases.

When no existing predicate fits, the discipline is to add a new predicate to the local vocabulary by seeding a Predicate node in `nodes/Predicates/` (via the Predicate Propose skill) rather than to fall back on a generic. A new predicate names the specific question it answers, earns its place in the vocabulary, and is available for other contributors to use. The vocabulary grows by accretion; it does not grow by admitting catch-alls.

## Alternatives Considered

**Permit `relates_to::` with a convention to refine later.** Allow contributors to assert `relates_to::` during initial authoring and expect a later curation pass to upgrade each instance to a specific predicate. Rejected because the authoring-time cost of picking a specific predicate is low and the accumulation cost of unrefined `relates_to::` is high. Every `relates_to::` edge added is one the curator must audit, one the reader who queried for a specific relation missed, and one that trains contributors to default to generic in the next session. The curation debt compounds faster than curation passes can drain it.

**Permit `relates_to::` with a deprecation-on-discovery policy.** Allow it but commit to converting every instance to a specific predicate whenever it is encountered. Rejected because discovery is incidental; the edges accumulate faster than they are encountered. A graph that is supposed to be navigable by predicate cannot rely on opportunistic fix-up for a predicate that is by design the most frequent default path.

**Permit `relates_to::` for genuinely unclassified relations.** Reserve it for cases where the author genuinely cannot name what the relation is and expects it to become clear later. Rejected because "genuinely unclassified" is rarely the actual state — what feels unclassified at authoring time is usually a specific relation the author has not yet named. The right move is to name the question the relation answers (`depends_on::`, `motivated_by::`, `overlaps_with::`), not to leave it generic. Cases where the relation truly cannot be named are rare enough to handle as a prose remark or a source annotation rather than as a typed edge; the `↗` marker already covers external provenance.

## What Would Change It

The commitment would be revisited under conditions that make the specific-predicate discipline unsustainable.

**Vocabulary grows large enough that picking a specific predicate becomes authoring burden.** If the local vocabulary reached the scale where a contributor faces twenty or thirty plausible predicates per relation and the cost of picking the right one outweighs the graph's benefit from the sharpness, the commitment would weaken. The current vocabulary is small and well-scoped; no such pressure exists. The commitment's revisit condition is pressure the vocabulary itself has not produced.

**Tooling makes generic-to-specific refinement cheap at read time.** If a reader or agent could reliably infer the specific predicate from node context at query time — a tool that read a `relates_to::` edge along with the bodies of both endpoints and produced the right specific predicate — the authoring-time discipline would matter less. The inference bar is high: the wrong inference silently mis-classifies every edge the tool processes. No current agent tool does this reliably enough to trust with the graph's semantic spine.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The Decision that makes named-edge predicates the graph's semantic spine. The prohibition on `relates_to::` is the spine's protection against the single predicate that would collapse every distinction the spine carries — a same-commitment-different-direction consequence of the substrate.

- grounded_in::[[Adopt Predicate Atomicity]]
  - The commitment that every predicate answers one specific question. `relates_to::` is the degenerate limit of overloaded predicate design — its question is "is there any connection?" — and prohibiting it enforces atomicity at the extreme case.

- informs_downstream::[[Markdown Node Contract]]
  - Markdown Node Contract's Relations Requirement carries the thin enforcement clause pointing at this Decision. The Contract carries the compliance rule; this Decision carries the reasoning and the revisit conditions.

- informs_downstream::[[Refactor the Predicate's Axes]]
  - The Pattern that performs the refactor when an overloaded predicate is discovered. A generic `relates_to::` encountered during curation is the forcing case for the Pattern's move — the refactor names the specific predicate the relation actually wanted.
