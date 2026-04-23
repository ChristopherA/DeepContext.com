---
created: 2026-04-19
tagline: Form-specific predicates stay on their forms — commitment predicates on Decisions, epistemic status on Observations, role on References
brief_summary: A consolidated commitment that form-specific predicate vocabularies are reserved to the forms they classify. `has_commitment::` and `decided_on::` are Decision-only; `has_epistemic_status::` is Observation-only; `serves_as::` is Reference-only. These predicates MUST NOT appear on Patterns, Convictions, Aspirations, or other forms where they would mis-classify. Predicate vocabulary carries form distinctness at the graph level: a query filtering on a form-specific predicate returns only nodes of that form.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Reserve Predicate Vocabularies to Specific Forms

Form-specific predicates are reserved to the forms whose Contracts introduce them. `has_commitment::` and `decided_on::` appear on Decisions; they MUST NOT appear on Patterns, Convictions, Aspirations, Observations, References, or Glosses. `has_epistemic_status::` appears on Observations; it MUST NOT appear on Convictions, Aspirations, Decisions, Patterns, References, or Glosses. `serves_as::` appears on References; it MUST NOT appear on forms where an external-source role claim would mis-classify. The prohibitions compose — each form's Contract specifies both the predicates it requires and the predicates it forbids, and the forbidden-from lists cross-reference across forms.

## Why

The commitment makes **predicate vocabulary carry form distinctness at the graph level**. A node's form is asserted by `conforms_to::[[X Form Contract]]`, but the predicate vocabulary the node actually uses is a stronger signal — a node that asserts conformance to Conviction Form Contract while also asserting `has_commitment::[[Provisional Commitment]]` is internally inconsistent, because `has_commitment::` is a Decision predicate. The form-specific vocabulary is what makes conformance checkable beyond the single `conforms_to::` assertion: the presence or absence of form-specific predicates tells a validator or curator whether the node's practice matches its stated form.

A query filtering on a form-specific predicate returns exactly nodes of that form. `has_commitment::` filters for Decisions; `has_epistemic_status::` filters for Observations. Without the reservation, the same predicates could appear on nodes of other forms — a Conviction carrying `has_commitment::` because its author wanted to mark a "firm" stance, a Pattern carrying `has_epistemic_status::` because its author wanted to note the empirical grounds of an instance — and the query's selectivity would degrade. The filter would return a mix of genuine Decisions and non-Decisions that borrowed Decision predicates, and the reader would have to audit each match.

The commitment is the form-level expression of [[Adopt Predicate Atomicity]]. Predicate atomicity says each predicate answers one question; form-specific reservation says each predicate is asked only of the forms where the question makes sense. `has_commitment::` asks "what level of commitment does this Decision carry?" — the question assumes Decision-form context. Asking it of a Conviction produces a category error — Convictions don't commit situationally; they hold stances — and the answer is either meaningless (the Conviction has no situational commitment to level) or misleading (the author imports Decision semantics into a Conviction-shaped node, confusing later readers).

The commitment bundles the full set of cross-form predicate reservations — `has_commitment::` and `decided_on::` on Decisions only, `has_epistemic_status::` on Observations only, `serves_as::` on References only, with the mirror prohibitions across all other forms — into one Decision because they share one Why (predicate vocabulary carries form distinctness) and roll back together (weakening any one reservation would unwind the form-distinctness property the others depend on). Each form Contract's specific requirement ("a Conviction MUST NOT carry `has_commitment::`...") is a thin enforcement clause pointing back at this Decision.

## Alternatives Considered

**Shared predicate vocabulary with form disambiguation by `conforms_to::`.** Let `has_commitment::` appear on any form; let readers and validators distinguish Decision semantics from non-Decision semantics by checking `conforms_to::` separately. Rejected because the disambiguation burden compounds across every query. Every filter that wants Decisions with `has_commitment::[[Firm Commitment]]` has to compose two predicates; every reader encountering `has_commitment::` has to check `conforms_to::` to know whether the assertion carries Decision semantics or something else. The reservation rule is what lets the predicate be self-identifying — its presence asserts Decision form along with the commitment level.

**Form-specific predicate namespaces.** Distinguish form-specific predicates by naming (`decision:has_commitment::`, `observation:has_epistemic_status::`). Rejected because the namespace prefix adds authoring and reading cost with no graph-level benefit over the reservation rule. A reader encountering `has_commitment::` without a prefix does not know which form's semantics are in play; with the reservation rule, they know it is Decision semantics. The namespace approach addresses the same ambiguity less cleanly.

**Permit cross-form usage with explicit semantics per form.** Let `has_commitment::` mean one thing on Decisions, another on Convictions, another on Patterns. Rejected because it violates [[Adopt Predicate Atomicity]]. Predicate atomicity requires each predicate to answer one question; cross-form usage would make `has_commitment::` carry multiple axes (commitment level for Decisions, held-firmness for Convictions, adoption status for Patterns). The predicate would fail atomicity by semantic bundling even if each form kept its own meaning sharp.

## What Would Change It

The commitment would be revisited under one condition.

**The form distinctions collapse or the predicates become genuinely shared.** If a future refactor merged forms (Decision and Conviction collapsing into a single "commitment" form, say) the reservation rules would merge with them. Alternatively, if experience showed that some form-specific predicates were genuinely useful on other forms — if Aspirations benefited from `has_commitment::` to mark how firmly the project is pursuing the target, with a semantics that is genuinely the same as Decision commitment levels — the reservation would loosen predicate by predicate, not wholesale. Current form distinctions are active and the predicates carry form-specific semantics; no pressure exists.

## Relations

- grounded_in::[[Adopt Predicate Atomicity]]
  - Predicate atomicity requires each predicate to answer one question. Form-specific reservation is the form-level expression: each form-specific predicate's question assumes form-specific context, and reserving the predicate to that form is what keeps its question sharp.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine makes predicates first-class structural elements. Form-specific reservation extends the spine's discipline into form-level classification — predicates signal form, not just relation.

- informs_downstream::[[Decision Form Contract]]
  - Decision Form Contract's identity predicate block Requirement carries the thin enforcement clause pointing at this Decision for Decision's form-specific predicates.

- informs_downstream::[[Observation Form Contract]]
  - Observation Form Contract's identity predicate block Requirement carries the thin enforcement clause pointing at this Decision for `has_epistemic_status::` reservation.

- informs_downstream::[[Conviction Form Contract]]
  - Conviction Form Contract's identity predicate block Requirement forbids `has_commitment::`, `decided_on::`, and `has_epistemic_status::` on Convictions; the prohibitions point at this Decision.

- informs_downstream::[[Aspiration Form Contract]]
  - Aspiration Form Contract's identity predicate block Requirement forbids `has_commitment::`, `decided_on::`, and `has_epistemic_status::` on Aspirations; the prohibitions point at this Decision.

- informs_downstream::[[Pattern Form Contract]]
  - Pattern Form Contract's identity predicate block Requirement forbids `has_commitment::` and `decided_on::` on Patterns; the prohibitions point at this Decision.

- informs_downstream::[[Reference Form Contract]]
  - Reference Form Contract's identity predicate block Requirement establishes `serves_as::` as Reference-specific; the reservation points at this Decision for the form-distinctness rationale.
