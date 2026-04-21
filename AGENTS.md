# AGENTS

Orientation for AI agents working on this graph. Full conventions live in the
workshop repository; this file gives enough to start.

## What this repository is

`DeepContext.com` is a curated knowledge graph published as a static site.
This repository is the source of truth; contributions flow in via GitHub
Issues, Discussions, and Pull Requests.

## Graph conventions

- Nodes are plain markdown files in `nodes/<Taxonomy>/`.
- Wikilinks: `[[Target]]` resolves to a node by filename stem (or by the
  concept side of a `Concept -- definition` gloss/predicate name).
- Pipe wikilinks: `[[Target|Display Text]]` displays the alias.
- External marker: `[[Target]]↗` names a concept in another graph.
- Named edges: `predicate::[[Target]]` bullets below the H1 and in the
  `## Relations` section carry the graph's typed structure.

Full conventions: the Contract nodes under `nodes/Contracts/` and the landing
page's Link Legend and Form Types sections.

## Taxonomies

`Contracts/`, `Decisions/`, `Convictions/`, `Aspirations/`, `Observations/`,
`Patterns/`, `Predicates/`, `Glosses/`, `References/`.

## Local build

```
uv sync
uv run python .scripts/build.py
```

Output lands in `.build/`. The GitHub Action runs the same command and
commits `.build/` back to `main` on every push.

## Role for agents

Curate, do not overwrite. Suggest annotations, flag conflation, upgrade
construction predicates, never rewrite a contributor's vocabulary without
confirmation. Detailed stance: `Agents Translate, Not Extract` Conviction in
the workshop.
