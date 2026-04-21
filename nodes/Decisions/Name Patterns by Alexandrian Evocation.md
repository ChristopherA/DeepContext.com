---
created: 2026-04-19
tagline: Pattern names evoke the move or the situation with specificity and imagery; categorical or abstract labels are excluded
brief_summary: A commitment that Pattern filenames follow the Alexandrian tradition — evocative names for the move (`Refactor the Predicate's Axes`), the timing (`Progressive Summary Before Substance`, `Split Before Ossify`), or the recognized situation, rather than abstract category labels (`Refactoring Pattern`, `Axis Design Pattern`). A reader who has never encountered the node SHOULD be able to guess from the name alone what recognizable moment the pattern addresses. The choice imports Alexandrian naming semantics rather than inventing a new convention.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Name Patterns by Alexandrian Evocation

Every Pattern filename is Alexandrian-evocative — it names the move or the recognizable situation with specificity and imagery, not as an abstract category. Typical shapes: imperative verb plus object (`Refactor the Predicate's Axes`), timing imperative (`Split Before Ossify`, `Progressive Summary Before Substance`), or named failure-mode claim for anti-patterns (`Informal Edges Poison the Graph`). Categorical names (`Refactoring Pattern`, `Naming Pattern`) and abstract labels (`Axis Design`) do not satisfy the rule; a Pattern whose name reads as a category-of-things rather than a specific move is misnamed.

## Why

The commitment imports **Alexandrian pattern-naming semantics into the prototype's vocabulary**. Christopher Alexander's *A Pattern Language* established a naming tradition for patterns: each pattern carries a name that evokes the move or the situation it addresses, specific enough that a practitioner who has never read the pattern can often guess from the name alone what recognizable moment the pattern is for. "Light on Two Sides of Every Room"; "Sitting Circle"; "A Place to Wait." The names do the work of coherent discovery — a practitioner encountering a pattern library browses by name and reads the patterns whose names match situations they face.

The alternative — categorical or abstract naming — produces patterns whose names describe the kind-of-thing the pattern is rather than what applying the pattern does. `Refactoring Pattern` says "this is a pattern about refactoring," which is what every refactoring pattern says; the name does no distinguishing work among siblings. Alexandrian naming distinguishes at the filename level: `Refactor the Predicate's Axes` names a specific move; `Split Before Ossify` names a specific timing; `Progressive Summary Before Substance` names a specific ordering. A reader browsing the Patterns folder reads the names and knows what each pattern is about before opening any file.

The rule produces **pattern-language coherence**. A Pattern library where names evoke moves can be read as a language — "when you encounter X, apply Pattern Y, composed with Pattern Z, preferred over Pattern W." The names themselves compose in sentences; the library reads as prose rather than as a catalog. A library with categorical names reads as an index: each entry must be opened to know whether it is relevant. The Alexandrian tradition's success at producing read-as-language libraries is the evidence this commitment rests on.

The commitment is specifically about the filename. Pattern bodies may still benefit from Alexandrian tradition in structure (Heart, Problem, Forces, Solution, Consequences, Instances — themselves Alexandrian), but the filename-naming rule is the piece the commitment targets. A Pattern with a beautiful Alexandrian body and a categorical filename fails at the discovery layer; the filename is what readers see first, and Alexandrian evocation is what makes the Patterns folder readable as a language.

## Alternatives Considered

**Categorical names based on what the pattern is about.** Name Patterns by the domain they address (`Refactoring Pattern`, `Naming Convention`, `Edge Hygiene`). Rejected because categorical names flatten the Patterns layer into an index. Every pattern about refactoring shares the `Refactoring` prefix; readers cannot distinguish them by name alone and must open each to discover specificity. The coherence-as-language property the Alexandrian tradition produces is lost.

**Abstract label names.** Name Patterns by the abstract concept they address (`Axis Design`, `Context Economy`, `Vocabulary Ecology`). Rejected because abstract labels require a prior frame the reader may not have. `Axis Design` is meaningful to a reader who has already learned the concept of predicate axes; a new reader encounters the term without anchor. Alexandrian evocation is grounded in the move or the situation — both recognizable before the theoretical frame the Pattern articulates.

**Author-discretionary naming.** Let Pattern names be whatever the author prefers, without form-shape constraints. Rejected because without a shape rule, naming converges on whatever is easiest at authoring time — often a categorical name ("another refactoring pattern"). The rule exists to prevent the authoring-time path of least resistance from consuming the library's coherence.

## What Would Change It

The commitment would be revisited under one condition.

**Evocative naming proves harder to maintain than categorical naming.** If the project produces Patterns whose names resist Alexandrian evocation — where the honest name for the move is "the refactoring where you [technical procedure]" and the forced-evocative version reads as pretentious or opaque — the rule would weaken. The revisit would be corpus-driven: a review of Patterns' names would show the evocative discipline producing either forced names or names that convey less than a categorical alternative would. Current Patterns have named themselves evocatively without strain (`Refactor the Predicate's Axes`, `Progressive Summary Before Substance`, `Reconcile the Standing Account`); the commitment is carrying its weight.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine gives Patterns first-class graph identity via wikilink. Filename-shape conventions operate on top of that identity — the naming rule specifies how Pattern filenames carry their form and discoverability.

- grounded_in::[[Pattern Form]]↗
  - The Alexandrian tradition, via the Group Works deck and the larger estate-level Pattern Form, supplies the naming-convention substrate. The prototype imports the naming semantics rather than inventing one.

- informs::[[Pattern Form Contract]]
  - Pattern Form Contract's filename pattern Requirement carries the thin enforcement clause pointing at this Decision.
