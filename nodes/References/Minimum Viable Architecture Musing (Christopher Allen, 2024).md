---
created: 2026-04-23
tagline: Christopher Allen's 2024 Musing defining Minimum Viable Architecture — upfront architectural planning paired with deferred non-essential components, contrasted against Minimum Viable Product's feature-first approach
brief_summary: Blockchain Commons Musing, published 2024-06-19 from notes originally drafted in 2021, that defines Minimum Viable Architecture (MVA) as "the simplest architecture that can support future development within a product's technological ecosystem" rather than the simplest marketable product. The post distinguishes MVA from MVP (Minimum Viable Product) along three axes — MVA requires upfront architectural planning where MVP pursues rapid market testing; MVA hollows out spaces for future development where MVP accepts architectural lock-in; MVA stakes modular, expandable, interoperable interfaces where MVP stakes delivered features — and argues that MVP's survivorship bias hides the brand damage, competitive disadvantage, and scaling-obstructed lock-in that accrue when architecture is deferred. Examples the post adopts as MVA-in-practice: TLS/SSL's modular ciphersuites, the Gordian System's layered specifications (dCBOR, URs, Envelope) connected via airgaps and torgaps, and DIDs' separation of core specification from methods and signature suites. DeepContext's Adopt Minimum-Viable-Architecture Stance Decision takes this post as its direct framing substrate; the Decision's name, its deferral discipline, and its Revisit Conditions all specialize Allen's MVA framing for a knowledge-graph project's scale.
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Foundational Framing]]
- authored_by::[[Christopher Allen]]↗
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Minimum Viable Architecture Musing (Christopher Allen, 2024)

URL: <https://www.blockchaincommons.com/musings/musings-mva/>

The Blockchain Commons Musing, published 2024-06-19 from notes originally drafted in 2021, that names **Minimum Viable Architecture** as an alternative to the dominant Minimum Viable Product framing. The post reframes the "minimum viable" formulation at the architecture layer: not the simplest marketable feature set, but the simplest architectural substrate that can support unforeseen future development without requiring rework. The post is the direct terminological and conceptual source of [[Adopt Minimum-Viable-Architecture Stance]]'s name and discipline.

### Adopted

- **MVA vs MVP as the load-bearing distinction.** The post's argument that the "minimum viable" framing belongs at the architectural layer rather than the feature layer carries forward as the Decision's core move. DeepContext's first cycle delivers much less than its full vision not because it is pursuing rapid market validation but because the architecture must be simple enough to understand, scion, and evolve; MVA names that stance precisely.
- **Hollowing out spaces for future development.** The post's phrase captures the positive side of deferral: capabilities not built today are *space left for* tomorrow's design choices, not features regrettably omitted. DeepContext's deferred capabilities (heading-link resolution, transclusion, interactive graph explorer, full-text search, custom theming, collaboration tooling) are framed in the Decision as exactly this — hollowed-out space rather than feature debt.
- **Modularity, expandability, and interoperable interfaces as the architectural stakes.** The post names these three properties as what MVA must preserve to support future development. DeepContext's form-contract architecture operationalizes each: modularity (each form has its own Contract), expandability (new forms can be added without rewriting existing ones), and interoperable interfaces (the wikilink-and-named-edge substrate is the interface every form shares).
- **Delayed decisions on non-essential components.** The post argues that MVA requires distinguishing essential (what the architecture must commit to now) from non-essential (what can be deferred without structural damage). DeepContext's Alternatives Considered sections across Decisions embody this: most non-essential alternatives are not rejected outright but deferred with explicit revisit conditions.
- **Interoperable interfaces as the survivable boundary.** The post's examples (TLS ciphersuites, Gordian dCBOR/URs/Envelope layering, DIDs separating methods from core) all turn on interfaces that let internal components change without breaking external compositions. DeepContext's counterpart is the graph itself: named-edge predicates are the interface nodes compose across, and individual nodes can be revised without the interface breaking.

### Not adopted

- **The TLS/SSL and Gordian System case examples.** The post's specific worked examples are substrate for the MVA concept but do not transfer literally — DeepContext is not a cryptographic protocol layer. The examples inform the shape of the argument (layered specifications, modular components, interoperable interfaces) without committing the project to cryptographic-protocol-style implementation.
- **The product-business framing (brand damage, competitive disadvantage, scaling lock-in).** The post's argument against MVP names risks specific to commercial product development. DeepContext's risks are different — participation dropout, vocabulary calcification, tool-dependency drift — and the Decision's Revisit Conditions name those rather than importing the commercial framing.
- **Coopetition as industry-wide collaboration.** The post emphasizes that MVA benefits from industry-scale coopetition (multiple actors each contributing to the interoperable substrate). DeepContext's scale is different — one steward or a small team at first cycle — and while scions provide a multi-actor path, the post's industry-scale framing is not the operational model.
- **The "Twitter barely made it" cautionary framing.** The post illustrates MVP's danger with Twitter's architectural near-miss. DeepContext cites the MVA framing directly without importing the specific cautionary tale, which is a product-scaling example rather than a knowledge-practice example.

### Key moves to remember

- The MVA formulation is Christopher Allen's, originating in 2021 notes and published as a Blockchain Commons Musing in 2024. DeepContext adopts the stance wholesale at the name level — [[Adopt Minimum-Viable-Architecture Stance]] is a direct specialization of the post's framing for knowledge-graph architecture.
- The post's "hollows out spaces for future development" phrase is the positive framing the Decision's Alternatives Considered sections lean on — deferral is not omission but reservation.
- The same author's 2009 [[Creating Shared Language and Shared Artifacts Post (Christopher Allen, 2009)]] and 2014 [[Deep Context Shared Languages Post (Christopher Allen, 2014)]] are upstream of other load-bearing commitments in this graph; this post sits alongside them as the architectural-layer companion to the earlier shared-language-layer work.

## Relations

- informs_downstream::[[Adopt Minimum-Viable-Architecture Stance]]
  - The Decision whose name and discipline specialize this Musing's MVA framing for DeepContext's scale. The Decision is the concrete application; this Reference is the framing substrate.

- informed_by::[[Open Integrity Project (Blockchain Commons, 2025)]]
  - Both Blockchain Commons works share the project's architectural stance. The OI project is a concrete application of MVA principles at the cryptographic-identity layer (layered specifications, modular components, interoperable interfaces for signing and verification); the Musing is the general framing those applications exemplify.
