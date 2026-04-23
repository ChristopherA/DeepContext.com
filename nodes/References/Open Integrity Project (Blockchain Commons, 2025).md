---
created: 2026-04-23
tagline: A specification for per-repository cryptographic identity through an empty, signed root commit that produces a unique DID
brief_summary: The Open Integrity Project specifies a cryptographic-identity layer for git repositories. Each repository has a unique DID of the form `did:repo:<root-commit-sha1>`, derived from a specially-constructed inception commit — empty tree, signed with a specific SSH key, canonical commit message. The inception commit is mandatorily the root commit; its empty-tree property is the security claim, reducing the SHA-1 collision attack surface. Delegated authority for subsequent commits lives in an in-repo `allowed_commit_signers` file. DeepContext adopts the inception-commit ceremony as the mechanism by which each scion gets its own DID, decoupled from git hosting — a scion moving from GitHub to Radicle keeps its DID because the DID is content-addressed, not location-addressed. Adopted: the inception ceremony, the `did:repo:<sha1>` derivation, the delegated-authority mechanism for post-inception commits. Not adopted: the full `.repo/` directory structure proposal (deferred; DeepContext places the allowed-signers file where it fits the pipeline), the zsh dependency of the authoritative reference implementation (DeepContext ports the ceremony to POSIX sh at `.scripts/scion-inception.sh` with byte-identical commit output), pre-receive hook enforcement (optional reinforcement only).
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Repository Identity Foundation]]
- authored_by::[[Blockchain Commons]]↗
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Open Integrity Project (Blockchain Commons, 2025)

URL: <https://github.com/OpenIntegrityProject/core>

## Sources

- Problem Statement: <https://github.com/OpenIntegrityProject/core/blob/main/docs/Open_Integrity_Problem_Statement.md>
- Script Snippets: <https://github.com/OpenIntegrityProject/core/blob/main/docs/Open_Integrity_Script_Snippets.md>
- Repository Directory Structure: <https://github.com/OpenIntegrityProject/core/blob/main/docs/Open_Integrity_Repo_Directory_Structure.md>

The Open Integrity Project (OI) is a specification for cryptographic identity of git repositories. An OI-compliant repository begins with an inception commit — an empty-tree commit signed with a specific SSH key, carrying a canonical Ricardian-contract commit message. The inception commit's SHA-1 hash is the repository's DID: `did:repo:<inception-commit-sha1>`. Because the DID is derived from content (the commit hash), not location (a URL or hosting provider), it survives migration between hosts and remains authoritative across GitHub, GitLab, Radicle, or self-hosted git.

Post-inception commits carry authority through a delegated-authority file at `.repo/config/verification/allowed_commit_signers`, listing SSH public keys authorized to sign future commits. The inception key is the root of trust; the allowed-signers file extends authority outward.

### Adopted

- **The inception-commit ceremony as the DID-generating moment.** Every DeepContext scion has its own OI inception commit, which is what gives the scion its own DID. This is decoupled from git hosting; the same scion hosted on two services shares one DID because both hosts carry the same root commit. Git-fork publishing is rejected for the opposite reason: a fork shares its parent's root commit and therefore its parent's DID.
- **The `did:repo:<sha1>` derivation.** DeepContext uses OI's scheme verbatim. Scion identity is the DID; scion URL is location; the two are distinct concerns.
- **The delegated-authority mechanism for post-inception commits.** The `allowed_commit_signers` file is the authoritative list of keys whose commits count toward the scion's OI-signed history. Scions with multiple contributors use this mechanism rather than sharing the inception key.
- **Content-level lineage expression.** OI provides no metadata field for "this inception derives from another inception." DeepContext expresses scion-to-template lineage at the graph layer — a dedicated named edge from the scion's identity declaration to the template's DID — rather than lobbying for an OI-layer predicate. The graph is where reasoning lives; OI is where identity lives; the two layers compose without either having to reach into the other.

### Not adopted

