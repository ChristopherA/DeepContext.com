---
created: 2026-04-20
tagline: Contributors with different naming traditions co-author the same graph through translation layers, without convergence pressure collapsing any contributor's vocabulary
brief_summary: An Aspiration that the project demonstrates cross-vocabulary collaboration — contributors with different naming traditions co-author a shared graph, and each contributor's vocabulary stays legible to the others through glosses, named cross-references, and translation annotations rather than through normalization into a single shared ontology. The target is the specific test case for whether the Vocabulary Diversity Is a Feature Conviction and the Translation Over Convergence Conviction hold under plural-contributor pressure. The gap is concrete: no multi-vocabulary authoring has been tested, the seed graph is single-author, glosses that would ground cross-vocabulary translation are mostly ghost links, and no contributor onboarding path exists.
---

- conforms_to::[[Aspiration Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Contributors Across Vocabularies Can Collaborate

The project works toward a state in which contributors with different naming traditions can co-author a shared graph without being forced to converge on one vocabulary. Each contributor's vocabulary stays legible to the others through translation layers — glosses, named cross-references, annotated edges — rather than through normalization into a single shared ontology.

## Why It Is Worth Pursuing

Vocabulary Diversity Is a Feature and Translation Over Convergence are stances the project currently holds, but both stances are unvalidated until a multi-vocabulary authoring case tests them. A single author writing in a single vocabulary cannot produce the pressure that reveals whether the conventions actually support plural vocabularies — the author's own predicates accumulate without friction, and translation never has to carry load. The cross-vocabulary case is the first situation where the stances earn their weight.

The Aspiration also specializes the project's core success metric. The Second Cycle of Contribution Happens names a general sustainability target; this Aspiration names the specific form of second-cycle success that the vocabulary-diversity Convictions commit the project to. A second cycle reached by flattening contributor vocabularies would not satisfy this Aspiration — the conventions would have held in form while drifting in substance. The cross-vocabulary test forces the distinction.

The test also produces information the project cannot get any other way. Every point at which a new contributor's predicates fail to land cleanly, every gloss that is missing between vocabularies, every review that reaches for normalization — each is a specific observation that improves the conventions. A graph authored by one person cannot surface these; a graph authored across vocabularies cannot hide them.

## Current Gap

No multi-vocabulary authoring has been tested. The seed graph carries the founding author's predicates and classification vocabulary; no second author has introduced a divergent tradition, no translation has had to be written, no review has had to navigate between two contributors' distinct predicates. The translation surface is unexercised.

Glosses that would ground cross-vocabulary translation are mostly ghost links. The Reference Form Contract's `serves_as::` vocabulary, for instance, references `[[Primary Convention Source]]`, `[[Structural Pattern Source]]`, and `[[Federation Precedent]]` as target concepts that do not yet have gloss nodes. These are the kinds of nodes that would carry translation between contributors' vocabularies when the first cross-vocabulary pressure appears, and they are not yet seeded.

No contributor onboarding path exists. A new contributor arriving at the graph today can read `CONVENTIONS.md` and the Contract nodes, but has no walkthrough of how to introduce their own predicates, how to document a translation between their vocabulary and the existing one, or how to signal to reviewers that a proposed rename would be a convergence move the project rejects. The onboarding surface is implicit in the existing conventions; explicit onboarding does not exist.

The founding author's agent-curator configuration is itself a vocabulary. Claude's curatorial behavior — which predicates it suggests, which shapes it flags, which conventions it treats as stable — encodes the founding author's vocabulary decisions. A second contributor with divergent predicates encounters not just the first author but the first author's agent configuration; whether that agent translates or normalizes determines whether the cross-vocabulary Aspiration is achievable at all.

## Work It Asks

Seed the first non-founder contributor. The contributor does not need to produce a large volume of nodes; even a handful of nodes authored in a divergent vocabulary is enough to exercise the translation surface. The target is not contribution volume but cross-vocabulary coverage.

Seed glosses that translate between the founder's vocabulary and the incoming contributor's. Each cross-vocabulary pairing produces specific translation work — a gloss entry naming each term, a cross-reference showing how they correspond, an annotation naming what each preserves that the other does not. The work is small per pairing but accumulates as the translation layer matures.

Run the first curation pass across two vocabularies. The pass should report what translation required, which predicates needed glosses, which cross-references had to be added, and where normalization pressure appeared in the curator's suggestions. The pass is as much a diagnostic of the curator's translating-versus-extracting mode as it is a maintenance operation on the graph.

Test whether new predicates added by a second contributor stay first-class rather than being rewritten. The test is procedural: does the review surface accept the new predicate as a distinct edge, or does it propose rewriting? Does the next curation pass keep the predicate in `CONVENTIONS.md`, or does it consolidate it silently? The answer determines whether the Aspiration is on track or already drifting.

## Progress Recognition

Two or more contributors with distinct naming preferences author nodes in the same graph. The distinction is verifiable: contributors' nodes carry predicates the other contributors did not use, and those predicates remain in place after review.

Translation glosses accumulate as vocabularies meet. Each new cross-vocabulary pairing adds a gloss entry or cross-reference; the glossary grows in proportion to the divergence the contributors bring, not in proportion to the number of nodes.

A curation pass reconciles the graph through translation rather than merging. The pass's output is a diff of glosses and cross-references added, not a diff of predicates renamed to canonical forms. Where translation was needed, it was written; where normalization was tempting, the pass resisted.

A new contributor's predicates survive into the graph's standing vocabulary rather than being rewritten into existing ones. `CONVENTIONS.md`'s predicate list grows by accretion as new contributors join, and the growth is visibly attributable to specific contributors' traditions.

The agent-curator configuration demonstrably operates in translating mode across multiple contributors' vocabularies. A cross-vocabulary session produces curatorial suggestions that respect each contributor's predicates rather than proposing convergence; where the agent did suggest normalization, the suggestion was flagged and corrected.

## Sources

- `CONVENTIONS.md` — the "Scope of these conventions" section names cross-contributor vocabulary diversity as the project's test case; the "Contributor vocabulary" section specifies the translate-don't-converge instruction this Aspiration's work depends on.
- `context/Founding Conversation.md` — the "What was considered" and "The question" sections name diverse knowledge workers (not software engineers, not a single organization) as the intended contributor population; cross-vocabulary collaboration is the concrete form that diversity takes.

## Relations

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction names the stance this Aspiration tests. The Aspiration is the directional target that takes the Conviction seriously — without the Conviction, cross-vocabulary collaboration would be a feature preference; with it, cross-vocabulary collaboration is the success case the stance commits the project to.

- grounded_in::[[Translation Over Convergence]]
  - The Conviction names the operational rule this Aspiration's work follows. Every move the work asks — seed the first non-founder contributor, seed translation glosses, run curation across two vocabularies — is a concrete instance of the translation-over-convergence rule applied at the plural-contributor scale.

- grounded_in::[[The Second Cycle of Contribution Happens]]
  - The second-cycle Aspiration is the general target this Aspiration specializes. The cross-vocabulary Aspiration names a specific dimension of second-cycle success — the specific form that sustainability takes when the sustainability includes contributor vocabulary plurality.

- informed_by::[[Adopt Wikilinks and Named Edges]]
  - The substrate Decision whose plurality property this Aspiration tests. The Decision commits the graph to author-declared edges with contributor-vocabulary plurality as a property; this Aspiration is the test case for whether the plurality property holds when plural contributors actually arrive.

- informed_by::[[Participation Takes Different Forms Not Different Levels]]
  - The Observation names form-plurality as an adjacent property to the vocabulary-plurality this Aspiration targets. Contributors bring both different naming traditions and different participation forms; a plural-participation stance that preserves vocabulary-plurality and collapses form-plurality is partially inconsistent. The Observation grounds the extension.

- composes_with::[[Participation Diversity Is Legible and Valued]]
  - Adjacent specialization of the same plural-participation stance at a different layer. This Aspiration targets vocabulary-plurality; the companion Aspiration targets form-plurality. Both are load-bearing; neither subsumes the other; the two compose into a plural-participation stance that operates at both layers.
