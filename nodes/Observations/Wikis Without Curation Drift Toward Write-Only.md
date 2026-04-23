---
created: 2026-04-20
tagline: Collaborative wikis without active curation practice drift toward write-only dynamics — contributors add, but readers cannot navigate and newcomers cannot onboard
brief_summary: A Retrospective Observation that reconstructs a recurring failure pattern across multiple collaborative-wiki attempts. Without active curation practice — vocabulary tending, ontology reconciliation, link integrity, onboarding surface maintenance — wikis accumulate nodes that cannot be navigated, arbitrate ontology questions that stall decisions, concentrate bus factor in whoever does the bookkeeping, and close the onboarding path. The pattern is grounded in reconstructed community experience of wikis across several traditions (Federated Wiki, Agora, Massive Wiki, personal-wiki traditions) rather than in a controlled study; the record's limit is that no attempt has run the counterfactual of identical-wiki-with-curation versus identical-wiki-without.
---

- conforms_to::[[Observation Form Contract]]
- has_epistemic_status::[[Retrospective Observation]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Wikis Without Curation Drift Toward Write-Only

Collaborative wikis operated without active curation practice drift toward write-only dynamics. Contributors continue adding nodes, but readers cannot navigate the accumulation, ontology decisions stall in arbitration, the bus factor concentrates in whoever does the bookkeeping, and newcomers cannot find an onboarding path into the existing material. The drift is the failure mode the Deep Context practice is designed to address.

## Grounds

The record rests on reconstructed community experience across several collaborative-wiki traditions. Federated Wiki (Ward Cunningham) developed a rich architecture and a small committed community but has not sustained mass contribution — reader navigability of the federation remains the open problem. Agora and Anagora experiments sustained contributor enthusiasm for a period and accumulated material, then slowed as the link-integrity and ontology-reconciliation work outpaced contributor willingness to do bookkeeping. Massive Wiki has produced multiple garden instances with the same pattern — an active seeding phase, then a plateau when the maintenance overhead becomes visible. Personal-wiki traditions (digital garden, Obsidian public vaults, Zettelkasten publications) show the same dynamic at single-author scale: the garden thrives under the author's active curation and decays when the author's attention moves elsewhere.

The Founding Conversation names this pattern as the project's motivating problem: "Prior attempts at this — wikis of various shapes — have stalled from a mix of technical and cultural obstacles: ontology fights, curation burden, write-only dynamics, bus factor, onboarding friction." The `External Sources` document supplies the annotated list of the specific wiki traditions the founding exploration reviewed, each with a structural note on what worked, what did not, and what Deep Context chose to adopt or decline.

The record's limits are substantive. No collaborative wiki has run a controlled counterfactual — identical wiki with active curation versus identical wiki without — and the observed pattern could be confounded by community-specific factors (size, domain, platform friction, maintainer incentives) that curation discipline alone does not address. The claim is that write-only drift appears reliably across the reviewed cases, not that curation discipline is sufficient to prevent it in any particular case. The Observation supports the hypothesis that active curation is *necessary*; it does not prove it *sufficient*.

## What Would Revise It

A documented case where a large collaborative wiki sustained contributor engagement, reader navigability, and newcomer onboarding over multiple years without active curation practice — no vocabulary tending, no ontology reconciliation, no link-integrity maintenance, no onboarding-surface upkeep — would revise the claim. The revision would be particularly strong if the case's surrounding community and domain were comparable to the traditions already reviewed.

A demonstrable mechanism that removes the curation-burden pressure — automated curation at sufficient quality to carry the vocabulary-tending and ontology-reconciliation load without human attention — would also revise the claim. The Deep Context practice is a partial test: if agent-mediated curation at current capability levels can sustain a multi-contributor graph past the point where comparable manually-curated wikis plateaued, the Observation would need to account for the mechanism.

The project's own experience is itself in the record's tail. If the Deep Context practice reaches a second cycle of contribution without write-only drift — or if it drifts despite the conventions — the case becomes additional evidence in whichever direction the outcome runs.

## Sources

- Allen, Christopher. "Wikilinks and Named Edges," 2026 — the gist's "gardening metaphor" and vocabulary-maintenance sections supply the specific failure modes (redundant predicates, ambiguous predicates, vocabulary drift) that this Observation generalizes across non-predicate-level curation work.

## Relations

- informs_downstream::[[Deep Context as an Architecture for Captured Reasoning]]
  - The architecture decision's emphasis on structural contracts, progressive disclosure, and typed relations follows from this Observation — the write-only failure mode is what the architectural moves are designed to counter. The Decision is the response; this Observation is the grounds.

- informs_downstream::[[The Second Cycle of Contribution Happens]]
  - The second-cycle Aspiration is defined against this Observation as its failure mode. A wiki that fails at the second cycle has drifted toward write-only; the Aspiration is the target of sustained contribution this Observation's drift describes the absence of.

- informs_downstream::[[Reconcile the Standing Account]]
  - The Pattern names the recurring curation move — audit for drift between what a node says and what the graph now is, collapse duplication to pointers, realign stale counts and references. The move is what active curation practice looks like in operation; this Observation is the motivating case for why the Pattern is worth running as a cadence rather than an occasional cleanup.

- informed_by::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The gist's gardening-metaphor and vocabulary-lifecycle sections supply the micro-level failure modes (weed predicates, un-tended vocabularies, precedent poisoning) this Observation generalizes to the wiki-maintenance level.

- informed_by::[[Agora Project (Flancian, 2019)]]
  - The Observation's Grounds reconstruct the write-only plateau pattern partly from Agora and Anagora — sustained contributor enthusiasm for a period, then a slowdown as link-integrity and ontology-reconciliation work outpaced contributor willingness to do bookkeeping. This Reference is the specific source the Grounds reference at that layer.

- informs_downstream::[[LLM Assistance Widens the Participation Gap]]
  - The write-only failure mode at the system level and the LLM-assistance rejection pattern at the contribution-review level compose. Without curation, contributions accumulate; with curation of the current Wikipedia style, newcomer LLM-assisted contributions are filtered at the membership-fluency register. This Observation names the mechanism at one layer; the LLM Observation names a specific mechanism at a different layer.

- informs_downstream::[[Meaningful Wiki Contribution Requires Both Pride and Humility]]
  - The system-level failure mode (this Observation) and the trait-level filtering (the pride-humility Observation) describe the same failure at different layers. The aggregate write-only drift results from trait-level filtering on the contributor tail; the two Observations compose into a two-layer account.
