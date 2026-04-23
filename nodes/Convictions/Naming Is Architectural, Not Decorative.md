---
created: 2026-04-20
tagline: Names encode design decisions and activate semantic fields that shape every subsequent inference — choosing a name is architectural work, not cosmetic packaging
brief_summary: A held stance that a name choice — `conforms_to::` vs `is_a::`, `estate` vs `workspace`, `gardener` vs `content curator`, `Adopt <X>` vs `<X> as <Role>` — activates a web of associations that shapes every downstream interpretation. Naming is architectural work because the chosen name carries design decisions forward into every inference that runs through it; alternative namings would have carried different decisions forward and produced a different graph. The stance is load-bearing for why the project deliberates over single predicates, resists `is_a::` and `relates_to::`, and holds filename-shape conventions as structural rather than stylistic commitments.
---

- conforms_to::[[Conviction Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Naming Is Architectural, Not Decorative

A name choice is a design decision. Choosing `conforms_to::` over `is_a::`, `estate` over `workspace`, `gardener` over `content curator` activates a web of associations — etymology, cultural resonance, prior use, semantic neighbors — that becomes the context through which every subsequent inference runs. The project holds that naming is architectural work, not cosmetic packaging.

## Why It Is Held

Every name carries decisions forward. `conforms_to::[[Gloss Form Contract]]` decides that node-to-form is a relation of compliance (pluralizable, revisable, open to a node conforming to multiple contracts at once); `is_a::[[Gloss Form]]` decides it is a relation of identity (singular, terminal, forcing commitment before the relationship is understood). Both are sovereign choices about what the graph asserts. The first is made in the open; the second is smuggled through convention. Neither is cosmetic — each decides in advance what every downstream node inheriting the relation can say and cannot say.

The effect compounds across a corpus. A single predicate's naming ripples through hundreds of nodes that use it; a single form-contract name shapes how every conforming node reads. When the naming is deliberated, the design decisions are visible and revisable. When the naming is treated as packaging, the design decisions are still made — just silently, by whichever name happened to be typed first. Naming neglected is still naming, and the decisions it encodes still carry. The only choice is whether the author is deliberate about them or not.

Le Guin's *A Wizard of Earthsea* ("For magic consists in this, the true naming of a thing") and Vinge's *True Names* arrive at the same observation from opposite directions — one working inward toward self-knowledge, the other projecting outward toward networks and infrastructure. Both describe naming as the act by which power is claimed or surrendered. In a knowledge graph, the predicate vocabulary is where naming sovereignty is exercised or surrendered. A system that infers its edges from prose has answered *whose vocabulary wins?* silently — the system's vocabulary wins. A system built on author-declared predicates answers it differently — the author's distinctions survive, and the agent's role shifts from extractor to translator. The shift is architectural: it decides what kind of artifact the graph is.

## What It Asks

New predicates are deliberated at the naming layer, not just the semantic layer. When the project adds a predicate to `CONVENTIONS.md`, the proposal carries a named alternative and a reason for preferring the chosen name — `grounded_in::` over `derived_from::` because grounding names a normative substrate while derivation names a provenance chain, and the distinction is load-bearing. A predicate added without a named alternative has skipped the deliberation the stance requires.

Filename-shape conventions are held as design, not style. The `Adopt <X>`, `Use <X>`, `Prefer <X>`, `<Subject> as <Role>` shapes for Decisions and the held-stance shapes for Convictions (value declaration, subject-carries-object declarative, bounded stance) are not ornamental preferences. They encode form-from-filename classification — a reader scanning a folder can tell a Decision from a Conviction from a Gloss by filename shape alone. Loosening the shape rules to accept "whatever reads best" converts the filename from a classification tier to a readability tier and loses the cheap-classification property the conventions were designed to preserve.

Vocabulary reviews treat name choices as sovereign acts, not terminology preferences. When a reviewer proposes a rename — a predicate, a form-contract name, a domain term — the proposal is evaluated as a decision about what the graph will assert, not as copy editing. The conversation names what the current name carries, what the proposed name would carry instead, and why the change is worth the downstream re-inference.

Single-word predicates and bare noun-phrase filenames are rejected. `source::`, `type::`, `status::`, and their peers are rejected because their naming carries too little — they have no internal structure to disambiguate the axes they conflate and no enough semantic weight to survive traversal across nodes that mean different things by them. Bare noun-phrase filenames are rejected because they read as topics being described, not as commitments being made.

## Drift Recognition

The stance has drifted when new predicates arrive without naming deliberation. A predicate enters the vocabulary because it was convenient to type, with no documented alternative considered and no argument for the chosen name over its peers. The review cadence stops asking "what is this name carrying that the alternative would not?" and starts asking "does this name work?" — the second question can be answered without architectural reasoning, and the first cannot.

Filename shapes drift toward whatever is easiest to type. Decisions appear with bare noun-phrase filenames because the author did not want to rephrase as an action verb; Convictions appear with action-verb leads because they were being drafted under Decision-style momentum; Gloss filenames drop the ` -- <definition>` separator because it felt redundant. The drift is cumulative — each individual concession is small, and the filename convention is gone by the time the cumulative effect becomes visible.

Reviews stop treating naming as load-bearing. A rename proposal is evaluated for whether it "reads better" rather than for what it decides; a vocabulary audit reports predicate frequency without asking which of the high-count predicates carry more than one question; a new form contract adopts whatever classification name seems natural without considering what the alternative name would have smuggled in. The surface signal is that vocabulary review becomes terminology review, and the graph's assertions become less deliberate over time.

## Sources

- Allen, Christopher. "Wikilinks and Named Edges," 2026 — the "Why the name itself matters" section develops the full argument this Conviction rests on, including the Le Guin and Vinge references and the sovereignty framing that extends through the extractor-versus-translator distinction.
- Le Guin, Ursula K. *A Wizard of Earthsea*, 1968 — cited in the gist as the epigraph for the naming-as-architectural claim ("For magic consists in this, the true naming of a thing").
- Vinge, Vernor. *True Names*, 1981 — cited in the gist as the outward-facing counterpart to Le Guin's inward-facing treatment of naming and power.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The substrate Decision that makes names first-class in the graph. When edges are author-declared predicates and wikilink targets are filenames, the names *are* the structural claims — choosing them is architectural by construction. A graph whose structure was inferred rather than declared would make this Conviction unholdable, because the names would not be what the graph's meaning rested on.

- informed_by::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The gist's "Why the name itself matters" section is the argumentative substrate this Conviction compresses. The Le Guin epigraph, the extractor-versus-translator distinction, and the naming-sovereignty framing all come from that section.

- informed_by::[[Deep Context Shared Languages Post (Christopher Allen, 2014)]]
  - The earlier 2014 framing that specialized terminology carries design decisions encoded as web-of-associations is the upstream of this Conviction's claim that naming choices activate semantic fields shaping downstream inference.

- informs_downstream::[[Name Decisions by Action Verb or Role Declarative]]
  - The Decision that specifies Decision filename shapes. Its filename-shape rule and its verbatim-embedding rule are downstream concretizations of the stance that naming is architectural — form-from-filename classification and citation stability are architectural properties the rule exists to preserve.

- informs_downstream::[[Name Patterns by Alexandrian Evocation]]
  - The Decision that specifies Pattern filename shapes. Pattern naming carries its own architectural load — a Pattern name that reads as a recurring move or situation is a different architectural commitment than a name that reads as a topic.

- informs_downstream::[[No Generic relates_to Predicate]]
  - The Decision that prohibits `relates_to::`. The prohibition follows directly from the stance — `relates_to::` names too little for the architectural weight a predicate carries, and its use substitutes a naming shortcut for the deliberation the stance requires.
