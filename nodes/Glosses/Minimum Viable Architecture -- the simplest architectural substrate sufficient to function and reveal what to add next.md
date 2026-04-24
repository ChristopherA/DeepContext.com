---
created: 2026-04-23
tagline: The simplest architectural substrate sufficient to function and reveal what to add next
brief_summary: A design discipline naming the minimum architecture a project commits to in its first cycle -- enough structural shape to let the practice run end to end and enough hollowed-out space to absorb what use reveals must be added later. Distinguished from Minimum Viable Product, which optimizes for market validation through delivered features; Minimum Viable Architecture optimizes for structural validation through practice. The "viable" half is functional sufficiency; the "architecture" half is structural decisions rather than feature scope. Capabilities deferred under MVA are reservation rather than omission -- space left for the choices a future cycle will be in a position to make. The Allen 2024 Musing is DeepContext's direct source for the concept's name and framing; the Adopt Minimum-Viable-Architecture Stance Decision specializes the discipline for this graph's scale.
---

- conforms_to::[[Gloss Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Minimum Viable Architecture

The simplest architectural substrate sufficient to let a practice function end to end while leaving room for what use reveals must be added next. The "viable" half names functional sufficiency -- the substrate works for the practice as it currently runs. The "architecture" half names structural decisions -- the substrate is about how parts compose and persist, not about which specific features ship. The discipline is the deliberate restraint of building only what the practice needs to run and treating everything else as space reserved for a future cycle's design choice rather than as feature debt.

The concept is distinguished from Minimum Viable Product, which optimizes for market validation through the smallest set of delivered features that can attract users. MVA optimizes for structural validation through the smallest set of structural commitments that can let the practice reveal what it actually needs. The two have different test conditions: MVP's test is users; MVA's test is practice. A project applying MVA may build something that is not yet usable in the MVP sense -- the goal is not yet to attract users but to discover what the architecture must support before users would arrive.

The discipline cuts in two directions. Capabilities not yet built are reservation rather than omission -- they are *space left for* tomorrow's design choices, made when the practice has revealed what those choices need to look like. Capabilities built before they are needed are not free -- they accumulate as maintenance surface that filters who can continue participating, often before any contributor has surfaced the need. Both deferral discipline and pre-emptive caution against building-for-anticipated-need are part of the same stance.

## Sources

- [[Minimum Viable Architecture Musing (Christopher Allen, 2024)]] -- the Blockchain Commons Musing this Gloss's framing comes from directly. Allen's post originates the term and contrasts it with MVP at the cryptographic-protocol-architecture layer; this Gloss carries the concept forward at the knowledge-graph layer DeepContext occupies.
- Adapted from `glosses/Minimum Viable Architecture` in Christopher Allen's personal knowledge garden (obsidian-pkm), 2026-03. The garden articulation generalizes the concept across personal-PKM and infrastructure-architecture contexts; this Gloss preserves the same generality without importing the garden-specific instances.

## Relations

- informs_downstream::[[Adopt Minimum-Viable-Architecture Stance]]
  - The Decision that adopts this concept as DeepContext.com's first-cycle discipline. The Decision specializes this Gloss's general framing for this graph's scale -- naming the specific deferred capabilities (heading-link resolution, transclusion, graph explorer, search, theming, collaboration tooling), the Revisit Conditions that would change them, and the asymmetry between firmly-deferred and softly-deferred capabilities.

- composes_with::[[Convention Overhead vs Graph Quality -- the ongoing trade-off between the cost of each convention and the quality the convention enables]]
  - Both Glosses name disciplines for evaluating proposed structural additions. Convention Overhead vs Graph Quality is the trade-off; MVA is the discipline applied to that trade-off in first-cycle work -- when the trade-off is unclear, defer.
