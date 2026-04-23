---
created: 2026-04-22
tagline: When a new Contract holds through speculative drafting but has not been run against real cases, exercise the first conforming skill or node against real data and let the exercise surface gaps the drafting missed
brief_summary: A recurring craft move when a Contract has been authored ahead of 2-3 conforming nodes existing. The discipline: draft the first conforming node or skill, then run it against real graph data (validate a real node, audit the real graph, walk a real workflow). The run surfaces gaps the speculative drafting missed -- unspecified edge cases, implicit exceptions, silent reservations about what the Contract is actually claiming. Revise the Contract from what the run revealed. The pattern replaces "think harder about the Contract" with "let the first exercise be the audit."
---

- conforms_to::[[Pattern Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Let the Exercise Audit the Contract

## Heart

A Contract authored ahead of its conforming nodes cannot find the gaps in itself by being stared at harder. Draft the first conforming node or skill, run it against real graph data, and let the run surface what the speculative drafting missed. The Contract is revised from what the exercise revealed, not from what further reflection might imagine.

## Problem

`Contract Form Contract` asks that contracts be introduced "only when two or three concrete nodes already want the same shape." The discipline is sound: the Contract should codify observed shape, not speculative shape. But in practice there are cases where the Contract must exist before the first node conforming to it can exist — because without the Contract, the node has no `conforms_to::` target to declare, and the node's shape is not yet trustworthy enough to stand without the structural rule.

In those cases the Contract is drafted speculatively. The author sits alone with the form's intent and writes down what they expect conforming nodes to need. Speculative drafting is easy to get wrong in specific ways: unspecified edge cases, implicit exceptions the author assumed everyone shared, silent reservations about what the Contract is actually claiming. These gaps are invisible while the Contract has zero instances. Staring harder at the Contract does not reveal them, because they are gaps in the *relationship* between the Contract and real cases, not gaps inside the Contract's prose alone.

The recurring difficulty: how to find the gaps without waiting for 2-3 nodes to independently demonstrate them.

## Forces

- **Author confidence.** A newly-drafted Contract feels complete to its author. Every Requirement was considered; every body section was specified. The author's view of the Contract is the view of someone who just assembled all its parts and saw them fit together on paper. That feeling resists "I bet this misses something." The Force pulls toward assuming the Contract is done.

- **Absence of evidence.** A Contract with zero conforming nodes has no instances to point at when claiming it undersays something. The absence of evidence is interpretable as evidence of absence: the Contract works, because nothing has broken. But nothing has touched it either. The Force pulls toward confusing "no failures" with "no gaps."

- **Exercise cost.** Running a real exercise — drafting a real node, running a real audit, walking a real workflow — is more work than re-reading the Contract. The Force pulls toward cheaper cycles of re-reading when the real exercise would be more revealing.

- **Corrective churn.** A Contract that is revised through speculative reflection tends to gain scope speculatively too. Each speculative revision adds requirements the author thought of on second thought. A Contract revised through exercise tends to gain only what the exercise demanded. The Force pulls toward revision styles: speculation adds breadth the exercise did not ask for; exercise adds specificity the speculation missed.

## Solution

When a Contract has been authored speculatively, draft its first real instance immediately and run the instance against real data. For a Form Contract: draft a conforming node and invoke a validation skill against that node plus two others of adjacent forms. For a Skill-form Contract: draft a skill and run it against the real graph (or real documents, real data — whatever the skill operates on). For a tooling Contract: draft the tool and run it end-to-end.

The exercise surfaces gaps in two kinds:

1. **Requirements that undersay.** A Requirement written as "the body MUST include X" turns out, when X is actually drafted, to need specific content or ordering the author did not state. The exercise reveals the implicit expectation.

2. **Cross-Contract interactions the author missed.** A Requirement in Contract A interacts with a Requirement in Contract B in ways the A-author did not foresee. The exercise, by touching both contracts at once, surfaces the interaction.

Revise the Contract from what the exercise revealed, not from what the author thinks of on reflection. Each exercise-revealed gap becomes a concrete Requirement refinement with the real case that prompted it. Revisions that cannot point at an exercise are deferred; speculative additions at this stage are drift, not improvement.

Repeat the exercise with a second and third conforming instance. The Contract stabilizes when two or three consecutive exercises surface zero revisions. At that point the `has_lifecycle::[[Seed Stage]]` marking the Contract carries can advance to `[[Growth Stage]]`: the Contract has demonstrated it works for more than the first case.

## Consequences

- **The Contract becomes specific through use, not through scope growth.** Each exercise-revealed gap is a narrow, well-grounded refinement. The Contract grows only where the work demanded growth. Speculative additions do not accrete.

- **Author confidence is recalibrated honestly.** The author who drafted the Contract discovers, through running the exercise, what they did not know they did not know. The gap between "feels complete" and "works on the first real case" closes by exposure rather than by more thinking.

- **Early exercise is cheap; late exercise is expensive.** Running the first conforming instance while the Contract has zero other instances is a session's work and catches gaps while the refactor is small. Running it after the Contract has ten conforming instances means each revision potentially invalidates the instances. The Pattern compresses the exercise to the earliest point at which it is possible.

- **The Contract's lifecycle predicate becomes honest.** A Contract marked `has_lifecycle::[[Seed Stage]]` stays at Seed until exercise demonstrates its shape holds. The marking communicates "speculatively drafted; exercise pending" rather than "authored; status unknown." Growth Stage is reached through exercises, not through time.

- **Exercise quality matters more than exercise quantity.** One honest run against real data surfaces more than three perfunctory runs against contrived cases. The Pattern asks that the first exercise be a real one — a real node with real content, a real audit over real graph data — not a synthetic test that conforms by construction.

## Instances

- **Skill Form Contract drafted speculatively; held through six skills without revision.** The Contract was authored ahead of any skill node existing because skills needed a `conforms_to::` target. Six skills were then drafted under it (`graph-orient`, `graph-audit`, `node-create`, `node-read`, `node-validate`, `predicate-propose`), each of which was exercised against real work: Node Validate was run against three real nodes (a Decision, a Conviction, a Predicate); Graph Audit was run against the whole graph. The exercises surfaced revisions not to Skill Form Contract itself but to adjacent Contracts it depended on — Markdown Node Contract's Named-edge syntax Requirement gained a scalar-valued-predicate clause; `Use Pipe Wikilinks for Display-Target Divergence` had its MUST scoped to prose-flow contexts. The Skill Form Contract held; the exercise instead audited the Contracts it rested on.

- **Node Validate exercised against three real nodes surfaced three Contract gaps.** Running the skill's form-specific-requirement checks against a real Decision, Conviction, and Predicate revealed that Markdown Node Contract's Named-edge syntax Requirement didn't acknowledge scalar-valued predicates (the `decided_on::YYYY-MM-DD` form Decision Form Contract specified); that the pipe-wikilink MUST was over-broad (structural contexts had been using bare-full-filename form); and that Node Validate's own Step 6 vocabulary check was over-flagging base-contract predicates. Each gap was a narrow revision prompted by a specific real case.

- **Graph Audit exercised against the whole graph surfaced five script-recipe gaps.** The `rg 'relates_to::'` pattern matched prose discussions in skill bodies (not actual edges); the `find -type f` loop broke on filenames with spaces; the ghost-link detection counted template-token placeholders (`[[X]]`, `[[<Domain>]]`) as ghosts; external-marker wikilinks (`[[X]]↗`) showed as ghosts; deliberate ghosts (Predicate Crescent H3 headings targeting predicates that will never have nodes) were not distinguished from drift. Each was a concrete refinement demanded by the exercise.

## Also Known As

- *Dogfooding applied to graph Contracts* — the broader tradition of using your own tool is the ancestral form. This Pattern specializes it to the Contract-instance relationship and names the lifecycle move (Seed → Growth) that the exercise enables.

## Relations

- grounded_in::[[Contract Form Contract]]
  - The meta-contract that asks Contracts be introduced when "two or three concrete nodes already want the same shape." This Pattern names the discipline that protects the spirit of that rule when the Contract must be drafted speculatively: the first two or three instances arrive as exercises, and the Contract is revised from what they reveal.

- grounded_in::[[Adopt Minimum-Viable-Architecture Stance]]
  - The Decision that holds scope growth to what is demanded by use. This Pattern operationalizes the stance at the Contract-refinement layer: revisions follow exercise-revealed needs, not author-imagined extensions.

- composes_with::[[Refactor the Predicate's Axes]]
  - Both are craft moves triggered by working with the graph rather than by pre-planning. This Pattern applies to Contracts and surfaces their gaps through exercise; Refactor the Predicate's Axes applies to predicates and surfaces their conflations through use. Each recognizes that speculative design often misses what real data reveals.

- informs_downstream::[[Skill Form Contract]]
  - The Skill Form Contract's own `has_lifecycle::[[Seed Stage]]` marking and its "first skills drafted under it are expected to revise it" prose anticipate this Pattern. The Pattern names the move the Contract's own lifecycle design was inviting.
