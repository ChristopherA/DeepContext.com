---
created: 2026-04-23
tagline: Each scion is a self-contained repository with its own cryptographic identity via a locally-performed Open Integrity inception ceremony, and publishes its own GitHub Pages site
brief_summary: The publication unit of DeepContext is the scion — a graph whose content began as a clone of another DeepContext graph (the template), re-rooted locally with the first steward's own Open Integrity inception commit to produce a unique `did:repo:<sha1>` DID. Standing up a scion requires a local Scion Bootstrap ceremony because the OI inception commit must be signed by the first steward's SSH key, not by any hosting platform's. Each scion is a self-contained repository (its own build pipeline, its own content, nothing external required), publishes its own live GitHub Pages site after Bootstrap completes and Actions/Pages are enabled, accepts both OI-signed commits and GitHub Web-UI commits as contribution paths, and carries curation discipline in named conventions rather than in editorial permissions. The template relationship is recorded in a `.scion-identity.yml` file at the scion's root — the template DID and the scion's own DID live there and are updated by Bootstrap. No git-fork relationship is claimed because git-fork would share the root commit and therefore share the DID, collapsing identity sovereignty; GitHub's "Use this template" path is not supported either, because the re-root must be signed by the first steward and Actions cannot do that signing. Scions are the mechanism by which DeepContext's practice survives any one actor stepping away, authority calcification, and host-specific dependencies.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-23
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Growth Stage]]
- has_curation::[[Working Draft]]

# Adopt Scion Publication Model

A DeepContext graph publishes as a **scion** — a repository whose content began as a clone of another DeepContext graph, re-rooted locally with the first steward's own Open Integrity inception commit, producing a unique `did:repo:<sha1>` DID. Each scion is self-contained: its own build pipeline, its own content, its own configuration, nothing external required. Standing up a scion requires a local Scion Bootstrap ceremony — a clone, a local re-root signed by the first steward's SSH key, and a push to a newly-created GitHub repository under the first steward's GitHub account. After Bootstrap completes and the scion's Actions and Pages settings are enabled, subsequent pushes build and deploy the scion's own Pages site. The GitHub Web UI edit path remains a first-class contribution surface for ongoing content edits. Curation discipline lives in named conventions that travel with the nodes rather than in editorial permissions.

The scion relationship to its source template is recorded structurally in a `.scion-identity.yml` file at the scion's root. Bootstrap reads the template's DID from the file, performs the OI inception, and writes the scion's own DID alongside the template DID. The template relationship is also expressible at the graph layer as a `scion_of::[[did:repo:<template-sha1>]]↗` edge when the scion wants it traversable via graph queries. No git-fork relationship to the template is maintained, because git-fork would share the root commit and therefore share the DID, which would collapse the identity sovereignty each scion needs in order for cross-scion references to be unambiguous.

Identity sovereignty and identity-over-URL compose here. Because the DID is content-derived (the SHA1 of the OI inception commit), the same scion carries one DID across any git host (GitHub, GitLab, Radicle, and others); cross-host mirroring does not change identity. A resolver that walks from a DID to the scion's current host(s) does not yet exist — the DID widget in each page's footer records the identity in anticipation rather than because anything resolves it today.

## Scion, defined

A scion is a graph that carries some or all of another graph's content while holding its own cryptographic identity and editorial sovereignty. The term is chosen deliberately. In horticulture a scion is a cutting from a parent plant grafted onto a fresh rootstock; the grafted tree bears the parent's fruit and grows from the rootstock's roots. DeepContext scions work the same way: content can be inherited from the template, but the root — the cryptographic root, the inception commit, the DID — is fresh for each scion. The horticultural sense composes with the aristocratic sense, in which a scion is a descendant who carries a line forward under their own name.

The term replaces "fork" for this specific relationship. "Fork" in the GitHub sense is a git operation that shares the parent's commit history, including the inception commit, and therefore shares the DID. A scion is not a fork in that sense. Standing up a scion is a local ceremony — a clone of the template graph, followed by removal of the clone's `.git` directory, followed by a fresh OI inception commit signed by the first steward's SSH key — followed by a push to a newly-created GitHub repository (or any git host the first steward prefers). "Scion" leaves "fork" to mean what it means in git and does not fight for the term.

