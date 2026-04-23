---
created: 2026-04-19
tagline: When a document's accuracy depends on something external that has moved, audit the document and reconcile — collapse duplicated passages to pointers at their authoritative locations, realign stale descriptions with current state, keep what is genuinely native to this document
brief_summary: "A recurring curation move. When a document is an account of something external — a growing graph, a past event, a living system — the external thing changes and the document does not. Periodically, run a curation pass over the document: for each passage, decide whether its claim now lives at an authoritative location (collapse to pointer), whether the description has gone stale (realign to current state), or whether the passage is genuinely native to this document and belongs here (keep). The Pattern applies to intake documents (logs, inboxes), narrative records (founding conversations, meeting notes), and orientation documents (READMEs, convention docs, overview pages) — any document whose accuracy depends on external state that is changing faster than the document is being rewritten."
---

- conforms_to::[[Pattern Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Reconcile the Standing Account

## Heart

A document that accounts for something external — a graph, an event, a living system — loses accuracy as the external thing moves. Audit the document periodically: collapse passages whose claims now live at authoritative locations into pointers, realign stale descriptions with current state, keep only what is genuinely native to this document. A *standing account* (one still held open, still referenced, still read) needs recurring reconciliation the same way a standing ledger does; the discipline is noticing that the move is due, not the move itself.

## Problem

Some documents describe something other than themselves. An intake log accumulates entries that will later be extracted into atomic nodes. A founding conversation records an exploration whose conclusions will settle into Decision nodes. An orientation document describes a graph that will grow new nodes, retire old ones, and reorganize its structure. Each of these documents is an *account of* something, and each becomes inaccurate when the something moves faster than the document gets rewritten.

The inaccuracy is silent. Nothing alerts a reader that a passage has a better home now, that a count is stale, that a path points at a file that was renamed. Two locations claim authority for the same content; downstream references accumulate against the wrong one; contributors pattern-match on the outdated form. By the time the drift is visible, many edges have calcified around the mistake.

The difficulty is recognition and cadence, not mechanics. Once a writer has noticed the drift, reconciling the passage is ordinary editing — collapse to pointer, realign the count, remove the dead path. The craft this Pattern teaches is noticing that the document is now inaccurate, and having a ritual that runs before the drift ossifies.

## Forces

- **Comprehensibility versus atomicity.** Holding zones and narrative records read as stories — a contributor can open the Decision Log and follow the reasoning as it developed, open a Founding Conversation and trace the exploration. Atomic nodes are precise but require graph traversal to reconstruct. Pruning a story to a pointer trades reader legibility for non-duplication; keeping the full story trades non-duplication for silent drift. The Force exists because both goods are real.
- **Cost of delayed reconciliation.** The longer a duplicated passage sits after extraction, the more downstream references accumulate against it, and the more tangled the eventual cleanup. Refactor is cheap early and expensive late — the same asymmetry that makes predicate refactors urgent makes account reconciliation urgent. Inertia rewards acting early and punishes delay.
- **Distinguishing narrative from record.** Not every passage in a standing account is a duplication waiting to be collapsed. The *story* of how a decision emerged, the exploration arc of a founding conversation, the contextual framing around a stale count — these belong to the document, and pruning them would strip what the document uniquely carries. The Pattern requires judgment: some passages collapse to pointers, some realign to current state, some are genuinely native and stay.
- **Absence of automatic triggers.** Nothing in the corpus raises an alarm when a document becomes stale. A reader can pass over the inaccurate count without noticing; an agent can quote the outdated passage with confidence; a new contributor can adopt the drifted vocabulary and propagate it. Without a deliberate cadence — a *standing practice* of reconciliation — the drift is silent until it is already expensive.

## Solution

When a significant change to the external system has landed — a node graph milestone, an event's conclusions settling into nodes, an orientation document's system growing past the scope its current description assumed — run a curation pass over the standing accounts affected. For each document and each passage:

1. **Does the claim now have an authoritative home?** If yes, collapse the passage to a pointer. Preserve the narrative framing around the pointer (the story of how the passage came to be) and link to the node that now owns the claim.
2. **Is the description stale with respect to current state?** If yes, realign. Update counts, replace dead paths, clear resolved TODOs, correct stale references. The realignment is mechanical once the drift is named.
3. **Is the passage genuinely native to this document?** If yes, keep. Not every passage is a duplication; some content belongs to the document because of what the document uniquely is (an origin story, a human-facing entry point, a landing paragraph).

Three sub-modes surface in practice, matching the three document types:

- **Extraction pruning** for intake documents and narrative records: prose existed because no node existed yet; node now exists. Collapse to pointer.
- **State alignment** for orientation documents: the description matched an earlier state of the system; the system has grown. Update counts, paths, and TODOs to match current state.
- **Cascade of back-pointers**: reconciliation leaves dangling references. A passage that collapsed to a pointer still has other documents pointing at the old form. Sweep the cascade — update the back-pointers as part of the same pass, not as a follow-up.

Write the updated document as a single coherent revision, not as scattered edits. The pass is the ritual unit; a partially reconciled document carries both the old claim and the pointer until the pass completes, which is worse than either.

## Consequences

- **Standing accounts shrink toward their minimum durable form.** A reconciled intake log contains only what has not yet been extracted. A reconciled narrative record contains the story plus pointers, not the extracted claims in duplicate. A reconciled orientation document describes the current system, not an earlier one.
- **Workshop documents stay trustworthy.** A README that accurately describes current counts, a conventions document whose TODO list reflects current candidates, an overview whose paths resolve — these serve onboarding and curation. A drifted version silently misleads new contributors.
- **The Pattern grounds the convention overhead.** The graph's discipline (multi-word predicates, form contracts, structured edges, annotation bullets) is only worth its cost if the corpus stays coherent. The Pattern is what makes the overhead bearable — it is the ritual that counters silent drift and keeps the graph's account of itself honest.
- **Judgment is required every time.** Unlike a mechanical check, reconciliation cannot be run as a lint. Some passages collapse, some realign, some stay. The judgment is part of the Pattern's craft, and the reason it must be applied by a contributor rather than a tool.
- **Cascade work is part of the pass, not an afterthought.** Back-pointers in other documents still reference pre-reconciliation forms. Leaving them for a later sweep creates compound drift — the original passage and all its references in different degrees of currency. The Pattern requires sweeping back-pointers in the same ritual unit.
- **The ritual must actually run.** Without cadence, the Pattern degrades into intention. Standing accounts accumulate drift until a crisis forces the pass; by then the cleanup is expensive. The Pattern's real cost is not the pass itself but the discipline of running it before the drift ossifies.

## Instances

- **Decision Log prune.** A running `context/Decision Log.md` accumulates Decision entries as a project's reasoning develops. As entries are extracted into their own Decision, Pattern, Conviction, or Reference nodes, the log is reconciled: extracted entries collapse to a pointer at the nodes that now authoritatively carry them; entries without a home yet (Open Questions whose form contract is unseeded) stay as the log's native content. The log shrinks toward a holding zone of what has not yet been extracted — its minimum durable form at the current stage of the graph.
- **Founding Conversation prune.** A `context/Founding Conversation.md` records the exploration that produced a project's starting conventions — alternatives considered, commitments made, questions deferred. As seeded Decision nodes and the orientation document's Working Assumptions section accumulate the same content authoritatively, the conversation is reconciled: "what was considered" collapses to a pointer at `[[External Sources]]`; "what was decided" collapses to pointers at the seeded Decision nodes; "what was deferred" collapses to a pointer at the Decision Log's Open Questions. The narrative arc — the question, the exploration, the meta-point — is kept because it is genuinely native to this document.
- **Workshop document refresh.** `CLAUDE.md`, `README.md`, and `CONVENTIONS.md` describe a growing graph. Counts go stale, paths break as folders reorganize, TODO lists keep asking for work that is already done. The pass realigns the descriptions with current state — counts updated, paths corrected, resolved TODOs moved from open to resolved. No passages are collapsed to pointers; the orientation documents are native by design. The reconciliation is state alignment, not extraction pruning.

## Also Known As

- **Curation pass** — the lowercase event-noun for a single application of this Pattern. A curation pass is the activity; the Pattern names the move and the discipline. CONVENTIONS.md carries *Curation Pass Ritual* as the in-document noun for the practice; the two names refer to the same move at different scales.
- **Prune to pointer** — a narrower framing that names the most visible sub-move (extraction pruning) but misses state alignment. Useful as a slogan for a pass in progress; too narrow as a Pattern name.
- **Point, don't duplicate** — a terse imperative that captures the Heart's directional push. A slogan version; useful as a mid-pass reminder, insufficient as a Pattern name.

## Relations

- grounded_in::[[Accounts Track Their Subject]]
  - The standing Conviction this Pattern realizes. A document that is an account of something external must remain accurate to that something; the Pattern is the recurring move that restores accuracy when it has drifted. Currently a ghost link; the Conviction will be seeded once a second documented instance of the drift-then-reconcile arc supplies corroborating evidence.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The Decision that makes extraction-plus-pointer structurally viable. Without named-edge predicates and filename-resolving wikilinks, collapsing a passage to a pointer would be prose reference only — readable but untraversable. The Decision is what lets reconciled accounts stay light while remaining machine-connected to the authoritative nodes they point at.

- grounded_in::[[Folders Serve Human Legibility, Not the Graph]]
  - The companion Conviction that justifies keeping workshop documents (CLAUDE.md, README.md, CONVENTIONS.md) as orientation material despite their drift risk. Because folders and orientation documents serve human readers without carrying graph authority, they can be reconciled freely without touching the graph; the Pattern's state-alignment sub-mode depends on this separation.

- composes_with::[[Refactor the Predicate's Axes]]
  - Both are periodic curation moves operating on different scales. The predicate refactor audits the vocabulary layer (one question per predicate, refactor when axes conflate); this Pattern audits the document layer (one authoritative location per claim, reconcile when documents drift from the graph). Applied together across a curation pass, they keep both the graph's vocabulary and the graph's accounts of itself honest.

- composes_with::[[Progressive Summary Before Substance]]
  - Both are craft moves on the corpus, operating at different orientations. Progressive Summary is the authoring move when writing a node; Reconcile the Standing Account is the curation move when auditing a document. Progressive Summary produces nodes that are readable at multiple depths; this Pattern ensures the documents that reference and describe those nodes stay accurate as the graph grows.

- informs_downstream::[[Convention Overhead vs Graph Quality]]
  - The standing tension the Pattern counters. The graph's convention overhead (multi-word predicates, form contracts, structured edges, annotation bullets) is only worth its cost if the corpus stays coherent — which requires the ritual. Currently a ghost link in CONVENTIONS.md; the Pattern's existence now makes the tension tractable rather than merely named.
