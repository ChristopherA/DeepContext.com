---
created: 2026-05-04
tagline: When two graphs share a meta-layer, coordinate via per-node grafts and external wikilinks rather than git-level forks or merges; let neither graph claim canonical ownership of the shared structure
---

- conforms_to::[[Pattern Form Contract]]
- in_practice_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Coordinate at Content, Not at Git

## Heart

Two Deep Context graphs that share a meta-layer (Form Contracts, Predicates, Skills) cannot stay in sync by becoming the same git repository — each graph has its own `did:repo:<sha1>` cryptographic identity and its own first-steward stewardship. They cannot stay in sync by one becoming the other's fork — git-fork shares the parent's root commit and therefore shares the DID, collapsing the identity sovereignty each graph needs. They stay in sync by **content-level coordination**: per-node grafts that record per-node provenance, external wikilinks that let nodes cite each other without copying, and periodic refresh passes that pull current donor state into recipient grafts. Neither graph claims canonical ownership of the shared meta-layer; changes flow either direction at the content layer; the relationship is *peer coordination*, not *upstream propagation*.

The same shape applies to other infrastructure peer graphs share. The static-site build pipeline under `.scripts/` is byte-identical between peer graphs that adopt it; per-graph values (site brand, GitHub repo URL, custom domain) live in a sidecar (`.scripts/site_config.py`) imported by the canonical scripts. The pipeline becomes shared infrastructure with exactly one legitimately-graph-specific file. Either graph may lead a change to the canonical scripts; the other adopts via byte-equivalence the next time a peer steward looks at the diff. The mechanism differs from per-node grafts (no `grafted_from::` per file, no per-script provenance edge) but the underlying stance is the same: shared structure coordinates at content scope, not at git scope.

## Problem

