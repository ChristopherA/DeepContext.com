- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Provisional Commitment

The commitment level carried by a Decision that has been made but is explicitly revisitable — the project has chosen an answer, is operating under that choice, and has named the conditions under which the choice would be reopened. A Decision carrying `has_commitment::[[Provisional Commitment]]` is not tentative in the sense of undecided; it is decided, but with an acknowledged revisit surface.

The distinction between Provisional and Firm Commitment is about reversal cost rather than current confidence. A Provisional Commitment can change without cascading cost across the rest of the graph; a Firm Commitment cannot. A Decision that reorganizes folder structure, adopts a new filename pattern for a single form, or introduces a workflow step can often be Provisional — changing it requires editing the affected nodes but does not invalidate the surrounding architecture. A Decision that sets the graph's spine (wikilinks-and-named-edges, predicate atomicity, the base Markdown Node Contract) cannot be Provisional because reversing it would cascade through every node in the graph.

Each Decision's `## What Would Change It` section names the specific conditions under which the commitment would be revisited. For Provisional Commitments, those conditions are usually reachable — measurable drift, adoption friction, tooling evolution. The body section is where the reversibility is documented; the `has_commitment::[[Provisional Commitment]]` identity predicate is where the reversibility is signaled at the identity layer so agents and readers can orient to the Decision's durability before reading its body.
