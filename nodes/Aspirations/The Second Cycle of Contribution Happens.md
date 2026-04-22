---
created: 2026-04-20
tagline: The project reaches a second cycle of contribution — the conventions sustain past the first seed-and-run round and the practice continues without dependency on any single author
brief_summary: An Aspiration that the project completes a second cycle of contribution — the first seed-and-run round of contribution produces nodes, the conventions survive that first round's authoring pressure, and a second round of contributors (returning or new) continues the practice. The second cycle is the project's core success metric, distinguishing sustainability from one-off effort. The gap is concrete — no first cycle has completed yet, no second author exists, the conventions have not been tested under contribution pressure, and the bounded-slice selection that would seed a first cycle is itself an Open Question in the Decision Log.
---

- conforms_to::[[Aspiration Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# The Second Cycle of Contribution Happens

The project works toward a second cycle of contribution — the conventions survive a first seed-and-run round, attract a second round of contributors (returning or new), and the practice demonstrably continues without dependency on any single author. Reaching the second cycle is the project's core success metric; one-off authoring is not sustainability.

## Why It Is Worth Pursuing

A first cycle of contribution proves that a seed corpus can be authored and that the conventions do not immediately break. A second cycle proves something different and harder: that the conventions are legible to authors who were not present at their creation, that curation stays tractable as the graph grows, and that the practice does not collapse when the founding author's attention moves elsewhere. These are the properties that distinguish a shared practice from a single-author garden.

The Founding Conversation names the second-cycle test directly: "The unit of success is whether the second cycle of contribution happens, not whether any particular artifact ships." The reframing is load-bearing for every design choice the project makes. A decision that improves first-cycle artifact quality at the cost of second-cycle legibility fails the test; a decision that sustains second-cycle legibility at some cost to first-cycle elegance passes. The ordering forces the project to ask, at each choice, *what makes the second cycle more likely?*

The second-cycle frame also distinguishes this project from an MVP. The first cycle is not a minimum viable product shipped to an audience; it is the first iteration of a discipline. Its success is not adoption metrics but whether the discipline proves sustainable when the author stops being the author — when a second contributor arrives and either completes the cycle or reveals that the conventions cannot hold.

## Current Gap

No first cycle has completed yet. The seed graph carries Contract, Decision, Conviction, Observation, Aspiration, Pattern, Predicate, Gloss, and Reference nodes — the substrate the practice runs on — but no real nodes in the intended knowledge domain. Every seeded node documents the convention layer; none documents the subject matter the practice is for.

The bounded-slice selection that would seed a first cycle is an open question. `context/Decision Log.md` tracks the "Seed corpus domain" Open Question as unresolved — the project has not decided which slice of the intended domain to seed with 15-30 real nodes that exercise the conventions under authoring pressure. Without that decision, the first cycle cannot start, and the second cycle is gated on the first.

No second author exists. The graph has been authored by one person with agent assistance; the conventions have not been read, applied, corrected, or challenged by a contributor who was not present at their creation. Every point at which the conventions might confuse a new reader is currently invisible, because there is no new reader.

The conventions have not been tested under contribution pressure. Authoring under composition-time pressure (what predicate should I use? what shape does this node take?) reveals which conventions are clear, which are under-specified, and which actively obstruct authoring. The current seed graph has been authored deliberately and slowly; a contribution-pressure test has not yet happened.

## Work It Asks

Resolve the "Seed corpus domain" Open Question in `context/Decision Log.md` — decide which bounded slice of the intended domain to seed first. The decision is the immediate blocker on starting the first cycle; without it, every subsequent move is postponed.

Seed 15-30 real nodes in the selected domain slice. The node count is the threshold at which the full predicate family, the form contract catalog, and the curation cadence all get exercised. Fewer than 15 does not stress the conventions; more than 30 risks committing to the conventions at scale before a contribution-pressure test has happened.

Invite 2-4 initial contributors to author in the same graph. The contribution-pressure test is what reveals which conventions hold and which fail. The contributors do not all need to finish nodes; even a single contributor attempting and abandoning a node in the conventions produces high-value information about where the conventions obstruct.

Support a curation ritual cadence through the first cycle. The Pattern `Reconcile the Standing Account` names the move; the cadence is what turns the move into practice. A weekly or bi-weekly curation pass during the first cycle holds the graph against the write-only drift that Observation `Wikis Without Curation Drift Toward Write-Only` names as the failure mode this Aspiration targets.

Observe and record what breaks, what holds, what contributors need. Every observation from the first cycle is input to whether the second cycle can be invited. A first cycle that produces only nodes (without recorded observations about the authoring experience) wastes the test.

### Contributor-level transition

The project-level target (the cycle continues) requires contributor-level work (individual contributors find return the natural next move). The scarcity at the first-to-second-cycle transition recorded in `[[Second-Cycle Contributors Are the Scarce Resource]]` is the specific attrition point this work addresses. Four friction points are named and addressable:

Contributor acknowledgment closes the loop between first contribution and the subsequent curation pass. The curator's acknowledgment names what the contribution added, where it now lives, and what edges it sits at. Acknowledgment is not optional politeness — it is a first-class curator responsibility, and the sustainability of the practice rests in part on whether curators carry it forward.

Curation output is visible to contributors between cycles. A contributor who authored in a first cycle can see the subsequent curation pass's result — a summary, a diff, or a narrative naming what was preserved, what was revised, and what was routed. Curation-as-contributor-surface turns a back-stage operation into a contributor-facing practice that contributors participate in rather than observe from outside.

A first-cycle follow-up cadence exists. Candidate cadences: acknowledgment within a week of contribution, a first curation-summary surface within a month, an explicit invitation to the second cycle within three months. The specific numbers are proposals; the cadence itself — that some cadence exists and is committed to — is the work. An unresponded-to contribution accretes the wrong signal.

Contribution recognition is built into the graph's structure where possible. Candidate predicates: `first_authored_by::` preserved through revision so the original author remains visible when the node has evolved; `cited_by::` or incoming-edge aggregation so a contributor can see what their contribution has come to ground; per-contributor summary surfaces that aggregate graph footprint. The specifics are open; the commitment is that recognition is graph-native rather than an external acknowledgment system.

## Progress Recognition

The first bounded slice is selected and seeded with 15-30 nodes that exercise the full predicate family, form contract catalog, and curation cadence.

A second contributor authors their first node in the graph without convergence pressure from the curator — their predicates, their naming, their annotations enter the graph alongside the founder's, not as translations into the founder's vocabulary.

A curation pass reconciles the graph without ontology arbitration. The pass runs; drift is caught; the graph stays legible; no decision gets stalled in "which term is right" arbitration.

A returning or new contributor arrives for the second cycle, reads the existing conventions and the existing nodes, and finds the ground legible enough to begin authoring. The contributor does not need the founder to explain the conventions or the nodes in real-time; the graph's own structure carries enough context to onboard.

At least one first-cycle contributor returns for a second contribution within the established follow-up cadence. The return is verifiable through graph state — new nodes authored by a returning contributor, edges added to existing nodes, curation participation — rather than through self-report alone. A first-to-second-cycle transition rate becomes measurable even if anecdotally, which is the signal that the contributor-level work is producing observable effects.

Curators report that acknowledgment practice is a sustainable part of the curation cadence rather than a burden that falls away under pressure. The practice holds if curators carry it forward; drifts if acknowledgment becomes an intermittent gesture. Sustainability is the measure — one-time acknowledgment is not cultivation.

The project reaches a steady state where contribution happens on at least two contributors' cadences, curation happens on at least one contributor's cadence, and the practice's continuation does not depend on any single author being present this week.

## Sources

- `context/Founding Conversation.md` — the "The meta-point" section supplies the second-cycle framing ("The unit of success is whether the second cycle of contribution happens, not whether any particular artifact ships").
- `CLAUDE.md` — the "Working assumptions" section names the second cycle as the unit of success and grounds the directional target this Aspiration captures.

## Relations

- grounded_in::[[Deep Context as an Architecture for Captured Reasoning]]
  - The architecture Decision is the substrate this Aspiration pursues at the cycle level. The architecture is what the second cycle is a cycle *of*; without the architectural commitment, the target has no shape. The Decision is the structural substrate; this Aspiration is the directional target the architecture serves across cycles.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction names the contributor-sovereignty property the second-cycle test validates. A second cycle that reached steady state by converging contributor vocabularies would not satisfy the Aspiration, because the vocabulary-diversity Conviction the project holds would have been abandoned in the process.

- informed_by::[[Wikis Without Curation Drift Toward Write-Only]]
  - The Observation names the failure mode this Aspiration is the counter-target of. A wiki that drifts toward write-only has not reached a second cycle; the Aspiration is the directional commitment not to drift, and the Observation grounds why the directional commitment is worth carrying the work it asks.

- informs::[[Contributors Across Vocabularies Can Collaborate]]
  - The cross-vocabulary Aspiration specializes the second-cycle target to the plural-contributor case. This Aspiration is the general target; the cross-vocabulary Aspiration is a specific dimension of it.

- informs::[[The Graph Survives Its Tooling]]
  - The tool-independence Aspiration specializes the second-cycle target to the tool-independence dimension. A second cycle that depends on a specific tool configuration remaining available has not reached the durability the Aspiration implies; the tool-independence Aspiration is what durability means at the tool layer.

- informed_by::[[Second-Cycle Contributors Are the Scarce Resource]]
  - The specific attrition at the first-to-second-cycle transition is what the Aspiration's project-level target is a response to. The Observation supplies the measured scarcity and the power-law distributional context within which the attrition operates; the Aspiration names the directional response.

- informed_by::[[Participation Takes Different Forms Not Different Levels]]
  - A second cycle may arrive in a different form than the first — a contributor whose first cycle was authoring-dominant may return in a responding-dominant or curating-dominant form. The Aspiration's progress recognition needs to be form-sensitive to catch this; the form-plurality Observation is what makes the form-sensitive reading available.

- informs::[[Pride and Humility Are Both Cultivable]]
  - The trait-cultivation Aspiration names the specific design response to one of the filters the second-cycle target has to address. Cultivating the trait-pair widens the contributor population who can sustain through to the second cycle.
