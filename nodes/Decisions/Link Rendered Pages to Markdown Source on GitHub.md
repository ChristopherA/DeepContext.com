---
created: 2026-04-22
tagline: Every rendered page that has a single markdown source carries a footer link to that source on GitHub
brief_summary: A commitment that the build pipeline renders a small "Edit on GitHub" link in the footer of every page whose HTML was rendered from a single markdown source -- node pages, the landing page, and hand-authored taxonomy indexes. Auto-generated taxonomy indexes (synthesized from multiple files) omit the link. The target URL is constructed from a GITHUB_REPO_URL constant plus the source file's repo-relative path, URL-encoded for filenames with spaces or special characters. Forks point the constant at their own repo, or set it empty to suppress the link entirely.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-22
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Link Rendered Pages to Markdown Source on GitHub

The build pipeline renders a small "Edit on GitHub" link at the bottom right of every page whose HTML was generated from a single markdown file. Node pages link to their source under `nodes/<Taxonomy>/<filename>.md`. The landing page links to `landing.md`. Hand-authored taxonomy indexes (when a taxonomy folder carries a `README.md`) link to that README. Auto-generated taxonomy indexes — synthesized from multiple node files' tagline and brief_summary metadata — omit the link, because they have no single markdown source to point at.

## Why

The commitment makes the graph's forkable model concrete at the reader's point of contact. A reader arriving at a rendered page who notices an error, disagrees with a claim, or wants to propose a revision can jump to the markdown source in one click and open a GitHub web-UI editor from there. The render-to-source path was implicit — any reader who understood the project could construct the URL themselves — but the click eliminates the distance between reading and contributing. The project's Adopt Forkable Publication Model Decision commits the graph to being contributable-in-place; this Decision is that commitment's surface manifestation on the rendered site.

The commitment also serves later-cycle contributors specifically. A first-cycle reader rarely contributes. A second-cycle reader — someone who has read enough of the graph to form a specific correction or elaboration — will contribute only if the path from reading to editing is short. A footer link that reads "Edit on GitHub" names the action and opens the path. The Aspiration `[[The Second Cycle of Contribution Happens]]` names the scarcity; this Decision's concrete move is to remove one small friction between reading and the second-cycle act of editing.

The GitHub-specific URL construction is a deliberate coupling to the hosting platform. The project is published via GitHub Pages, its source lives in a GitHub repository, and the Web UI editor is GitHub's. The Decision commits to that platform rather than trying to be hosting-neutral. Forks hosted elsewhere would need to revise the link generation; the `GITHUB_REPO_URL` and `GITHUB_BRANCH` constants in `.scripts/render.py` are the intended revision surface.

## Alternatives Considered

**No source link; trust the reader to find their way.** Rely on the project's Forkable Publication Model plus the README's fork-and-edit instructions. Readers who want to contribute can navigate from the rendered site to the repository by reading the README. Rejected because the README is a destination a contribution-minded reader must actively seek out; the footer link is a destination that finds the reader. The Decision's whole rationale is friction reduction at the point of contact; trusting the reader to find the path is exactly the friction the commitment exists to remove.

**Link to the rendered-page view, not the source.** Point at `/nodes/decisions/adopt-node-atomicity/` rather than at the markdown. Rejected because the rendered page is what the reader is already looking at; the link's purpose is to reach the *editable* form. A link back to the rendered page serves navigation, not contribution.

**Link to the repository folder, not the file.** Point at `/nodes/Decisions/` on GitHub rather than at the specific `.md` file. Rejected because it costs the reader a second click to find the file among its siblings, and that second click often loses readers who had a specific correction in mind. The direct file link opens the content the reader was just reading, ready to edit.

**Add the link through an HTML template layer with theme support.** Use a Jekyll, MkDocs, or Hugo theme that has the feature built in. Rejected because the build pipeline is already custom and minimal; adding a theme layer for one feature violates the project's zero-tooling-floor posture. The custom footer emission is six lines of Python; a theme migration is a project.

**Make the link optional per-page via frontmatter.** Let individual nodes opt in or out. Rejected because the default answer is "every page should link to its source." Per-page opt-out creates inconsistency for no demonstrated reason; a node that wanted to suppress the link could be addressed by a Contract-level refinement if such a need ever arose.

## What Would Change It

Three signals would prompt revisit.

**A fork adopts a different hosting platform and keeps the convention.** If forks start publishing to GitLab, Codeberg, Gitea, or self-hosted alternatives, the hard-coded GitHub URL becomes a drift hazard. The current `GITHUB_REPO_URL` / `GITHUB_BRANCH` constants suffice for single-platform forks; multi-platform abstraction would become worth adopting. No such pressure exists yet.

**The link accumulates maintenance burden out of proportion to its value.** If later work reveals that the footer link breaks (e.g., files renamed without updating references; branches other than main become relevant; filenames with characters the URL-encoding doesn't handle) at a rate that costs meaningful time to repair, the Decision would be reconsidered in favor of a lazier link-construction strategy or removal.

**GitHub changes its web-UI editor in ways that degrade the contribution path.** If GitHub removes the pencil-icon edit flow, paywalls the editor, or redirects logged-out users in ways that break the intended "click to edit" experience, the link's utility drops enough to warrant a rethink. The link itself is cheap to remove; the commitment rests on the destination serving its purpose.

## Relations

- grounded_in::[[Adopt Forkable Publication Model]]
  - The Decision that commits the graph to publication as an editable repository rather than a read-only site. This Decision is that commitment's surface manifestation: a click from every rendered page to the editable markdown source.

- informs::[[The Second Cycle of Contribution Happens]]
  - The Aspiration names second-cycle contribution as the scarce resource. This Decision's concrete move is to remove one small friction at the point where a second-cycle reader is most likely to contribute: they notice something they would fix, and the edit path is one click away.

- built_on::[[GitHub Pages]]↗
  - The hosting platform this Decision couples to. The `GITHUB_REPO_URL` and `GITHUB_BRANCH` constants in `.scripts/render.py` name that coupling explicitly; forks publishing elsewhere revise those constants.

- informs::[[Publish via Actions Artifact Deploy]]
  - The Decision backing the build-and-deploy pipeline this Decision extends. The source-link emission runs as part of `render.py`; the existing Actions workflow deploys the rendered output unchanged.
