---
created: 2026-04-19
tagline: When authoring or reviewing a node, arrange content so consumers encounter progressively denser material as they commit context, with each tier complete at its own scale
brief_summary: "A recurring craft move in node authoring. When writing or reviewing a node, lead with the cheapest structural tier and add depth in order: identity predicates above the H1; card-scale claim in the H1 plus opening sentences or Heart; full elaboration in the body; structured edges in Sources and Relations. Each tier stands alone as a complete read at its own scale, so any finite context — a reader's attention, an agent's token budget, a query's traversal — can be spent deliberately. The Pattern is the authoring move that realizes the layered-structure Requirement in [[Markdown Node Contract]] in every node."
---

- conforms_to::[[Pattern Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Progressive Summary Before Substance

## Heart

Lead with the cheapest structural tier and add depth in order: identity predicates above the H1, then the card-scale claim, then elaboration, then structured edges. Each tier stands alone as a complete read at its own scale. The move is summary-first composition against the authoring habit of writing detail-first — the discipline is what produces a node that serves both a minute of reading and an hour of it.

## Problem

Authoring flows detail-first. The writer thinks through the argument as they compose, and the card-scale summary emerges last, if at all. Readers and agents then pay the deepest read's cost to extract what they actually needed: a one-line orientation, a structural filter, a graph neighbor. Without progressive structure, every consumer reads the body in full or gives up; there is no middle tier at which to stop and have what they came for.

The difficulty is discipline, not mechanics. Once a writer has internalized summary-first composition, the tier arrangement is natural. The craft this Pattern teaches is fighting the detail-first habit long enough for the card-scale claim to be written before the body that elaborates it.

## Forces

- **Authoring flow.** Writing proceeds detail-first because argumentation is generative — the writer discovers the claim by elaborating it. Composing the summary last is natural; composing it first requires pre-formed clarity the writer may not yet have.
- **Consumer orientation.** Readers and agents encountering a node need to know cheaply whether to commit attention. The question *is this node worth reading?* is answerable only if the node offers something cheaper than its body to answer it.
- **Context budget.** Agent tools operate under literal token budgets. An agent traversing a hundred nodes cannot read a hundred full bodies; the structure must offer a cheap tier to scan. The same pressure holds for human readers at human scale.
- **Recursive fidelity.** The Pattern wants to apply within sections too — every section should lead with its purpose before its detail. Over-specifying this turns a craft move into a brittle checklist; under-specifying loses the recursive benefit. The Pattern must honor the recursion as craft without mandating it as rule.

## Solution

When authoring or reviewing a node, arrange content in four tiers:

1. **Tier 0 — Identity predicates (above the H1).** Structured data: `conforms_to::`, `in_domain::`, `authored_by::`, `has_lifecycle::`, `has_curation::`. Answers *what is this node?* structurally; cheapest to read for any consumer.
2. **Tier 1 — Card-scale claim (H1 plus opening prose, or `## Heart`).** Two to three sentences stating the node's claim, move, or commitment. Complete at its own scale — a consumer stopping here has the claim, not a promise of it.
3. **Tier 2 — Elaboration (body sections).** Why the claim holds, forces, structural consequences, instances, reasoning. The expensive tier, for consumers who have committed attention.
4. **Tier 3 — Structured edges (Sources, Relations).** Machine-traversable data: provenance, paired principle or pattern, grounded-in edges, informs edges. Cheap again — a consumer traverses the graph without paying body cost.

Write Tier 1 first as a discipline, even when the final wording is refined after the body drafts. The discipline is what produces the card-scale claim; without it, the writer defaults to detail-first and the card-scale tier never lands.

Apply the same move recursively within sections when it helps — lead a section with its purpose, then its detail — but treat recursion as craft, not requirement.

## Consequences

- **Nodes become readable at multiple depths without loss.** A consumer stopping at any tier completes their task at that tier's scale. Tier 1 readers have the claim; Tier 0 agents can filter; Tier 3 traversers find neighbors.
- **Agent augmentation becomes feasible at scale.** Agent tools can scan Tier 0 cheaply across many nodes before committing context to full body reads. The progressive shape is what makes graph-scale agent use possible without blowing token budgets on every traversal.
- **Form contracts encode the tier pattern per node type.** Pattern Form Contract requires a Heart section; Decision Form Contract requires Why content at the opening; Conviction Form Contract requires opening prose stating the stance; the Markdown Node Contract's layered-structure Requirement names the minimum tiering every node inherits. The contracts are the Pattern's structural enforcement per form.
- **Authoring requires discipline.** The summary-last habit has to become summary-first. The discipline is finite and learnable — across many nodes it becomes natural — but the first nodes an author writes after adopting the Pattern often have to be reworked once. That cost is the tradeoff for downstream reader and agent speed.
- **Recursive application is encouraged, not mandated.** A section that leads with its purpose and follows with detail is good craft; enforcing recursion as rule produces brittle templates. Authors exercise judgment about when the recursion pays.

## Instances

- **Every Form Contract in the prototype** specifies a required opening that carries the card-scale claim. Pattern Form Contract ("The body MUST open with a `## Heart` section of two to three prose sentences"); Decision Form Contract ("The body MUST contain content that states why the commitment was made"); Conviction Form Contract ("The body MUST open by stating the conviction in one or two prose sentences"); the Markdown Node Contract's layered-structure Requirement names the minimum structural tiering every extending contract inherits. The contracts are this Pattern's structural fingerprint per form.
- **The Group Works deck tradition** is the card-scale precursor. Each card IS the pattern at card scale — a reader holding only the card gets the whole of it. The prototype's `## Heart` convention adopts the same principle explicitly; see [[A Pattern Language (Christopher Alexander et al., 1977)]] for the tradition this draws on.
- **The Wikilinks and Named Edges Gist reference node** names this same move in one bullet as "Progressive disclosure for agents" — convention-stub scale. This Pattern is the prototype's reframed and elaborated rendition.

## Also Known As

- **Progressive disclosure** — the HCI and interaction-design tradition, though applied there to UI reveal rather than node structure.
- **Card-scale authoring** — the Group Works deck's claim that the card text IS the pattern, not a summary of it.
- **Progressive disclosure for agents** — the earlier informal naming in the Wikilinks and Named Edges gist; this Pattern is that convention stub elaborated.

## Relations

- grounded_in::[[Adopt Layered Node Structure]]
  - The Decision that commits the project to layered node structure. This Pattern is the authoring move that realizes that commitment in the prototype's specific vocabulary — identity predicates above the H1, card-scale opening or `## Heart`, elaboration body, and Relations. The Decision states the standing commitment; the Pattern names the craft applied when composing a node.

- grounded_in::[[Markdown Node Contract]]
  - The Contract's layered-structure Requirement is the thin enforcement clause for Adopt Layered Node Structure. This Pattern realizes the Requirement's compliance rule through the authoring move named in its Solution.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The Decision that makes Tier 0 and Tier 3 possible as machine-traversable structural data. Without the named-edge vocabulary, the progressive structure would collapse into prose tiers with no cheap-read layer.

- informs_downstream::[[Markdown Node Contract]]
  - The base contract whose structural shape — identity predicates above H1, H1, body, Relations — is this Pattern's enforcement at the base-form level. Every form contract extending Markdown Node Contract inherits the layered shape.

- informs_downstream::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The gist names the move as "Progressive disclosure for agents"; this Pattern is the prototype's reframed and elaborated rendition at Problem-plus-Forces-plus-Solution scale.

- composes_with::[[Refactor the Predicate's Axes]]
  - Both are node-design craft moves operating on different scales. This Pattern concerns macro-structure (how the node's tiers are arranged); the predicate refactor concerns predicate atomicity (how individual edges answer one question). Applied together, they produce nodes that are both well-layered and precisely queryable.

- composes_with::[[Reconcile the Standing Account]]
  - Both are craft moves on the corpus, operating at different orientations. This Pattern is the authoring move that produces well-layered nodes; Reconcile the Standing Account is the curation move that keeps documents describing those nodes accurate as the graph grows. Applied together, the graph stays readable at multiple depths and the documents about the graph stay trustworthy.
