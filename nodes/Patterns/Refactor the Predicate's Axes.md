---
created: 2026-04-19
tagline: When a predicate carries two or more independently-moving axes, recognize the axes and split the predicate into single-axis named predicates before corpus use ossifies the overloaded meaning
brief_summary: "A recurring craft move in predicate design. When a single predicate is asserting multiple axes at once — one name carrying lifecycle and curation, or inheritance and substrate and grounding, or every unspecific relationship — factor the axes apart into a family of single-axis predicates. Each resulting predicate asks one question; assertions migrate to the appropriate axis; the overloaded predicate retires. Apply while the corpus is small enough that migration is a session's work, not a project."
---

- conforms_to::[[Pattern Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Refactor the Predicate's Axes

## Heart

A predicate that looks atomic is often carrying two axes — or three — under one name. When a reader has to ask *which axis are you asserting?* of a predicate's values, factor the axes out: name each one, give each its own predicate, migrate existing assertions to the appropriate axis. Do it while the corpus is small enough that migration is a session's work. Every day the overloaded predicate stays in use, more assertions will need to move, and more contributors will habituate to the conflated form.

## Problem

Predicates are the query handles of a graph: each one is a question a reader can ask of any node. When a single predicate quietly smuggles two or more independently-moving questions, every assertion it carries becomes ambiguous. A reader filtering on `has_status::[[Seed Stage]]` cannot tell whether the match is about lifecycle maturity, curation state, review cycle, or something else the predicate has accumulated. Inferences diverge across readers. Queries soften. The graph degrades continuously — not catastrophically on any single day, but cumulatively as the corpus grows and as later contributors pattern-match on the overloaded form.

The difficulty is recognition, not mechanics. Once the second axis is seen, splitting the predicate is mechanical. The craft this Pattern teaches is noticing that the predicate is carrying an axis its name does not declare.

## Forces

- **Expressive compression.** One predicate that covers several cases is cheap to introduce, easy to remember, and fits in a contributor's head. A predicate family costs teaching time, onboarding documentation, and authoring discipline. The overloaded predicate feels simpler until the ambiguity accumulates.
- **Query precision.** Each predicate is a query handle. A predicate answering one clear question produces sharp filtering; a predicate answering two or three fuzzy questions produces soft filtering and contested interpretation. Precision pulls toward narrower predicates; compression pulls toward broader ones.
- **Corpus inertia.** The longer an overloaded predicate stays in use, the more assertions depend on its current reading. Migration cost grows roughly with the number of nodes using the predicate. Inertia rewards acting early and punishes delay.
- **Emerging distinctions.** New axes often become visible only after a predicate has been in use for a while. The first authors of `has_status::` did not notice lifecycle and curation were separate axes until a node needed to assert "seed-stage yet curated" and the predicate could express only one fact. The Pattern must act on distinctions that were not visible at introduction time.

## Solution

When reviewing a predicate's use — during authoring, during review, or during convention audit — ask: *can two assertions of this predicate with the same value mean different things?* If yes, the predicate is carrying more than one axis.

For each axis the predicate carries, name it (`lifecycle`, `curation`, `review`, `visibility`, whatever the axis is about). Create a named predicate per axis (`has_lifecycle::`, `has_curation::`, and so on). Migrate existing assertions to the appropriate axis — each old assertion becomes one or more new assertions across the family. Retire the overloaded predicate: add it to the "deliberately not used" section of the conventions document with a pointer to the replacement family.

The number of axes the refactor produces is not capped at two. A predicate may factor into three, four, or more. A status predicate that mixed lifecycle with curation, for example, factors into two predicates — `has_lifecycle::` and `has_curation::` — with room for later axes (`has_review::`, `has_visibility::`) as distinctions emerge. Each refactor is incremental: factor what is visible now, leave room for later axes that have not yet become clear.

Do this early. While the corpus has tens of assertions, migration is an afternoon. While the corpus has hundreds, migration is a project. While the corpus has thousands, migration is a rewrite.

## Consequences

- **Queries sharpen.** Each predicate answers one question; filters compose without ambiguity. A reader can ask *what is this node's lifecycle?* separately from *what is its curation state?*, and the graph answers each cleanly.
- **Vocabulary grows.** Contributors see more predicate names, which is a teaching cost paid in conventions documentation, onboarding, and authoring discipline. The vocabulary is larger but each predicate is clearer; readers lose the convenience of one-stop predicates and gain the ability to query any axis independently.
- **Migration debt is paid.** Every pre-refactor assertion needs to move to the appropriate axis. This is finite but real. Cost scales with how late the refactor happens: early refactor is cheap, late refactor is a project, very-late refactor is a rewrite.
- **Future axes add cleanly.** Once the refactor exists, a newly-recognized axis becomes a new predicate alongside the existing family — not another overload of an established name. The Pattern pays forward: the next distinction is cheap to express.
- **Deprecation becomes part of the record.** The retired predicate's Predicate node records the history of the move, with a Typing-section note naming the family it was replaced by and a lifecycle marking that indicates the predicate is no longer in use. A contributor encountering an old wiki dump or a pre-refactor note can look up the deprecated predicate and find the family it was replaced by.

## Instances

- **Status axes — `has_lifecycle::` and `has_curation::`.** Lifecycle maturity (`[[Seed Stage]]`, `[[Growth Stage]]`, `[[Mature Stage]]`) and curation state (`[[Pre-Draft]]`, `[[Working Draft]]`, `[[Curated]]`) answer different questions about a node. Each gets its own predicate so a node "at Seed, already Curated" can be expressed without contradiction. A single status predicate would collapse the two axes; the split keeps each query sharp.
- **Classification axes — `extends_contract::`, `built_on::`, `grounded_in::`.** Strict contract inheritance, underlying substrate, and flexible grounding are three distinct relationships a node can have to another node. Each is a named predicate in this graph rather than a value under a generic classification or relation predicate — so a query for "what does this node extend?" returns only strict inheritance, not substrate or grounding edges that happen to look similar. See [[extends_contract -- strict inheritance between form contracts|extends_contract]], [[built_on -- foundational substrate the subject rests on|built_on]], and [[grounded_in -- normative or structural foundation|grounded_in]] for each predicate's distinctions.

## Also Known As

- *Unconflation as a design discipline* — a framing that names the move from the defensive side (what contributors should *stop* doing when a predicate smuggles two axes). This Pattern names the same move from the positive side: the craft applied when the condition is recognized.

## Relations

- grounded_in::[[Adopt Predicate Atomicity]]
  - The Decision that commits the project to one-question-per-predicate discipline. This Pattern is the craft move that realizes or restores the commitment when an overloaded predicate is discovered in the wild.

- grounded_in::[[Markdown Node Contract]]
  - The Contract's predicate-atomicity Requirement is the thin enforcement clause for Adopt Predicate Atomicity. This Pattern is paired with the Requirement: the Requirement states the MUST rule; the Pattern names the craft applied when the rule is violated.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The Decision that makes predicates the graph's structural spine. This Pattern is about maintaining the quality of those predicates over time — the Decision carries the vocabulary layer, the Pattern keeps it clean as distinctions emerge.

- informs_downstream::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The gist names the move as "unconflation as discipline"; this Pattern is the prototype's reframed and elaborated rendition of that convention. The gist entry is the convention at stub-level; this Pattern is the convention at Problem-plus-Forces-plus-Solution level.

- composes_with::[[Progressive Summary Before Substance]]
  - Both are node-design craft moves operating on different scales. This Pattern concerns predicate atomicity (one question per predicate); that Pattern concerns node macro-structure (how the tiers are arranged). Applied together, they produce nodes that are both well-layered and precisely queryable.

- composes_with::[[Reconcile the Standing Account]]
  - Both are periodic curation moves operating on different layers of the corpus. This Pattern audits the vocabulary layer (one question per predicate, refactor when axes conflate); that Pattern audits the document layer (one authoritative location per claim, reconcile when documents drift from the graph). Applied together across a curation pass, they keep both the graph's vocabulary and the graph's accounts of itself honest.
