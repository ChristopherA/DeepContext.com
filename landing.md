# DeepContext

Deep Context is a **practice**, not a product -- a set of conventions for shared
knowledge work among heterogeneous contributors aligned around a common domain,
expressed in plain markdown with wikilinks and named edges, and curated with
Claude's help.

This repository is the source of truth for the published graph. The conventions,
the node drafts, and the discussion all live here on GitHub. Comments and
contributions are welcome via Issues, Discussions, and Pull Requests.

## Why this exists

Wikis drift toward write-only: contributors keep adding, but the shared
vocabulary gets flattened by editorial convergence, participation concentrates
in the bus-factor-of-one who does the curation, and newcomers can't find a way
in. [[Wikis Without Curation Drift Toward Write-Only]] reconstructs the pattern
across several wiki traditions.

Deep Context tries a different route: preserve contributors' vocabularies as
load-bearing rather than convergence-friendly, surface distinctions rather than
paper them over, and treat curation as a practice with named commitments
rather than an editorial instinct. The nodes in this graph are the result --
rules that make vocabulary diversity structurally supportable, and enough
visible scaffolding for a newcomer to enter mid-stream without having to learn
an oral tradition first.

## Where to start

Different entry points by what you want to understand.

**The conventions** -- [Contracts](/nodes/contracts/) specify node shapes
(Contract, Decision, Conviction, Gloss, Observation, and so on) with RFC 2119
compliance rules. Start with [[Markdown Node Contract]] for the base shape,
then [[Contract Form Contract]] for how contracts themselves are structured.

**The choices and their reasoning** -- [Decisions](/nodes/decisions/) each
record what was chosen, what was considered, and what would change the call.
[[Adopt Wikilinks and Named Edges]] is the foundational one.

**The stance** -- [Convictions](/nodes/convictions/) are normative positions
the practice holds. [[Human Authority Over Augmentation Systems]],
[[Vocabulary Diversity Is a Feature]], and [[Translation Over Convergence]]
are the current six.

**The direction** -- [Aspirations](/nodes/aspirations/) name what the
project pulls toward with honest acknowledgement of the gap.
[[The Second Cycle of Contribution Happens]] is the core success metric.

**The open questions** -- [Observations](/nodes/observations/) record
descriptive claims with epistemic grounds (Empirical, Retrospective,
Contested). Contested observations like
[[LLM Assistance Widens the Participation Gap]] are claims the project takes
seriously but does not yet have a definitive answer to.

**The predicates** -- [Predicates](/nodes/predicates/) document the typed
edges themselves. [[conforms_to]], [[grounded_in]], [[informed_by]], and
[[contrasts_with]] are the most load-bearing.

## Link legend

The graph is held together by `[[wikilinks]]` and `predicate::[[Target]]` named
edges. Six surface forms appear in node bodies.

**Resolved wikilink** -- source `[[Target]]`; rendered as a working link that
preserves the brackets, so the source pattern stays legible on the site.
[[Atomic Node]] is a live example; clicking it opens the Gloss. Brackets are
kept deliberately ([see the Decision](/nodes/decisions/render-bare-wikilinks-with-visible-brackets/)).

**Pipe wikilink** -- source `[[Target|Display]]`; rendered as the display text
only so it reads naturally in prose. The full filename stem on a Gloss like
Compound Node is long; the pipe lets a reference read as
[[Compound Node -- a folder of markdown nodes with a designated lead|Compound Node]]
(displayed as "Compound Node", linked to the Gloss).

**Ghost link** -- a named but unseeded concept. The target has no node yet, so
the graph shows the name in ghost styling. Every identity block in this graph
currently carries `has_lifecycle::[[Seed Stage]]`, but [[Seed Stage]] itself
is a ghost -- the lifecycle vocabulary is named but not yet seeded as nodes.

**External marker** -- a concept named in another graph. The `↗` suffix is
the source-form convention. [[Egregore]]↗ is a real one in this graph --
the Conviction that [[Agents Translate, Not Extract]] names it as the
adjacent vision this project engages with.

**Plain URL** -- a link to the web outside this graph. For example,
https://www.lifewithalacrity.com/2014/12/deep-context.html.

**Named edge** -- a typed relation in bullet form, e.g.
`conforms_to::[[Gloss Form Contract]]`. The predicate to the left of `::`
names the relation; the wikilink to the right names the target. Each
[Predicate](/nodes/predicates/) is itself a node specifying what the
predicate carries, what it distinguishes itself from, and the node shapes
it connects.

Unresolved and external targets render with visibly-distinct styling so a
reader can see where the graph ends.

## Form types

Each node conforms to one of nine Form Contracts. Each contract names a shape
and a compliance rule; the Decisions that ground each contract carry the
reasoning.

- **Contract** -- what a node of this form looks like. Example: [[Gloss Form Contract]].
- **Decision** -- what was chosen, why, and what would change it. Example: [[Adopt Wikilinks and Named Edges]].
- **Conviction** -- a normative stance the project holds. Example: [[Human Authority Over Augmentation Systems]].
- **Aspiration** -- a direction the project pulls toward, with acknowledged gaps. Example: [[The Second Cycle of Contribution Happens]].
- **Observation** -- a descriptive claim with epistemic grounds (Empirical, Retrospective, Contested). Example: [[Wikis Without Curation Drift Toward Write-Only]].
- **Pattern** -- a recurring craft move that resolves a tension. Example: [[Refactor the Predicate's Axes]].
- **Predicate** -- a typed edge with Carries, Crescent, and Typing sections. Example: [[conforms_to]].
- **Gloss** -- an interpretive definition that frames a concept. Example: [[Atomic Node]].
- **Reference** -- an external source the graph draws on. Example: [[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]].

## Browse by taxonomy

- [Contracts](/nodes/contracts/)
- [Decisions](/nodes/decisions/)
- [Convictions](/nodes/convictions/)
- [Aspirations](/nodes/aspirations/)
- [Observations](/nodes/observations/)
- [Patterns](/nodes/patterns/)
- [Predicates](/nodes/predicates/)
- [Glosses](/nodes/glosses/)
- [References](/nodes/references/)

## For agents

Agents collaborating on this graph should start with
[AGENTS.md](https://github.com/ChristopherA/DeepContext.com/blob/main/AGENTS.md),
which names the curator stance (suggest, flag, translate -- do not rewrite a
contributor's vocabulary without confirmation) and points at the taxonomy
entry points. Agents joining a fork should read their own fork's AGENTS.md
first; forks may customize the stance.

## How to contribute

This repository is the source of truth for the published graph. Contributions
are welcome through GitHub.

- **Read first.** Browse the taxonomies or follow the reading paths above.
  The graph is in its seed stage; not every node you want to reference will
  exist yet. Ghost links mark where gaps are.
- **Open an [Issue](https://github.com/ChristopherA/DeepContext.com/issues)
  or [Discussion](https://github.com/ChristopherA/DeepContext.com/discussions)**
  to propose a node, flag a conflation between two concepts, suggest a predicate,
  or ask a question about the conventions.
- **Edit directly in the GitHub Web UI.** Any node under `nodes/` can be
  edited in-browser; clicking "Commit changes" opens a pull request.
- **Fork the repository** to build your own garden on these conventions. A
  fork publishes to its own Pages site on first push -- see
  [README.md](https://github.com/ChristopherA/DeepContext.com#readme) for
  setup.

The practice is Egregore-style: forkable, collaboratively editable, no single
editorial gatekeeper. The curation discipline lives in the conventions, not in
permissions.
