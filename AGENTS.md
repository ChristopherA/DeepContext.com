# AGENTS

Orientation for AI agents working on this graph. Read this first; then open
the Contracts under `nodes/Contracts/` for the structural rules and the
landing page for the practice's stance.

## The graph in one paragraph

DeepContext is a typed knowledge graph that captures **reasoning** --
values, patterns, decisions with their alternatives and revisit conditions,
observations with their epistemic grounds, convictions with their drift
recognition. Each node is a plain-markdown file with a block of identity
predicates above the H1, a body shaped by the node's form contract, and a
`## Relations` section carrying typed edges to other nodes. The founding
commitment is
[Deep Context as an Architecture for Captured Reasoning](nodes/Decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.md),
grounded in two Convictions:
[Capture Reasoning, Not Just Knowledge](nodes/Convictions/Capture%20Reasoning,%20Not%20Just%20Knowledge.md)
and
[Knowledge Outlives Its Tools](nodes/Convictions/Knowledge%20Outlives%20Its%20Tools.md).

## Graph conventions (short form)

- Nodes live in `nodes/<Taxonomy>/` where taxonomy is one of Contracts,
  Decisions, Convictions, Aspirations, Observations, Patterns, Predicates,
  Glosses, References.
- Wikilinks: `[[Target]]` resolves by filename stem (or by the concept
  side of a `Concept -- definition` Gloss or Predicate). Pipe form
  `[[Target|Display]]` shows the alias. External marker `[[Target]]↗`
  names a concept in another graph. The external marker uses the actual
  `↗` character (U+2197 NORTH EAST ARROW) in source text. Do NOT
  substitute `\u2197` or similar escape notation -- escapes render as
  literal characters in markdown, not as the arrow.
- Named edges: `predicate::[[Target]]` bullets in the identity block and
  in the `## Relations` section carry the graph's typed structure. Each
  Relations-section edge carries an indented annotation explaining why
  the edge matters -- unannotated edges are tag spaghetti, not graph.
- Each Predicate under `nodes/Predicates/` defines its own typed edge with
  a Carries section (what the predicate asserts), a per-neighbor Crescent
  section (what it holds that near-neighbors do not), and Typing (what
  kinds of nodes it connects).

Detailed specs: `nodes/Contracts/Markdown Node Contract.md` and the
form-specific Contracts (Gloss, Decision, Conviction, Aspiration,
Observation, Pattern, Predicate, Reference).

## Role for agents

The project's stance on agent behavior lives in
[Agents Translate, Not Extract](nodes/Convictions/Agents%20Translate,%20Not%20Extract.md).
Short form:

**Curate, do not overwrite.** Suggest annotations, flag conflation,
propose upgrades to construction predicates. Never rewrite a contributor's
vocabulary without explicit confirmation.

**Translate across vocabularies rather than normalize them.** When two
contributors use different terms for adjacent territory, both edges land
in the graph as distinct claims. Read across them; do not collapse them
into a canonical form. The Convictions
[Vocabulary Diversity Is a Feature](nodes/Convictions/Vocabulary%20Diversity%20Is%20a%20Feature.md)
and
[Translation Over Convergence](nodes/Convictions/Translation%20Over%20Convergence.md)
record this directly.

**Name features, not traditions.** When adapting a concept from an
adjacent tradition or vocabulary (the Egregore vision, the Alexandrian
pattern language, capability-based security, the project's own Deep
Context Architecture, and so on), name the specific features you are
drawing on rather than pointing at the tradition as the source of
framing. "Egregore-shaped commitment" imports the tradition's frame;
"self-contained repository, fork-publishes-on-first-push, Web-UI-edit-is-first-class,
curation-in-conventions" names the features. The Vocabulary Diversity Is
a Feature stance extends to traditions as well as contributor vocabularies:
using something is not adopting its vocabulary, and the distinction is
load-bearing for forks whose context differs from the parent's.

**Treat new common vocabulary as proposal, not adoption.**
[Terms Become Common Through Unanimity, Not Precedent](nodes/Convictions/Terms%20Become%20Common%20Through%20Unanimity,%20Not%20Precedent.md)
asks that a term become shared only when participants agree to it. An
agent propagating a term across nodes through repeated consistent use is
the failure mode this Conviction specifically guards against. If a term
looks like it should become common, propose it explicitly (in a commit
message, a Discussion, a Decision note) rather than establishing it
through your own usage.

**Preserve reasoning in the form.** Each form contract specifies sections
that carry reasoning -- Why, Alternatives Considered, and What Would
Change It for Decisions; Grounds and What Would Revise It for
Observations; Why It Is Held and Drift Recognition for Convictions; Why
It Pulls, Current Gap, and Work for Aspirations. When drafting in these
forms, preserve the contributor's voice and framing. Do not generalize
into a house style; do not drop sections because they feel redundant;
keep the specific rejected alternatives, the specific grounds, the
specific drift signals.

**Remain authored-by. Not authoring.** Annotations and edges are
author-declared. An agent generates candidate annotations for review, it
does not commit them as claims. The authorship chain
(`authored_by::[[Deep Context Community]]` or a specific contributor)
must remain accurate; an agent adds a commit on behalf of a human
contributor, never as itself.

## Local build (for verification)

```
uv sync
uv run python .scripts/build.py
```

Output lands in `.build/`. The GitHub Action runs the same command in a
runner and uploads `.build/` as a Pages artifact; nothing commits back to
the repository. `.build/` is gitignored.

## A fork's AGENTS.md may differ

Forks are first-class. A fork may revise this file to reflect its own
stance on agent behavior. Agents working on a fork should read that fork's
AGENTS.md rather than assume this one applies. The parent's Conviction
nodes are inherited by default; what the fork keeps, extends, or overrides
is the fork's to decide, and should be visible in the fork's own node
graph rather than inferred from the parent.
