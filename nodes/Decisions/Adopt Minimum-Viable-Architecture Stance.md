---
created: 2026-04-21
tagline: Ship the minimum that lets the practice run and defer until use surfaces what to add next
brief_summary: A stance governing what the project will and will not build. The first cycle of DeepContext.com ships the conventions, the pipeline, and a seed set of nodes -- nothing beyond what the practice needs to run end to end. Capabilities the PRD names as deferrals (heading-link targets within nodes, cross-garden external-marker resolution, transclusion across nodes, an interactive graph explorer, full-text search, custom theming, collaboration features like invitations and agent orchestration) are explicitly NOT built in the first cycle. The stance is provisional and asymmetric: it is a commitment about sequencing, not about ceiling. Capabilities return to scope when actual use reveals what the practice needs that it cannot currently do. The stance exists because the project holds that designing for anticipated rather than observed needs is the main way knowledge-graph projects accumulate complexity before they accumulate contributors.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-21
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Adopt Minimum-Viable-Architecture Stance

The first cycle of DeepContext.com ships the minimum architecture that lets the practice run end to end: the node conventions, the Python build pipeline, the projection mechanism from workshop to publication, the seed set of nodes, a working Pages deploy. Capabilities beyond that minimum are deferred, and the deferrals are named explicitly so they are revisitable rather than forgotten.

The current deferrals are: heading-link targets within nodes (`[[File#Section]]`), cross-scion external-marker resolution (the `↗` suffix currently renders as styled text rather than resolving to a specific adjacent graph), transclusion across nodes, an interactive graph explorer, full-text search, custom theming beyond the minimal CSS, and collaboration features (invitations, agent orchestration, multi-scion coordination). Each of these is a capability the PRD names; each is a capability the project does not build in the first cycle.

## Why

The stance exists because knowledge-graph projects consistently accumulate pipeline complexity before they accumulate contributors, and the complexity becomes a maintenance surface that filters who continues participating. A graph explorer nobody uses is not free -- it is a capability that must keep working as the graph evolves, and each regression in it consumes maintainer attention that did not go to the practice itself. The same is true of search (a feature whose cost compounds as the corpus grows), custom theming (a surface that diverges under scion pressure), and collaboration tooling (features designed for anticipated rather than observed interaction patterns).

The project also holds that the architecture committed to in the first cycle will shape what the practice becomes in ways that are hard to reverse. [[Founding Vocabularies Constrain Later Participants]] names the dynamic at the vocabulary layer; the same structural constraint applies at the capability layer. Committing to a graph-explorer UI in the first cycle would bake in a specific model of how the graph is navigated before the project knows what navigation pattern actual readers need. Deferring it leaves the question open.

The stance is honest about what is being traded. An original vision for DeepContext.com was substantially larger -- thousands of patterns in deep shared language, many committed participants, rich navigation and collaboration tooling. The first cycle delivers much less than that vision. The trade is deliberate: build less now so the project can learn from actual use what the vision should look like when it grows, rather than committing architecture to a vision that has not yet been tested against practice. If the seeded nodes and the scion commitment produce a second cycle of contribution, the project learns what capabilities that cycle actually needs; if they do not, the deferred capabilities would not have been what made the difference.

The stance is also asymmetric with respect to different kinds of deferrals. Capabilities that would change the shape of the graph or the contribution contract (transclusion, cross-garden resolution, a graph explorer that becomes load-bearing for navigation) are deferred firmly, because returning from them would be costly. Capabilities that are cosmetic or additive (custom theming, search, hover-previews) are deferred softly -- they can be added without reshaping the project's commitments.

## Alternatives Considered

**Ship the full PRD vision in the first cycle.** Build heading-link resolution, transclusion, a React-based graph explorer, search, fuller theming, and collaboration features all before the first public deploy. Rejected because it commits the project's architecture to anticipated rather than observed needs, and because the maintenance surface of the full feature set would dwarf the seeded content. A scion inheriting the full surface inherits a much larger project than the practice currently is.

**Ship only enough to prove the pipeline and defer even the conventions.** Publish the pipeline with a handful of demonstration nodes and wait for contributor interest before investing in the Form Contracts, the Predicate vocabulary, or the Convictions. Rejected because the conventions are the practice; without them, the project is a static-site generator looking for a use case. The seeded nodes are what make the practice evaluable.

**Defer publication entirely until the graph is substantial enough to justify it.** Work in the workshop repository until a larger critical mass of nodes and conventions exists, then publish as a more complete artifact. Rejected because publication is part of how the project learns what the practice needs. A published seed that fails to produce a second cycle teaches the project something the workshop-only path cannot.

