---
tagline: A node that lives in another graph, referenced without being imported
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# External Node

A node that lives in another graph (another DeepContext repository, another Obsidian vault, another wiki) and is referenced from this graph without being imported. An External Node is addressable as content from outside the current graph's authority — this graph names it, links to it, and may annotate what it carries, but does not claim ownership of its evolution, its vocabulary, or its curation.

Two reference forms express an External Node in this graph. The `↗` external marker on a wikilink — `[[Target Name]]↗` — names the target as external without committing to a specific address; the marker is a styling cue rather than a resolution hook. A [[Scion Address]] as a DID href or as the `title` attribute on an HTML link names the target by canonical content-addressable identifier. The two forms compose rather than compete: a reference can carry `[[Target]]↗` in prose for readability and record a Scion Address in the link's `title` attribute for canonicity, so readers today see a working external marker and future DID resolvers have an unambiguous target.

An External Node is distinct from a [[Ghost Link]]. A Ghost Link names a concept the current graph has not yet seeded but intends to own — the target is a to-write note on the current graph's list. An External Node names a concept the current graph does not intend to own because it belongs to another graph; the target is acknowledged-but-not-owned. The distinction matters for curation: ghosts feed this graph's authoring backlog, External Nodes feed this graph's reference surface. A ghost may mature into a seeded node of this graph; an External Node typically does not.

## Relations

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes external references first-class rather than to-be-normalized. External Nodes let this graph point at other graphs' vocabulary without absorbing it; the diversity stance is operationalized at the cross-graph reference boundary by keeping external targets external rather than pulling them into this graph's ownership.

- composes_with::[[Scion Address]]
  - The address form that names an External Node by content-addressable DID. A reference to an External Node may carry a Scion Address as its canonical identifier, either as a `did:repo:...` href or as the `title` attribute on a reference-style markdown link whose `href` is the node's current HTTP URL.

- contrasts_with::[[Ghost Link]]
  - A Ghost Link is this graph's to-write list; an External Node is another graph's content this graph acknowledges but does not own. Both are unseeded-in-this-graph but for opposite reasons — the ghost waits to become a node here, the External Node is deliberately kept elsewhere.
