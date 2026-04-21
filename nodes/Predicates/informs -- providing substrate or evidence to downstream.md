- conforms_to::[[Predicate Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# informs

A predicate declaring that the subject provides substrate, evidence, or influence to the object — the forward edge on the substrate side of a relationship whose dependent-side edge is `grounded_in::` or `informed_by::`. The subject is what the object draws on; the edge makes the subject's downstream role visible from the subject's own node.

The edge lands in Relations on nodes that have downstream work — a Reference that informs multiple Decisions, a Decision that informs a Contract's Requirements, a Conviction that informs specialized Convictions. Authors choose whether to document the relationship from the substrate side (`informs::`) or the dependent side (`grounded_in::` / `informed_by::`); both sides documenting is common and preserves the bidirectional visibility.

## Carries

The predicate names a substrate-to-dependent direction. The subject is the providing side; the object is the drawing side. When a Decision writes `informs::[[X Contract]]`, the Decision declares that the Contract's Requirement carries the thin enforcement clause pointing back at it — the reader standing at the Decision can trace forward to where the Decision is cashed out. When a Reference writes `informs::[[Y Conviction]]`, the Reference declares its downstream role in the Conviction's argumentative substrate.

The web of associations the predicate activates is the forward side of provenance — from source to use, from commitment to enforcement, from substrate to specialization. The predicate is the graph's way of making a node's downstream presence visible without requiring a reader to crawl backwards from every potential dependent. Navigability improves when both directions carry edges; traversal is symmetric rather than one-sided.

## Crescent

### Against [[grounded_in -- normative or structural foundation]]

`grounded_in::` is the dependent-side edge for structural dependence; `informs::` is the substrate-side edge. They describe the same relationship from opposite ends — a Contract's Requirement `grounded_in::` a Decision and the Decision `informs::` the Contract are two edges on the same relation, each documented on the respective node. The distinction between the two predicates is direction and location, not substance: one is written on the dependent, the other on the substrate. Authors document both when navigability from either direction is useful; they document only one when the direction-asymmetry is acceptable.

### Against [[informed_by -- weaker influence than grounded_in]]

`informed_by::` is the dependent-side edge for weaker influence; `informs::` is the substrate-side edge that can carry either the weaker or stronger kind of relationship. When the author writes `informs::[[Y]]` on a source node, the downstream node's own declaration (`grounded_in::` or `informed_by::`) carries the weight distinction — `informs::` does not specify whether the downstream draws on this node as substrate or as influence. This is a deliberate asymmetry: the dependent side owns the weight claim because the dependent is what would or would not continue to stand without the substrate.

## Typing

- **Subject:** Any node that has downstream presence in the graph.
- **Object:** Any node that draws on the subject as substrate or influence. The object MUST carry a corresponding `grounded_in::` or `informed_by::` edge back to the subject for the relation to be mutually visible; partial visibility (only `informs::` on the subject) is permitted but weaker.

## Instances

- `prototype/nodes/Decisions/Require Body Elaboration Beyond Filename Definition.md` carries `informs::[[Gloss Form Contract]]` — the Decision declares that Gloss Form Contract's Body-shape Requirement carries the thin enforcement clause pointing at this Decision. The corresponding `grounded_in::` edge is on Gloss Form Contract itself.
- `prototype/nodes/Decisions/Require Carries Section in Predicate Nodes.md` carries `informs::[[Predicate Form Contract]]` — the Decision seeded in this plan declares its downstream role in Predicate Form Contract's Body-Carries Requirement.

## Relations

- contrasts_with::[[grounded_in -- normative or structural foundation]]
  - Same relation, opposite direction: `grounded_in::` on the dependent side, `informs::` on the substrate side. The predicate pair carries a bidirectional edge split into two one-sided declarations.

- contrasts_with::[[informed_by -- weaker influence than grounded_in]]
  - Same relation, opposite direction (with the weight distinction owned by the dependent side). `informed_by::` on the dependent side, `informs::` on the substrate side. The substrate-side predicate does not specify the weight; the dependent side does.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes authoring bidirectional provenance edges load-bearing. Leaving the substrate-side visible on its own node (rather than requiring dependents to declare their own draws) preserves navigability that an extraction agent could otherwise flatten.
