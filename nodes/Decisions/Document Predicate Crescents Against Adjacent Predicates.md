---
created: 2026-04-20
tagline: Each Predicate node documents a Crescent subsection per adjacent predicate, stating what this predicate holds that the neighbor does not
brief_summary: A commitment that every Predicate node declaring a `contrasts_with::` edge documents the distinction in a dedicated Crescent subsection headed `### Against [[adjacent predicate]]`. The per-neighbor structure keeps each distinction separately auditable rather than generalizing across them. The Crescent on two adjacent predicates is asymmetric by design — each node carries its own account of what it holds that its neighbor does not, and the two accounts together are the full pairing. An undocumented crescent is a silent invitation to merge predicates under later convergence pressure, which is the specific failure mode the Convictions Vocabulary Diversity Is a Feature and Translation Over Convergence name.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-20
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Document Predicate Crescents Against Adjacent Predicates

Every Predicate node that declares one or more `contrasts_with::` edges MUST include a `## Crescent` section containing one H3 subsection per adjacent predicate, headed `### Against [[adjacent predicate]]`. Each Crescent subsection states what this predicate holds that the adjacent one does not — the distinction that would be destroyed by merging them. The Crescent content on two adjacent Predicate nodes is not required to be symmetric; each node carries its own account of its stance against the neighbor.

## Why

Vocabulary Diversity Is a Feature holds that adjacent predicates' distinctions are load-bearing; Translation Over Convergence holds that convergence pressure is a drift signal. Undocumented crescents between adjacent predicates are the specific failure mode those Convictions name. When the distinction between `critiques::` and `challenges::` lives only in the shared understanding of the contributors who use both, it is one review cycle away from being collapsed into a normalized predicate; when the distinction lives in a structural section that every Predicate node carries, the merge move requires overriding an explicit account of what the distinction holds.

The per-neighbor structure is what makes each distinction separately auditable. A Predicate with four adjacent neighbors carries four distinctions; a single global paragraph listing all four would force the author to generalize across distinctions that may not compose. The generalization move is itself a convergence pressure — it subtly unifies the distinctions under a single framing — and separately-headed subsections resist the pressure by keeping each distinction in its own space. A reader checking whether `critiques::` still distinguishes itself from `challenges::` reads the `### Against [[challenges]]` subsection specifically, not a global paragraph that has diffused the `critiques`-vs-`challenges` content across several other comparisons.

Asymmetric Crescents are the honest structure. `critiques::`'s Crescent against `challenges::` names what `critiques` holds; `challenges::`'s Crescent against `critiques` names what `challenges` holds. The two accounts are independently authored and may differ in emphasis — one predicate's stance against the neighbor does not automatically yield the reverse stance. Requiring symmetric Crescents (the same content mirrored on both nodes) would either produce copy-paste that decays when one side is edited, or force the author to artificially flatten two independent accounts into one shared statement. Asymmetric authoring is what the distinctions earn.

## Alternatives Considered

**Optional Crescent sections per neighbor.** Let authors decide whether to document each adjacency or leave the `contrasts_with::` edge standing without explanation. Rejected because optional-under-time-pressure Crescent content disappears. The Convictions this Requirement serves are strongest when the distinction-naming discipline is enforced rather than suggested — an optional Crescent section is the first thing cut when the author is in a hurry, and the Requirement's purpose (making the distinction structurally visible) fails at exactly the moment when convergence pressure is strongest.

**One global Crescent paragraph listing all neighbors.** Replace the per-neighbor H3 subsections with a single Crescent paragraph that mentions every adjacent predicate in sequence. Rejected because a single paragraph loses the per-neighbor structure that makes each distinction separately auditable. A predicate with four neighbors has four distinctions; collapsing them into one paragraph forces generalization across distinctions that may not compose, and the reader checking a specific adjacency has to parse the whole paragraph rather than reading the named subsection. The paragraph form is also easier to soften under convergence pressure — editing one paragraph that blends four distinctions invites compressing the distinctions, while editing four H3 subsections preserves their separateness.

**Symmetric Crescents required on both nodes.** Require that the Crescent on Predicate A against Predicate B be mirrored on Predicate B against Predicate A, with the same content inverted. Rejected because symmetric Crescents can fall into wrote-once-copied-twice — the authored content on one side is copied to the other, and edits to one side do not propagate. Asymmetric Crescents (each predicate's node states what *it* holds against the neighbor) are the honest structure because each node's account is its own. The `critiques::` node's stance against `challenges::` is not automatically the inverse of the `challenges::` node's stance against `critiques::`; each predicate has its own voice, and the two accounts together are the full pairing.

**Apply the rule only to Predicate nodes with three or more neighbors.** Require per-neighbor Crescent subsections only when a predicate has enough neighbors for the global-paragraph failure mode to matter; allow single-adjacency Predicates to use a single Crescent paragraph. Rejected because the per-neighbor discipline is also what the single-adjacency case benefits from — the H3 heading is the cue that tells the author the distinction is load-bearing and that tells the reader where to look. A one-neighbor Predicate with a single Crescent paragraph invites later authors adding a second neighbor to append a second paragraph to the same section rather than adding an H3 — starting with the wrong structure. Uniform H3 structure from the start avoids the migration problem.

## What Would Change It

The commitment would be revisited under one condition.

**A majority of seeded Predicates have no adjacent neighbors.** If the graph accumulates Predicate nodes and a majority carry no `contrasts_with::` edges, the Requirement's load-bearing premise weakens — the enforcement is for a case that does not occur. The revisit would either soften the rule to a SHOULD (Crescent sections are still required when adjacencies exist but no rule needs to be stated for the case that doesn't arise) or reconsider whether the distinctions predicates draw are as adjacency-dependent as the Convictions assumed. Current evidence from the eleven-Predicate seeding set is that adjacencies exist in at least three semantic clusters (classification, provenance hierarchy, relational adjacency), which is the load-bearing confirmation the Requirement needs.

## Relations

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction this Requirement directly operationalizes at the predicate layer. The Conviction names adjacent vocabularies' distinctions as load-bearing; this Requirement is the structural enforcement that makes each distinction survive.

- grounded_in::[[Translation Over Convergence]]
  - The Conviction whose operational rule this Requirement encodes at the predicate layer. Translation between adjacent predicates requires each predicate's distinctive claim to be documented; per-neighbor Crescent subsections are the documentation.

- informs::[[Predicate Form Contract]]
  - Predicate Form Contract's Body-Crescent Requirement carries the thin enforcement clause pointing at this Decision.
