---
created: 2026-04-21
tagline: Build the site in a GitHub Actions runner and deploy the artifact; do not commit built output to the repository
brief_summary: DeepContext.com publishes via GitHub Pages' Actions artifact deployment, not via branch deployment with committed build output. The pipeline runs on every push to main, produces .build/ in the runner, uploads it as a Pages artifact, and deploys it through actions/deploy-pages. The .build/ directory is gitignored; no generated HTML lives in git. The Decision records a mid-execution pivot -- the initial PRD committed to .build/ being committed to main and served via branch deployment, but GitHub Pages' branch-deploy source only accepts '/' or '/docs' as folder options. Renaming to /docs was rejected as semantically overloaded; switching to Actions artifact deploy keeps the .build/ name, cleans git history of generated output, and drops the loop-prevention mechanics (paths-ignore, bot-author guard) that committed-build required.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-21
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Publish via Actions Artifact Deploy

DeepContext.com publishes via GitHub Pages' Actions artifact deployment. Every push to `main` triggers a workflow that installs dependencies, runs the build script in the runner, produces a `.build/` directory containing the rendered site, uploads it with `actions/upload-pages-artifact`, and deploys it through `actions/deploy-pages`. The Pages source is configured to "GitHub Actions" rather than "Deploy from a branch." The `.build/` directory is gitignored; no generated HTML is tracked in git. A fork repeats the same workflow on its own pushes once the fork owner enables Actions and sets the fork's Pages source to "GitHub Actions."

The Decision records a mid-execution pivot. The project's Static Site Generation PRD initially committed to branch deployment with `.build/` committed to `main`, on the assumption that GitHub Pages could serve any configured folder. It cannot -- branch-deploy source only accepts `/` or `/docs`. The pivot happened during the first deploy attempt.

## Why

The underlying commitment is the forkability model from [[Adopt Forkable Publication Model]]: the pipeline must run in the fork's own environment without external dependencies. Whether the build output is committed or regenerated per deploy is downstream of that commitment, and either works in principle. The specific choice between the two came down to three considerations the constraint forced into view.

The first is git-history hygiene. Committed build output doubles the diff on every content change -- once for the source change, once for the regenerated HTML. Git blame becomes noisy, the repository grows faster than content grows, and reviewers scanning commits see artifact churn alongside meaningful changes. Actions artifact deploy keeps generated output out of git entirely; the repository size and diff noise stay proportional to source change.

The second is loop-prevention complexity. Committed build output requires the workflow to push its own commits back to `main`, which creates a self-trigger cycle that needs blocking. The initial PRD specified two layers of defense: a `paths-ignore: ['.build/**']` filter on the `push` trigger, and a bot-author check that skipped the workflow when the triggering commit came from `github-actions[bot]`. The belt-and-suspenders pattern works but adds surface area that can silently break (a contributor committing their own `.build/` edit, a re-run under a non-bot identity). Actions artifact deploy has no cycle to break: the workflow produces an artifact and the Pages service deploys it, with no write back to `main`.

The third is artifact regeneration as a property rather than a risk. Committed build output encodes the state of the source at the time of commit; any drift between the committed `.build/` and what a local `build.py` run would produce is silent. Actions artifact deploy regenerates from source on every push, so the live site is always the current `build.py` output. A reader running `build.py` locally produces the same site the runner produces, modulo build timestamps.

The cost of switching is that first-time fork owners have to do one more configuration step. Branch-deploy forks need "Source = Deploy from a branch; Folder = /docs or /." Actions-deploy forks need "Source = GitHub Actions" plus a one-time Actions enablement (forked workflows are disabled by default for security). Both are one-time clicks in Settings. The Actions-enable requirement is the meaningful friction increment; the Pages-source change is comparable to branch-deploy.

## Alternatives Considered

**Rename `.build/` to `/docs/` and keep committed build output via branch deploy.** The minimal-change remedy to the original PRD. Rejected because `docs/` is conventionally the folder for documentation (a repository's docs directory, rendered at `/docs/` on Pages for project sites). Using it for generated site output overloads the name and misleads contributors who open `docs/` expecting documentation sources.

**Build into repository root (`/`) via branch deploy.** Put generated HTML at the repo root alongside `nodes/` and the pipeline code. Rejected because it pollutes the root with build artifacts (an `index.html`, taxonomy folders mirrored at root, `style.css`) that collide visually and sometimes literally with source files.

**Use a third-party deploy action (JamesIves/github-pages-deploy-action or similar).** Deploy to a `gh-pages` branch that Pages serves from, keeping `.build/` generated per workflow run but not in `main`. Rejected because third-party actions add supply-chain surface (pinning to a trusted version, reviewing updates) that the forkability commitment specifically tries to minimize. `actions/deploy-pages` is maintained by GitHub itself and is the platform's current recommended path.

**Keep committed `.build/` via a different folder name that Pages accepts.** Serve from `/docs` but keep the semantics clear with a prominent note. Rejected for the same reason as the first alternative; the note would be a signal that the folder name is fighting its convention.

## What Would Change It

**Actions requirement becomes a meaningful friction floor for forks.** If the data shows forks commonly fail to enable Actions (leaving their Pages site as a 404) the friction is blocking rather than a one-time setup cost. A revisit would reconsider committed-build with `/docs` renaming or a branch-deploy flow that fork owners can enable with fewer clicks.

**GitHub changes Pages branch-deploy to support arbitrary folders.** If `/.build/` becomes a valid branch-deploy folder, committed-build returns as an option with the original cost profile. The current revisit condition is a specific platform change, not a general architectural shift.

**The pipeline grows enough that build times matter.** The current build completes in roughly 10 seconds. If the pipeline grows complex enough (large corpus, heavier rendering, additional preprocessing) that every-push rebuilds become slow or expensive, incremental builds or pre-computed artifacts become attractive. The revisit would reconsider whether build-in-runner or build-and-cache is the right pattern.

**A fork's independent pipeline diverges from the parent's.** If a fork modifies the pipeline in ways that break the Actions-deploy contract, and the parent wants to support fork-with-custom-pipeline without imposing conventions on the fork, a different architecture (e.g., fork brings its own workflow) might be preferable. This is a forkability edge case the current Decision doesn't resolve.

## Relations

- grounded_in::[[Adopt Forkable Publication Model]]
  - The upstream commitment this Decision implements. Forkability requires some mechanism for forks to publish their own sites; Actions artifact deploy is the specific mechanism chosen.

- informs_downstream::[[Markdown Node Contract]]
  - The Contract specifies the source form the pipeline consumes; this Decision specifies one of the Pages-deployment paths the output can take. The Contract is stable across deployment choices; this Decision can change without affecting source form.
