---
created: 2026-04-19
tagline: A Decision's Why is prose, and it leads with the capability the commitment provides rather than the symptom that prompted it
brief_summary: A bundled commitment covering two paired rules about how Decision Why content is written. The Why MUST be prose, not bullets — bullet-only rationale signals misidentification or too-small scope. When the Decision responds to a reported symptom, the Why SHOULD lead with the underlying capability the commitment provides, naming the symptom as a prominent example rather than the framing. The two rules share one Why: making the Why durable across occasions and readers. Prose keeps the argument composable; capability-first keeps the argument applicable beyond the forcing case.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Require Prose, Capability-First Why in Decisions

A Decision's Why is prose, and it leads with the capability the commitment provides. The **form rule**: Why content MUST be prose, not bullet lists; a Decision whose rationale can only be expressed as bullets is either too small to be its own Decision or misidentified. The **framing rule**: when the Decision responds to a reported symptom (a failure noticed in practice, a specific friction a contributor encountered), the Why SHOULD lead with the underlying capability the commitment provides, naming the symptom as a prominent example rather than the framing. Both rules govern how the Why section works; both exist to keep the Why durable across occasions and readers.

## Why

The commitment makes Decision Whys **durable across occasions and readers**. A Decision's rationale needs to survive the originating incident, scale beyond one author's framing, and remain load-bearing when the specific case that prompted it is no longer fresh. The two rules approach that durability from different sides.

**Prose carries connective argument.** A Decision's Why is not a list of reasons-against-a-menu; it is the argument for why this specific commitment holds up. The argument moves through a sequence — this is the problem, here is the constraint, these are the prior commitments this one depends on, therefore the commitment takes this shape — and the sequence requires prose to track. Bullets enumerate; they do not argue. A bulleted Why produces a list the reader must themselves assemble into reasoning; the prose version delivers the reasoning assembled.

**Capability framing broadens the rationale's reach.** A symptom names one occasion — one contributor's friction, one broken workflow, one case that forced the commitment. A capability names what the commitment is for across all occasions the commitment applies to. A Why leading with the symptom narrows the rationale to the symptom-encountered cases; a Why leading with the capability extends the rationale to every case where the capability is load-bearing. The framing controls the rationale's perceived scope — the same content carries differently depending on which framing opens the section.

The two rules bundle because **they share one Why and reinforce each other**. Prose makes capability-first framing possible — bullets would enumerate symptoms rather than compose an argument from capability through forcing case to connective reasoning. Capability-first framing makes prose load-bearing — a prose Why that led with symptoms would still narrow its reach, even well-argued; capability-first is what the prose argues toward. Dropping either weakens the other: a bulleted capability-first Why flattens into a list of capabilities; a prose symptom-first Why composes an argument that doesn't generalize. The two together produce a Why that is both argumentatively dense and broadly applicable.

The form rule forbids trivial rewording specifically, not brief bodies. A Decision whose Why is a single paragraph of two or three sentences is fine if those sentences add specificity beyond the H1 opening. The target is fragmentation — a Why split into bullets has usually also been stripped of the "because" and "therefore" connectors that make the argument cohere.

The framing rule requires the symptom to remain present in the Why, not to be erased. A Decision with no concrete forcing case reads as abstract theorizing; the capability's anchoring instance is what makes the capability claim concrete. The Why structure runs capability-first, then "the forcing case was..." or "this surfaced when...", then the connective reasoning. Both parts are required; the order is what does the work.

Both rules apply specifically to the Why section. Alternatives Considered, Consequences, and What Would Change It each have their own structural discipline (per [[Require Alternatives, Consequences, and What Would Change It in Decisions]]); the Why is the load-bearing argument for why the commitment is the right commitment, and the prose-and-capability-first discipline is specific to that section.

## Alternatives Considered

**Bullet rationales for brevity.** Allow bullets in Why sections when the reasoning feels short enough to enumerate. Rejected because short-enough reasoning fits in a single prose paragraph; a bulleted Why is not shorter than a prose Why, it is differently structured. The "brevity" rationale usually masks reasoning that has not yet been assembled — the author knows the reasons but has not yet articulated how they connect.

**Symptom-first framing.** Let Decisions open the Why with the symptom that forced the commitment. Rejected because the framing controls the rationale's perceived scope. Incident-report framing narrows the commitment's applicability — a reader years later, encountering the Decision, may conclude the rationale no longer applies because the contributor-A case no longer arises. Capability framing survives the incident's end.

**Symptom-only Whys.** Leave the Why as a description of the forcing case without naming the underlying capability. Rejected because the Decision cannot survive the forcing case becoming irrelevant. A Decision whose only justification is "this incident happened" has no way to defend itself once the incident is forgotten.

**Capability-only Whys.** Omit the symptom entirely and reason only at the capability level. Rejected because symptom-free reasoning loses the anchoring that makes the capability claim concrete. Without the forcing-case instance, the capability risks reading as generic.

**Mixed prose and bullets within the Why section.** Let the Why open with a paragraph and then list supporting considerations as bullets. Rejected because the mixed form usually signals the bullets carry content that either belongs in a different section (Alternatives, Consequences) or does not belong in the Decision at all. The prose-only rule is what forces the author to identify what each bullet actually contributes and place it in the right section.

**Structured Why templates.** Provide a fixed sub-section template inside Why (`### Problem`, `### Constraint`, `### Prior commitment`, `### Therefore`). Rejected because templates impose a shape that most Decisions do not actually take — the argument's structure is Decision-specific.

## What Would Change It

The commitment bundles two rules; the revisit conditions are independent enough to split by part.

**Prose requirement.** Revisit if the project accumulates Decisions whose honest Whys resist prose — where the connective "because/therefore" argument is genuinely absent because the decision really is a menu selection or a point-wise choice. The revisit would be corpus-driven: a review of Decisions' Whys would show the prose discipline producing unnatural writing. Current Decisions fit prose-structured Whys without strain.

**Capability-first framing.** Revisit if a pattern emerges where most Decisions are genuinely responses to specific incidents rather than commitments providing durable capabilities — where the honest account of "why we did this" really is "this particular friction forced our hand" without a broader capability claim being available. The revisit would allow symptom-first framing when the honest rationale is genuinely incident-driven. Current Decisions have produced honest, non-strained capability framings.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine lets Decisions reference each other, prior commitments, and substrate by typed edge. Prose Whys carry the argument; the edges carry the graph-structural relations the argument depends on. The two together produce a Decision that is both readable and traversable.

- grounded_in::[[Adopt Layered Node Structure]]
  - The layered-structure commitment makes the Why part of the elaboration tier. Prose is what the elaboration tier is for — a card-scale claim tier carries the commitment in a few sentences, and the elaboration tier carries the argument that supports it. Bulleted elaboration flattens the tier into a list that could as easily live in the cheap structural layers, eroding the cost-gradient distinction.

- informs_downstream::[[Decision Form Contract]]
  - Decision Form Contract's Body-Why Requirement carries the thin enforcement clause pointing at this Decision.
