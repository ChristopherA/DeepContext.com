---
created: 2026-04-19
tagline: Every Relations-section edge carries an indented sub-bullet explaining why the relationship matters
brief_summary: A commitment that every named edge in a node's Relations section carries an indented sub-bullet annotation explaining why the relationship matters — not what the predicate means in general, but what this particular edge does for this particular node. The annotation is where reader context lives; the predicate carries the relation type. The two are paired: typed predicates without annotations produce a machine-readable skeleton with no reader payoff; annotations without typed predicates collapse into prose without graph participation.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Annotate Edges With Why-They-Matter

Every named edge in a node's `## Relations` section carries an indented sub-bullet annotation immediately below it. The annotation states why the relationship matters to this specific node — not what the predicate means in general, and not a summary of the target node's content. A reader stopping at the Relations layer reads the annotation to understand what the edge contributes to this node's meaning; a reader who wants more traverses to the target. Classification predicates in the identity block above the H1 usually do not need annotations; Relations-section edges do.

## Why

The commitment makes **typed predicates and reader context paired**. A bare edge like `grounded_in::[[X]]` carries the relation type — this node rests on X as substrate — but not the reason a reader should care. Two different nodes may both ground in X for very different reasons: one because X's structural machinery is load-bearing for it, another because X provides a conceptual frame it specializes. The predicate cannot distinguish the two; the annotation can. Without annotations, the Relations layer is a machine-readable skeleton that gives every reader the same flat information regardless of what they came to the node for.

Annotations carry what inline prose would carry if the edge were written in running text. A body paragraph saying "this node rests on X because X provides the substrate for the wikilink mechanics the node's Why depends on" becomes the annotation for `grounded_in::[[X]]`. The information is preserved; its placement moves from prose to structural context. The structural-tier benefit is what makes this move worthwhile: [[Adopt Layered Node Structure]] commits the graph to cheap structural layers that are complete at their scale, and the Relations layer is complete only when its edges are self-explanatory to a consumer who stops there.

The annotation states *why this edge, for this node*, not *what this predicate means in the vocabulary*. Predicate-level definitions live in `CONVENTIONS.md` and in the predicate's own Gloss (when seeded); repeating them in every annotation would produce a boilerplate tax that reduces the Relations layer's signal. The annotation's job is to carry the specific load-bearing reason the target node appears here — the one-to-three-sentence account that makes the edge meaningful to a reader who has not yet traversed it.

Classification predicates in the identity block above the H1 do not usually need annotations. `conforms_to::[[Decision Form Contract]]`, `in_domain::[[Deep Context Architecture]]`, and similar identity edges are classification, not relation — the reader learns what form the node takes and what domain it belongs to without needing a "why this classification matters" explanation. The Relations-section edges are where cross-node meaning accretes; the annotation requirement lives there.

## Alternatives Considered

**Bare edges without annotation.** Let Relations-section edges stand alone: `- grounded_in::[[X]]` without an indented sub-bullet. Rejected because the Relations tier stops being complete at its scale. A reader relying on the tier for cheap traversal has to load either the current node's body or the target node's body to understand why the edge is there — the cost of the traversal moves from the Relations tier to a full-body read. The [[Adopt Layered Node Structure]] commitment is what makes this rejection load-bearing: the tiers must be complete or the commitment fails.

**Prose paragraphs carrying edge context.** Keep edges bare in Relations and put the "why this relationship matters" content in body prose, referencing the edges by inline mention. Rejected because it forces two sources of truth. The edge's reason lives in a paragraph; the edge lives in the Relations section; keeping them aligned as nodes are revised is continuous maintenance work. Every edge added or removed requires finding and updating the corresponding paragraph; every paragraph edit risks leaving an edge orphaned without context. Placing the annotation adjacent to the edge collapses both into one place.

**YAML-encoded annotations.** Encode edges and annotations as structured YAML (`grounded_in: { target: X, annotation: "..." }`). Rejected because it violates the plain-markdown floor. Named-edge predicates MUST NOT live in YAML per [[Restrict YAML to Scalar Metadata]]; moving annotations there would force the predicate to follow, and the graph's semantic spine would move out of the body it is supposed to inhabit.

## What Would Change It

The commitment would be revisited under two conditions.

**Predicate vocabulary grows rich enough that annotations become noise.** If the local vocabulary reached a scale where each predicate's semantics were sharp enough that the "why this edge matters" annotation reduced to boilerplate — where `grounded_in::[[X]]` unambiguously meant one specific thing in the context of this node's form — the annotation requirement would weaken. The current vocabulary is too young for this; the predicates cover broad territory, and the annotations carry real specificity per edge. A future state where form-specific predicates proliferated (each Contract defining its own vocabulary) could produce the relevant sharpness.

**Contributors cannot produce annotations reliably.** If contributors consistently omit annotations or produce them as boilerplate, the commitment has failed at the authoring layer. Remedies would move toward authoring aids — templates, seed scripts, curation passes flagging bare edges — before loosening the commitment. Only if aids cannot hold the discipline would the requirement itself be revisited, and the alternative would have to address reader context some other way.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge convention is what lets edges carry typed predicates and annotations as paired structural tiers. The annotation requirement extends the convention's author-declared-edge principle into the edge-level reader-context layer.

- grounded_in::[[Adopt Layered Node Structure]]
  - The layered-structure commitment requires each layer to be complete at its own scale. Annotations are what make the Relations tier complete — without them, the tier is a machine-readable skeleton that forces every reader to the body tier for context.

- informs_downstream::[[Markdown Node Contract]]
  - Markdown Node Contract's Relations-section Requirement carries the thin enforcement clause pointing at this Decision. The Contract carries the compliance rule; this Decision carries the reasoning and the revisit conditions.
