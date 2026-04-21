---
created: 2026-04-19
tagline: One predicate, one question, one axis of distinction; overloaded predicates refactor into single-axis families
brief_summary: A commitment that every predicate in the local vocabulary answers exactly one question along one axis of distinction. Predicate families — each member a single-axis predicate — replace overloaded predicates rather than revised-but-still-overloaded names. The discipline is about the question a predicate answers, not the cardinality of its values: a predicate taking many values along one axis is atomic, a predicate taking two values that span two axes is not. The commitment is the edge-level companion of node atomicity.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Adopt Predicate Atomicity

Every predicate answers exactly one question. When a predicate is found carrying two or more axes of distinction, the remedy is a predicate family — each member a single-axis predicate — not a revised but still-overloaded name. The commitment is to keep the vocabulary's query handles sharp: a reader filtering on a predicate finds nodes whose assertion on that predicate means one thing, not several.

## Why

The commitment provides **query sharpness**. Predicates are the graph's query handles — each is a question a reader poses to any node: *what is this node's X?* When the question has one answer per node along one axis, filtering is sharp: a query for all nodes with `has_lifecycle::[[Seed Stage]]` returns exactly the nodes at that lifecycle stage, no disambiguation required. When the predicate carries multiple axes, the same query returns nodes whose value *might* mean any of several things, and the reader has to re-interpret each match against the original author's intent. The sharpness degrades continuously with corpus growth — the more nodes assert the overloaded predicate, the more work any reader does to sort the clusters back apart.

The commitment is the edge-level companion of [[Adopt Node Atomicity]]. Node atomicity says a node names one concept, not a collection; compound shapes exist for supporting material, not for sub-concepts. The predicate-level commitment is the same shape: a predicate names one question, not a bundle. Predicate families carry related distinctions, but each family member owns exactly one axis. The graph has atomicity commitments at both levels — vertices and edges — and each grounds the other.

The commitment is not a count-the-values rule. A predicate can take many values (`[[Seed Stage]]`, `[[Growth Stage]]`, `[[Mature Stage]]`) and still answer one question (*what lifecycle stage?*). The discipline is about the *question*, not the cardinality of the answer. A predicate with three values along one axis is atomic; a predicate with two values spanning two axes is not. The recurring craft move that performs the refactor when an overloaded predicate is discovered in the wild is [[Refactor the Predicate's Axes]].

Deprecations become part of the graph. Retired overloaded predicates do not vanish; they land in the "deliberately not used" section of the conventions document with a pointer to the family that replaced them. The deprecation record is how the graph carries the history of its predicate atomicity work, and it protects future contributors from reintroducing the same overload under a new name.

## Alternatives Considered

**Tolerate overloaded predicates with runtime disambiguation.** Allow predicates to carry multiple axes and expect readers or tools to sort the clusters at query time. Rejected because runtime disambiguation requires that every reader know how to split the axes, and that knowledge is not expressible in the predicate itself. The reader is left auditing the author's intent on every match. The cost compounds: a single overloaded predicate is tolerable, three overloaded predicates composing in a query produces matches whose meaning no reader can reconstruct without reading each cited node's full body.

**Revise the overloaded name rather than split.** Keep one predicate but rename it to signal the overload (`has_combined_status::` for lifecycle-plus-curation). Rejected because the overload persists — the rename makes the predicate more honest about its sin without fixing it. Filtering on the renamed predicate still returns nodes whose value means multiple things; the reader still audits each match.

**Global fixed vocabulary.** Define the predicate set in advance, schema-style, and require contributors to use only the predefined predicates. Rejected because the convention is specifically designed to let contributor vocabulary stay local-dialect and emergent. Fixed vocabularies prevent *introducing* overloaded predicates but also prevent the contributor diversity the graph depends on; the discipline needs to live at the authoring moment, not at the schema layer. The `relates_to::` case is the forcing example — the overload was introduced organically, and the fix is a specific-predicate family introduced as contributors needed it, not a vocabulary locked in advance.

## What Would Change It

Two classes of condition would prompt revisit.

**Predicate typing absorbs disambiguation.** If the underlying convention grew a standard way to type predicate values — typed ranges like `has_status::lifecycle=[[Seed Stage]]`, typed tuples, or predicate-internal schema — the runtime cost of overload would fall. A reader or tool could filter on the typed component rather than on the predicate-as-a-whole. No such typing exists at the plain-markdown floor today, and inventing one would require agreement across contributor vocabularies the convention is specifically designed not to centralize.

**Tooling re-interprets overloaded predicates reliably.** If agent tooling grew the ability to split overloaded predicate assertions into their constituent axes at read time — recognizing that `has_status::[[Seed]]` was asserting lifecycle while `has_status::[[Curated]]` was asserting curation — the authoring-time split would become less load-bearing. The tooling would have to be reliable across the full contributor vocabulary, not just the predicates one implementer wrote. The bar is high because the wrong split silently mis-classifies every node the tool processes.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The Decision that makes predicates first-class structural elements. This commitment is a standing claim about the quality those predicates should carry as the vocabulary grows — the question-per-predicate discipline is what keeps the named-edge spine usable at corpus scale.

- grounded_in::[[Adopt Node Atomicity]]
  - The parallel atomicity commitment at the vertex level. Node atomicity (one concept per node) and predicate atomicity (one question per predicate) are the two faces of the same design discipline — the graph has atomicity claims at both levels, and each grounds the other.

- informs::[[Markdown Node Contract]]
  - Markdown Node Contract's predicate-atomicity Requirement is the thin enforcement clause pointing at this Decision. The Contract carries the compliance rule; this Decision carries the reasoning and the revisit conditions.

- informs::[[Refactor the Predicate's Axes]]
  - The Pattern that realizes or restores this commitment when a predicate is discovered in the wild carrying multiple axes. This Decision states the standing commitment; the Pattern names the craft move applied when the commitment is violated.
