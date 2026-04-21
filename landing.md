# DeepContext

Deep Context is a **practice**, not a product -- a set of conventions for shared
knowledge work among heterogeneous contributors aligned around a common domain,
expressed in plain markdown with wikilinks and named edges, and curated with
Claude's help.

This site is the published view of the graph. Nodes are authored in the
[`deepcontext-dev`](https://github.com/ChristopherA/deepcontext-dev) workshop
and projected here for publication. The workshop retains drafts, decisions, and
process; this repository carries only the curated graph.

## Link legend

The graph is held together by `[[wikilinks]]` and `predicate::[[Target]]` named
edges. Six surface forms appear in node bodies.

**Resolved wikilink** -- renders as a working link to the target node.
[[Atomic Node]] is a live example; clicking it opens the Gloss.

**Pipe wikilink** -- displays custom text and links to the target. Source
syntax is `[[Atomic Node|atomic]]`, rendered: [[Atomic Node|atomic]].

**Ghost link** -- a named but unseeded concept. The target has no node yet, so
the graph shows the name without a destination.
[[A Concept That Does Not Yet Have A Node]] renders as ghost styling.

**External marker** -- a concept named in another garden or graph. The `↗`
suffix is the source-form convention; the rendered site styles it distinctly.
[[Egregore]]↗ is an example.

**Plain URL** -- a link to the web outside this graph. For example,
https://www.lifewithalacrity.com/2014/12/deep-context.html.

**Named edge** -- a typed relation in bullet form, e.g.
`conforms_to::[[Gloss Form Contract]]`. The predicate to the left of `::`
names the relation; the wikilink to the right names the target.

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
[AGENTS.md](https://github.com/ChristopherA/DeepContext.com/blob/main/AGENTS.md)
and the full
[CONVENTIONS.md](https://github.com/ChristopherA/deepcontext-dev/blob/main/CONVENTIONS.md)
in the workshop repository.

## Forking and contributing

This repository is **forkable and collaboratively editable** -- Egregore-style.
A fork produces its own Pages site on first push. Edit nodes directly via
github.com's web editor or clone locally; the same pipeline publishes every
downstream garden.
