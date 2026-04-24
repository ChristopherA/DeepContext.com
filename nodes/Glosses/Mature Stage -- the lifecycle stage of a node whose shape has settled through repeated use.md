---
tagline: The lifecycle stage of a node whose shape has settled through repeated use
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Mature Stage

The lifecycle stage of a node whose shape has settled through repeated use -- multiple exercises across independent cases have surfaced no structural revisions, and the node is cited and composed with across the graph without strain. Mature Stage is the anticipated final lifecycle value; a node that reaches it has earned the right to be treated as foundational for the work that cites it.

A Mature-stage node declares `has_lifecycle::[[Mature Stage]]` in its identity block. The declaration says the shape is trusted: an agent can cite the node without hedging about provisionality, and other authors can model new nodes on its form. Mature-stage nodes still carry `has_curation::` state because content polish continues to evolve independently of structural maturity -- a Mature-stage node's body can be revised, elaborated, or retrenched without disturbing its lifecycle marking.

No node in this graph currently carries `has_lifecycle::[[Mature Stage]]`. The value exists in the vocabulary as the anticipated end state; advancement to Mature requires a pattern of sustained use the graph is too young to have demonstrated. The bar is deliberately high -- treating a node as Mature before its shape has actually held through repeated use would weaken the lifecycle predicate's signal for every other node that carries it.

Mature Stage is paired with `has_curation::` per [[Adopt Predicate Atomicity]]. Adjacent stages are `[[Seed Stage]]` (newly authored, shape not yet tested) and `[[Growth Stage]]` (shape has held through at least one real exercise). A Mature-stage marking is reversible in principle -- if a later exercise surfaces a structural gap the node did not anticipate, the node can be revised and its lifecycle rolled back to Growth -- but such reversions should be rare, because the Mature marking's value depends on not being given out prematurely.
