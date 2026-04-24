---
created: 2026-04-21
tagline: The graph captures how contributors actually reason -- values, patterns, choices, and the grounds behind decisions -- not merely what they know
brief_summary: A held stance that the graph's value is correspondence between captured reasoning and lived reasoning. A Decision in the graph should record not just what was decided but what was considered, what was rejected, and what would change it. A Pattern should record the tension it resolves. An Observation should name its epistemic grounds. The alternative -- a graph that stores facts without reasoning -- produces output that is technically informed but personally wrong. The stance does not demand completeness; a graph with three well-connected Convictions and two grounding Observations carries more reasoning than a corpus of a thousand loosely-tagged notes. Quality of the reasoning web matters more than the volume of captured knowledge.
---

- conforms_to::[[Conviction Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Capture Reasoning, Not Just Knowledge

The graph should capture how contributors actually reason, not merely what they know. What gets stored is correspondence to lived reasoning: an agent or reader traversing the graph can make decisions consistent with how contributors actually think because the reasoning substrate is present, not just the artifacts of thinking. A Decision that records only the choice is a fact; a Decision that records what was considered, what was rejected, and what would change the call is captured reasoning.

The stance does not demand completeness. A graph with three well-connected Convictions and two grounding Observations carries more reasoning than a corpus of a thousand loosely-tagged notes. The quality of the reasoning web -- whether one node's commitments can be traced through its named edges to the grounds that support them -- matters more than the volume of captured knowledge.

## Why It Is Held

The value distinguishes this graph from encyclopedic knowledge management, from document repositories, and from AI fine-tuning approaches that try to replicate surface patterns rather than capture reasoning. Each of those stores outputs; none of them stores the reasoning that produced the outputs, so each of them produces output that is technically informed but can be personally wrong -- right for the average case, wrong for the specific contributor whose reasoning was supposed to inform it.

The graph's form contracts are the structural implementation. [[Decision Form Contract]] requires Why, Alternatives Considered, and What Would Change It; those sections are reasoning, not facts. [[Observation Form Contract]] requires epistemic grounds and What Would Revise It; those sections are reasoning, not claims. [[Conviction Form Contract]] requires Why It Is Held and Drift Recognition; same pattern. The named-edge convention adds the traversable substrate: `grounded_in::`, `informed_by::`, `informs_downstream::`, `contends_with::` each carry reasoning between nodes. Without the contracts and the edges, the graph would store claims; with them, the graph stores the web of reasoning that justifies the claims.

In a multi-contributor graph, fidelity is pluralized: the goal is fidelity to each contributor's reasoning, not to a normalized consensus. [[Vocabulary Diversity Is a Feature]] is the stance that lets this work; fidelity without diversity collapses into convergence, and convergence loses the specific reasoning each contributor brought. Reasoning fidelity and vocabulary diversity compose: each preserves what would otherwise be lost to flattening.

## What It Asks

Nodes carry their reasoning, not just their conclusions. A Decision names the alternatives it rejected and the condition that would change the call. An Observation names the grounds it rests on and what would revise the claim. A Conviction names the stance it holds and what would count as drift from it. A Pattern names the tension it resolves. The sections are load-bearing; a node that skips them carries a fact without the reasoning that justifies it.

Edges carry reasoning between nodes. `grounded_in::` points at the foundation a claim rests on; `informed_by::` points at a weaker influence; `informs_downstream::` points forward at what a node shapes downstream. An annotation under each edge names why the edge is load-bearing -- what the reader gains from following it. A graph of unannotated edges is tag spaghetti; a graph of annotated edges is reasoning made traversable.

Contributor reasoning stays in the contributor's voice. When a Decision captures how one contributor reasoned, it does not normalize that reasoning into a house style or flatten it into the aggregate. The contributor's specific framing, their specific concerns, their specific rejected alternatives are what make the Decision worth capturing; removing them to fit a template collapses the thing the value is protecting.

## Drift Recognition

The value has drifted when the graph starts accumulating nodes that record what but not why. A Decision with no Alternatives Considered. An Observation with no Grounds. A Conviction with no Why It Is Held. Each of these is still technically a valid node structurally, and each of them is a small step toward a graph that stores facts rather than reasoning. The drift is visible to a reader who follows an edge expecting to find the reasoning behind a claim and finds only the claim restated.

The drift also shows up in edge quality. `relates_to::` becoming a catch-all is the most visible form -- the predicate does not carry reasoning, only loose association. Unannotated edges, or edges whose annotations describe rather than explain, are the subtler form. A reader scanning a node's Relations section should be able to tell why each edge is in the graph; when the answer becomes "because these two nodes came up in the same conversation," the reasoning layer is gone.

## Relations

- informs_downstream::[[Deep Context as an Architecture for Captured Reasoning]]
  - The Decision that makes the graph's architecture a structural implementation of this value. The Decision grounds in this Conviction rather than in the external value of the same name; the foundational grounding now lives inside the graph.

- informs_downstream::[[Knowledge Outlives Its Tools]]
  - The sibling value the durability stance serves. The project holds durability because captured reasoning must survive to remain useful — reasoning captured in a format that doesn't outlast its tooling loses the fidelity this Conviction protects. The motivation direction: this Conviction is why the durability Conviction is load-bearing, not merely convenient.

- informs_downstream::[[Decision Form Contract]]
  - The Contract's required sections (Why, Alternatives Considered, What Would Change It) are the form-level implementation of the fidelity commitment. A Decision node that complies carries its reasoning; a Decision that drops the sections carries a fact.

- informed_by::[[Vocabulary Diversity Is a Feature]]
  - The composition with vocabulary diversity: fidelity to each contributor's reasoning requires preserving each contributor's vocabulary, which convergence would destroy.
