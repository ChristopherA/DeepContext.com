---
created: 2026-04-19
tagline: Patterns open with a two-or-three-sentence Heart that stands alone as the Pattern at card scale
brief_summary: A commitment that every Pattern body opens with a `## Heart` section of two to three prose sentences that stands alone as the Pattern at card scale. A reader holding only the name and the Heart gets the Pattern — what moment it addresses, what move to make, why the move works. The Heart is not a summary of the longer body; it is the Pattern compressed to the card-scale claim tier. Everything that follows elaborates what the Heart already said.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Require Heart Section at Pattern Card Scale

Every Pattern body opens with a `## Heart` section of two to three prose sentences. The Heart stands alone as the Pattern at card scale — a reader holding only the name and the Heart gets the pattern, complete at that tier. The Heart names the moment the Pattern addresses, the move to make, and why the move works. The sentences are not a summary of the longer Pattern body; they ARE the Pattern, compressed to card scale.

## Why

The commitment imports the **Group Works deck convention** — the card text IS the pattern. The Group Works deck (and the larger Alexandrian tradition it extends) established that a pattern's card-scale expression must be complete at its scale: a facilitator holding only the card can run the pattern, a practitioner scanning the deck can recognize which cards apply to their situation, and a library reader can absorb patterns without committing to the full body reading cost. The card scale is load-bearing for pattern discovery and use; the Heart section is what brings that property into the prototype's specific form.

The Heart completes the Pattern at card scale in the same sense [[Adopt Layered Node Structure]] requires every layer to be complete at its own scale. A reader who stops at the Heart has the Pattern — not a teaser for the body, not a summary, but the Pattern itself. A teaser would force every reader who wanted the Pattern to read the body; a summary would produce two statements of the Pattern that could drift apart. The Heart's sentences are designed to carry the Pattern's whole claim in the space the card-scale tier admits; the body that follows elaborates (Problem, Forces, Solution, Consequences, Instances) but does not re-state.

The two-to-three-sentence specification targets the Pattern's compressible essence. A Pattern with a genuine Heart fits in two or three sentences; a Pattern that strains toward five or six sentences at the card scale is usually two patterns sharing a body or a Pattern whose forces have not yet been sharpened to their core tension. The tight sentence budget is itself a diagnostic — if the Heart cannot be written in three sentences, the Pattern has not yet been named clearly enough. Card-scale tightness is part of the pattern-discovery practice, not a formatting rule.

The Heart carries the *moment*, the *move*, and *why the move works*. Each of those is part of the Pattern at card scale. The moment names the recurring situation a practitioner recognizes ("when a predicate carries multiple axes"); the move names what to do ("split into a predicate family"); the why names the change the move produces ("queries regain sharpness"). All three fit in two or three sentences when the Pattern is clearly named; forcing them to fit is how the Heart refines the Pattern's expression over time.

## Alternatives Considered

**Summary-after-body.** Open the Pattern with Problem and Forces; put a `## Summary` section at the end. Rejected because the summary-after pattern forces every reader to the body before encountering the card-scale claim. The card-scale tier disappears — the body is the primary expression, and the summary becomes a brief recap. The Heart's whole point is that it precedes the elaboration and stands independent of it.

**Problem-forces-solution without a card layer.** Let Patterns go straight into Alexandrian body structure (Problem, Forces, Solution, Consequences) without a Heart section. Rejected because the Problem-Forces-Solution structure requires the reader to traverse three sub-sections to reach the move — a reader scanning the Pattern for applicability pays body-level cost before knowing what the Pattern actually says to do. The Heart is the single-section preview that makes the body readable as elaboration.

**Embed the card-scale claim in the opening prose without a dedicated section.** Let the Pattern open with two or three prose sentences immediately after the H1, without the `## Heart` heading. Rejected because the dedicated heading is what lets the card-scale tier be extractable. A build tool or reader preview wanting to present just the Pattern's card uses the `## Heart` section boundary; unmarked opening prose is not reliably extractable without body parsing. The convention is to mark the tier explicitly so it is usable as a tier.

## What Would Change It

The commitment would be revisited under one condition.

**Card-scale portability proves less valuable than tight body integration.** If Patterns become primarily consumed through full-body reading — where the card-scale preview is rarely used in practice and the Heart becomes a formalism the author writes but no reader reads — the tier would be carrying authoring cost without reader benefit. The revisit would weaken the rule to "Patterns SHOULD have a Heart when card-scale use is anticipated; Patterns MAY integrate the card-scale claim into opening prose when the Pattern is body-heavy." Current Patterns' Hearts have been read independent of bodies (cited, previewed, referenced in conversation); the tier is carrying its weight.

## Relations

- grounded_in::[[Adopt Layered Node Structure]]
  - The layered-structure commitment requires each layer to be complete at its scale. The Heart is the claim-layer complement to Patterns' elaboration-tier body; both are required for the Pattern's layered structure to hold.

- grounded_in::[[A Pattern Language (Christopher Alexander et al., 1977)]]
  - The Alexandrian tradition, via the Group Works deck and its descendants, supplies the card-IS-the-pattern convention: each pattern is legible at card scale through its Heart alone; further sections serve elaboration, not completion. The `## Heart` section is this graph's specific realization of that convention.

- informs::[[Pattern Form Contract]]
  - Pattern Form Contract's Body-Heart Requirement carries the thin enforcement clause pointing at this Decision.
