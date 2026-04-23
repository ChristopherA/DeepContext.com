---
created: 2026-04-19
tagline: A Reference captures one artifact or a tight cluster; ecosystem cataloging does not belong in a Reference
brief_summary: A commitment that every Reference captures one external artifact or a tight cluster of closely-related artifacts (a primary gist and its two immediate follow-ups, a paper and its published errata). Ecosystem-level surveys — "all the related work in the space," "a catalog of adjacent tools" — do not belong in a Reference; they belong in the body of a `## Sources` section elsewhere, or in a dedicated Case Study node once that form contract is seeded. The rule keeps per-Reference signal clarity high.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Restrict References to Tight Artifact Clusters

Every Reference captures one external artifact or a tight cluster of closely-related artifacts. A tight cluster means: a primary artifact plus its immediate follow-ups (a gist and the two short posts answering questions about it), or a paper plus its published errata, or a repository and its companion documentation site. Ecosystem-level surveys — "all the related work in this design space," "a catalog of adjacent tools," "the full history of one tradition" — do not fit this rule and belong in a different container (body `## Sources` sections elsewhere, or a dedicated Case Study node once that form contract is seeded).

## Why

The commitment preserves **signal clarity per Reference**. A Reference captures what one source contributes to this graph — its role, what the project adopts from it, what the project declines. When a Reference is cluster-scoped, the body answers these questions crisply: here is the primary artifact and its two follow-ups; here is what this project adopts from the cluster as a unit; here is what it declines. When a Reference is ecosystem-scoped, the body becomes a catalog — each entry's role, adoption, and decline diluted across many entries, and the Reference's per-entry signal drops.

The rule is about the Reference form's **scale** versus the question's scale. A reader citing a Reference by wikilink asks one thing: what does this Reference contribute? A tight-cluster Reference gives a crisp answer; an ecosystem Reference gives a sprawling one that makes the citation ambiguous ("does citing this Reference mean citing the whole ecosystem, or one artifact in it?"). The rule picks the Reference scale to match the citation scale.

Two sources that play distinct roles must be split into separate References, even when the same author produced both. **Role separation is the primary splitting criterion; authorship is secondary.** A paper articulating a design principle and a repository implementing that principle are two References with two roles (`serves_as::[[Structural Pattern Source]]` and `serves_as::[[Reference Implementation]]`); lumping them into one Reference would force the `serves_as::` predicate to carry both roles or to lose specificity. The tight-cluster exception is for artifacts that play the *same* role — a primary and its immediate follow-ups are all playing the "primary convention source" role, just at different levels of detail.

Ecosystem-level content does not vanish; it moves. When the project wants to record "the five main tools in this space" or "the full taxonomy of related methodologies," that content belongs in a dedicated form — a Case Study node when the Case Study Form Contract is seeded, or a narrative `## Sources` section inside a Decision or Conviction that needs to place the project's work in a broader landscape. Each destination carries the ecosystem content at the scale and role it warrants.

## Alternatives Considered

**Ecosystem-cataloging References.** Permit References to catalog a full tradition or design space — all related work, all adjacent tools. Rejected because the Reference form's purpose is specific-source contribution, not landscape surveying. An ecosystem Reference can be written, but it trades specificity for breadth and makes every citation a citation of "the whole space" rather than of what a particular artifact contributes. The form bends but does not hold.

**One Reference per tradition regardless of artifact count.** Create one Reference per tradition and list all artifacts inside. Rejected for the same reasons [[Disambiguate Reference Artifacts from Traditions]] separates artifacts — per-artifact citation specificity is lost; the `serves_as::` predicate cannot distinguish the roles played by different artifacts within the tradition.

**Split every Reference to atomic-artifact granularity.** Never bundle artifacts; every gist, every post, every paper gets its own Reference. Rejected because tight clusters genuinely hang together. A primary gist with two immediate follow-ups functions as a single source for citation purposes — the follow-ups elaborate but do not change the gist's role or what the project adopts. Splitting them into three References produces three near-duplicate adoption accounts. The tight-cluster exception admits bundling at the natural joint.

## What Would Change It

The commitment would be revisited under one condition.

**Ecosystem-level reasoning becomes common and warrants dedicated References.** If the project accumulates use cases where ecosystem surveys are genuinely load-bearing — where downstream Decisions cite "the full design space" rather than specific artifacts — the rule would produce content with no proper home. The revisit would introduce an ecosystem-survey form (perhaps Case Study Form Contract or a new Survey Form Contract) to host this content at the form scale that fits it. The tight-artifact Reference rule would remain for source-specific References; the ecosystem content would get its own form. Current project needs have not produced ecosystem-scale citation pressure; the revisit condition is latent.

## Relations

- grounded_in::[[Disambiguate Reference Artifacts from Traditions]]
  - The artifact/tradition disambiguation commitment separates artifacts that warrant separate References. This commitment establishes the complementary scale rule: within one Reference, the content is tight-cluster, not ecosystem.

- grounded_in::[[Distinguish Adopted from Not-Adopted in References]]
  - The adopted/not-adopted commitment makes Reference bodies accountable to specific adoption claims. Ecosystem-scale References cannot be accountable in the same way — a catalog's adoption claims would be diffuse. The tight-cluster scale keeps the adoption distinction maintainable.

- informs_downstream::[[Reference Form Contract]]
  - Reference Form Contract's "When to split or consolidate" Requirement carries the thin enforcement clause pointing at this Decision.
