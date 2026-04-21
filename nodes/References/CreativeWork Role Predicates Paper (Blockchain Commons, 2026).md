---
created: 2026-04-20
tagline: Christopher Allen's Blockchain Commons paper specifying 14 role predicates for creative work contributions — deferred substrate for the project's future role system
brief_summary: Blockchain Commons Research paper (bcr-2026-xxx), dated 2026-02-02, specifying fourteen role predicates (Author, Editor, Architect, Designer, Manager, Documenter, and others) for creative-work contributions. Designed to function across media types (text, code, audiovisual) and remain agent-agnostic — applying equally to human, AI, and hybrid contributors. Maps to existing standards (CRediT, ONIX, MARC) and operates as registered predicates in the Gordian Envelope system. Deep Context carries this as deferred substrate: the MVA authorship model uses collective `authored_by::[[Deep Context Community]]` with the lead named in the Community Gloss prose; the 14-role vocabulary is the candidate substrate for when specific-role predicates become load-bearing.
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Deferred Role Vocabulary]]
- authored_by::[[Christopher Allen]]↗
- authored_by::[[Blockchain Commons]]↗
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# CreativeWork Role Predicates Paper (Blockchain Commons, 2026)

URL: <https://github.com/BlockchainCommons/Research/blob/00fd2b1e24f8200e3f92a649e116960e7d723910/papers/bcr-2026-xxx-creativework-roles.md>

A Blockchain Commons Research paper, dated 2026-02-02, specifying a vocabulary of fourteen role predicates for creative-work contributions. The fourteen include Author, Editor, Architect, Designer, Manager, Documenter, and others. The vocabulary is designed to operate across media types (text, code, audiovisual) and to stay agent-agnostic — each role applies equally whether the contributor is a human, an AI system, or a hybrid team. The paper aligns the vocabulary with existing standards (CRediT, ONIX, MARC) and specifies the predicates as registered terms in the Gordian Envelope system. The URL is pinned to a specific commit SHA; later revisions live on the paper's branch.

### Adopted

Nothing directly adopted in MVA. The paper is deferred substrate.

### Not adopted (yet)

- **The 14-role vocabulary.** Deep Context MVA uses a single collective `authored_by::[[Deep Context Community]]` with the lead steward named in the Community Gloss's prose. Specific-role predicates (for editor, steward, reviewer, contributor distinctions) are not yet load-bearing for the project's work; the simplification is deliberate.
- **The CRediT / ONIX / MARC mappings.** These alignment tables are useful when Deep Context needs to interoperate with publication and library traditions. No such interop is active in MVA.
- **Gordian Envelope predicate registration.** Deep Context's convention layer is plain markdown with author-declared edges; Envelope-registered predicates would be a later convergence move toward a cross-system registry.

### Key moves to remember

- Cross-media applicability (one role vocabulary for text, code, audiovisual) avoids the balkanization that comes from separate role systems per medium.
- Agent-agnostic role definitions (a role is a contribution kind, not a contributor kind) matches Deep Context's stance that agents and humans are peers in the translation layer.
- Mapping to CRediT, ONIX, MARC is the translation-over-convergence move at the role-system layer: the vocabulary stays its own while making interop with neighboring systems explicit.

## Relations

- informs::[[Deep Context Community]]
  - The Gloss that carries the project's MVA authorship model. The Community Gloss cites this paper as deferred substrate — the role system to draw on when specific-role predicates become warranted.
