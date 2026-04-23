---
created: 2026-04-19
tagline: Observations carry has_epistemic_status:: with four values, and each status requires matched grounds in the body
brief_summary: A bundled commitment that Observations are classified by `has_epistemic_status::` into four values — `[[Empirical Observation]]`, `[[Retrospective Observation]]`, `[[On-Faith Observation]]`, `[[Contested Observation]]` — and each value comes with matched body-level grounds requirements. Empirical Observations name the measurement; Retrospective Observations name the record; On-Faith Observations name the source and the promotion path; Contested Observations name the sides and the stakes. The taxonomy and the matched-grounds discipline bundle because they co-specify.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Classify Observations by Epistemic Status With Matched Grounds

Observations carry `has_epistemic_status::[[<Status>]]` in the identity block, with one of four values: `[[Empirical Observation]]`, `[[Retrospective Observation]]`, `[[On-Faith Observation]]`, `[[Contested Observation]]`. Each status brings a matched Grounds requirement in the body. An `[[Empirical Observation]]` names the measurement, experiment, or direct observation that produced the claim. A `[[Retrospective Observation]]` names the record or reconstruction the claim rests on and acknowledges the limits of that record. An `[[On-Faith Observation]]` names the source adopted and the reason for accepting it provisionally, and SHOULD name what it would take to promote the claim to empirical or retrospective status. A `[[Contested Observation]]` names the sides of the contest and why the debate is load-bearing for this graph.

## Why

The commitment grounds **transparency about epistemic trust**. An Observation is a descriptive claim about the world — "X is the case" — and a reader assessing the claim needs to know how much weight to give it. The four-tier taxonomy makes the trust level explicit: empirical claims the author has tested firsthand; retrospective claims resting on historical records; on-faith claims adopted from trusted sources without independent verification; contested claims where the truth is under active debate. A reader filtering for empirical Observations finds the claims grounded in measurement; a reader wanting a broader view includes on-faith and contested claims and treats them with appropriate caution.

The taxonomy and the matched-grounds discipline bundle because they **co-specify**. A status without matched grounds is classification without verification — a claim marked `has_epistemic_status::[[Empirical Observation]]` whose body names no measurement is not actually grounded; the classification would be a tag. Matched grounds without explicit status is verification without classification — a body that names a measurement but does not declare the claim's epistemic tier leaves the reader to infer the tier from body prose. Either half without the other produces a weakened form; together they produce Observations accountable for their grounds.

Each status has **its specific grounds requirement**, matching the kind of grounds that would warrant the status. Empirical grounds name the measurement because "I observed X through experiment Y" is what makes a claim empirical. Retrospective grounds name the record and its limits because a reconstructed record's limits are what distinguish retrospective from empirical. On-faith grounds name the source and the promotion path because the claim is provisionally accepted, and the promotion path is what makes "provisional" accountable. Contested grounds name sides and stakes because the contest is why the claim carries the contested status; without sides and stakes, the status is unsupported.

The four-tier taxonomy is deliberately small. Finer distinctions (subdividing empirical by measurement type, subdividing contested by stakes level) would produce a taxonomy requiring constant value-gloss maintenance. Coarser distinctions (binary verified-vs-unverified) would lose the important middle ground — on-faith observations that rest on trust in a source without independent verification, or contested observations where the debate itself is what matters. Four tiers covers the common epistemic types a seed-stage graph encounters.

## Alternatives Considered

**Prose-only grounds framing.** Let Observations carry epistemic context in body prose without a classification predicate. Rejected because prose-only classification is not filterable. A reader wanting to query "show me empirical claims" or "show me contested claims" cannot do so without body-level parsing that inferential tools do unreliably. The classification predicate makes the epistemic tier a first-class graph property.

**Simpler binary taxonomy (verified / unverified).** Use `has_epistemic_status::[[Verified]]` or `[[Unverified]]`. Rejected because the binary collapses the important on-faith and contested cases. On-faith claims are not "verified" but they are not "unverified" in the sense of "awaiting verification" — they are provisionally accepted without independent verification, which is a distinct epistemic posture. Contested claims are not about whether they are verified; they are about an active debate. The binary loses these specific positions.

**Per-observation prose-justified classification without predicate reservation.** Let authors declare any epistemic descriptor they choose, relying on convention to converge. Rejected because it defeats form-specific reservation — different authors would use different terms, and graph-level queries would fragment. The four-value enumeration is what makes the predicate vocabulary tight across authors.

**Matched grounds as guideline, not requirement.** Keep the classification but let body grounds be author-discretionary. Rejected because classification-without-verification produces tags. A claim marked `has_epistemic_status::[[Empirical Observation]]` must be accountable to what makes it empirical; the matched-grounds requirement is the accountability.

## What Would Change It

The commitment bundles the taxonomy and the matched-grounds discipline; the revisit conditions converge.

**Four-tier taxonomy proves too coarse or too fine.** If the project's Observations cluster in ways the four tiers miss — persistent sub-clusters within empirical that want distinction, or frequent borderline cases between on-faith and contested that need a fifth tier — the taxonomy would refine. The revisit would likely add values rather than restructure, preserving the matched-grounds discipline with the new values' grounds requirements.

**Matched-grounds discipline proves too rigid for mixed-type claims.** If Observations arise whose grounds genuinely span tiers (a claim partially empirical, partially retrospective, partially contested), the matched-grounds rule would require the author to pick one tier and under-specify. The revisit would soften the rule to allow mixed grounds with explicit tier-per-claim accounting. Current Observations (the Contract Form Contract seeded the form; no Observations have been written yet) haven't tested this; the condition is latent.

## Relations

- grounded_in::[[Reserve Predicate Vocabularies to Specific Forms]]
  - The form-specific reservation commitment places `has_epistemic_status::` on Observations only. This commitment establishes the taxonomy the reservation protects — what values the Observation-only predicate takes, and what each demands of the body.

- grounded_in::[[Adopt Predicate Atomicity]]
  - `has_epistemic_status::` answers one question: what epistemic tier grounds this claim? The atomicity commitment ensures the predicate stays sharp; this commitment specifies the values and their matched requirements.

- informs_downstream::[[Observation Form Contract]]
  - Observation Form Contract's identity predicate and Body-Grounds Requirements carry the thin enforcement clauses pointing at this Decision.
