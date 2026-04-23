---
created: 2026-04-23
tagline: DeepContext.com is a template; each scion is a self-contained repository with its own cryptographic identity via an Open Integrity inception commit, and publishes its own GitHub Pages site
brief_summary: The publication unit of DeepContext is the scion — a graph instantiated from a template repository, re-rooted with its own Open Integrity inception commit that produces a unique `did:repo:<sha1>` DID. Each scion is a self-contained repository (its own build pipeline, its own content, nothing external required), publishes its own live GitHub Pages site on first push, accepts both OI-signed commits and GitHub Web-UI commits as contribution paths, and carries curation discipline in named conventions rather than in editorial permissions. The template relationship between a scion and its source is expressed in the graph via a content-level `scion_of::` edge pointing at the template's DID; no git-fork relationship is claimed because git-fork would share the root commit and therefore share the DID, collapsing identity sovereignty. Scions are the mechanism by which DeepContext's practice survives any one actor stepping away, authority calcification, and host-specific dependencies.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-23
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Growth Stage]]
- has_curation::[[Working Draft]]

# Adopt Scion Publication Model

A DeepContext graph publishes as a **scion** — a repository instantiated from a template, re-rooted with its own Open Integrity inception commit, producing a unique `did:repo:<sha1>` DID. Each scion is self-contained: its own build pipeline, its own content, its own configuration, nothing external required. A scion's first push triggers its GitHub Pages site, and the GitHub Web UI edit path remains a first-class contribution surface. Curation discipline lives in named conventions that travel with the nodes rather than in editorial permissions.

The scion relationship to its source template is expressed at the graph layer, not the git layer. A scion's identity declaration carries a `scion_of::[[did:repo:<template-sha1>]]↗` edge pointing at the template's DID. No git-fork relationship to the template is maintained, because git-fork would share the root commit and therefore share the DID, which would collapse the identity sovereignty each scion needs in order for cross-scion references to be unambiguous.

## Scion, defined

A scion is a graph that carries some or all of another graph's content while holding its own cryptographic identity and editorial sovereignty. The term is chosen deliberately. In horticulture a scion is a cutting from a parent plant grafted onto a fresh rootstock; the grafted tree bears the parent's fruit and grows from the rootstock's roots. DeepContext scions work the same way: content can be inherited from the template, but the root — the cryptographic root, the inception commit, the DID — is fresh for each scion. The horticultural sense composes with the aristocratic sense, in which a scion is a descendant who carries a line forward under their own name.

The term replaces "fork" for this specific relationship. "Fork" in the GitHub sense is a git operation that shares the parent's commit history, including the inception commit, and therefore shares the DID. A scion is not a fork in that sense. The GitHub operation that produces a scion is `gh repo create --template` followed by a scion-bootstrap ceremony that performs the OI inception. "Scion" leaves "fork" to mean what it means in git and does not fight for the term.

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

## What Would Change It

**No scions happen.** If the template runs for an extended period with zero external scions, the scion machinery is carrying cost (pipeline self-containment, no-external-deps discipline, OI inception ceremony, re-root tooling) for no realized benefit. The revisit would ask whether the commitment is actually load-bearing for this practice or whether it is aspirational architecture that the reality of the practice does not need.

**Scions happen but the Web UI edit path is unused.** If scions exist but contributors always work from local clones, the Web-UI-edit commitment specifically — and the OI-signing compromise that enables it — is over-designed. The revisit would distinguish "scion-able at all" from "scion-able via Web UI" and might tighten OI-signing requirements while relaxing the Web UI path.

**DID management proves too high-friction.** If the OI inception ceremony, the Python reimplementation, or the allowed-signers maintenance turns out to filter out the contributors the practice is trying to reach, the stance would narrow — keep template instantiation as the mechanism but reduce the cryptographic-identity layer to something lighter. The revisit would ask what level of identity sovereignty is actually necessary for the practice vs aspirationally nice to have.

**Two-tier provenance creates confusion.** If the mixed OI-signed and Web-UI-signed history turns out to be harder to reason about than either pure path, the revisit would choose one. The default lean would be toward Web UI — preserving the non-developer edit path — with OI-signing restricted to specific operations (scion inception, key rotation, major content migrations) rather than every commit.

**Concentration of contribution stays high even with scioning.** If the scion mechanism works technically but contribution still concentrates in one or two actors, the commitment's value proposition is not working. The revisit would ask whether the concentration is downstream of the scion commitment itself (scioning alone is not enough to distribute participation) or downstream of other factors the project has not yet named.

**A successor architecture preserves the same properties more simply.** If a different mechanism produces the same content-lineage-plus-identity-sovereignty property with less pipeline overhead, the commitment survives but its implementation changes. The property is what is held; the specific machinery is how it is held today.

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
