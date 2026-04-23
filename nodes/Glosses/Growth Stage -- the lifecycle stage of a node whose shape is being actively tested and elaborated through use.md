- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Growth Stage

The lifecycle stage of a node whose shape has been tested against real use and held -- revisions prompted by the exercise landed on the node's specifics or on adjacent nodes rather than overturning the node's form. A node advances to Growth Stage after at least one real exercise demonstrates the shape works for more than the first case; it remains at Growth Stage while the shape continues to accept elaboration without structural revision.

A Growth-stage node declares `has_lifecycle::[[Growth Stage]]` in its identity block. The declaration carries a sharper signal than Seed -- not merely "authored," but "exercised." An agent or reader encountering a Growth-stage node can treat its claims as more load-bearing than a Seed-stage neighbor's, though still not as settled as a Mature-stage node's would be. The Skill Form Contract advanced to Growth Stage after six conforming skills were drafted and exercised; the Contract held while revisions it prompted landed on adjacent Contracts.

Growth Stage is reached through exercise, not through time. A node that has sat for months with no other nodes testing its shape stays at Seed Stage -- the clock does not advance the lifecycle. The Pattern [[Let the Exercise Audit the Contract]] names the move that produces Growth-stage advancement: draft a conforming instance, run it against real data, and let the exercise either revise the node's shape or confirm it.

Growth Stage is paired with `has_curation::` because the two axes are orthogonal per [[Adopt Predicate Atomicity]]. A Growth-stage node can still be a Working Draft, or already be Curated. Lifecycle tracks structural maturity; curation tracks content polish. Adjacent stages are `[[Seed Stage]]` (newly authored, shape not yet tested) and `[[Mature Stage]]` (shape settled through repeated use).
