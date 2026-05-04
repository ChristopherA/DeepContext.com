---
created: 2026-05-04
tagline: A Reference node's URL must resolve to a publicly-accessible artifact every reader can fetch — not a private path, sibling-project filesystem location, or otherwise reader-specific resource
brief_summary: A Reference node anchors an external source the graph draws from. The Reference's value depends on a reader being able to follow the URL to the source itself; if the URL resolves only for the original author or for some specific local environment, the Reference is opaque to everyone else and the graph carries a citation it cannot honor. This Decision commits Reference URLs to artifacts every reader can fetch — public web pages, archived gists, published papers, repositories with public access. Sibling-project filesystem paths (`~/Workspace/skotos-dev/deliverables/...`), corp-internal share links, ephemeral session URLs, and other reader-specific locations are explicitly disallowed as Reference targets. The reasoning: a graph's Reference layer is part of how the graph survives its author stepping away; if Reference URLs assume the author's local context, the survival claim is false. The Reference Form Contract enforces this Requirement; nodes failing it should either be rewritten against a public-equivalent URL, demoted to inline citation prose with the path noted as a private trace, or removed.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-05-04
- in_practice_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Reference Targets Must Be Resolvable to Other Readers

A Reference node anchors an external artifact this graph draws from. The Reference carries the artifact's URL so any reader who wants to verify, extend, or contest the citation can fetch the source for themselves. The URL therefore has to resolve for someone other than the original author — a public page, an archived gist, a published paper, a repository with public access, or some equivalently-fetchable artifact.

Reader-specific URLs are explicitly disallowed as Reference targets. A path like `~/Workspace/skotos-dev/deliverables/foo.md` resolves only on the original author's machine and only while the sibling project's filesystem layout matches what the Reference was authored against. A Confluence link behind corp SSO resolves only for employees of that corporation. A session-bound URL resolves only during the original author's session. Each of these cases produces a Reference that *looks* citable but is not — readers other than the author cannot follow the citation, and the graph silently carries a broken claim.

## Why

A Reference's value depends on the reader being able to follow it. Reading a node's prose and seeing `[[Some Reference]]` carries one specific promise: *if you want to check this, here is where to look*. The node's local content might be entirely correct, but the Reference's value to the reader depends on the reader's ability to actually visit the source. A Reference whose URL the reader cannot fetch is a citation the graph cannot honor.

The Reference layer is also part of how a Deep Context graph survives the original author stepping away. The graph's content is plain markdown, the conventions are documented inline, and the references are external sources future readers can re-trace independently. If References point at the author's local environment, the survival claim is false at the citation layer — the graph's verifiability dissolves with the author's local context.

The Decision is small but load-bearing because Reference authoring is a tempting place for shortcuts. A draft might cite `~/Workspace/skotos-dev/deliverables/the-thesis.md` because that path is the author's working location for the artifact; later when the artifact is published, the Reference URL is meant to be updated. In practice, these get authored, the cycle of "publish later" doesn't complete, and the Reference is left with a private path. The Requirement makes the test mechanical: the Reference Form Contract checks the URL resolves before merge, treating the resolvability constraint as a structural rule rather than a stylistic preference.

The Decision is grounded in a specific incident. The eos-harness Minimum Viable Architecture workstream's `FX-6` misstep authored two Reference nodes against `~/Workspace/skotos-dev/deliverables/...` paths before the resolvability test was applied. Those Reference nodes carried correct local-context information for one reader and were unverifiable for everyone else. Catching it made the principle visible; codifying it as a Decision makes the principle universal across graphs.

## Alternatives Considered

**Allow private Reference URLs with annotation.** Permit references to private paths so long as the body annotates "author-only path" and explains what the source is. Rejected because the annotation does not make the URL fetchable by other readers — it only makes the unfetchability explicit. The Reference promises a clickable path to a source, and an annotated private path violates that promise structurally; the annotation is at best a confession that the citation is broken.