## Scion Bootstrap Ceremony

Identity sovereignty requires that the OI inception commit be signed by the first steward's own SSH key. No hosting platform's Actions runner has access to that key — Actions run with an ephemeral token and cannot produce a commit cryptographically traceable to the first steward. The Bootstrap ceremony is therefore local-only, and the first steward is the only party who can perform it.

Concretely:

1. Clone the template graph to the first steward's machine — `git clone <template-url> <scion-dir>`. What the first steward just got is a working directory of template content plus the template's full commit history.
2. Read the template's DID from `.scion-identity.yml` at the scion-dir root. The template ships this file with its own DID under `this_did:` — that value is what the scion will copy into its own `scion_of:` after Bootstrap produces the new inception commit.
3. Remove the scion-dir's `.git` directory entirely. This discards the template's history; the working-directory content remains.
4. Run the Scion Bootstrap skill. The skill checks for a configured signing SSH key (`user.signingkey` pointing at the first steward's SSH private or public key, with the corresponding public key in the first steward's GitHub allowed-signers), guides setup if missing, and then runs the OI inception ceremony (`.scripts/scion-inception.sh`) to produce a fresh root commit signed by the first steward. The new root commit's SHA1 is the scion's DID.
5. Commit the template's content as the scion's initial content commit (also signed by the first steward).
6. Update `.scion-identity.yml`: write the scion's own DID as `this_did`, preserve the template's DID as `scion_of`.
7. Create a new GitHub repository under the first steward's GitHub account (via `gh repo create <name>` or the GitHub web UI). This repository has no inherited state; it starts empty.
8. Add it as the scion's `origin` remote and push.
9. In the scion's GitHub Settings → Actions → General, allow Actions to run.
10. In the scion's GitHub Settings → Pages, set Source = GitHub Actions.
11. Subsequent pushes trigger the build-and-deploy Action and publish the scion's own Pages site with its own DID in the footer.

A deploy-gate step in the build Action reads `.scion-identity.yml` and compares `this_did` against the current repo's root-commit SHA1; if they do not match, Bootstrap has not been completed correctly and the site is not deployed. This prevents a partial setup from publishing with the wrong identity in the footer.

Bootstrap runs once per scion. Subsequent contributions use either the GitHub Web UI or local clones; only the initial OI inception requires the author-signed ceremony.

The first steward is the scion's founding **principal** — the cryptographic identity whose SSH key signs the inception commit and whose public key sits in the scion's allowed-signers. The first steward can add additional principals later by amending allowed-signers and delegating signing authority via the OI chain mechanism; additional principals become co-stewards whose OI-signed commits extend the chain of cryptographic authority the first steward founded. The scion's identity sovereignty therefore flows from an individual at inception but is not bound to that individual indefinitely — stewardship can expand as the practice around the scion grows.

`scion_of::` records initial lineage (how a scion began) and does not impose a fixed hierarchical relationship over time. Two scions of the same template — or a scion and its template — may become peers that exchange nodes bidirectionally through content-level operations. DeepContext.com is designed as a minimal seed rather than an active contribution target, so node flow from scions back to this repository is not expected; peering between two richer scions (for example, iterations.com and its own scions) is expected and normal, with nodes passed in both directions. Peer relationships are a separate architectural concept from initial scion lineage, not modeled by `.scion-identity.yml`; the practice may seed a corresponding Predicate when the first peering actually occurs and its shape is observable rather than speculated.

## Why

The practice's durability does not survive dependency on any single repository or editorial authority. The self-sovereign decentralized identity community, and several collaborative-wiki efforts, supply adjacent cases where centralization produced either bus-factor vulnerability or authority calcification. Scion publication is the architectural response: if anyone can stand up a scion, no one can own the practice.

