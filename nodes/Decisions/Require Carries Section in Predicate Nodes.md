---
created: 2026-04-20
tagline: Every Predicate node carries a dedicated Carries section stating the positive sense of the predicate, not derivable from Crescent content alone
brief_summary: A commitment that every Predicate node includes a dedicated Carries section stating what claim the predicate makes when attached as an edge. The inherited Gloss body opening (restate-and-elaborate) does not satisfy this Requirement because the opening is not specifically reserved for the positive sense of the predicate; without a dedicated Carries section, a predicate Gloss could meet all structural Requirements while its only load-bearing content is comparative. The Carries section forces the author to name what the predicate is, so that Crescent content names what it is not against — two complementary moves, each with its own content.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-20
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Require Carries Section in Predicate Nodes

Every Predicate node MUST include a dedicated `## Carries` section that states the positive sense of the predicate — what claim the predicate makes when attached as an edge, what stance it encodes, what web of associations it activates. The Carries section is authored as positive content, not as contrast; comparative content belongs in Crescent.

## Why

A Predicate node without a positive statement of what the predicate carries is a stub that cannot ground downstream nodes' `conforms_to::` and adjacency edges. The capability the Requirement provides is authorial separation between the positive sense (what the predicate claims) and the negative sense (what it distinguishes itself against). Separating the two into distinct body sections makes the predicate's content independently auditable: a reader can read the Carries section and understand what the predicate commits to without reading Crescent, and can read Crescent and understand the adjacencies without the Carries paragraphs being mixed in.

The Carries section is not redundant with the inherited Gloss body opening. The Gloss Form Contract requires the opening sentence to restate the filename definition and elaborate it by one useful clause; that elaboration clause may be positive-sense, contrast, instance, or derivation. A Predicate Gloss whose opening was "the subject does X, as opposed to Y which does Z" would satisfy the Gloss body-opening Requirement while carrying no dedicated positive-sense claim — the reader would have to reconstruct the positive sense from the comparative framing. Requiring a dedicated Carries section prevents this failure mode by pinning the positive claim to a named section the author cannot leave empty.

The separation earns its weight because Crescent content, under convergence pressure, is the content most vulnerable to being read as the predicate's primary definition. An author revisiting a predicate defined only through contrasts with neighbors will be tempted to normalize it into whichever neighbor most resembles it — the predicate has no independent account of itself to fall back on. A Carries section is the independent account; Crescent adds the adjacency work on top.

## Alternatives Considered

**Leave the Gloss body opening as the only positive-sense Requirement.** Rely on the inherited Gloss Form Contract's body-opening rule to carry the positive-sense content. Rejected because the Gloss body opening is restate-and-elaborate without further specification of what the elaboration clause must do; the elaboration clause is permitted to be comparative, an instance, or a one-step derivation. A Predicate node whose body opening restated the filename and elaborated with adjacency content would pass the body-opening Requirement while carrying no positive-sense commitment. The Carries Requirement closes this gap by naming a dedicated section for the positive sense, so the elaboration clause is free to do the body opening's restate-and-elaborate work while Carries carries the load-bearing positive claim.

**Require positive-sense content only when no adjacent predicates exist.** Exempt Predicate nodes that declare `contrasts_with::` edges from the Carries Requirement, on the reasoning that their Crescent sections carry the content. Rejected because the positive sense is load-bearing regardless of adjacency. A predicate with many adjacent neighbors still needs a positive claim about itself; Crescent describes what it is against, Carries describes what it is. Merging the two under "define yourself by contrast" inverts the right structure — the contrasts are secondary to a primary positive claim, not replacements for it.

**Make the Carries section optional, recommended for load-bearing predicates.** Downgrade the MUST to a SHOULD. Rejected because optional-under-time-pressure structural sections disappear. The Convictions this Requirement serves (Vocabulary Diversity Is a Feature and Translation Over Convergence) are strongest when the positive-sense discipline is enforced rather than suggested; a SHOULD would produce predicates whose Carries sections are the first thing cut when the author is in a hurry, and the failure mode the Requirement guards against would return.

## What Would Change It

The commitment would be revisited under one condition.

**The Carries section duplicates the body opening in most cases.** If experience with real Predicate nodes shows that authors write the same content twice — the body opening restates-and-elaborates the positive sense, then the Carries section restates it again in different words — the rule would soften to "Carries MAY be a dedicated section or MAY be carried by the body opening when the opening explicitly names the predicate's positive sense." The current Requirement assumes the separation earns its weight because the body opening is free to do other work (contrast, instance, derivation). If Predicate authors consistently use the body opening to carry the positive sense anyway, the dedicated Carries section becomes the duplicate rather than the load-bearing section, and the rule should adjust.

## Relations

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction the Requirement operationalizes at the predicate layer. A positive-sense Carries section is the structural home for the distinction each predicate encodes. Without it, a predicate defined only by contrast with neighbors carries no independent account of itself, and convergence pressure has no content to resist against.

- grounded_in::[[Adopt Layered Node Structure]]
  - The layered-structure commitment requires each layer to be complete at its scale. A Predicate node's body layer carries two complementary moves — Carries (positive sense) and Crescent (contrast) — each complete at its own scale. This Decision names the positive-sense move's layer as a dedicated section.

- informs_downstream::[[Predicate Form Contract]]
  - Predicate Form Contract's Body-Carries Requirement carries the thin enforcement clause pointing at this Decision.