**Allow embargoed sections of References.** Permit a Reference whose URL is intentionally not yet public, with the expectation that the URL becomes public later. Rejected because the embargo creates an asymmetric trust model — the author claims something the reader cannot verify until the embargo lifts, and there is no graph-layer mechanism to detect or expire the embargo. If a draft cites unpublished material, the citation belongs in inline prose noting the unpublished status, not in a Reference node that presents itself as a verifiable citation.

**Symbolic placeholder targets.** Reference URLs that point at a local-or-stub location with a redirect rule that resolves to the canonical URL when present. Rejected because it adds a redirect layer that every reader's tooling must understand, and the redirect rule itself becomes a load-bearing piece of infrastructure that the graph depends on. The simpler discipline — only commit a Reference when its URL is genuinely fetchable — has the same effect with no redirect machinery.

**Allow `↗` markers without resolvable URLs.** Permit a `[[Reference]]↗` external marker pointing at a Reference whose URL cannot be resolved. Rejected because the `↗` already signals "this is in another graph"; it cannot do double duty as "this URL might or might not be fetchable." The two states have different reader implications and need different vocabulary.

## What Would Change It

**A graph-layer embargo mechanism.** If the practice grows to need embargoed References (cited material temporarily off-public), a separate Predicate (`embargoed_until::<date>` or similar) and a build-time check could carry the embargo state explicitly. With that mechanism, the Decision could relax to "Reference URLs must resolve OR carry an explicit embargo edge with an expiry" — the embargo becomes structurally legible rather than a hidden author commitment.

**Extension to private graphs.** This Decision is for public graphs that intend to survive their authors. A private graph operating within a closed organization may legitimately reference private resources its readers can in fact access. If Deep Context develops a recognized "private graph" mode, the Decision could narrow to "public graphs require public-resolvable Reference URLs" with private graphs choosing differently.

**A different reader-verification mechanism.** If the practice develops content-addressable references (DID-tagged artifacts where the content is fetchable by hash from any of multiple hosts), the URL constraint could relax to "the Reference must carry a content-addressable identifier, with the URL as one optional resolver." That would let URLs become unstable while preserving the verifiability promise. The Open Integrity Project's `did:repo:<sha1>` form is the closest precedent at the repository layer; node-level addressing via Scion Address extends the pattern.

## Relations

- conforms_to::[[Decision Form Contract]]
  - This file is itself a Decision; it conforms to the Form Contract specifying what Decision nodes look like (Why / Alternatives Considered / What Would Change It / commitment level).

- in_practice_domain::[[Deep Context Architecture]]
  - The principle applies across the Deep Context architecture as a whole — every Deep Context graph that authors References inherits this Requirement via the Reference Form Contract that grounds in this Decision.

- informs_downstream::[[Reference Form Contract]]
  - The Reference Form Contract grounds in this Decision via a `grounded_in::` edge: the Contract's URL-resolvability Requirement is the structural enforcement of this Decision's commitment.

- grounded_in::[[Knowledge Outlives Its Tools]]
  - The Conviction that the graph's content survives its tools applies to its References too: a Reference whose URL resolves only for the author dies with the author's local environment. Public-resolvable URLs are how References extend the survival commitment to the citation layer.

- grounded_in::[[Capture Reasoning, Not Just Knowledge]]
  - References are part of how reasoning travels — readers follow citations to verify the chain. A broken citation breaks the chain at the reader's end. Public-resolvable URLs preserve the reasoning's verifiability for readers other than the author.

- informed_by::[[The Second Cycle of Contribution Happens]]
  - The Aspiration that second-cycle contributors arrive and either complete the cycle or reveal that the conventions cannot hold. A second-cycle reader who hits an unfetchable Reference URL is an early signal that the conventions have not held; making URL resolvability a structural Requirement is one of the conventions the Aspiration counts on.
