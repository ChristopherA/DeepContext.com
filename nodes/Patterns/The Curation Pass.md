---
created: 2026-04-21
tagline: The composed unit of curation work — a session that reads the graph's recent state, applies the curator-layer Patterns in sequence, and produces a record that reaches contributors and leaves the graph more legible
brief_summary: "A recurring unit of curation work. A curation pass is the composed session in which the curator reads the graph's recent state, applies the curator-layer Patterns (Acknowledge Before Revise, Treat Objection as Structural Contribution, Gloss the Translation Surface, Reconcile the Standing Account) in the order the pass's findings require, and produces a curation-pass record that reaches contributors. The Pattern names the composition, not any one of its component moves — those are separate Patterns with their own depth. A curation pass is the ritual unit; its cadence is the practice-level commitment the project makes to keep the graph legible and the contributors included."
---

- conforms_to::[[Pattern Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# The Curation Pass

## Heart

A curation pass is a session in which the curator reads the graph's recent state, applies the curator-layer Patterns — acknowledging contributions, engaging objections as structural input, glossing vocabulary contact surfaces, reconciling drifted accounts — and produces a record contributors can read. The Pattern names the unit; the component moves are separate Patterns. What this Pattern carries is the composition and the cadence.

## Problem

Curation without a unit of work is curation deferred. A curator who addresses issues as they arise, without a bounded session in which the issues are attended to as a batch, produces partial work that loops back to itself — a drift noticed is not necessarily a drift addressed; a contribution acknowledged in conversation is not necessarily acknowledged in the record. The graph's curation needs become visible only at the bounded session that reads them together and produces a record.

The default state of a new project is that curation happens ad-hoc. The curator opens a file, fixes a problem, closes the file. The next fix is disconnected from the previous one; no cumulative record exists; contributors have no visibility into what was tended. The graph accumulates small improvements and no visible practice — the problem `[[Wikis Without Curation Drift Toward Write-Only]]` names, arriving through a different door.

The difficulty is establishing the ritual as a practice rather than an event. Once a curation-pass cadence exists, the composition of the component Patterns is ordinary work. The craft this Pattern teaches is holding the session as a bounded unit — reading the graph as a whole, applying the component moves together, producing a record — rather than dissolving curation into continuous small attention that produces no visible practice.

## Forces

- **Continuous attention versus bounded session.** Continuous attention feels responsive; bounded sessions feel delayed. The trade-off is real — a bounded session means some issues wait days or weeks for attention. What the bounded session buys is the composition: issues seen together surface patterns individual fixes would miss, and the record the pass produces serves contributors in a way continuous fixes cannot.
- **Component Patterns have their own depth.** The curator does not need to re-derive Acknowledge Before Revise or Treat Objection as Structural Contribution at each pass. Those Patterns carry their own craft. The Curation Pass composes them; it does not re-specify them. Over-specifying the Pattern's internal work at the composition layer duplicates the component Patterns.
- **The record must reach contributors.** A curation-pass record that lives only in the curator's private notes does not address the contributor-visibility concern `[[Pride and Humility Are Both Cultivable]]` names. The record is a first-class output, not a byproduct of the session.
- **Cadence trades recency for pattern.** A daily curation pass catches small drifts immediately but rarely accumulates enough signal to reveal patterns; a monthly pass accumulates signal but lets drifts ossify. The cadence is the practice-level commitment — not a universal right answer, but a specific choice a project makes and revisits as the contributor population grows.

## Solution

A curation pass has four moves in sequence:

1. **Read the graph's recent state.** New contributions since the previous pass, flagged drifts, Open Questions that may now have substrate to resolve, pre-existing staged or uncommitted changes, and any back-pointers that may have drifted as nodes moved. The read is survey-level; the pass does not exhaustively re-read the graph each time.
2. **Apply the component Patterns per finding.** For each contribution: `[[Acknowledge Before Revise]]`. For each objection or divergent vocabulary surface: `[[Treat Objection as Structural Contribution]]` and `[[Gloss the Translation Surface]]` as appropriate. For each drifted account: `[[Reconcile the Standing Account]]`. The component Patterns carry their own depth; this Pattern composes them.
3. **Produce the pass record.** A markdown document (or commit message, or `.state/` log entry) that names what the pass addressed: which contributions were acknowledged, which objections were captured and in what form, which Glosses were written, which accounts were reconciled. The record is concise but complete — a contributor reading it can see what the pass did without reading the underlying diffs.
4. **Communicate the record to contributors.** The record reaches contributors who authored content addressed in the pass. The specific channel depends on the project's contribution surface (a comment on a PR, a note in a shared document, a message at a cadence the project commits to). The communication is part of the Pattern; a record that does not reach its audience has not completed the pass.

The pass's cadence is a project-level commitment, not a per-pass decision. The cadence is recorded (in `CLAUDE.md`, `CONVENTIONS.md`, or a Decision) and revisited as the contributor population grows. Typical candidate cadences: weekly during active growth, bi-weekly during steady state, on-trigger when specific events (a new contributor arrives; a form contract changes) warrant out-of-cadence attention.

## Consequences

- **Curation becomes a visible practice.** A project with a committed curation-pass cadence has curation as a named practice contributors can point to; without the cadence, curation dissolves into individual attention that contributors cannot see or participate in.
- **The component Patterns get applied together.** Acknowledging contributions, capturing objections, glossing vocabulary surfaces, and reconciling drifted accounts happen in the same session — patterns that would not be visible from any single move surface when the moves are composed.
- **Cadence becomes a signal of project health.** A project that holds its curation-pass cadence is sustaining the practice; a project whose passes slip signals that curation is becoming back-stage work or that the curator's capacity is exceeded. The cadence is a practice-level health metric.
- **Curation overhead is bounded.** The bounded session is a container for curation work; curation does not expand to fill all available attention. A curator running weekly passes has a bounded unit of work that fits in a definable time window.
- **The pass record is the project's standing account of itself.** Over time, the pass records compose into the project's record of its own curation history — which contributions were acknowledged, which objections reshaped the vocabulary, which drifts recurred. The record is one of the graph's standing accounts, subject to `[[Reconcile the Standing Account]]` like any other.

## Instances

- **First curation pass in a multi-contributor cycle.** The pass addressing the first non-founder contributor's work is the canonical first instance at cross-contributor scale. The pass's record is inspected for how the component Patterns composed — was the contribution acknowledged before revised? Did a vocabulary contact surface generate a Gloss? Were there objections, and were they captured as structural content? The record from that first cross-contributor pass is diagnostic for whether the project holds its own commitments under pressure.
- **Single-author pass in the seed phase.** The current project has run single-author curation passes while the seed graph has been built. The passes addressed drift in the graph's own accounts (stale counts, ghost parentheticals, extracted decisions superseding the Decision Log holding zone). These passes exercise the composition at lower pressure — the acknowledge-before-revise move applies to the author's own prior work, and the reconcile-the-account move addresses documents describing a graph the author also edited. The single-author instance is a dress rehearsal for the cross-contributor application.

## Also Known As

- **Curation session** — event-noun alternative. Same referent.
- **Reconciliation ritual** — emphasizes one component (Reconcile the Standing Account) as the frame; appropriate when the pass is predominantly document-layer work, narrower than The Curation Pass's full composition.

## Relations

- grounded_in::[[Wikis Without Curation Drift Toward Write-Only]]
  - The Observation names the failure mode curation practice counters. A project without a curation-pass cadence is a candidate for the write-only drift the Observation describes; this Pattern is the unit of work that holds against the failure mode.

- composes_with::[[Reconcile the Standing Account]]
  - A component of the pass — the document-layer reconciliation move runs during the pass on standing accounts that have drifted. The Pattern composes it alongside the contributor-layer and vocabulary-layer moves.

- composes_with::[[Acknowledge Before Revise]]
  - A component of the pass — the curator-side acknowledgment move runs on each contribution the pass addresses before any revision is proposed.

- composes_with::[[Treat Objection as Structural Contribution]]
  - A component of the pass — when objections are surfaced during the pass, this Pattern governs the curator's response.

- composes_with::[[Gloss the Translation Surface]]
  - A component of the pass — when vocabulary contact surfaces appear, this Pattern is the move the pass applies at those surfaces.

- informs::[[The Second Cycle of Contribution Happens]]
  - The Aspiration's Work names "a curation ritual cadence" as one of the first-cycle deliverables. This Pattern names what the ritual's unit of work actually is; the cadence is the frequency at which the unit runs.
