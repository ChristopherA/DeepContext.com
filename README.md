# DeepContext.com

A curated knowledge graph that captures reasoning -- the values, patterns,
decisions, and what would change them -- in plain-markdown nodes with
named-edge predicates. Published at **[deepcontext.com](https://deepcontext.com/)**.

The site is the reader-facing view: start at the landing page for the
project's vision, link legend, and reading paths. The founding commitment
is [Deep Context as an Architecture for Captured Reasoning](nodes/Decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.md)
-- typed markdown forms with traversable named-edge predicates, not
fine-tuning, not retrieval chunks, not databases, not tags.

This README is the GitHub-facing view: what you need to stand up your own
Deep Context graph, build, and contribute.

**Stand up your own graph:** see the Graph Inception section below.
Standing up a graph is a local `git clone` (or fresh `git init`) plus an
Inception ceremony signed by your own SSH key -- not a GitHub "Use this
template" click, because Actions cannot sign an Open Integrity inception
commit as you. A new graph has its own DID and its own purpose; it may
optionally claim **scion-of lineage** from a donor graph when the new
graph intends to track the donor as upstream (the rare parallel-fork
case), but most new graphs do not.

## Graph Inception

A Deep Context **graph** is a repository carrying typed markdown nodes
with named-edge predicates. Each graph has its own `did:repo:<sha1>` DID
derived from its own OI inception commit, its own Pages site, and its own
content to evolve as its first steward sees fit. The curation discipline
lives in the conventions captured under `nodes/Contracts/`, not in
editorial permissions.

A graph standing up from a clone of an existing graph (the donor)
typically grafts the donor's meta-layer (Contracts, Predicates, generic
Skills) and authors its own content from there. Per-node graft provenance
is recorded via the `grafted_from::` predicate when traceability matters.
The new graph may additionally claim **scion-of lineage** from the donor
by recording `scion_of:` in `.deep-context-identity.yml` -- but most graphs do
not, because the scion claim signals upstream-tracking intent (parallel-
fork case) rather than mere content adoption. The seed graph
(DeepContext.com) carries no donor and is not a scion.

Standing up a graph is a local ceremony. The inception commit must be
signed by the first steward's own SSH key, so no one-click GitHub path
works -- Actions cannot sign as the steward. The template-repository
setting is not enabled on this repository for the same reason; the entry
point is `git clone` (or fresh `git init`), not "Use this template."

### Prerequisites

The Graph Inception skill checks and helps install these; a first steward
running the ceremony manually sets them up directly.

- `git config user.name` and `git config user.email` set.
- `git config user.signingkey` pointing at an SSH private or public key.
- The corresponding SSH public key registered for signing at
  https://github.com/settings/ssh/signing.
- `ssh-keygen` available on PATH (standard on macOS and most Linux).

### Ceremony

1. Clone this repository to your machine (skip if standing up a fresh
   graph with no donor):
   ```
   git clone https://github.com/ChristopherA/DeepContext.com.git <graph-name>
   cd <graph-name>
   ```

2. Remove the cloned `.git` directory -- the donor's history is
   discarded along with it; the working-tree content remains:
   ```
   rm -rf .git
   ```

3. Run the Open Integrity inception ceremony to produce a fresh root
   commit signed by your SSH key. The Graph Inception skill wraps this;
   running manually, `.scripts/oi-inception.sh` is the core primitive.
   The new root commit's SHA1 is your graph's DID.

4. Commit the working-tree content as your graph's initial content commit
   (also SSH-signed). Update `.deep-context-identity.yml` at the graph root:
   write your graph's new DID under `this_did`. If your graph claims
   scion-of lineage from the donor (parallel-fork-tracking intent), write
   the donor's DID under `scion_of`; otherwise leave `scion_of: null`.
   Most graphs do not claim scion-of.

5. Create a new GitHub repository under your account:
   ```
   gh repo create <graph-name> --public --source=. --push
   ```
   or create via the GitHub web UI, then `git remote add origin <url>`
   and `git push -u origin main`.

6. In your graph's **Settings -> Actions -> General**, allow Actions to run.

7. In your graph's **Settings -> Pages**, set **Source = GitHub Actions**.

8. Subsequent pushes trigger the build-and-deploy Action and publish your
   graph's Pages site with its own DID in the footer.

Decision backing this model: [Adopt Scion Publication Model](nodes/Decisions/Adopt%20Scion%20Publication%20Model.md).

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