Two graphs share a non-trivial meta-layer they both need to evolve. Each is a sovereign self-publishing graph with its own DID, its own pipeline, its own first steward. Neither wants to be the canonical owner of the shared structure — both want their own evolution. But the shared meta-layer is real: a Form Contract or Predicate that drifts between the two graphs creates incoherence at the citation layer (each graph's nodes claim conformance to slightly-different specifications). How do the two graphs stay legibly aligned without one of them becoming the source of truth?

The git-shape options collapse:
- **Same repository.** Defeats per-graph sovereignty and per-graph DIDs.
- **Git-fork (one repo, two URLs).** Shares the root commit and therefore shares the DID; identity collision.
- **Cherry-pick across forks.** Treats one graph as upstream and the other as downstream, baking in a hierarchy neither graph claims.
- **Manual file-copy with git unaware.** Loses provenance entirely; readers cannot trace what came from where.

## Forces

- **Sovereignty.** Each graph's identity is its own; neither can submit to the other without surrendering the per-graph-DID property the practice rests on.
- **Coherence.** The shared meta-layer must stay legible across graphs — readers and agents traversing one graph that grafted from another should encounter consistent conventions.
- **Bidirectional flow.** Coordination cannot be one-way push; insights from either graph should be able to flow into the other (the receiving graph chooses whether to adopt).
- **Friction.** Heavy sync mechanisms — required cadence, mandatory tooling, full pipeline duplication — burden every recipient and select against the lightweight downstream graphs the practice wants to enable.
- **Provenance legibility.** When content moves between graphs, a reader of either graph should be able to trace what came from where without external knowledge.

## Solution

Coordinate at the content layer using three composable mechanisms:

**Per-node grafts.** When recipient graph R wants donor graph D's specific node N, R copies N's content into its own `nodes/<Tax>/<N>.md` and adds a `grafted_from::[[<D's Reference proxy>]]` edge in N's identity block. The graft records per-node provenance without claiming graph-level lineage — most graphs are not scions, just recipients with grafts. The donor's DID and URL live in a local Reference node in R that proxies D, so the graft target resolves locally while the lineage stays explicit.

**External wikilinks for shared concepts neither graph wants to own.** When R's prose references a concept that D's graph defines, R uses `[[Taxonomy/Target]]↗` external-wikilink syntax. The build pipeline resolves the target against the donor Reference's URL, producing a clickable link to D's published version. R does not graft the node, does not duplicate D's content, and stays current with D's evolution automatically.

**Periodic refresh passes.** R's first steward periodically pulls current state from D for the grafted nodes — a manual pass, not an automated sync. The pass overwrites grafted node content with D's current version (preserving R-specific edits where present), refreshes the donor Reference body to reflect any new D additions, and runs the audit to catch drift the refresh introduces. The cadence is per-relationship; tagged-release on D plus periodic refresh on R is one workable pattern.

**Canonical pipeline scripts with a per-graph config sidecar.** When peer graphs share the static-site build pipeline (the scripts under `.scripts/`), the canonical scripts are kept byte-identical between graphs; per-graph values (site brand, GitHub repo URL, custom domain) live in a sidecar (`.scripts/site_config.py`) imported by the canonical scripts. The pipeline becomes shared infrastructure with exactly one legitimately-graph-specific file; non-config drift is visible via `diff -rq .scripts/` between peer worktrees and is drift to reconcile, not divergence to maintain. This is the script-layer realization of the same content-level-coordination shape per-node grafts realize at the node-content layer.

**Either graph may lead a change.** A change to a Form Contract, Predicate, Skill, or canonical script can originate in either graph. The graph where the change first lands carries it; the other graph picks it up on the next refresh (for grafted nodes) or on the next peer-diff pass (for canonical scripts). Neither graph is canonical; the move that benefits both gets adopted both ways.

## Consequences

**Bidirectional flow becomes natural.** Changes to the shared meta-layer can originate in either graph. The donor graph isn't locked into its role — a recipient that surfaces a useful refinement can offer it back, and the donor adopts it on the next cycle in either direction.

**Selective adoption is structural.** A recipient graph can adopt some changes from the donor without taking all of them; a donor can adopt some refinements from a recipient without imposing them on every recipient. Each graph's first steward decides what fits.

**Some drift between refresh cycles.** Between refresh passes, the recipient's grafted nodes may lag the donor's current state. The drift is bounded by the refresh cadence and made visible by the audit — not eliminated, but legible. Readers encountering a grafted node know it was copied at a specific point in time and can check the donor for current state.

**No canonical owner of the shared meta-layer.** This is the load-bearing consequence. The practice does not have a "main upstream" for Form Contracts and Predicates; it has graphs that share conventions and coordinate at content scope. New scions of the practice should expect this shape, not a single canonical source they pull from.

**The audit becomes a coordination tool.** Per-graph audits surface drift between donor and recipient. The audit is what keeps the coordination honest — without it, drift accumulates silently until a contributor encounters two slightly-different Form Contracts in two graphs and has to figure out which to follow.

## Instances

- **DeepContext.com ↔ eOS-DeepContext.** The two graphs share the meta-layer this pattern names. eOS-DeepContext grafted DC's Form Contracts, Predicates, and generic Skills at instantiation; subsequent refreshes pulled DC's evolutions (tagline-tightening Requirement, Touch Point Form Contract, OI/Minimum Viable Architecture spell-outs, the `is_home` and `hide_identity_block` frontmatter scalars). The "scion-vs-graph" rename and the `SITE_NAME` parameterization originated in eOS first and flowed back to DC. Neither graph is the canonical owner; the pattern is what makes the bidirectional flow legible.

  The 2026-05 `.scripts/` work realized the script-layer mechanism for the same two graphs. Per-graph constants (`SITE_NAME`, `GITHUB_REPO_URL`, `CUSTOM_DOMAIN`) moved to `.scripts/site_config.py`; an HTML-escape pass that had drifted between the graphs was reconciled to the canonical version; `diff -rq .scripts/` between the two worktrees now shows only `site_config.py` differing. Two bugs the script extraction surfaced — the Skill Form Contract's `runtime_name` field that the Anthropic Agent Skills runtime did not recognize, and the Graph Orient skill's Step 2 still pointing at `landing.md` after both graphs had migrated to home Touch Points — were caught and fixed in peer commits because both worktrees were locally available for diff and edit.

## Also Known As

- **Content-layer federation** — distinguishes from URL-layer federation (aggregator-as-service) and git-layer federation (forks). The federation is in the content, not in the infrastructure.
- **Peer coordination** — emphasizes the symmetric relationship; neither graph is master.

## Relations

- conforms_to::[[Pattern Form Contract]]
  - This Pattern declares compliance with the Pattern Form Contract's Heart-Problem-Forces-Solution-Consequences shape.

- grounded_in::[[Adopt Self-Sovereign Graph Publication]]
  - The Decision that makes per-graph sovereignty load-bearing — each graph carries its own DID via Open Integrity inception, refusing the git-fork-sharing-DID collapse. Without that commitment, the same-repository or git-fork options would be on the table; with it, content-level coordination is the only remaining shape.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that contributor vocabularies carry design decisions worth preserving. When two graphs share a meta-layer but one introduces a vocabulary refinement (the scion-vs-graph rename, for example) the bidirectional flow this Pattern names is what lets the refinement land in both graphs without forcing convergence prematurely.

- composes_with::[[grafted_from -- per-node content provenance from a donor graph]]
  - The Predicate that records per-node grafts is one of the three mechanisms this Pattern composes. The Pattern names the architectural shape; the Predicate is one of the structural tools the shape uses.

- composes_with::[[Graft -- a node copied from a donor graph into a recipient graph]]
  - The Gloss that names the unit-of-coordination at the per-node level.

- composes_with::[[Graph Audit]]
  - The Skill that surfaces drift between coordinated graphs. The Pattern's "periodic refresh" mechanism depends on having a way to detect when refresh is overdue or when refresh introduced inconsistency.

- contrasts_with::[[Adopt Self-Sovereign Graph Publication]]
  - The Decision rejects the git-fork option because it shares the DID; this Pattern names what fills the void left by that rejection — content-level coordination as the alternative to git-level coordination. The Decision says "not git-fork"; the Pattern says "what instead."
