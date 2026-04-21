---
created: 2026-04-19
tagline: Convictions carry both a what-it-asks section and a drift-recognition section — the pair makes the stance accountable
brief_summary: A bundled commitment covering two body sections that together distinguish a Conviction from a silently-held belief. What-It-Asks names the observable commitments, mechanisms, boundaries, or practices that follow from taking the stance seriously. Drift Recognition names how a reader would notice the stance weakening without being explicitly revoked — cumulative and cultural rather than pointwise and structural. The two sections bundle because each is incomplete without the other: what-it-asks without drift recognition has no maintenance accountability; drift recognition without what-it-asks has nothing concrete to recognize drift against.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Require What-It-Asks and Drift Recognition in Convictions

Every Conviction body contains two paired sections that together make the stance accountable. The **what-it-asks** content describes what taking the stance seriously asks of the project — the observable commitments, mechanisms, boundaries, or practices that follow when contributors hold the conviction. The **drift recognition** content describes how a reader or contributor would notice the stance weakening without being explicitly revoked — cumulative and cultural practices, outputs, or omissions that would signal drift. Both are required; neither alone is sufficient.

## Why

The commitment **distinguishes a Conviction from a silently-held belief**. A belief may be held without showing up in what the project does; a Conviction is a stance that actively shapes practice and whose maintenance is observable. The two sections express that distinction from opposite sides: what-it-asks says "here is what holding the stance does"; drift recognition says "here is what losing the stance would look like." Together they make the stance accountable both at the action layer (the project takes these moves) and at the maintenance layer (the project notices when the moves stop happening).

The two sections bundle because **each is incomplete without the other**. What-it-asks without drift recognition describes what the stance motivates but leaves no mechanism for noticing when motivation has faded; the Conviction becomes a list of commendable practices without a way to detect their erosion. Drift recognition without what-it-asks names signals of drift without anchoring them to concrete practice; the Conviction's drift becomes unverifiable because the baseline it drifts from is unnamed. Both sections reinforce each other: what-it-asks supplies the concrete content that drift recognition watches for; drift recognition supplies the maintenance accountability that makes what-it-asks more than aspirational.

The two sections operate at **different scales of observation**, and that difference is load-bearing. What-it-asks content is specific-and-actionable — "the project maintains human authorship on all published nodes." Drift recognition is cumulative-and-cultural — "over time, the project's content begins leaning toward ambiguity between human and AI authorship." A Contract Requirement is violated when its structural MUST rule fails at a specific point; a Conviction drifts when contributors stop acting as though the stance were held, even without any single structural rule being broken. The two sections cover both scales; either alone would cover only one.

The what-it-asks content MAY be partitioned by level of application (session-level, architectural, knowledge-level) when a conviction's consequences span scales; partitioning should emerge from the conviction's own shape, not be imposed. Drift recognition MAY appear as a closing paragraph of the what-it-asks section or as its own brief section. Both MUST be concrete: specific asks that can be checked against practice; observable drift signals that a reviewer can assess against actual content.

## Alternatives Considered

**Permit pure values statements.** Let Convictions record a stance without either section. Rejected because values-only Convictions are silently-held beliefs in form — the project holds them without showing up in behavior or in maintenance accountability. The Conviction form's whole contribution is the active shaping of practice and its visibility.

**Require only what-it-asks.** Keep the observable-commitments rule but let drift recognition be author-discretionary. Rejected because optional-at-discretion drift recognition is absent under time pressure. The Conviction then has no maintenance accountability — the project can drift without the form noticing. The asymmetric rule (strict on one side, loose on the other) would admit Convictions whose maintenance is invisible.

**Require only drift recognition.** Keep the drift signals but let what-it-asks be implicit. Rejected because drift recognition has no concrete anchor without named asks. "The stance has drifted when things feel different" is the degenerate form; avoiding it requires what-it-asks to supply the observable baseline drift is measured against.

**Treat drift recognition as the Conviction's violation condition, parallel to Contract Requirements.** Rejected because a Conviction does not violate pointwise; its drift is cumulative and cultural. A Contract Requirement is violated when a specific file fails a specific MUST rule; a Conviction drifts when the project's content, over time, stops reflecting the stance. The recognition is a different kind of signal, and conflating it with Requirement violation semantics would lose the kind of accountability the Conviction form targets.

## What Would Change It

The commitment bundles two sections; the revisit conditions converge.

**Convictions prove so abstract that deriving observable asks feels forced.** If the project accumulates Convictions whose honest asks are at the values-only level — where the stance shapes thinking but does not translate into observable practice at current scale — the rule would produce Convictions with placeholder asks. The revisit would soften the rule to "what-it-asks SHOULD be observable when the stance's consequences are observable at current scale; a Conviction at a scale that has not yet surfaced observable asks MAY note the scale issue explicitly." Drift recognition would follow the same softening, since unmeasurable asks produce unmeasurable drift.

**Drift proves unmeasurable or too subjective at any level of concreteness.** If the honest answer to "how would we know if we are losing this?" has no observable form even after serious effort, the rule would force authors to produce drift content that is either vague or fabricated. The revisit would allow explicit acknowledgment of unmeasurability rather than forcing content; the what-it-asks side would remain as the primary accountability.

## Relations

- grounded_in::[[Adopt Layered Node Structure]]
  - The layered-structure commitment requires each layer to be complete at its scale. The what-it-asks and drift-recognition sections are part of the Conviction's elaboration tier — the stance is the claim tier, and these two sections together complete the elaboration. Both tiers must be complete.

- informs::[[Conviction Form Contract]]
  - Conviction Form Contract's Body-what-it-asks and Body-drift-recognition Requirements carry the thin enforcement clauses pointing at this Decision.
