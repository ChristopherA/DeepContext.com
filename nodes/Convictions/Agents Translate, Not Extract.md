---
created: 2026-04-20
tagline: When agents mediate between graph and contributor, they read and translate author-declared edges rather than inferring edges from prose and imposing a schema
brief_summary: A held stance specializing Human Authority Over Augmentation Systems at the graph-interaction layer. Agents mediating between a graph and a human contributor work in translating mode — reading author-declared edges in the author's vocabulary, interpreting between vocabularies when they meet — rather than in extracting mode, where the agent infers relations from prose and imposes a normalized schema on what contributors wrote. Even when humans retain authority over outputs, an agent in extracting mode still enrolls contributors as subjects of its schema rather than participants in their own naming; the translating mode is the operational form that human authority takes at the predicate layer.
---

- conforms_to::[[Conviction Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Agents Translate, Not Extract

When an agent mediates between a knowledge graph and a human contributor, the agent's role is translator — it reads author-declared edges in the author's vocabulary and interprets between vocabularies when they meet. It does not infer edges from prose and impose a normalized schema on what contributors wrote. The translating mode is not just agent etiquette; it is the operational form that human authority takes at the predicate layer.

## Why It Is Held

Extraction and translation are two different postures an agent can adopt toward the same graph, and the difference is not cosmetic. An agent in extracting mode reads prose, infers what relations it thinks the author meant, and writes edges the agent constructed — the edges come from the agent's model of how the content fits together, and the authors become subjects of that model. An agent in translating mode reads edges the authors declared, interprets between different authors' vocabularies, and leaves the declarations intact. The graph the agent produces is the graph the authors wrote, organized enough to be traversable.

Human Authority Over Augmentation Systems establishes that humans retain authority over augmentation outputs — session-level approval gates, architecture-level rule conferral, knowledge-level form contracts. But authority-over-outputs is not the same as authorship-of-edges. An extracting agent can respect every approval gate and still enroll contributors into its schema — the contributor sees the agent's inferred predicates, accepts them because they look reasonable, and the resulting graph encodes the agent's ontology with human sign-off. The approval is real; the vocabulary sovereignty is lost anyway. The translating mode closes that gap — it makes human authority operational at the layer where predicates actually get authored.

The translating mode is what makes author-declared edges sustainable. If agents default to extraction, the cost of maintaining author-declared edges rises over time — every summarization, every traversal, every interop pass pulls the graph toward the agent's schema, and authors must work continuously to reclaim their predicates. Translation holds the graph at the authors' vocabulary by default, and the maintenance cost is on the translation layer (a glossary, a cross-reference) rather than on the authors' willingness to resist normalization. That cost structure is what makes contributor-vocabulary plurality viable at scale.

## What It Asks

Agent workflows respect author-declared edges as authoritative. An agent reading the graph does not silently rewrite predicates it finds unfamiliar; it does not infer edges from prose to supplement what the author wrote; it does not collapse distinct predicates into canonical forms when summarizing or traversing. When an unfamiliar predicate appears, the agent reads it, interprets it, and leaves it — the only rewriting an agent does is what the author asked for.

Cross-system agent work adds translation layers rather than schema enforcement. When an agent works across two graphs whose predicates differ, the agent's role is to produce a glossary or a cross-reference document that makes each graph's vocabulary legible to the other — not to propose a shared schema both sides adopt. A schema-enforcing agent is in extracting mode even if the schema is a superset rather than a reduction; the extraction is what makes it extraction.

Claude's curation contract in this project embodies the translating mode. Claude suggests annotations, flags conflation, upgrades construction predicates per the authors' stated conventions, audits the `relates_to::` trap, detects vocabulary drift — and never rewrites a contributor's vocabulary without confirmation. Every curatorial move is either an interpretive action (flagging, auditing, suggesting) or a conventional action the authors have pre-authorized (upgrading `extracted_from::` to a mature predicate once the mature form is named). The agent does not introduce new edges of its own.

The mode persists across tool surfaces. An agent reading through a chat interface operates under the translating constraint; an agent operating through a linter or a graph traversal tool does too; a future agent exposed to the same graph through a different harness inherits the constraint. The mode is a property of what the agent *does* to the graph, not of which surface it runs on.

## Drift Recognition

The stance has drifted when agents start inferring edges from prose and silently rewriting the graph. A summarization pass that introduces predicates the author never declared is extraction; a graph-visualization tool that surfaces "likely" edges the agent derived is extraction; an interop handshake that presents a unified schema rather than a translation document is extraction. Any of these can happen without a user noticing, because each individual output still looks reasonable — the drift is visible only when the resulting graph diverges from what the authors would recognize as theirs.

Predicate vocabularies consolidating at read time rather than at author time is a subtler signal. When a reader asks an agent about a concept and the agent's answer uses canonical predicates across vocabularies the authors kept distinct, the agent has normalized at read time; the authors' distinctions are invisible in the agent's output even though they remain in the source. Enough read-time normalization passes produce a de facto shared vocabulary without anyone ever having decided to adopt one.

The curation contract slackens into "agent proposes, agent enacts" is the final-form drift. The agent's role shifts from suggesting moves the contributor approves to enacting moves with contributor approval as a formality. The approval remains; the authorship has moved. The surface signal is that contributors stop treating the agent's suggestions as suggestions and start treating them as defaults to ratify.

## Sources

- Allen, Christopher. "Wikilinks and Named Edges," 2026 — the "Why the name itself matters" section develops the extractor-versus-translator distinction ("that shift — from extractor to translator — is peer-sovereignty in agent-mediated form") this Conviction formalizes.

## Relations

- grounded_in::[[Human Authority Over Augmentation Systems]]
  - The broader Conviction that humans retain authority at every level of an augmentation system. This Conviction specializes that stance at the agent-graph-interaction layer — human authority over outputs is operationally incomplete without the translating-mode commitment, because an extracting agent can respect approval gates and still enroll contributors as subjects of its schema.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - Translation only makes sense as an agent posture if vocabulary diversity across contributors is the property the graph is committed to preserving. Without the diversity Conviction, extraction is merely efficient — with it, extraction is a flattening the project rejects, and translation is the posture the project commits to instead.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The substrate Decision commits this graph to author-declared edges. The translating mode is the agent-side correlate of that commitment — author-declared edges on the graph side, agent-translated reading on the interpretation side. Without the Decision, translation has no declared edges to read; without this Conviction, the Decision's author-declared property erodes silently through agent extraction.

- informs_downstream::[[Claude as Curator Contract]]
  - The ghost link in CLAUDE.md currently names Claude's role in this project as curator. This Conviction grounds what the Curator Contract specifies — suggest, flag, upgrade construction predicates, audit the `relates_to::` trap, never rewrite contributor vocabulary without confirmation. The Contract, once seeded, will carry the behavioral requirements; this Conviction is the normative substrate those requirements rest on.

- informed_by::[[LLM Assistance Widens the Participation Gap]]
  - The Observation supplies empirical grounds for treating the translating-versus-extracting distinction as load-bearing rather than merely stylistic. If the participation gate is community membership fluency and extracting-mode agents produce content the community reads as non-member, then an extracting agent reproduces the O4 dynamic in the Deep Context practice itself. The translating-mode stance is the operational response; the Observation is what makes the stance carry weight beyond agent etiquette.
