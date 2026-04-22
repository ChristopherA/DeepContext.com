# DeepContext.com

A curated knowledge graph that captures reasoning -- the values, patterns,
decisions, and what would change them -- in plain-markdown nodes with
named-edge predicates. Published at **[deepcontext.com](https://deepcontext.com/)**.

The site is the reader-facing view: start at the landing page for the
project's vision, link legend, and reading paths. The founding commitment
is [Deep Context as an Architecture for Captured Reasoning](nodes/Decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.md)
-- typed markdown forms with traversable named-edge predicates, not
fine-tuning, not retrieval chunks, not databases, not tags.

This README is the GitHub-facing view: what you need to fork, build, and
contribute.

## Forking

The repository is self-contained. A fork produces its own Pages site on
first push -- no external build service, no linked data repository, no
package registry beyond PyPI. The curation discipline lives in the
conventions captured under `nodes/Contracts/`, not in editorial
permissions; a fork inherits the conventions and decides what to keep or
revise.

To fork:

1. Fork on GitHub.
2. In the fork's **Settings -> Actions -> General**, allow Actions to run
   (forked workflows are disabled by default for security).
3. In the fork's **Settings -> Pages**, set **Source = GitHub Actions**.
4. Edit nodes directly via the web UI, or clone locally.
5. Push. The Action builds `.build/` and deploys it as a Pages artifact.

Decision backing this model: [Adopt Forkable Publication Model](nodes/Decisions/Adopt%20Forkable%20Publication%20Model.md).

## Local build

Requirements: Python 3.11+ and [`uv`](https://docs.astral.sh/uv/).

```
uv sync
uv run python .scripts/build.py
```

Output appears in `.build/`. The local output should match the Action's
output (modulo build timestamps). `.build/` is gitignored and regenerates
per deploy -- no generated HTML lives in git.

## Pipeline

```
Source (nodes/*.md, landing.md)
   |
   v
slugify.py           filename -> slug table, with collision detection
linkify.py           wikilinks -> links / ghost spans / external spans
render.py            markdown -> HTML via python-markdown
generate_indexes.py  per-taxonomy indexes, landing page, style.css,
                     .nojekyll, CNAME
   |
   v
.build/  uploaded as Pages artifact, deployed via actions/deploy-pages
```

Decision backing this pipeline: [Publish via Actions Artifact Deploy](nodes/Decisions/Publish%20via%20Actions%20Artifact%20Deploy.md).

## Layout

```
DeepContext.com/
|-- README.md            <- this file (GitHub-facing)
|-- landing.md           <- site landing page source
|-- AGENTS.md            <- orientation for AI agents
|-- LICENSE
|-- pyproject.toml       <- Python dependencies (uv-managed)
|-- uv.lock              <- dependency lockfile
|-- .gitignore
|-- nodes/               <- the node graph, organized by taxonomy
|-- .scripts/            <- Python build pipeline + CSS
|-- .github/workflows/   <- build-and-deploy action
`-- .build/              <- generated site (gitignored)
```

## Contributing

Contributions are welcome via this repository's
[Issues](https://github.com/ChristopherA/DeepContext.com/issues),
[Discussions](https://github.com/ChristopherA/DeepContext.com/discussions),
and Pull Requests. Any node under `nodes/` can be edited via the GitHub
Web UI; committing opens a pull request branch.

Two Convictions shape how contributions land in this graph:

- [Vocabulary Diversity Is a Feature](nodes/Convictions/Vocabulary%20Diversity%20Is%20a%20Feature.md)
  -- contributors keep their own vocabulary; the graph translates across
  vocabularies rather than normalizing them.
- [Terms Become Common Through Unanimity, Not Precedent](nodes/Convictions/Terms%20Become%20Common%20Through%20Unanimity,%20Not%20Precedent.md)
  -- a term becomes part of the shared vocabulary only by explicit
  agreement, never by one contributor's repeated usage alone.

The practice is built on the understanding that collaborative knowledge
work is genuinely hard -- power-law participation, vocabulary accumulation,
and the rare trait combination contribution requires. The landing page's
"The tension this addresses" section walks through the Observations behind
this. The bet is that culture and tooling can do better than past best
practices, not that past failure modes can be wholly overcome.

## License

See `LICENSE`.
