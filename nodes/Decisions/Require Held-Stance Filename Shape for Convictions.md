---
created: 2026-04-19
tagline: Conviction filenames read as held stances — never action-verb leads or Subject-as-Role declaratives
brief_summary: A commitment that Conviction filenames take held-stance shapes — scoped authority claim, value declaration, directional commitment, bounded stance, or subject-carries-object declarative — and MUST NOT use action-verb leads (`Adopt <X>`, `Use <X>`, `Prefer <X>`, `No <X>`) or `<Subject> as <Role>` declaratives. Those two shapes belong to Decisions; a filename conforming to either classifies as a Decision, not a Conviction. The filename shape enforces the Decision-vs-Conviction distinction at the cheapest classification tier.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Require Held-Stance Filename Shape for Convictions

Every Conviction filename reads as a held stance the reader can assess as held-or-not-held by the project. Typical shapes include scoped authority claims (`Human Authority Over Augmentation Systems`), value declarations (`Vocabulary Diversity Is a Feature`), directional commitments (`Content Over Container`), bounded stances (`Translation Over Convergence`), or subject-carries-object declaratives (`Folders Serve Human Legibility, Not the Graph`). The filename MUST NOT begin with an imperative action verb (`Adopt <X>`, `Use <X>`, `Prefer <X>`, `No <X>`) and MUST NOT use the `<Subject> as <Role>` shape. Those shapes belong to Decision Form Contract; a filename conforming to either classifies as a Decision, not a Conviction.

## Why

The commitment **enforces the Decision-vs-Conviction distinction at the filename level**. A Decision is a situational commitment the project made at a moment with revisit conditions; a Conviction is a held normative stance the project holds over time without situational dating. The two forms share a domain — both commit the project to how something ought to be — but they differ in temporality and accountability. Decisions are accountable through `decided_on::` dates and `has_commitment::` levels; Convictions are accountable through drift recognition and what-it-asks elaboration. The filename carries the distinction before any body is read.

Filename-shape-carries-form extends the prototype's general classification-by-filename discipline (which [[Name Decisions by Action Verb or Role Declarative]] applies to Decisions and [[Use Double-Hyphen Separator for Gloss Definitions]] applies to Glosses). A reader scanning the Convictions folder knows each file is a Conviction by filename shape — no action verbs, no `as Role` declaratives. A reader scanning the Decisions folder knows each file is a Decision by the mirror shape rules. The two folders and the two rules compose: if a filename shape fits a Decision, it does not fit a Conviction, and vice versa.

The rule **prevents mis-classification by filename shape**. An author uncertain whether a commitment is a Decision or a Conviction writes a filename that fits one shape, and the shape forces the classification. An author who wants to write "Adopt Vocabulary Diversity" as a Conviction finds the action-verb shape forbidden; the forced rewrite to "Vocabulary Diversity Is a Feature" or "Adopt Vocabulary Diversity as Value" clarifies which form the author actually intends. The filename-shape rules are diagnostic as well as prescriptive — they surface the form question at the authoring moment.

A bare noun phrase (`Human Authority`, `Vocabulary Diversity`) does not satisfy the rule. Bare noun phrases read as topics the node describes, not as stances the node holds. The rule does not permit them because the Conviction form's whole contribution is recording a specific stance, not a topic. The recommended rewrites — `Human Authority Over Augmentation Systems`, `Vocabulary Diversity Is a Feature` — carry the stance in the filename itself.

## Alternatives Considered

**Runtime type disambiguation via predicates.** Let any filename shape be permitted and distinguish Decisions from Convictions by `conforms_to::` predicate alone. Rejected because filename-level classification is the cheapest tier. Reading each file to check its `conforms_to::` predicate is an order of magnitude more expensive than scanning the filename; filename-shape conventions are what let classification be a folder-view operation. The predicate is still required for graph participation, but filename shape is what makes the predicate unnecessary for casual classification.

**Permit action-verb leads on Convictions when the stance reads as a directive.** Let `Adopt Human Authority` work as a Conviction filename. Rejected because action verbs read as situational commitments ("we adopted this at this time"), which is Decision territory. A stance read as a held directive still reads as a move the project made, which is what Decision filenames are for. The forced-stance rewrite (`Human Authority Over Augmentation Systems`) preserves what the author meant — the stance itself — in a filename shape that does not overlap with Decisions.

**Permit `<Subject> as <Role>` on Convictions.** Let the Decision-form `<X> as <Y>` declarative also be valid for Convictions when the stance reads that way. Rejected because the declarative explicitly frames the subject as playing a committed role — "Deep Context as an Architecture for Captured Reasoning" commits to a specific interpretive frame. Convictions hold stances rather than committing to interpretive frames; the shape overlap would blur the distinction the filename-shape rules exist to preserve.

## What Would Change It

The commitment would be revisited under one condition.

**Filename shape proves insufficient and predicate-only typing becomes reliable.** If tooling or conventions grew the ability to disambiguate Decisions from Convictions by `conforms_to::` predicate at every reading surface — folder views, search results, inline citations — the filename-shape discipline would become a convention without its load-bearing purpose. The shape rules would remain for authoring diagnostic (surfacing form questions at the authoring moment) but would no longer be the cheapest classification tier. Current tooling does not provide universal predicate-level classification; the filename-shape rules carry their weight.

## Relations

- grounded_in::[[Name Decisions by Action Verb or Role Declarative]]
  - The Decision-form filename-shape rule is the mirror commitment. Decisions must use action-verb or Subject-as-Role shapes; Convictions must not. The two rules compose — a filename that fits one does not fit the other, and classification follows the filename.

- informs_downstream::[[Conviction Form Contract]]
  - Conviction Form Contract's filename pattern Requirement carries the thin enforcement clause pointing at this Decision.

- contrasts_with::[[Decision Form Contract]]
  - The Conviction/Decision distinction the filename shape preserves is load-bearing for how each form handles commitment. Decisions commit situationally (with `decided_on::` and `has_commitment::`); Convictions hold stances without situational dating. The filename rule is the first tier of the distinction.