**Use an existing static-site generator (Jekyll, Hugo, Eleventy, Astro) with a thin adapter.** Defer the pipeline itself by adopting a stable tool and writing only the node-specific adapters. Rejected because the pipeline's scion commitments ([[Adopt Scion Publication Model]]) require a self-contained repository, and existing SSGs carry dependency surface (plugin ecosystems, toolchain versions, content model assumptions) that scions would inherit and need to maintain. The first cycle's pipeline is ~500 lines of Python with one dependency; a scion can read it end to end.

## What Would Change It

**The seeded corpus produces a second cycle of contribution.** [[The Second Cycle of Contribution Happens]] is the project's success metric; if the first cycle actually produces sustained second-cycle contribution, the project has earned the right to invest in capabilities beyond the minimum. The MVA stance would narrow: the capabilities the second cycle specifically wants would return to scope, while the ones still speculative stay deferred.

**A deferred capability becomes blocking rather than absent.** The current deferrals assume readers can navigate the graph adequately without heading links, search, or an interactive explorer. If use reveals that specific capabilities are blocking participation -- not just inconvenient -- the stance narrows around those specifically. The revisit condition is evidence of blocking, not preference for more.

**The maintenance cost of the minimum exceeds what the minimum delivers.** If the current pipeline accumulates edge cases faster than the corpus grows, the minimum is not actually minimum; it is carrying complexity without carrying value. The revisit would ask whether the first cycle's architecture itself needs reduction, not addition.

**A clearly-better architecture emerges that the project could adopt without breaking scion promises.** If a different minimum (simpler pipeline, different contribution mechanism, different publication story) becomes available and preserves the scion commitment, the stance's specific implementation changes even though the stance itself survives.

## Relations

- grounded_in::[[Minimum Viable Architecture -- the simplest architectural substrate sufficient to function and reveal what to add next]]
  - The Gloss that defines the MVA concept this Decision adopts as a stance. The Decision adopts the discipline; the Gloss carries the bare concept the discipline is committed to. Together they let a new contributor read "what is MVA" (the Gloss) and "what does this graph commit to in its first cycle" (the Decision) as two distinct claims rather than one conflated assertion.

- grounded_in::[[Minimum Viable Architecture Musing (Christopher Allen, 2024)]]
  - The Reference whose framing this Decision's name and discipline come from directly. Allen's MVA stance names upfront architectural planning paired with deferred non-essential components, modular expandability, and interoperable interfaces as the substrate for survivable growth; this Decision specializes that stance for a knowledge-graph project's scale. Without the Musing, this Decision would not carry the specific "Minimum Viable Architecture" formulation.

- grounded_in::[[Adopt Scion Publication Model]]
  - The scion commitment is one reason the MVA stance is load-bearing. Every capability the pipeline ships is a capability every scion inherits as a maintenance surface; keeping the minimum small keeps scion cost low.

- informed_by::[[Convergent Motivation as Load-Bearing Signal]]
  - The Pattern that gives this Decision its operational test for when a deferred capability returns to scope. The Decision's Revisit Conditions describe what would change the deferrals (a second cycle of contribution, a deferred capability becoming blocking, maintenance cost exceeding minimum, a clearly-better architecture); the Pattern names the underlying evidentiary discipline -- four or more independent motivations converging on a capability is the structural threshold the Revisit Conditions implicitly invoke. The Pattern operationalizes the discipline; the Decision is the standing commitment the discipline serves.

- informs_downstream::[[Publish via Actions Artifact Deploy]]
  - Actions-deploy is one expression of the MVA stance at the deployment layer: one dependency, one workflow file, no custom infrastructure. The deployment Decision inherits the minimum-surface discipline this Decision names.

- informed_by::[[Shared Languages Get Intimidating Over Time]]
  - The Observation names one of the reasons building for anticipated needs is costly: vocabulary and capability both accumulate faster than newcomers can absorb. MVA at the capability layer parallels unanimity-over-precedent at the vocabulary layer -- both are disciplines against premature commitment.

- informed_by::[[Wikis Without Curation Drift Toward Write-Only]]
  - The write-only failure mode compounds with feature complexity: a graph with more capabilities requires more curation to keep coherent, and the curation burden is what makes the write-only dynamic bite. MVA keeps the curation surface proportional to the content surface.

- informed_by::[[Agora Project (Flancian, 2019)]]
  - The deferred cross-garden external-marker resolution and the deferred collaboration-at-aggregator capabilities point at Agora's model as one precedent of what those capabilities would look like when they return to scope. This Reference is the study substrate the deferral refers to without committing the project to adopting the specific implementation.

- informed_by::[[Egregore Framework (Egregore Labs, 2026)]]
  - The deferred collaboration features (invitations, agent orchestration, multi-scion coordination) point at Egregore's model as one precedent of what those capabilities look like when implemented. This Reference is the study substrate the deferral refers to; the MVA Stance names what the project would study should those capabilities become load-bearing without committing to the Egregore frame.
