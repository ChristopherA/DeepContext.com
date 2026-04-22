- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Firm Commitment

The commitment level carried by a Decision whose reversal would cascade through the graph at cost high enough that the commitment is treated as architectural rather than situational. A Decision carrying `has_commitment::[[Firm Commitment]]` is still formally revisitable — the graph does not have irrevocable commitments — but reversing it would require reworking every node whose shape depends on the commitment. The `## What Would Change It` section names conditions that would warrant that cost; those conditions are typically severe.

Firm Commitments include the Decisions that define the graph's spine: the named-edge convention, the prohibition on `relates_to::`, predicate atomicity, the layered-structure Requirement, the base Markdown Node Contract. Reversing any of them would invalidate the identity predicates on every node, the Relations sections on every node, or the form contracts every node conforms to. The commitment level signals this weight to anyone reading the Decision — Firm means "we have committed to this as infrastructure; don't propose changing it casually."

Firm Commitment is not the same as Canonical curation or Mature lifecycle stage. Commitment is about reversal cost; curation is about content polish; lifecycle is about structural maturity. A Firm-Commitment Decision can be Seed Stage at lifecycle (just written, hasn't been tested through extended use) and Working Draft at curation (cross-references not yet aligned). The axes compose; a Decision can be firm in what it commits to and still be young in the graph.

The two commitment levels — Firm and `[[Provisional Commitment]]` — are the only values `has_commitment::` takes. Items that would carry `has_commitment::[[Open Question]]` are Inquiries, not Decisions, per `Decision Form Contract`.
