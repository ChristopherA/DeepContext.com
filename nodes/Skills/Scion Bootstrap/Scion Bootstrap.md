---
runtime_name: scion-bootstrap
tagline: Performs the local Open Integrity inception ceremony that turns a cloned DeepContext graph into a scion with its own SSH-signed root commit and DID
description: |
  Guides a first steward through the local Scion Bootstrap ceremony that re-roots a cloned DeepContext graph with a fresh Open Integrity inception commit signed by the steward's own SSH key, producing the scion's own `did:repo:<sha1>` DID. Verifies prerequisites, walks a missing-prereq steward through the brew/gh/ssh-keygen install chain, runs `.scripts/scion-bootstrap.sh` for the ceremony proper, and reports next steps for standing up the scion's GitHub repository and Pages site.

  WHEN: the user has cloned a DeepContext graph locally and wants to turn the clone into a scion with its own cryptographic identity; the user says "bootstrap scion", "scion bootstrap", "initialize my scion", "run bootstrap", "/scion-bootstrap"; a fresh scion directory contains `.scion-identity.yml` with `scion_of: null` and `.git` pointing at the template's history.

  WHEN NOT: the repository is DeepContext.com itself or another root template (the ceremony is for scions, not for the graph being cloned from); the local repository already has a Bootstrapped scion identity (the directory's `.scion-identity.yml` records a `scion_of` value and `this_did` matches the current root-commit SHA1); the user is exploring a scion someone else stood up (use Graph Orient for orientation); a contributor is editing content on an existing scion (direct git edits, not re-Bootstrap).
---

- conforms_to::[[Skill Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Scion Bootstrap

Performs the local ceremony that turns a cloned DeepContext graph into a scion with its own cryptographic identity. The ceremony is local-only because the Open Integrity inception commit must be signed by the first steward's own SSH key; no hosting platform's Actions runner has access to that key, so a single-click "Use this template" path cannot produce an inception with identity sovereignty flowing from the scion owner rather than from the runner's ephemeral token.

The skill runs in two phases. The first phase verifies prerequisites and walks a missing-prereq first steward through the install chain — Homebrew if absent, `gh` via Homebrew, and an SSH signing key generated and registered by `gh auth login -p ssh` (the modern `gh` flow generates a key if none exists and registers it with GitHub for both authentication and signing in one interactive walk), with git configured to use the key for signing. The second phase runs `.scripts/scion-bootstrap.sh`, which reads the template's DID from `.scion-identity.yml`, removes the cloned `.git` directory, produces a fresh OI-signed root commit via `.scripts/scion-inception.sh`, commits the scion's content signed by the first steward, and writes the scion's new DID back into `.scion-identity.yml`.

Bootstrap runs once per scion. After it completes, the steward creates a new GitHub repository under their account, pushes, and enables Actions and Pages. The Decision backing the ceremony's shape is [[Adopt Scion Publication Model]].

## Steps

### Step 1: Confirm the user is ready to Bootstrap

Before touching prerequisites or running any ceremony commands, confirm with the user that they have cloned a DeepContext graph locally and want to turn this working directory into a new scion. Name what the ceremony does at a high level — it discards the template's git history, produces a fresh OI-signed root commit with the steward's own SSH key, and commits the scion's initial content. Name what it cannot do — it cannot be signed by GitHub Actions, cannot be undone by a simple git command once the content commit lands, and requires an SSH key the user controls.

If the user has not cloned the graph yet, walk them through the clone step first: `git clone https://github.com/ChristopherA/DeepContext.com.git <scion-name>` and `cd <scion-name>`. If the user is in DeepContext.com itself rather than a fresh clone, stop — Bootstrap is for scions, not for the template.

### Step 2: Verify platform and package manager

Check the platform:

```sh
uname
```

If `Darwin` (macOS), the install chain uses Homebrew. If `Linux`, the install chain uses Homebrew or the distribution's package manager; the instructions below assume Homebrew for consistency, and the steward running on Linux may substitute `apt`/`dnf`/`pacman` for the equivalent packages.

Check whether Homebrew is installed:

```sh
command -v brew
```

If missing, offer to install it. Homebrew's install script requires an admin password and takes several minutes. Do not install without user consent. If consented, run:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After install, ensure the new `brew` shim is on PATH for the current session (the installer prints the two-line `eval "$(...)"` snippet to run).

### Step 3: Verify gh

Check whether `gh` (GitHub CLI) is installed:

```sh
command -v gh
```

If missing, install it:

```sh
brew install gh
```

Then ensure the user is authenticated:

```sh
gh auth status
```

If not authenticated, run `gh auth login` and walk the user through the interactive prompts. Choose HTTPS (for now; SSH auth is orthogonal to the SSH signing key the ceremony uses) and authenticate via web browser.

### Step 4: Verify an SSH signing key

Check whether git has a signing key configured:

```sh
git config user.signingkey
```

If empty, use `gh` to generate and register one. The `gh auth login -p ssh` flow walks an interactive prompt that generates a new SSH key (if none exists on disk), registers the key with GitHub, and in the modern flow offers to register it for **both authentication and signing** in a single walk:

```sh
gh auth login -p ssh
```

Follow the prompts: choose to generate a new SSH key, accept the default filename unless there's a reason not to, pick a passphrase or accept empty, and complete the browser handoff for authentication. When the flow asks about signing key upload, accept it — the generated key is registered as a signing key in the same step.

After `gh` completes, configure git to use the key for commit signing:

```sh
git config --global gpg.format ssh
git config --global user.signingkey "$HOME/.ssh/id_ed25519.pub"
```

(Adjust the path if `gh` placed the key under a different filename — the interactive flow reports the path.)

Verify the key is registered for signing:

```sh
gh ssh-key list
```

The output should show at least one entry with type `signing`. If the modern `gh auth login` flow did not register the key for signing on this user's install, add it explicitly:

```sh
gh ssh-key add ~/.ssh/id_ed25519.pub --type signing --title "DeepContext scion Bootstrap signing key"
```

### Step 5: Verify git identity

Check that `user.name` and `user.email` are set:

```sh
git config user.name
git config user.email
```

If either is empty, set them globally. The email should match the email on the user's GitHub account so the signing key is associated correctly with commits.

```sh
git config --global user.name "Name"
git config --global user.email "email@example.com"
```

### Step 6: Run the Bootstrap script

With prerequisites satisfied, run:

```sh
.scripts/scion-bootstrap.sh
```

The script:

1. Reads the template's `this_did` from `.scion-identity.yml`.
2. Removes the cloned `.git` directory (discards template history).
3. Runs `.scripts/scion-inception.sh .` to produce a fresh empty OI-signed root commit in the current directory.
4. Captures the new scion DID from `git rev-parse HEAD`.
5. Updates `.scion-identity.yml`: `this_did` becomes the new DID, `scion_of` becomes the template's former `this_did`.
6. Stages all working-tree content and commits it as the scion's initial content commit, signed by the first steward's SSH key.

If the script errors, read the error message and return to the appropriate step. The script's errors name which prerequisite is missing or which path is wrong; re-running after the fix is safe as long as `.git` is still present from the original clone (if the script partially ran and already removed `.git`, see the skill's troubleshooting notes under `## Scripts` below).

### Step 7: Create the scion's GitHub repository

Create a new repository under the steward's GitHub account. Recommended via `gh`:

```sh
gh repo create <scion-name> --public --source=. --push
```

This creates the repository, adds it as `origin`, and pushes in one command. If `--public` is not desired, substitute `--private` (Pages requires a paid plan for private repos on some GitHub accounts; the ceremony does not depend on repository visibility).

Alternatively, create via the GitHub web UI, then:

```sh
git remote add origin https://github.com/<user>/<scion-name>.git
git push -u origin main
```

### Step 8: Enable Actions and Pages

Open the scion's repository settings on GitHub and configure:

- **Settings → Actions → General**: allow Actions to run (the default is often "Allow all actions and reusable workflows").
- **Settings → Pages**: set **Source** to **GitHub Actions**.

### Step 9: Push again to trigger the first build

Make any small content edit (or an empty commit) and push. The build-and-deploy Action runs and publishes the scion's Pages site with its own DID in the footer.

```sh
git commit --allow-empty -m "Trigger first Pages build"
git push
```

Monitor the Action at `https://github.com/<user>/<scion-name>/actions`. When it completes, the scion's site is live at the URL shown under **Settings → Pages**.

### Step 10: Report

Report the scion's identity to the user:

- The scion's DID (the `this_did` value in `.scion-identity.yml`).
- The `scion_of` value pointing at the template's DID.
- The scion's GitHub URL and Pages URL.
- Any remaining post-Bootstrap customization the steward plans (a custom domain, edits to `AGENTS.md` for scion-specific agent stance, first content revisions).

The scion is now a first-class graph with its own cryptographic identity; subsequent work happens through ordinary git operations, not through Bootstrap again.

## Scripts

### `.scripts/scion-bootstrap.sh`

The wrapper script for the ceremony proper. POSIX-sh. Runs from the scion-dir root.

- **Inputs**: the current working directory must contain `.scion-identity.yml` and `.git` (a fresh clone of a DeepContext graph). Git signing configuration (`user.name`, `user.email`, `user.signingkey`) must be set and the signing key file must be readable.
- **Outputs**: `.git` rewritten with two signed commits (the OI inception commit plus the scion's initial content commit); `.scion-identity.yml` updated with the scion's new DID and the template's DID as `scion_of`.
- **Failure modes**: missing prerequisite → exits with clear message naming the missing piece; partial run (script exited after removing `.git` but before completing inception) → safe to re-clone into a fresh directory and re-run; signing failure → check that the signing key's public half is in GitHub allowed-signers and that `git config user.signingkey` points at the correct path.

### `.scripts/scion-inception.sh`

The OI inception primitive this skill's wrapper calls. Produces a fresh empty signed root commit establishing the scion's `did:repo:<sha1>`. Not normally called directly by a user; the Bootstrap wrapper invokes it with the current directory as the target.

## Relations

- conforms_to::[[Skill Form Contract]]
  - This skill declares compliance with the Skill Form Contract's Requirements. Sits alongside Graph Orient and Node Read as first-session skills a new scion's first steward walks through: Bootstrap stands up the scion, Orient reads the inherited graph into context, Node Read drills into specific inherited nodes.

- grounded_in::[[Adopt Scion Publication Model]]
  - The Decision this skill operationalizes. The Decision names what a scion is (a graph with its own OI-signed DID), why Bootstrap must be local (OI signing requires the steward's SSH key, which Actions cannot access), and what file records the lineage (`.scion-identity.yml` with `this_did` and `scion_of`). This skill is the concrete procedure that makes the Decision's commitments actionable for a first steward.

- grounded_in::[[Open Integrity Project (Blockchain Commons, 2025)]]
  - The cryptographic specification that makes the scion's DID identity-sovereign rather than hosting-derivative. The inception-commit ceremony, the SHA1-derived DID, the allowed-signers delegation model — all are OI moves this skill's script composes together.

- informs_downstream::[[scion_of -- content lineage from a template graph]]
  - The Predicate whose value this skill writes into `.scion-identity.yml` at step 6 of the Bootstrap script. The scion's `scion_of` value is the template's `this_did`, recorded structurally in the YAML file and (at the scion author's option) expressible as a graph-layer wikilink in the scion's identity predicate block.

- composes_with::[[Graph Orient]]
  - Invoked after Bootstrap completes to walk the newly-stood-up scion's inherited graph into context. Bootstrap establishes the scion's identity; Orient establishes the scion's content understanding for subsequent work. The two skills are the standard first-session pair for a new scion.