The scion model also makes the project's other Convictions operational rather than aspirational. [[Vocabulary Diversity Is a Feature]] requires that contributors can hold their own vocabularies; a scion is the mechanism by which a contributor whose vocabulary diverges can continue the practice under their own identity. [[Terms Become Common Through Unanimity, Not Precedent]] requires that new common terms are chosen deliberately; the scion path is the escape hatch when unanimity cannot be reached. [[Translation Over Convergence]] names what agents do across vocabularies; scioning is what people do when translation cost exceeds what they are willing to pay.

The per-scion DID is not cosmetic. Each scion's DID is content-addressed — derived from the inception-commit SHA-1 — and therefore stable across hosts. A scion that moves from GitHub to Radicle keeps its DID; cross-scion references from peers do not break when hosting changes. URL-based federation is brittle to hosting decisions; DID-based federation is not. The federation layer's future cross-scion reference resolution runs on DIDs precisely because scions have them.

The commitment derives the pipeline's other architectural choices. Python-only with standard-library-plus-one-dependency exists so a scion does not need to configure external build services. All pipeline code and all configuration live inside the repository so a scion is self-contained. No committed secrets, no external repo references, no required package registries beyond PyPI. The GitHub Web UI is a supported edit path so a scion contributor can make changes without installing git or a local editor. Each of these choices is an implementation of the scion commitment; changing the commitment would cascade through them.

## Alternatives Considered

**Git-fork as the publication unit.** Let a reader fork the repository on GitHub, inheriting the full commit history including the root commit. Rejected because a git-fork shares the parent's root commit and therefore shares the parent's `did:repo:<sha1>` DID. Two repositories claiming the same DID are identity collision; scions need distinct identities to participate in federation unambiguously. The git-fork model also chains sync obligations between parent and fork in ways that make vocabulary divergence expensive; scions diverge without a git-upstream relationship and sync content via explicit content-level operations rather than git merges.

**Centralized publication, copies as read-only.** One canonical repository exists; others may mirror it for offline reading but cannot publish independently. Rejected because it vests practice continuity in a single actor. If the canonical publisher steps away, the practice has no default continuation. The self-sovereign identity community's post-COVID fracture is one of the concrete failures this alternative invites.

**Template with no ongoing deployment.** Provide a template repository new scions can instantiate, but do not commit to each scion producing its own live site. Rejected because it treats scioning as initial setup rather than the ongoing practice. The commitment is specifically that a scion is a live site on every push, not a project waiting for a deploy to be manually configured.

**Pages-enabled but private-repo-only.** Permit scioning among authorized collaborators only; keep the practice invite-only. Rejected because it recreates the authority-over-vocabulary dynamic the project is specifically trying to avoid. [[Consensus Creates Priesthoods]] records the pattern: whoever controls invitation controls which vocabularies count. Public scioning removes that lever entirely.

**Scioning via external tooling (static site hosting elsewhere).** Let scions use whatever hosting they prefer (Netlify, Vercel, personal servers). Rejected because it moves the scion-publish step outside GitHub's friction floor. A contributor who can edit a markdown file in the GitHub Web UI can scion-and-publish; a contributor who has to configure Netlify cannot, or will not. This rejection is specific to the current cycle's friction-floor concern; later cycles may relax it once alternative hosting's friction profile is understood.

**Enforce OI-signed commits exclusively.** Require every post-inception commit to carry an authorized SSH signature, per OI's chain-of-authority model. Rejected because it conflicts with the GitHub Web UI edit path — Web UI commits are signed by GitHub's internal key, not the committer's SSH key, and would all be rejected as unauthorized. The enforcement would raise the friction floor to "every contributor configures SSH signing," which moves scioning toward terminal-first contribution and collapses the non-developer edit path. The scion model accepts two-tier provenance instead: OI-signed commits extend the chain of cryptographic authority, and Web UI commits participate in the scion's history without extending the chain. Both are legitimate contributions; they carry different provenance strength, and the graph's rendering layer makes the distinction visible where it is load-bearing.

