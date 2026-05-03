---
tagline: A shared language community where practitioners share specific vocabulary and conventions — a bounded context for terms with compressed meaning
created: 2026-05-03
---

- conforms_to::[[Contract Form Contract]]
- extends_contract::[[Gloss Form Contract]]
- in_practice_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Practice Domain

A Practice Domain is a shared language community — a bounded context where specific terms carry compressed meaning among practitioners. It is not a library-science classification, not a hierarchical taxonomy slot; it is a lived vocabulary that participants share when they participate in the community of practice. "Deep Context Architecture" is a Practice Domain (where "form," "predicate," "seed stage" and "Crescent" mean specific things without explanation); "Self-Sovereign Identity" is another (where "principal authority" carries specific weight); "Anthropology" and "Management Theory" are recognized academic Practice Domains where each field's vocabulary is shared by its practitioners.

A Practice Domain page serves dual roles in the graph. As a **structural index**, it lists what's in the domain — Decisions, Convictions, Glosses, Patterns, References — and tracks what's seed versus growing versus mature. As a **vocabulary index**, it serves as the entry point for newcomers learning the community's shared language. When the structural-index role and the reader-orientation role diverge enough that a single page cannot serve both well, a separate Touch Point may be authored to handle the reader-orientation role at finer-than-domain granularity.

A Practice Domain is distinct from a Concept Facet. Concept Facets are units of inquiry that may cross multiple Practice Domains — the Dunbar Number Concept Facet appears in both Anthropology and Management Theory — while Practice Domains are the communities whose shared language Concept Facets traverse. The relationship is `appears_in::` from Concept Facet to Practice Domain.

The Practice Domain form supersedes the bare "domain" usage that older nodes carry via `in_domain::` edges. The bare predicate has been renamed to `in_practice_domain::` to remove the ambiguity (web domain? library-science knowledge domain? problem domain?) and to point explicitly at this form's definition.

## Requirements

### Inherits Gloss Form Contract

- All requirements of [[Gloss Form Contract]] apply, including the double-hyphen filename pattern, the bare-concept H1, and the restate-and-elaborate body opening.
- The requirements below are additions for Practice Domain instances specifically.

### Filename pattern

- The filename MUST follow `<Practice Domain Name> -- <one-clause sense of the community>.md`, inherited from Gloss.
- The concept side names the community by its proper name. Naming heuristic: knowledge-area or practitioner-community proper name, concise. One to three words that name the field as practitioners themselves would name it. "Deep Context Architecture" not "Deep Context Architecture Domain"; "Synpraxis" not "Coordination Practice."

### Identity predicate block

- The identity block MUST include `conforms_to::[[Practice Domain]]`.
- The identity block SHOULD include `in_practice_domain::[[<broader practice>]]` when the Practice Domain itself participates in a broader community of practice (e.g., a sub-discipline whose practitioners are also part of the parent discipline).

### Body: Scope

- The body MUST include a `## Scope` section that names what this Practice Domain covers and what it deliberately does not. The scope statement is the load-bearing piece for newcomers — it says "here is the bounded context within which terms have compressed meaning, and here is where that compression breaks down."

### Body: Key Nodes

- The body MUST include a `## Key Nodes` section listing the nodes belonging to this Practice Domain, organized by form type (Decisions, Convictions, Glosses, Patterns, etc.) or by theme. The index serves as a structural-index for practitioners working within the domain.
- The list SHOULD note the lifecycle stage (Seed, Growth, Mature) of each node so a reader can see which parts of the practice are settled and which are under active elaboration.

### Body: Open Questions

- The body SHOULD include an `## Open Questions` section listing what's unresolved or under-explored within this Practice Domain. Open questions point at Inquiry nodes (when authored) or describe gaps in the practice. A Practice Domain page without open questions is implicitly claiming the practice is settled — an unusual claim for an active community.

### Body: Sources

- A `## Sources` section MUST appear when the Practice Domain draws on external authoritative material. Sources are listed as Reference nodes with brief annotations.

### Relations section

- A Practice Domain SHOULD include `narrower::[[<broader Practice Domain>]]` when a broader Practice Domain exists in the graph (e.g., "Agentic Architecture" narrower than "Software Architecture" if both are authored).
- A Practice Domain MAY include `related::[[<peer Practice Domain>]]` for non-hierarchical neighborhoods.
- A Practice Domain MAY include `composes_with::[[Touch Point]]` when one or more Touch Points orient readers to Concept Facets within this Practice Domain.

## Relations

- extends_contract::[[Gloss Form Contract]]
  - Inherits the double-hyphen filename pattern, the restate-and-elaborate body opening, and the body shape allowances. Adds the Scope, Key Nodes, and Open Questions sections plus the SKOS-style narrower::/broader::/related:: edges and the structural-index role.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract specifying what Contract nodes look like. The Gloss-style filename (`Practice Domain -- ...`) is a deliberate departure from the older `<X> Form Contract.md` pattern; new Form Contracts that fundamentally define a node form (rather than purely specifying structure) use Gloss-style filenames so the Form Contract carries its own definition in the filename.

- contrasts_with::[[Gloss Form Contract]]
  - A Gloss defines a single term; a Practice Domain names a community whose shared language includes many terms. A Practice Domain extends Gloss with structural-index, community-membership, and open-question obligations.

- composes_with::[[in_practice_domain -- membership in a Practice Domain]]
  - The Predicate that carries node-to-Practice-Domain membership. Practice Domain instances are the targets of `in_practice_domain::` edges from every other node in the graph; the Predicate makes membership traversable, and this Form specifies what membership means.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes Practice-Domain framing load-bearing. Without the diversity stance, a single shared vocabulary across the graph would be adequate; with it, recognizing distinct Practice Domains lets the graph hold multiple vocabularies without forcing convergence.
