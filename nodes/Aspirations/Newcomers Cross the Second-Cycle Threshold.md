---
created: 2026-04-20
tagline: The practice develops the specific scaffolds that make first-cycle contributors likely to become second-cycle contributors — contributor-level specialization of the project-level second-cycle target
brief_summary: An Aspiration that specializes The Second Cycle of Contribution Happens at the contributor-transition layer. The project-level Aspiration names reaching a second cycle as the success metric; this Aspiration names the specific contributor-level transition — first-cycle contributors becoming second-cycle contributors — as its own directional target. Grounded in the Second-Cycle Contributors Are the Scarce Resource Observation (the reported ~5-of-20 continuation rate and the reported four-tier cascade in large-scale online communities), which identifies the first-to-second transition as the load-bearing attrition point. The gap is that the practice currently assumes the transition without designing scaffolds for it; the work is to name the friction points and build acknowledgment, curation-visibility, and follow-up practices that close the loop.
---

- conforms_to::[[Aspiration Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Newcomers Cross the Second-Cycle Threshold

The project works toward a state where first-cycle contributors become second-cycle contributors at rates substantially above the baseline attrition the literature and experience describe. The directional target is the specific contributor-level transition — not just that the project reaches a second cycle, but that first-cycle contributors find the conditions that make returning the natural next move rather than a friction-heavy decision.

## Why It Is Worth Pursuing

The project-level target of reaching a second cycle (`[[The Second Cycle of Contribution Happens]]`) names success at the cycle scale. It does not name the mechanism by which individual contributors decide to return. Without a contributor-level target, the project-level target becomes an aggregate outcome the practice hopes for rather than a specific state the practice is designed to produce. The contributor-level specialization makes the transition the practice is accountable for.

The scarcity of second-cycle contributors (`[[Second-Cycle Contributors Are the Scarce Resource]]`) is the specific attrition point this Aspiration addresses. The reported ~5-of-20 continuation rate and the reported four-tier cascade both place the first-to-second transition as the load-bearing drop-off; a practice that reaches a second cycle without specifically addressing that transition is relying on chance or on unrecognized contributor selection. Naming the contributor-level target exposes the transition to design rather than leaving it to emergence.

The contributor perspective differs from the project perspective in what it measures. Project-level success is "does the practice continue?" Contributor-level success is "did the practice make me want to come back?" The two are correlated but not identical — a project can continue through steady replacement of contributors who each complete one cycle and do not return, while individual contributors experience the practice as a thing they did once rather than a practice they joined. Sustained contribution rests on the contributor-level experience, not just on the project-level aggregate.

## Current Gap

No mechanism is named for how a first-cycle contributor comes to return. The practice's existing documentation describes what contributors author (forms, predicates, annotations) and what curation does (reconciliation, cascade, drift correction); it does not describe the specific contributor-facing surface — acknowledgment of contribution, visibility of where the contribution lives in the graph's ongoing life, invitation back — that would make the return the natural next step.

Curation output is currently invisible to contributors between cycles. A contributor who authored in a first cycle does not receive the curation-pass output, does not see whether their contribution was preserved, revised, or routed to another node, and has no surface where "my contribution's continued life in the graph" becomes visible. Without that visibility, the contribution is experienced as an endpoint — the contributor wrote something, and now it exists somewhere, and the practice moved on.

The follow-up cadence that would close the loop between first contribution and invited return is not established. No schedule exists for contacting first-cycle contributors, no invitation format for the second cycle, no surface where the curation practice's ongoing work is presented as something the contributor participates in rather than something that happens to their contribution.

The contribution-recognition surface within the graph is implicit. Predicates distinguish authorship (`authored_by::`) from participation modes (`responds_to::`, and so on), but there is no surface that surfaces "this contributor authored these nodes" or "this contribution has been cited by N subsequent nodes" as visible signal to the contributor. Recognition exists in the graph's structure; it is not surfaced to the contributor as something they can see.

## Work It Asks

Name the specific friction points in the first-to-second-cycle transition. At minimum: the absence of acknowledgment after first contribution, the invisibility of curation output between cycles, the lack of an invitation cadence, and the absent contribution-recognition surface. Each friction point is a design candidate; naming them is the first move toward addressing them.

Design contributor acknowledgment practices that close the loop between first contribution and the subsequent curation pass. The acknowledgment does not need to be elaborate — a curator's note that names what the contribution added, where it now lives, and what edges it sits at — but it must be consistent and must reach the contributor. The practice commits to acknowledgment as a first-class curator responsibility, not an optional politeness.

Design curation rituals that visibly include first-cycle contributors as readers of the curation output. The curation-pass result is currently internal to the practice; making it legible to first-cycle contributors — through a summary, a diff, or a narrative — turns curation from a back-stage operation into a contributor-facing surface. Contributors who see their contribution's continued life are more likely to return than contributors whose contribution disappears into back-stage work.

Establish the first-cycle follow-up cadence. Timing is a design decision: too soon and the contributor has not yet had time to process the first cycle; too late and the connection cools. Candidate cadences: acknowledgment within one week, a first curation-summary surface within one month, an explicit invitation to participate in the second cycle within three months. The specific numbers are proposals; the cadence itself is the commitment.

Consider whether contribution recognition can be built into the graph's own structure. Candidate predicates: `first_authored_by::` preserved through revision so the original author is still visible even when the node has evolved; `cited_by::` or incoming-edge aggregation so a contributor can see what their contribution has come to ground; contributor-facing summary surfaces that aggregate a contributor's graph footprint. The specifics are open; the commitment is to make recognition part of the graph rather than part of a separate acknowledgment system.

## Progress Recognition

At least one first-cycle contributor returns for a second contribution within the established follow-up cadence after their first. The return is verifiable through graph state — new nodes authored by a returning contributor, edges added to existing nodes, curation participation — rather than through self-report alone.

Contributors report reading subsequent curation output voluntarily — opening the curation summary, following links to their contributions' current state, engaging with the practice's ongoing work rather than waiting for direct invitation. Voluntary engagement is the signal that the curation-output-as-contributor-surface is working.

A first-to-second-cycle transition rate is measurable, even if anecdotally. The practice tracks first-cycle contributors and measures how many complete a second contribution within the follow-up cadence. The specific rate is less important than the fact of measurement — a rate that can be observed is a rate that can be designed against.

Curators report that acknowledgment practice is a sustainable part of the curation cadence rather than a burden that falls away under pressure. The practice holds if curators carry it forward; drifts if acknowledgment becomes an intermittent gesture.

## Sources

- `[[Second-Cycle Contributors Are the Scarce Resource]]` — the grounding Observation that identifies the first-to-second-cycle transition as the load-bearing attrition point.

## Relations

- grounded_in::[[The Second Cycle of Contribution Happens]]
  - Specializes the project-level target at the contributor-transition layer. The existing Aspiration names the cycle scale; this Aspiration names the contributor scale. Both are load-bearing at different scales; neither fully captures what the other targets.

- grounded_in::[[Second-Cycle Contributors Are the Scarce Resource]]
  - The Observation identifies the scarcity; this Aspiration targets closing the scarcity through design. The grounding is direct — without the Observation, the Aspiration would read as an assumed-obvious target; with it, the Aspiration is a specific response to a specific measured attrition.

- informed_by::[[Online Participation Follows Power-Law Distributions]]
  - The general power-law shape is the distributional context within which the first-to-second transition is one tier-drop. The Aspiration does not target flattening the power-law distribution (that would be its own, harder target); it targets moving the specific first-to-second transition rate within the distribution's ordinary shape.

- informed_by::[[Participation Takes Different Forms Not Different Levels]]
  - Second-cycle contribution may arrive in a different form than first-cycle contribution. A volume-only measure of return would miss this; the Aspiration's progress-recognition markers need to be form-sensitive to catch contributors who return in responding or curating forms rather than authoring-dominant forms.
