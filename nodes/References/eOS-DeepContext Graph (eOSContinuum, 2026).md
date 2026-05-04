---
created: 2026-05-04
tagline: A downstream Deep Context graph carrying the eOS Continuum project's substrate-vs-glue architectural argument; first non-self instance of the practice and primary live test of the meta-layer's portability
brief_summary: eOS-DeepContext is the first Deep Context graph other than DeepContext.com itself — a self-sovereign graph standing up at https://eoscontinuum.com with its own Open Integrity inception (`did:repo:9dc47a293f5b2352dba288b3e2ef9c73c508ca0f`), its own first steward, and its own purpose (carrying the eOS Continuum project's argument that agentic AI runtimes need substrate primitives, not external glue). It grafted DeepContext.com's meta-layer at instantiation — Form Contracts, Predicates, generic Skills — and continues to refresh those grafts as DeepContext.com's meta-layer evolves. eOS-DeepContext is explicitly **not** a scion (`scion_of: null` in its `.deep-context-identity.yml`); the relationship to DeepContext.com is per-node graft, recorded via `grafted_from::` edges throughout `nodes/`. Several conventions originated in eOS-DeepContext and flowed back to DeepContext.com (the `SITE_NAME` parameterization, the scion-vs-graph rename that produced the `Adopt Self-Sovereign Graph Publication` Decision, the `Reference Targets Must Be Resolvable to Other Readers` Decision authored from eos-harness's FX-6 misstep). The bidirectional flow is the practice working as intended — content-level coordination per the `Coordinate at Content, Not at Git` Pattern, with neither graph claiming canonical ownership of the shared meta-layer.
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Reference Implementation]]
- in_practice_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# eOS-DeepContext Graph (eOSContinuum, 2026)

URL: https://eoscontinuum.com

