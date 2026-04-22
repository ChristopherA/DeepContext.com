- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Seed Stage

The lifecycle stage of a node that has been authored but whose structural shape and claims have not yet been tested against other nodes, revised through use, or cited across the graph. Every node enters the graph at Seed Stage and remains there until a later author's work demonstrates that the node's shape has settled and its claims are holding.

A Seed-stage node declares `has_lifecycle::[[Seed Stage]]` in its identity block. The declaration carries an honest signal — the node is authored, the Contract it claims is satisfied, but the reader should not yet treat it as the final word. An agent encountering two nodes on the same topic, one at Seed Stage and one at a later stage, gives retrieval preference to the later one.

Seed Stage is paired with `has_curation::` (its curation-state companion predicate) because the two axes are orthogonal per [[Adopt Predicate Atomicity]]. A node can be Seed-stage (shape not yet settled) while its current content is already a Working Draft, or even further along in curation. Lifecycle is about structural maturity; curation is about content polish.

Adjacent lifecycle stages exist in the graph's anticipated vocabulary — `[[Growth Stage]]` for nodes whose shape is being actively tested and elaborated, and `[[Mature Stage]]` for nodes whose shape has settled through repeated use. Those stages are not yet in widespread use; Seed Stage is what the overwhelming majority of this graph's current nodes carry.