**Single-click scion via GitHub template plus Bootstrap Action.** Let a first steward click "Use this template" and have a GitHub Action perform the OI re-root automatically on first push, so no local clone is required. Rejected because the Action has no access to the first steward's SSH key, so the OI inception commit would be signed by the Actions runner's ephemeral token rather than by the first steward. That weakens identity sovereignty to "whoever controls the Actions token at bootstrap time," which defeats the commitment the scion model rests on. The scion model accepts a mandatory local step at inception in exchange for OI-grade identity sovereignty the first steward actually owns; the template-repository setting is therefore not enabled on this repository, and the scion-creation entry point is `git clone` rather than "Use this template."

## What Would Change It

**No scions happen.** If the template runs for an extended period with zero external scions, the scion machinery is carrying cost (pipeline self-containment, no-external-deps discipline, OI inception ceremony, re-root tooling) for no realized benefit. The revisit would ask whether the commitment is actually load-bearing for this practice or whether it is aspirational architecture that the reality of the practice does not need.

**Scions happen but the Web UI edit path is unused.** If scions exist but contributors always work from local clones, the Web-UI-edit commitment specifically — and the OI-signing compromise that enables it — is over-designed. The revisit would distinguish "scion-able at all" from "scion-able via Web UI" and might tighten OI-signing requirements while relaxing the Web UI path.

**DID management proves too high-friction.** If the OI inception ceremony, the Python reimplementation, or the allowed-signers maintenance turns out to filter out the contributors the practice is trying to reach, the stance would narrow — keep template instantiation as the mechanism but reduce the cryptographic-identity layer to something lighter. The revisit would ask what level of identity sovereignty is actually necessary for the practice vs aspirationally nice to have.

**Two-tier provenance creates confusion.** If the mixed OI-signed and Web-UI-signed history turns out to be harder to reason about than either pure path, the revisit would choose one. The default lean would be toward Web UI — preserving the non-developer edit path — with OI-signing restricted to specific operations (scion inception, key rotation, major content migrations) rather than every commit.

**Concentration of contribution stays high even with scioning.** If the scion mechanism works technically but contribution still concentrates in one or two actors, the commitment's value proposition is not working. The revisit would ask whether the concentration is downstream of the scion commitment itself (scioning alone is not enough to distribute participation) or downstream of other factors the project has not yet named.

**A successor architecture preserves the same properties more simply.** If a different mechanism produces the same content-lineage-plus-identity-sovereignty property with less pipeline overhead, the commitment survives but its implementation changes. The property is what is held; the specific machinery is how it is held today.

**Local Bootstrap friction filters out the contributors the practice is trying to reach.** If would-be first stewards consistently drop off at the "clone locally, configure SSH signing, run Bootstrap" ceremony — because signing-key configuration is too opaque, because OI tooling expects a command-line fluency the target audience does not have, or because the multi-step ceremony is experienced as forbidding — the local-only commitment is filtering what it should admit. The revisit would ask whether a lighter-weight tier (a GitHub-Actions-signed inception accepted as a weaker sovereignty tier, suitable for stewards who do not need full OI discipline) could sit alongside the local-signed tier rather than replace it. The full-sovereignty path stays available for stewards who want it; a lighter path is admitted for those for whom full sovereignty is not load-bearing.

## Relations

- grounded_in::[[Founding Vocabularies Constrain Later Participants]]
  - The pre-convergence architect-imposition Observation that makes the scion commitment more than a technical choice. If founding vocabularies calcify, scioning is the structural escape hatch that lets later participants carry the practice forward without being bound to the founding choices.

- grounded_in::[[Open Integrity Project (Blockchain Commons, 2025)]]
  - The cryptographic-identity specification that gives each scion its own DID. The inception-commit ceremony, the `did:repo:<sha1>` derivation, the delegated-authority mechanism for post-inception commits — all are OI moves this Decision rests on.

- informs_downstream::[[Adopt Minimum-Viable-Architecture Stance]]
  - The MVA Decision defers capabilities (heading links, transclusion, cross-scion resolution, interactive graph explorer) that would add pipeline complexity. The MVA deferrals are partly a scion-cost discipline: every capability added to the pipeline is a capability every scion inherits as a maintenance surface.