DID: `did:repo:9dc47a293f5b2352dba288b3e2ef9c73c508ca0f` (the SHA1 of eOS-DeepContext's Open Integrity inception commit, derived per [[Open Integrity Project (Blockchain Commons, 2025)]]).

eOS-DeepContext is the first Deep Context graph standing up other than DeepContext.com itself. The graph carries the eOS Continuum project's architectural argument — that agent platforms today are orchestration layers around stateless LLM calls, that the resulting state-collision drives a class of bugs that practitioners are addressing in user-space rather than at the substrate, and that the answer is a runtime carrying eight primitives (orthogonal persistence as foundational; atomic operations, capability separation, hot reload, sandboxed code load, asynchronous events, multi-agent coherence, state introspection derived from it). The graph is at https://eoscontinuum.com; its first steward is Christopher Allen.

eOS-DeepContext is **not** a scion of DeepContext.com. Its `.deep-context-identity.yml` records `scion_of: null` and explicitly declines the lineage claim. The relationship is per-node graft: eOS-DeepContext copied DeepContext.com's meta-layer (Form Contracts, Predicates, generic Skills) at instantiation, recorded each copy via a `grafted_from::[[DeepContext.com Graph (Allen, 2026)]]` edge, and continues to refresh those grafts as DeepContext.com's meta-layer evolves. Per-node graft provenance lives on each grafted node in eOS-DeepContext; eOS-DeepContext-specific content (the substrate-vs-glue argument's Convictions, Decisions, Patterns, Observations as they get authored, plus the eOS-specific Inquiry Form Contract and the agent-memory-literature Reference corpus) is locally authored.

### Adopted

DeepContext.com adopts eOS-DeepContext as a known downstream instance of the Deep Context practice — the first live test of the meta-layer surviving outside its origin graph and the primary case study for the bidirectional-flow pattern.

- **The graft-not-scion default.** eOS-DeepContext's deliberate `scion_of: null` confirmed empirically what the original `Adopt Scion Publication Model` framing under-acknowledged: most Deep Context graphs are not scions. The practice's documentation moved from "scion is the publication unit" to "self-sovereign graph publication, scion-of as optional" — the Decision rename ([[Adopt Self-Sovereign Graph Publication]]) was DC catching up to the framing eOS already operated under.
- **Bidirectional content-level coordination.** Several conventions originated in eOS-DeepContext and flowed back to DeepContext.com: the `SITE_NAME` parameterization in `render.py` (eOS forked the file to add the constant; DC pulled it back); the scion-vs-graph vocabulary rename (eOS led; DC followed); the `Reference Targets Must Be Resolvable to Other Readers` Decision (authored from eOS's eos-harness FX-6 misstep). The pattern is captured as [[Coordinate at Content, Not at Git]].
- **The donor Reference proxy pattern.** eOS-DeepContext's `nodes/References/DeepContext.com Graph (Allen, 2026).md` is the canonical donor proxy — the Reference whose `this_did:` and `url:` frontmatter let `[[Taxonomy/Target]]↗` external wikilinks resolve to deepcontext.com. The pattern is symmetric: this Reference (the eOS-DeepContext donor proxy on DC) does NOT carry `this_did:` or `url:` because DC does not graft from eOS — only the other direction.
- **Empirical signal on the form-content authoring gap.** eOS-DeepContext has the meta-layer fully grafted but very little content-layer authoring (one Touch Point, no Decisions or Convictions yet). The signal is that *standing up the graph and grafting the meta-layer* is one mountain; *authoring substantive content using the forms* is the larger second mountain. Future scions should expect the same shape; the practice may eventually need an Aspiration or Pattern around what reduces content-authoring cost.

### Not adopted

- **The eOS-specific Inquiry Form Contract.** eOS-DeepContext authored its own form for unresolved-question nodes with reasoning attached (a structural shape DC's Decision form does not cover, since Decisions are *resolved* commitments). DC does not adopt the Inquiry Form Contract at this point; the gap is real but not load-bearing for DC's current work. The form may flow back to DC if and when DC encounters its own pre-resolution moments worth authoring as nodes.
- **The eOS-specific Reference corpus.** eOS-DeepContext's References cover the agent-memory-and-runtime literature (MemGPT, A-MEM, Mem0, MemMachine, Memoria, ClawVM, Recursive Language Models, DSPy, Compound AI Systems). DC's References cover graph-publishing patterns and tradition-aware Allen Musings. Both Reference taxonomies are correct for their respective graphs; DC has no reason to import eOS's domain-specific corpus.
- **eOS-DeepContext's content-layer Convictions.** When eOS-DeepContext authors its load-bearing Convictions (the eight runtime primitives), those Convictions are about agent runtimes, not about the Deep Context architecture. DC does not import them; readers of DC who want the substrate argument follow the link to eoscontinuum.com.

### Practical use

- **Cross-graph reference resolution.** Both graphs use external-wikilink syntax (`[[Taxonomy/Target]]↗`) to cite each other's nodes without copying. DC's references to eOS-DeepContext-specific concepts would resolve through this Reference once such citations exist.
- **Refresh cadence study.** eOS-DeepContext is the first relationship in which the practice has had to reason about graft-refresh cadence. Drift accumulates between refreshes; the audit makes drift visible. Future scion relationships will benefit from whatever cadence pattern this one settles into.
- **Survival evidence.** A core claim of `Adopt Self-Sovereign Graph Publication` is that the practice survives any one actor stepping away. eOS-DeepContext is the first empirical test: if DeepContext.com paused for a year, eOS-DeepContext's graph would still publish, still resolve its grafts (with the cached donor Reference URL), and still be readable. The claim is not yet stress-tested at long duration but is structurally feasible because of this graph's existence.

## Sources

- Repository: https://github.com/eOSContinuum/eOS-DeepContext
- Published site: https://eoscontinuum.com
- Sibling implementation project: https://github.com/eOSContinuum/eos-harness (the runtime work this graph anchors the architectural argument for)

## Relations

- conforms_to::[[Reference Form Contract]]
  - This file is itself a Reference; it conforms to the Form Contract specifying what Reference nodes look like (URL, adopted/not-adopted body shape, citation parenthetical filename).

- serves_as::[[Reference Implementation]]
  - The eOS-DeepContext graph serves DC as a reference implementation of the meta-layer's downstream usage. Other downstream graphs can study its donor Reference, its `grafted_from::` patterns, its `SITE_NAME` parameterization, and its bidirectional-flow contributions to see what graft-not-scion looks like in practice.

- composes_with::[[Coordinate at Content, Not at Git]]
  - The Pattern this Reference's relationship to DC instances. eOS-DeepContext's content-level coordination with DC (per-node grafts, external wikilinks, periodic refresh) is the canonical example of the Pattern in action.

- composes_with::[[grafted_from -- per-node content provenance from a donor graph]]
  - eOS-DeepContext's grafted nodes carry `grafted_from::[[DeepContext.com Graph (Allen, 2026)]]` edges in their identity blocks. The Predicate's primary current usage is by this graph.

- informs_downstream::[[Adopt Self-Sovereign Graph Publication]]
  - The Decision was renamed and reframed in part because eOS-DeepContext's `scion_of: null` made the old "Adopt Scion Publication Model" framing visibly wrong. eOS-DeepContext is the empirical case the rename absorbed.

- informs_downstream::[[Reference Targets Must Be Resolvable to Other Readers]]
  - The Decision was authored after a misstep in eOS-DeepContext's sibling project (eos-harness Minimum Viable Architecture workstream, FX-6) where two References pointed at sibling-project filesystem paths. Catching the misstep on the eOS side made the principle visible; the Decision codifies it for all graphs.

- contrasts_with::[[DeepContext.com Graph (Allen, 2026)]]
  - The two References are mirror images: DeepContext.com's donor Reference on the eOS side records DC as the meta-layer source; this Reference on the DC side records eOS as a known downstream instance. eOS's Reference carries `this_did:` and `url:` (donor proxy). This Reference does not (DC does not graft from eOS — only the other direction).
