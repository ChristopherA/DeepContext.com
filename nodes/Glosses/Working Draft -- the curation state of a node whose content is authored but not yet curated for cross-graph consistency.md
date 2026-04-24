---
tagline: The curation state of a node whose content is authored but not yet curated for cross-graph consistency
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Working Draft

The curation state of a node whose content is authored and coherent on its own terms, but has not yet been curated for cross-graph consistency — its cross-references have not been fully checked, its vocabulary has not been aligned with adjacent nodes through a curation pass, its annotations have not been sharpened against the graph's evolving conventions. A Working Draft is legible and usable; it is not yet curated.

A node declares `has_curation::[[Working Draft]]` in its identity block. The declaration is an honest signal that the content is ready to read but the cross-graph polish is still owed. A reader who finds a claim in a Working Draft and wants to cite it should either perform the cross-check personally or note that the curation state is Working Draft and the claim may need verification against adjacent nodes.

Working Draft pairs with `has_lifecycle::` — lifecycle tracks structural maturity, curation tracks content polish, and the two axes are deliberately split per [[Adopt Predicate Atomicity]]. A node can be Seed Stage Working Draft (newly authored, not yet curated), Growth Stage Working Draft (shape settling but content not yet polished), or Mature Stage Curated (shape settled and polish complete). Each combination says something different about the node's readiness.

The Working Draft state is overwhelmingly the current curation value across this graph. Later curation states — such as `Curated` for a node whose cross-references and vocabulary are aligned, or `Canonical` for a node the project treats as authoritative — are anticipated by the predicate axis but are not yet in active use.
