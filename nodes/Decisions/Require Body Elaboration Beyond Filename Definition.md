---
created: 2026-04-19
tagline: A Gloss body elaborates beyond the filename definition; pure repetition of the filename clause is not permitted
brief_summary: A commitment that every Gloss body elaborates beyond what the filename definition already carries. The opening restates and elaborates the definition by at least one useful clause — a contrast, a concrete instance, a one-step derivation — and the body grows from there. A Gloss whose only content is a verbatim repetition of the filename definition is not conforming; the filename already delivered that content, and the body must add something a reader benefits from opening the file for.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Require Body Elaboration Beyond Filename Definition

Every Gloss body elaborates beyond the filename definition. The opening sentence restates the definition and adds at least one useful clause — a contrast with an adjacent term, a concrete instance, a one-step derivation, a grounding reference — and the body grows from there as the term warrants. A Gloss whose body is a verbatim repetition of the filename definition (or a trivial rewording of it) is not conforming; the filename has already delivered that content, and the body must add value a reader benefits from opening the file for.

## Why

The commitment ensures **body adds substance beyond what the filename carries**. The filename-carries-definition pattern makes the folder view readable as a dictionary — but the file itself must justify its existence beyond the dictionary entry. A reader who opens the file has decided to pay the reading cost; the body must return something that cost. A verbatim-repeating body returns nothing — the reader sees the same content the filename already delivered, and the whole file becomes redundant with its filename.

The one-clause-minimum elaboration is what distinguishes a Gloss from a filename entry. The filename says what the concept is at a single-clause resolution; the body extends — the opening restates with one more clause of specificity, the body's second paragraph (when present) adds an instance or a structural consequence, the body's third paragraph (when present) distinguishes the concept from an adjacent term. The growth path is from filename to body; truncating the body at the filename's resolution leaves the file pointless.

The rule forbids trivial rewording specifically, not brief bodies. A Gloss whose body is a single paragraph of two or three sentences is fine if those sentences add specificity the filename did not carry. A Gloss whose body is a single paragraph of two sentences that say in different words exactly what the filename already said is the violation — the rule targets repetition, not length. Short Glosses are welcome; trivially repetitive Glosses are not.

The elaboration bar is low enough that most concepts worth a Gloss can meet it. A concept has adjacent concepts from which it differs, typical uses, one-step derivations from prior Glosses, or concrete instances in the graph — any of these provides material for the required elaboration. A concept that cannot be elaborated beyond the filename definition is usually one whose filename definition is already comprehensive — and the question the reviewer should ask is whether the concept needs a file at all, or whether a ghost link with the filename-level definition is sufficient. The rule is both a quality gate and a diagnostic.

## Alternatives Considered

**Permit pure-filename Glosses with empty bodies.** Let Gloss files exist with filename-only definitions and no body content. Rejected because the file adds nothing over a ghost link — a wikilink to a nonexistent file provides the same "the concept exists, here is the definition" signal via the filename-as-ghost-link convention. Creating empty-bodied Gloss files to serve that signal wastes filesystem entries and trains contributors that opening a Gloss file is not worth the click. Either the concept warrants a body (and the Gloss should have one) or the concept does not yet warrant a file (and a ghost link carries the definition adequately).

**Permit trivial rewording as elaboration.** Accept Gloss bodies whose content is the filename definition expressed in different words. Rejected because the reader's cost of opening the file is paid for content-that-is-not-content — different words, same information. The rule's purpose is to ensure the body pays back the reading cost; trivial rewording fails that test as clearly as verbatim repetition.

**Require a minimum body word count.** Specify "Gloss bodies MUST contain at least 50 words" or similar. Rejected because word-count rules target the wrong failure mode. The failure mode is content-free repetition, not shortness; a 50-word body can still be trivially repetitive, and a 15-word body can add real specificity. The rule targets elaboration semantics directly ("adds at least one useful clause") rather than indirectly through length.

## What Would Change It

The commitment would be revisited under one condition.

**Minimal Glosses become common and the body requirement feels forced.** If the project accumulates many concepts whose filename definitions are genuinely comprehensive — where the one-clause definition already carries everything a reader needs and further elaboration would be padding — the rule would produce Glosses with forced bodies rather than valuable ones. The revisit would weaken the rule to "Glosses SHOULD elaborate; pure-filename Glosses are permitted when the concept genuinely needs nothing beyond the definition." Current Glosses have all elaborated comfortably; no pressure exists. The rule is carrying its weight.

## Relations

- grounded_in::[[Use Double-Hyphen Separator for Gloss Definitions]]
  - The filename-carries-definition commitment is what makes the body-elaboration rule load-bearing. Without the filename-as-definition pattern, the body would be the primary definition source and the elaboration question would not arise; with it, the body's job is specifically to add what the filename cannot.

- grounded_in::[[Adopt Layered Node Structure]]
  - The layered-structure commitment requires each layer to be complete at its scale. The Gloss form's claim layer is split across the filename (definition) and the body's opening (restate-and-elaborate); the body tier must be complete at its scale, which means adding specificity beyond the filename's resolution.

- informs::[[Gloss Form Contract]]
  - Gloss Form Contract's Body-shape Requirement carries the thin enforcement clause pointing at this Decision.
