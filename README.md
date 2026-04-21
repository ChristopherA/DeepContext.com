# DeepContext.com

The published view of the Deep Context graph. This is the GitHub-facing
front page; the site's landing page is in `landing.md` and renders to
`/index.html` during build.

## What this repository publishes

A curated node graph published as a static site. See `landing.md` (or visit
the published site) for the graph's vision, link legend, and form-type
guide. This repository is the source of truth; contributions are welcome
via Issues, Discussions, and Pull Requests.

## Forking

Forks produce their own Pages site on first push -- no external build
dependencies, no external repo references. The pipeline is self-contained
in `.scripts/` and the workflow in `.github/workflows/build-and-deploy.yml`.

To fork:

1. Fork on GitHub.
2. In the fork's **Settings -> Actions -> General**, allow Actions to run
   (forked workflows are disabled by default for security).
3. In the fork's **Settings -> Pages**, set **Source = GitHub Actions**.
4. Edit nodes directly via the web UI, or clone locally.
5. Push. The Action builds `.build/` and deploys it as a Pages artifact.

## Local build

Requirements: Python 3.11+ and [`uv`](https://docs.astral.sh/uv/).

```
uv sync
uv run python .scripts/build.py
```

Output appears in `.build/`. The output should match what the Action
produces (modulo build timestamps).

## Pipeline

```
Source (nodes/*.md, landing.md)
   |
   v
slugify.py      filename -> slug table, with collision detection
linkify.py      rewrite wikilinks to links / ghost spans / external spans
render.py       markdown -> HTML via python-markdown
generate_indexes.py
                per-taxonomy index pages, landing page, style.css, .nojekyll
   |
   v
.build/  uploaded as Pages artifact and deployed via actions/deploy-pages
```

`.build/` is gitignored; the workflow regenerates it in the runner for each
deploy. No build output in git, no self-triggering cycle to prevent.

## Layout

```
DeepContext.com/
|-- README.md            <- this file (GitHub-facing)
|-- landing.md           <- site landing page source
|-- AGENTS.md            <- orientation for AI agents
|-- pyproject.toml       <- Python dependencies (uv-managed)
|-- nodes/               <- the node graph (see landing page for overview)
|-- .scripts/            <- Python build pipeline + CSS
|-- .github/workflows/   <- build-and-deploy action
|-- .build/              <- generated site (gitignored; regenerated per deploy)
```

## Contributing

Contributions are welcome via this repository's
[Issues](https://github.com/ChristopherA/DeepContext.com/issues),
[Discussions](https://github.com/ChristopherA/DeepContext.com/discussions),
and Pull Requests. Edit nodes via the GitHub Web UI or clone locally. See
`landing.md` for the link legend, form types, and reading paths.

## License

See `LICENSE`.
