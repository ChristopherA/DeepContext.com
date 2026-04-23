---
created: 2026-04-19
tagline: Decision filenames use an action-verb lead or a Subject-as-Role declarative; named subjects embed verbatim
brief_summary: A bundled commitment covering two co-specifying rules about Decision filenames. The filename takes one of two shapes — an action-verb lead (`Adopt <X>`, `Use <X>`, `Prefer <X>`, `No <X>`) or a `<Subject> as <Role>` declarative — so a reader can classify the node as a Decision from the filename alone. When the Decision's subject is a thing with an established title (a named convention, tool, node, or practice), the filename embeds the subject verbatim — no paraphrase, no appended category nouns. The two rules share a Why about citation stability and form-from-filename classification.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Name Decisions by Action Verb or Role Declarative

Every Decision filename takes one of two shapes. The **action-verb lead** begins with an imperative verb naming the move the project made — `Adopt <X>`, `Use <X>`, `Prefer <X>`, `Require <X>`, `Treat <X>`, `No <X>` (prohibitive, read as "do not X"). The **`<Subject> as <Role>` declarative** frames the subject as playing a role the project has committed to — `Deep Context as an Architecture for Captured Reasoning`. When the subject is a thing with an established title (a named convention, tool, person, practice, or existing node), the filename embeds that subject verbatim with only the Decision-shape verb or connector added; paraphrase, appended category nouns, and implicit-category rewording are excluded.

## Why

The commitment provides **form-from-filename classification**. A reader scanning a folder of nodes can tell a Decision from a Conviction, a Gloss, or a Pattern by filename shape alone — before opening any file. The Decision's filename reads as a move the project made at a moment (an adopted commitment, a chosen use, a stated preference); a Conviction's filename reads as a held stance (`Folders Serve Human Legibility, Not the Graph`, `Human Authority Over Augmentation Systems`); a Gloss carries the `<Concept> -- <definition>` separator; a Pattern reads as a recurring move or situation. The filename carries the form; the form carries the reader's expectations.

The two permitted shapes serve the same classification job differently. The action-verb lead is the ordinary case — the project made a choice, and the filename names the choice as a directive the reader can match against the project's behavior. The `<Subject> as <Role>` declarative is for Decisions whose force is about a subject playing a specific role — `Deep Context as an Architecture for Captured Reasoning` commits to reading Deep Context through a specific interpretive frame. Bare noun phrases (`YAML Scalar Rules`, `Three-Layer Architecture`) are excluded because they read as topics being described, not as commitments being made; comparative and declarative shapes starting with the subject (`<X> Over <Y>`, `<X> Is <Y>`, `<X> Carries <Y>`) are excluded because they overlap with Conviction filename shape and would silently mis-classify.

The verbatim-embedding rule protects **citation stability**. When a Decision's subject is something the graph already names — `Wikilinks and Named Edges` (the gist), `Markdown Node Contract` (an existing Contract), `Named Edge` (a Gloss) — the filename embeds the subject exactly as the graph names it. The Decision `Adopt Wikilinks and Named Edges.md` uses the gist's exact title; it does not paraphrase to `Adopt Wikilinks and Named Edges Convention.md` (appends an implicit category noun) or `Adopt the Wikilinks-and-Named-Edges Approach.md` (paraphrases and adds implicit category). Paraphrased filenames break citation in two directions: other nodes citing the subject lose resolution to the verbatim target, and readers looking up the subject by its established name find a file with a different title.

The two rules bundle because they share the form-from-filename Why and because rollback is bundled. Loosening the shape rule (accepting bare noun phrases) would produce Decisions indistinguishable from topic-descriptor files; loosening the verbatim-embedding rule (accepting paraphrases) would produce Decisions whose subjects drift from what the graph actually names. Both compromises would unwind the same discipline — that filenames classify form and preserve citation — from different directions. They are adopted and revisited together.

## Alternatives Considered

**Uniform filenames with type-in-predicate classification.** Let every node use a neutral `<Subject>.md` filename and classify by `conforms_to::` predicate in the identity block. Rejected because classification-by-filename is a tier cheaper than classification-by-identity-block. A reader scanning a folder of forty nodes sees forty filenames; to classify each by predicate, they would need to open each file. The filename-shape-carries-form convention is what makes classification a folder-view operation rather than a forty-file-open operation. The identity block is still required — the predicate is the graph-participating classification — but the filename shape is the cheap preview.

**Paraphrase for filename flow.** Allow Decision filenames to paraphrase their subjects for better reading ("Adopt the Wikilinks and Named Edges Convention" flows better than "Adopt Wikilinks and Named Edges"). Rejected because paraphrase introduces drift. A Decision named with a paraphrased subject no longer cites the subject by its established name; over time, the paraphrase becomes the de facto name of the subject in downstream nodes, and the original reference is lost. Verbatim embedding holds the graph's naming stable across Decisions that adopt or reinterpret existing nodes.

**Allow any filename the author chooses.** Treat the classification job as secondary and let authors name Decisions however they read best. Rejected because the filename is the cheapest classification tier. Giving it up means every folder-level operation (browse, search, cite, triage) has to pay the cost of opening or previewing each file to know what it is. The convention's benefit — form-from-filename at zero tooling — is what makes large corpora navigable; abandoning it collapses navigation onto tooling the graph is committed to not requiring.

## What Would Change It

The commitment bundles two rules; the revisit conditions share a source.

**Filename-based classification becomes redundant.** If tooling reliably classified nodes at folder-view time — if a file browser or wiki tool showed `conforms_to::` values alongside filenames in all common reading surfaces — the filename-shape convention would lose its cheap-tier benefit. The convention would remain valid but non-load-bearing. Current tooling does not do this across Obsidian, VS Code, GitHub's repository view, and the shell simultaneously; the convention continues to earn its weight.

**Citation resilience through renaming.** If wiki tooling grew universal redirect-on-rename support (any wikilink to an old filename resolved to the new one, annotated as a rename), the verbatim-embedding rule's citation-stability rationale would weaken. The rule would remain valid as a discipline (preventing paraphrase-drift in the graph's naming) but would no longer protect citation specifically. No such universal support exists; rename-tracking is tool-specific where it exists at all.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The wikilink spine resolves by filename. Filename-shape conventions are what let the graph's folder-level classification and citation operate at zero-tooling cost on top of that resolution.

- informs_downstream::[[Decision Form Contract]]
  - Decision Form Contract's filename-pattern Requirement carries the thin enforcement clause pointing at this Decision.

- contrasts_with::[[Conviction Form Contract]]
  - Conviction Form Contract's filename pattern is the mirror: Convictions MUST NOT use the action-verb lead or the `<Subject> as <Role>` declarative; their filenames read as held stances. The two Contracts' filename rules compose — if a filename shape fits a Decision, it does not fit a Conviction, and vice versa. Classification-by-filename depends on both rules holding.
