---
created: 2026-04-19
tagline: A node is arranged in layers of differing cost to read, each layer complete at its own scale
brief_summary: A commitment that every node is structured in tiers a consumer can deliberately stop at — a cheap structural identity block that orients, a card-scale claim complete at its scale, elaboration prose for consumers who have committed to the deeper read, and a structured Relations layer that is traversable without re-reading the body. The commitment answers the universal constraint of finite context — a human reader's minute of attention, an agent's token budget, a query's traversal cost — by letting each consumer choose the layer their need can afford without paying the cost of the deepest tier.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Adopt Layered Node Structure

A node is arranged in layers that differ in their cost to read, and each layer is complete at its own scale. The minimum layering is an identity predicate block above the H1 (cheap, structural, machine-readable), an opening claim at card scale, an elaboration body carrying reasoning and instances, and a Relations section listing graph neighbors (cheap, structural, machine-readable). Specific form contracts may extend or refine the shape; none may collapse it below the minimum. The commitment is to a node whose consumer can stop at any layer and have what that layer's scale claims to carry — not a teaser forcing them deeper.

## Why

The commitment answers **finite context as the universal constraint**. Human readers arrive with a minute, not an hour; agents operate under literal token budgets; graph queries filter under traversal-cost limits. The common shape across all three consumers is identical: each has limited room and needs to know, cheaply, whether a node is worth the deeper cost. A node without structural layering forces every consumer to the full cost of the deepest tier regardless of what their task actually requires — skim-to-classify burns the same tokens as read-to-reason.

Layered structure answers that constraint by letting each consumer choose where to stop. Classification predicates above the H1 orient the reader to the node's form, domain, and maturity before any prose is read — an agent deciding whether to load a node's body reads the identity block first. The opening claim (the H1 and its paragraph, or a `## Heart` section) states the node's commitment or move at card scale — complete in a handful of sentences, not a teaser for deeper prose. Elaboration follows for consumers who have committed to the deeper cost. A structural Relations layer exposes graph neighbors without re-reading the body — a consumer traversing the graph should not have to parse body prose to find outgoing edges.

Completeness at each layer is what makes the layering usable. A consumer who stops at the claim layer has the claim itself — not a promise of the claim, not a summary-of-a-summary, but the claim complete at its scale. A consumer who reads only the cheap structural layer can filter authoritatively — the data is the data, not preview text. Each layer is designed to stand alone; none is a teaser for a deeper tier. The authoring move that composes a node through these tiers in the prototype's specific vocabulary is [[Progressive Summary Before Substance]].

The cheapest structural layer appears before the expensive prose. Inverting the ordering defeats the cost gradient the layering exists to serve — a consumer paying the cost of the elaboration tier before seeing the identity tier cannot benefit from the early stop the cheap layer was designed to permit. The identity block above the H1 is a deliberate violation of Markdown's usual "H1 first" pattern for exactly this reason.

## Alternatives Considered

**Unstructured prose with tooling-extracted structure.** Let authors write nodes as flowing prose and rely on an agent or curator to extract identity, claim, and relations from the body at read time. Rejected because tooling-extracted structure violates the author-declared property of the wikilinks-and-named-edges commitment. An extractor decides which sentence is the claim, which predicates are identity, which mentions are relations — decisions the author never made explicit. The graph becomes a record of what the extractor inferred rather than what the author intended, and the plain-markdown floor dissolves.

**Single-layer prose nodes.** Let every node be a single block of prose without structural tiers. Rejected because it forces every consumer to the same cost regardless of task. A reader classifying a node pays the same cost as a reader reasoning about it; an agent deciding whether to load a node pays the full load cost before the decision. The layering exists specifically to break that equivalence.

**Teaser-style claim layers.** Let the opening be a preview pointing at the body rather than a complete claim at card scale. Rejected because teasers force every consumer committed to the claim tier's cost into the body tier anyway. The cost gradient the layering promises is lost; the reader who needed the claim ends up paying body cost to extract it. Completeness at each layer is non-negotiable — a teaser is a failure of the tier.

## What Would Change It

The commitment would be revisited under conditions that no longer hold.

**Finite context stops being the binding constraint.** If reader attention, agent token budget, and query traversal cost all became effectively unbounded — if context windows grew large enough that loading every node in full became free for every consumer — the layering's central purpose would weaken. No plausible candidate exists: agent token budgets are growing but not outpacing graph growth; human attention is the slowest-moving constraint in the system. The commitment is firm because the constraint that motivates it is the firmest thing in the environment.

**A layered structure becomes un-authorable at scale.** If contributors consistently cannot produce layers complete at their own scale — if teaser claim layers dominate or identity blocks decay into partial data — the authoring discipline has failed. The failure is at the authoring layer, not the structural one; remedies would move toward authoring aids (templates, seed scripts, curation passes) before loosening the commitment. Only if aids cannot hold the discipline would the layered commitment itself be revisited, and the alternative would have to address finite context some other way.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge infrastructure is what lets the cheap structural layers (identity block, Relations section) be machine-traversable. Without author-declared predicate edges, those tiers would collapse into prose with no tier distinction left — classification and relation would become inferential rather than structural.

- informs::[[Markdown Node Contract]]
  - Markdown Node Contract's layered-structure Requirement is the thin enforcement clause pointing at this Decision. The Contract carries the compliance rule; this Decision carries the reasoning and the revisit conditions.

- informs::[[Progressive Summary Before Substance]]
  - The Pattern that realizes this commitment in the prototype's specific vocabulary — identity predicates above the H1, card-scale opening or `## Heart`, elaboration body, and Relations. This Decision states the standing commitment; the Pattern names the authoring move an author makes composing a node in practice.
