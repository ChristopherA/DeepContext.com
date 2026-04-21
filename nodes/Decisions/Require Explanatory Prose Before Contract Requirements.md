---
created: 2026-04-19
tagline: A Contract opens with explanatory prose between the H1 and the Requirements section, orienting readers before they read the spec
brief_summary: A commitment that every Contract's body includes explanatory prose between the H1 and the `## Requirements` section. The prose names what the Contract is for, when it is used, how it relates to sibling Contracts, and what distinguishes the form from adjacent forms. It provides orientation, not a second source of truth — the Requirements section carries the normative spec, and the prose MUST NOT restate the Requirements in other words.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Require Explanatory Prose Before Contract Requirements

Every Contract's body opens with explanatory prose between the H1 and the `## Requirements` section. The prose states what the Contract is for — the form it specifies, when conformance is claimed, and what the form is not (the adjacent forms it distinguishes itself from). The prose orients a reader before they read the normative spec. It MUST NOT restate the Requirements in other words; the Requirements section is the single source of truth for obligation, and the prose is orientation.

## Why

The commitment orients **readers before spec-reading**. A reader arriving at a Contract wants to know, before parsing RFC 2119 keywords, what the Contract's form is, when they would conform to it, and what distinguishes this form from its siblings. The Requirements section answers "what does conformance require?"; the opening prose answers "what is this form, and should I be reading this Contract at all?" A Contract that opens directly with `## Requirements` forces the reader to reverse-engineer the Contract's purpose from its rules — a much higher cognitive cost than reading two or three orienting paragraphs first.

The prose carries **form distinctions that the Requirements cannot**. A Decision Form Contract's Requirements specify what a Decision's filename, identity block, and body must contain; the prose explains that a Decision is not a Conviction, not a Reference, not an Inquiry — and names what distinguishes each. Distinction-prose belongs above the Requirements because it shapes the reader's disposition toward the Requirements that follow. A reader who does not yet know whether their node wants Decision Form or Conviction Form reads the Requirements section differently from a reader who has already classified their node; the orienting prose is what enables the classification step.

The commitment's "MUST NOT restate the Requirements" clause is load-bearing. An orienting paragraph that summarizes the Requirements section in more readable language creates two sources of truth for obligation: when the Requirements section changes and the prose does not, readers who rely on the prose receive stale normative guidance. The prose's job is orientation — what the form is, when it applies, what makes it distinct — not compact re-expression of the spec. Specifying the form distinctively enough to enable self-classification is exactly what the prose is for; summarizing the spec is exactly what the prose must avoid.

The rule applies specifically to Contracts. Non-Contract nodes (Decisions, Convictions, Patterns, References, Observations, Aspirations, Glosses) have their own body-structure requirements governed by their own Form Contracts; the explanatory-prose commitment is Contract-specific because the Contract form is the one that pairs orientation and spec within a single document.

## Alternatives Considered

**Normative-first structure.** Let Contracts open with `## Requirements` directly, no explanatory prose. Rejected because it inverts the orientation/spec relationship. A reader needs to know the form before the rules make sense; without the prose, every reader reconstructs the form from the rules, and the reconstruction is uneven across readers. The prose's absence shifts authoring cost (the author did less) to reader cost (every reader does more), and the aggregate is higher than if the author wrote the prose once.

**Prose as optional introduction.** Let Contracts include explanatory prose at author discretion, encouraging but not requiring it. Rejected because optional-at-author-discretion effectively means "absent by default." Contracts written under time pressure would systematically omit the prose; the orientation benefit would live only in the strongest Contracts, not in the form's baseline. The Requirement is what ensures every Contract orients readers, not just the ones whose authors chose discipline.

**Redundant prose summarizing the spec.** Let the explanatory prose summarize the Requirements in more readable language, serving as a cheat-sheet for the spec. Rejected because it creates two sources of truth. A reader who reads only the prose-summary receives an approximation of the Requirements; a reader who reads the Requirements and then the prose finds them redundant. The MUST NOT restate clause is what keeps the prose focused on orientation and the Requirements focused on obligation.

## What Would Change It

The commitment would be revisited under one condition.

**Validator-first reading becomes dominant.** If Contracts are read primarily by build-time or curation-time validators — and human readers rarely encounter them directly — the orientation prose's benefit shifts toward the ignored-by-validator category. The revisit would move toward making the prose optional rather than removing it, since the human-reader benefit remains for the cases where humans do read Contracts. Current reading is human-first; the validator use case has been anticipated but not yet implemented. The commitment is carrying its weight for the current reader population.

## Relations

- grounded_in::[[Adopt Layered Node Structure]]
  - The layered-structure commitment requires each layer to be complete at its scale. The Contract's body tier has a specific structure — opening prose orients, Requirements section specifies, Relations structures edges. The opening prose is the claim-layer complement to the Requirements' spec layer; both are required for the body tier to be complete.

- informs::[[Contract Form Contract]]
  - Contract Form Contract's Body-precedes-Requirements Requirement carries the thin enforcement clause pointing at this Decision.
