---
created: 2026-04-19
tagline: A specification a node conforms to — the mechanism by which node shapes are named, checkable, and pluralizable
brief_summary: A Form Contract is a Markdown Node whose purpose is to specify the structural obligations other nodes take on when they declare `conforms_to::[[X Form Contract]]`. Each Form Contract carries a parseable `## Requirements` section written with RFC 2119 keywords, an inheritance declaration via `extends_contract::` when it specializes a parent contract, and self-conformance to [[Contract Form Contract]]. Conformance rather than identity is the classification move — a node can conform to multiple Form Contracts from different traditions, and conformance stays revisable as the graph's understanding of a form evolves.
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Form Contract

A specification nodes conform to by declaring `conforms_to::[[X Form Contract]]` in their identity predicate block. A Form Contract names a node shape ([[Gloss Form Contract]], [[Decision Form Contract]], [[Reference Form Contract]]) and makes the shape's requirements explicit enough that a validator — a build-time script, a curation-time agent, or a human reviewer — can check a candidate node against them. The requirements use RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY) so the obligation level of each clause is unambiguous.

Form Contracts form a shallow inheritance tree. [[Markdown Node Contract]] is the root: every node conforms to it, and it specifies file-form basics every other contract assumes. A specializing contract declares `extends_contract::[[Parent Contract]]` and adds requirements on top of the parent's without silently overriding them. A conforming node satisfies the parent's requirements and the child's requirements. Contracts themselves are Markdown Nodes, and every Contract declares `conforms_to::[[Contract Form Contract]]` — the meta-contract — which makes the Contract form self-describing.

The reason for conformance rather than identity (`is_a::[[X]]`) is pluralism. A single node may conform to multiple Form Contracts when its role bridges forms — a case-study-shaped decision, a gloss that also functions as a reference stub. Conformance is additive; identity is exclusive. Conformance is revisable when the contract evolves; identity becomes entangled with the node's meaning. The graph accommodates the first; the second forces premature commitment every time a form's definition shifts.

## Relations

- grounded_in::[[Contract Form Contract]]
  - Contract Form Contract is the meta-specification for what Form Contracts look like — parseable Requirements section, self-conformance, inheritance declaration, filename ending in `Contract`. Every Form Contract conforms to it, including itself.

- grounded_in::[[Markdown Node Contract]]
  - Markdown Node Contract is the file-form substrate every Form Contract extends. The base requirements (filename rules, identity block, Relations section, named-edge syntax) apply to Form Contracts the same way they apply to any other node.

- informed_by::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The gist specifies `conforms_to::[[X Form Contract]]` over `is_a::[[X]]` as the classification move. Form Contract as a concept is the local elaboration of that move into named node shapes with checkable requirements.