- informs_downstream::[[Publish via Actions Artifact Deploy]]
  - The Actions-deploy Decision records the specific Pages mechanism the scion publication runs on. Scion publication is the upstream claim; Actions-deploy is one implementation of it.

- informs_downstream::[[Link Rendered Pages to Markdown Source on GitHub]]
  - The source-link surface manifestation of the scion commitment. The Decision adds an Edit-on-GitHub link to every rendered page so a reader who wants to edit never has to reason about the repository's structure to find the source — one click exits the rendered site into the editable markdown.

- informed_by::[[Vocabulary Diversity Is a Feature]]
  - The Conviction that makes scioning load-bearing beyond technical concern. Without the diversity stance, a single-repo publication would be adequate; with it, scioning is what prevents vocabulary convergence from becoming the project's growth path.

- informed_by::[[Agora Project (Flancian, 2019)]]
  - The adjacent precedent that commits to aggregator-plus-many-gardens. The Alternatives section's "Scioning via external tooling" rejection contrasts against Agora's aggregator-as-separate-service model; the Reference captures the discrete features Agora names that this Decision decided differently on (unit of participation, whether each contribution produces its own live site, whether aggregation is a separate service).

- informed_by::[[Egregore Framework (Egregore Labs, 2026)]]
  - The adjacent precedent that commits to provision-from-template plus collaborator-invite. This Decision adopts Egregore's provision-from-template move (decoupled from the collaborator-invite and terminal-first bundle) and extends it with OI inception for cryptographic identity. The Egregore Reference names the discrete features this Decision draws on and the ones it leaves aside.

- informs_downstream::[[scion_of -- content lineage from a template graph]]
  - The Predicate that expresses a scion's template relationship as a first-class named edge. Each scion's `.scion-identity.yml` records the `scion_of` relationship structurally (template DID and the scion's own DID, written by Bootstrap); the Predicate's wikilink form `scion_of::[[did:repo:<template-sha1>]]↗` is the graph-layer expression the scion may additionally use when traversability matters. The edge is the graph-layer mechanism this Decision's identity-sovereignty commitment is expressed through on a specific scion.

- informs_downstream::[[Scion Bootstrap]]
  - The Skill that operationalizes this Decision's local-only ceremony for standing up a scion. The Decision's Scion Bootstrap Ceremony section names the procedure at the architectural level; the Skill walks a first steward through the concrete steps (prerequisite install chain via brew / gh / ssh-keygen, the clone + rm .git + inception commit sequence, the `.scion-identity.yml` update, the GitHub repo creation and Pages enablement). Without the Skill, the Decision's ceremony is prose only; with the Skill, it is an agent-invocable procedure.

- informs_downstream::[[Scion Address -- the compound DID form identifying a specific node within a specific graph]]
  - The Gloss that names the compound DID form this Decision's node-level addressing commitment takes. When the Decision says "cross-scion references carry identity rather than URL," the Scion Address is the shape those references have at page granularity — a `did:repo:<sha1>/<path>` that identifies a specific node within a specific scion without embedding any git-forge URL convention. Every rendered page's footer emits this form in anticipation of future resolvers.

- informs_downstream::[[External Node -- a node that lives in another graph, referenced without being imported]]
  - The Gloss that names the concept scions create: a node this graph references but does not own because it lives in another graph (a peer scion, the template, or some unrelated graph). The Decision's peering paragraph acknowledges that nodes flow bidirectionally between some scions; External Node is the vocabulary for the receiving side of any such reference.

- informs_downstream::[[Embed Images via Obsidian Wikilink Syntax]]
  - The image-embed Decision's commitment to committing `Attachments/` alongside the content, and to copying it into the build output, is grounded in this Decision's self-containment rule: every scion must get working image rendering on first clone with no additional configuration. Gitignored attachments or externally-hosted images would break the scion promise at the asset layer; committed attachments and the copy-attachments build step keep it holding.
