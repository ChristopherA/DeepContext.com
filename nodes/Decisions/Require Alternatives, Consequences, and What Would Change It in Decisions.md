---
created: 2026-04-19
tagline: Decisions carry Alternatives Considered, Consequences, and What Would Change It sections under stated conditions — making reasoning legible and the commitment accountable
brief_summary: A bundled commitment covering three body-section requirements for Decisions. Alternatives Considered is required when the commitment was reached by weighing multiple viable options. Consequences is required when the commitment has been operative long enough to observe effects. What Would Change It is always required — the conditions under which the Decision would be revisited. The three share one Why — a posture of accountability for the commitment — and they distinguish a Decision from post-hoc justification.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Require Alternatives, Consequences, and What Would Change It in Decisions

Decisions carry three body sections that distinguish them from post-hoc justification: `## Alternatives Considered`, `## Consequences`, and `## What Would Change It`. Alternatives Considered is required when the commitment was reached by weighing multiple viable options — each alternative named, its shape stated, its rejection reason identified as a specific weakness. Consequences is required when the commitment has been operative long enough to observe effects — factual positives and negatives, not projections. What Would Change It is always required — the specific conditions under which the Decision would be revisited. The three bundle because each expresses the same posture: a Decision is accountable for the commitment it makes, and accountability shows up in these three sections.

## Why

The commitment makes **reasoning legible and commitments accountable**. A Decision without Alternatives Considered cannot be distinguished from a Decision that never considered alternatives — either the weighing happened and the result is invisible, or the weighing did not happen and the commitment is not yet defended against the options it foreclosed. A Decision without Consequences (once operative long enough) cannot be distinguished from a Decision whose effects are unobserved — either the effects have been tracked and the record is missing, or the effects have not been tracked and the commitment is unaudited. A Decision without What Would Change It cannot be distinguished from a claim that the commitment is permanent — either the revisit conditions exist and are unstated, or they do not exist and the Decision is a Conviction mislabeled.

The three sections bundle because they share this accountability posture. Each is the form's way of refusing a specific mode of post-hoc justification: Alternatives Considered refuses "we chose X because X was right" with no accounting of what else was on the table; Consequences refuses "the decision is working" with no factual observation of what has actually happened; What Would Change It refuses "the decision is permanent" with no conditions for revisit. Together, the three make a Decision a node the project can be held to — by itself and by later readers.

Each section has its own conditions for inclusion. Alternatives Considered is required when alternatives were genuinely on the table; a Decision that was a forced move (no alternatives were viable at the time) may omit the section but SHOULD note the forced-move character in the Why. The section is omitted when there were no alternatives, not when alternatives were not examined. Consequences is required when the commitment has been operative long enough to observe effects; a Decision too new for observable consequences may omit the section, adding it as effects become visible. What Would Change It is unconditional — every Decision has revisit conditions, even if the condition is "nothing plausible" (permitted for irreducibly foundational Decisions, with one sentence explaining why no revisit criterion is meaningful, and carrying `has_commitment::[[Firm Commitment]]`).

The three bundle into one Decision because the rules co-specify. Weakening any one of them would weaken the accountability posture the others depend on. A Decision with Alternatives and Consequences but no What Would Change It is legible about the past but commits the project to nothing about its future revision. A Decision with What Would Change It but no Alternatives is revisable in principle but not defended against the alternatives it foreclosed. The three together produce a Decision that is answerable to the past, the present, and the future of its commitment; any one missing weakens the accountability the others depend on.

## Alternatives Considered

**Settled-once-made Decisions without revisit or alternatives tracking.** Let a Decision simply state the commitment and its rationale, without Alternatives, Consequences, or What Would Change It. Rejected because the form then cannot be distinguished from a pronouncement. A reader encountering the Decision has no way to assess what the project weighed, how the commitment has played out, or when it would change — the Decision becomes a historical statement rather than an active commitment the project holds. The bundled sections are what make the Decision answerable; without them, the node is a memorandum, not a commitment.

**Require only What Would Change It.** Keep the revisit-conditions section required, make Alternatives and Consequences optional at author discretion. Rejected because optional-at-author-discretion effectively means "absent by default." Decisions written under time pressure or without reviewer gate would systematically omit them; the accountability posture would live only in the strongest Decisions, not in the form's baseline. The bundled requirement is what makes Alternatives and Consequences appear in most Decisions, not just the ones whose authors chose discipline.

**Alternatives and Consequences in prose without dedicated sections.** Let authors weave alternatives and consequences into the Why or body prose rather than giving each its own `##` section. Rejected because the dedicated-section placement is what makes the content findable and verifiable. A reader auditing the Decision for alternatives-considered can look for `## Alternatives Considered` and confirm presence or absence at a glance; content buried in prose requires close reading to verify. The sections are cheap structural tiers in the same sense as the Relations layer: they carry content the reader can audit without the body's full cost.

## What Would Change It

The commitment would be revisited under one condition.

**The sections prove unmaintainable for most Decisions.** If a pattern emerges where most Decisions cannot support the three sections honestly — where Alternatives Considered reduces to a forced-move note in most cases, where Consequences either remains empty (Decisions are too new to observe) or reduces to "it worked," where What Would Change It produces "nothing plausible" as the standing answer — the bundle would produce structure without substance. The revisit would be corpus-driven: an audit of seeded Decisions would show the sections either absent (honestly, because the conditions do not apply) or present-but-content-free (dishonestly, because the sections feel required). The rule would relax to require only What Would Change It as unconditional, with the other two explicitly conditional on the stated triggers. Current Decisions have supported the three sections substantively; the bundle is carrying its weight.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine lets Decisions reference their alternatives, their consequences' observable effects, and their revisit conditions' substrate by typed edge. The accountability posture the three sections express depends on the graph connecting claims to their grounds; without the spine, the sections would carry prose claims without structural verification.

- grounded_in::[[Require Prose, Capability-First Why in Decisions]]
  - The prose and capability-first Why commitment together with this bundle define what a Decision's body looks like. The Why carries the argument; Alternatives, Consequences, and What Would Change It carry the accountability scaffolding. Both together produce a Decision body that is both reasoned and answerable.

- informs::[[Decision Form Contract]]
  - Decision Form Contract's Alternatives Considered, Consequences, and What Would Change It Requirements carry the thin enforcement clauses pointing at this Decision.