- **The proposed `.repo/` directory layout.** OI's `Open_Integrity_Repo_Directory_Structure.md` proposes a `.repo/` root for verification files, hooks, scripts, and docs. The layout document marks itself as "a first pass" and acknowledges "much of this doesn't currently work with various Git hosting services (for instance GitHub & GitLab put their files in `.github/` `.gitlab/` respectively)." DeepContext places the allowed-signers file where the pipeline and conventions call for it, without committing to the full `.repo/` layout. A later scion or a future revision may adopt the layout when its value justifies the migration; the OI mechanism works without it.
- **Zsh dependency of the reference implementation.** The authoritative OI inception implementation is the `z_Create_Inception_Repository` function in Blockchain Commons' `_Z_Utils.zsh` library (invoked via `setup_git_inception_repo.sh`), which is zsh-specific. A simpler one-line educational snippet lives in `Open_Integrity_Script_Snippets.md` and is also zsh; its output shape differs from the authoritative implementation in Signed-off-by position, Signed-off-by identity, and one comma in the canonical body. DeepContext ports the authoritative implementation's inception logic to POSIX sh at `.scripts/scion-inception.sh` so the ceremony runs in any POSIX shell (sh, dash, ash, bash, zsh) without a zsh dependency. The port uses the same two `-m` arguments plus `--signoff` as the authoritative implementation, producing commit output byte-identical to DeepContext.com's own root commit (modulo author identity, committer key, timestamp, and signature nonce). The ceremony calls external tools (`git`, `ssh-keygen`, `awk`, `date`) that are shell-native across platforms; no Python wrapper is introduced because a wrapper would just call the same external tools with a Python layer on top.
- **Pre-receive hook enforcement of signature policy.** OI's problem statement mentions pre-receive hooks as a reinforcement mechanism. DeepContext relies on client-side verification only; the scion's published site is the artifact, and signature verification is available to anyone auditing the repository but not enforced at push time.
- **The "every commit after inception requires an authorized SSH signature" requirement as a blocking rule.** DeepContext accepts two contribution paths: OI-signed commits from contributors with configured SSH signing, and GitHub Web-UI commits (signed by GitHub's internal key, not by the scion's authorized signers). The two paths carry different provenance strength; the scion's history is a mixture of OI-signed and unsigned commits by design. This is a deliberate departure from OI's chain-of-authority model, made to preserve the GitHub Web-UI edit path as a first-class contribution surface.

### Key moves to remember

- The inception commit's empty-tree property is load-bearing for OI's security claim. A commit with arbitrary files as commit #0 does not provide the SHA-1 collision resistance OI rests on. When a scion is bootstrapped from a GitHub template (whose first commit is a non-empty "Initial commit" carrying all template files), the scion's first action is to re-root — rewrite history so the first commit is a fresh OI inception, with template content re-parented as commit #1. This re-rooting is an operation that establishes OI for a repository that never claimed OI; it is distinguished from the attack case (rewriting a repository's established OI history) by the declared pre-OI state of the initial commit.
- DIDs are content-addressed, not location-addressed. A scion's `did:repo:<sha1>` is stable across hosts. Cross-scion references in the federation layer use DIDs rather than URLs, which means a scion migrating from GitHub to Radicle does not break its peers' references to it.
- The "controller" and "subject" distinction in OI's future W3C DID Controller Document example (repo-as-subject, developer-as-controller) composes with the scion model at the long-term extension layer. A scion's DID is the subject; the contributor who holds the inception key is the controller. Scions with rotating maintainers manage this through the allowed-signers file rather than through inception-key transfer.

## Relations

- informs_downstream::[[Adopt Scion Publication Model]]
  - The Scion Publication Decision commits to each scion having its own OI inception commit and therefore its own DID. This Reference is the specification the commitment runs on.

- informs_downstream::[[Knowledge Outlives Its Tools]]
  - The Conviction's commitment that knowledge survive particular tools composes with OI's commitment that identity survive particular hosts. A scion's DID is not dependent on GitHub; the scion can migrate between hosts without losing its cryptographic name. This Reference is the mechanism the Conviction's host-agnostic commitment runs on at the identity layer.

- contrasts_with::[[Egregore Framework (Egregore Labs, 2026)]]
  - Egregore uses `gh repo create --template` for instance provisioning — the same mechanism DeepContext adopts — but does not layer cryptographic identity over it. Each Egregore instance shares the same underlying GitHub identity model as any other repo in the organization. DeepContext adopts Egregore's provision-from-template move and extends it with OI inception to give each scion its own DID.

- informs_downstream::[[scion_of -- content lineage from a template graph]]
  - The Predicate that expresses template-to-scion lineage as a first-class named edge. Because OI makes the scion's DID distinct from the template's, the relationship between them cannot be the shared-root-commit git-fork relation; it must live at the graph layer. This Predicate is the graph-layer expression of a distinction that OI makes real at the cryptographic layer.
