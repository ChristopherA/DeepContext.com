---
created: 2026-04-21
tagline: DeepContext.com is a self-contained repository that any reader can fork and publish as their own Pages site with no external dependencies
brief_summary: The publication model for DeepContext.com is shaped by four specific features: the repository is self-contained (its own build pipeline, its own configuration, its own content, nothing external required); a fork produces its own live site on first push (forking is the ongoing practice, not initial-setup-then-fork-goes-dormant); the GitHub Web UI is a first-class edit path (no local tooling required to contribute); and curation discipline lives in named conventions that travel with the nodes rather than in editorial permissions. These features together make the practice durable against any one actor stepping away, against authority calcification, and against the post-COVID fracture of online knowledge communities the project sits adjacent to. This Decision is the upstream commitment that derives most other pipeline choices -- Python-only, no external build dependencies, all configuration in the repo.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-21
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Adopt Forkable Publication Model

The DeepContext.com repository is a self-contained publication unit. A reader encountering the graph can fork the repository, and the fork's own GitHub Pages site publishes on the fork's first push with no external repo dependencies, no private build infrastructure, and no required local tooling. Editing a node through the GitHub Web UI is a first-class contribution path -- a commit from the Web UI triggers the same build and deploy that a local git push does. The curation discipline lives in the conventions encoded in the node graph itself, not in editorial permissions.

The four features that characterize the model are named deliberately, not borrowed from any one tradition. A self-contained repository is one where nothing external is required: no private build service, no external data repository, no linked package the maintainer controls. A fork that produces its own live site is one where forking is the ongoing practice rather than an initial setup step; the fork's first push builds its own site the same way the parent's push builds the parent's. A first-class Web UI edit path is one where editing a single file through github.com's browser-based editor and clicking Commit produces a deployed change without the contributor ever needing local tooling. Curation-in-conventions is the discipline that each fork inherits the same named commitments the parent holds, and both keep or revise them in the open rather than through permissioned review.

## Why

The project holds that the practice's durability does not survive dependency on any single repository or editorial authority. The self-sovereign decentralized identity community, and several collaborative-wiki efforts, supply adjacent cases where centralization produced either bus-factor vulnerability or authority calcification. The forkable publication model is the project's architectural response: if anyone can fork and publish, no one can own the practice.

The forkability commitment also makes the project's other Convictions operational rather than aspirational. [[Vocabulary Diversity Is a Feature]] requires that contributors can hold their own vocabularies; forking is the mechanism by which a contributor whose vocabulary diverges can continue the practice without either converging on the parent's vocabulary or having to start over. [[Terms Become Common Through Unanimity, Not Precedent]] requires that new common terms are chosen deliberately; forking is the escape hatch when unanimity cannot be reached. [[Translation Over Convergence]] names what agents do across vocabularies; forking is what people do when the translation cost exceeds what they are willing to pay.

The commitment derives most of the pipeline's other architectural choices. Python-only with standard-library-plus-one-dependency exists so a fork does not need to configure external build services. All pipeline code and all configuration live inside the repository so a fork is self-contained. No committed secrets, no external repo references, no required package registries beyond PyPI. The GitHub Web UI is a supported edit path so a fork contributor can make changes without installing git or a local editor. Each of these choices is an implementation of the forkability commitment; changing the commitment would cascade through them.

## Alternatives Considered

**Centralized publication only, fork as read-only copy.** The traditional pattern: one publisher's repository is canonical, forks exist for reading but do not produce their own sites. Rejected because it vests continuity of the practice in a single actor. If the publisher steps away, stops maintaining, or shifts direction, the practice has no default continuation. The community's experience with the post-COVID fracture of the self-sovereign identity space is one of the concrete failures this alternative invites.

**Fork-from-template but no ongoing deployment.** Provide a repository template new gardens can copy, but do not commit to forks producing their own live sites. Rejected because it treats forking as initial setup rather than as the ongoing practice. The Egregore-shaped commitment is specifically that forks are sites, not projects waiting for a deploy to be manually configured.

**Pages-enabled but private-repo-only.** Allow forkability among authorized collaborators only; keep the practice invite-only. Rejected because it recreates the authority-over-vocabulary dynamic the project is specifically trying to avoid. [[Consensus Creates Priesthoods]] records the pattern: whoever controls invitation controls which vocabularies count. Public forkability removes that lever entirely.

**Forkability via external tooling (static site hosting elsewhere).** Let forks use whatever hosting they prefer (Netlify, Vercel, personal servers). Rejected because it moves the fork-and-publish step outside GitHub's friction floor. A contributor who can edit a markdown file in the GitHub Web UI can fork-and-publish; a contributor who has to configure Netlify cannot, or will not.

## What Would Change It

The commitment is provisional in the sense that it sits on empirical claims about forkability actually being used. Several conditions could revise it.

**No forks happen.** If the repository runs for an extended period with zero external forks, the forkability machinery is carrying cost (pipeline self-containment, no-external-deps discipline) for no realized benefit. The revisit would ask whether the forkability commitment is actually load-bearing for this practice or whether it is aspirational architecture that the reality of the practice does not need.

**Forks happen but the Web UI edit path is unused.** If forks exist but contributors always work from local clones, the Web-UI-edit commitment specifically (and its downstream pipeline constraints) is over-designed. The revisit would distinguish "forkable at all" from "forkable via Web UI" and might relax the latter.

**Concentration of contribution stays high even with forkability.** If the forkability works technically but contribution still concentrates in one or two actors, the commitment's value proposition is not working. The revisit would ask whether the concentration is downstream of the forkability commitment itself (e.g., forkability alone is not enough to distribute participation) or downstream of other factors the project has not yet named.

**A successor architecture preserves the same properties more simply.** If a different mechanism produces the same fork-publish-travel property with less pipeline overhead (for instance, a GitHub Actions template marketplace entry that absorbs the boilerplate), the commitment survives but its implementation changes.

## Relations

- grounded_in::[[Founding Vocabularies Constrain Later Participants]]
  - The pre-convergence architect-imposition Observation that makes the forkability commitment more than a technical choice. If founding vocabularies calcify, forking is the structural escape hatch that lets later participants carry the practice forward without being bound to the founding choices.

- informs::[[Adopt Minimum-Viable-Architecture Stance]]
  - The MVA Decision defers capabilities (heading links, transclusion, cross-garden resolution, interactive graph explorer) that would add pipeline complexity. The MVA deferrals are partly a forkability-cost discipline: every capability added to the pipeline is a capability every fork inherits as a maintenance surface.

- informs::[[Publish via Actions Artifact Deploy]]
  - The Actions-deploy Decision records the specific Pages mechanism the forkability commitment runs on. The forkability commitment is the upstream claim; the Actions-deploy choice is one implementation of it.

- informed_by::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes forkability load-bearing beyond technical concern. Without the diversity stance, a single-repo publication would be adequate; with it, forkability is what prevents vocabulary convergence from becoming the project's growth path.
