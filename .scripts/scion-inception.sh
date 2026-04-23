#!/bin/sh
# Create an Open Integrity Project inception commit in a fresh repository.
#
# Portable POSIX-sh equivalent of the zsh reference snippet at
# <https://github.com/OpenIntegrityProject/core/blob/main/docs/Open_Integrity_Script_Snippets.md#create-and-sign-an-open-integrity-repository-inception-commit-zsh>.
#
# The three -m message lines are byte-identical to the zsh reference output,
# so the resulting commit SHA-1 (and therefore the scion's did:repo:<sha1>)
# is determined solely by the scion's author identity, committer key, and
# commit timestamp -- the canonical text is shared across all OI scions
# produced by either implementation.
#
# Usage:
#   .scripts/scion-inception.sh                      # creates ./new_open_integrity_repo/
#   .scripts/scion-inception.sh ./my-scion-dir       # creates at the named path
#
# Prerequisites (checked at runtime):
#   - git config user.name
#   - git config user.email
#   - git config user.signingkey pointing at an SSH private key
#   - ssh-keygen, git, awk, date in PATH

set -eu

target="${1:-$(pwd)/new_open_integrity_repo}"

if [ -d "$target/.git" ]; then
    printf 'Error: repository already exists at %s\n' "$target" >&2
    exit 1
fi

SIGNING_KEY="$(git config user.signingkey || true)"
GIT_AUTHOR_NAME="$(git config user.name || true)"
GIT_AUTHOR_EMAIL="$(git config user.email || true)"

if [ -z "$SIGNING_KEY" ]; then
    printf 'Error: git config user.signingkey is not set\n' >&2
    exit 1
fi
if [ -z "$GIT_AUTHOR_NAME" ] || [ -z "$GIT_AUTHOR_EMAIL" ]; then
    printf 'Error: git config user.name or user.email is not set\n' >&2
    exit 1
fi
if [ ! -r "$SIGNING_KEY" ]; then
    printf 'Error: signing key not readable at %s\n' "$SIGNING_KEY" >&2
    exit 1
fi

GIT_COMMITTER_NAME="$(ssh-keygen -E sha256 -lf "$SIGNING_KEY" | awk '{print $2}')"
GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
GIT_AUTHOR_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE"

export GIT_AUTHOR_NAME GIT_AUTHOR_EMAIL GIT_COMMITTER_NAME GIT_COMMITTER_EMAIL GIT_AUTHOR_DATE GIT_COMMITTER_DATE

mkdir -p "$target"
git -C "$target" init --quiet

git -C "$target" \
    -c gpg.format=ssh \
    -c user.signingkey="$SIGNING_KEY" \
    commit --allow-empty --no-edit --gpg-sign \
    -m "Initialize repository and establish a SHA-1 root of trust" \
    -m "Signed-off-by: $GIT_AUTHOR_NAME <$GIT_AUTHOR_EMAIL>" \
    -m "This key also certifies future commits' integrity and origin. Other keys can be authorized to add additional commits via the creation of a ./.repo/config/verification/allowed_commit_signers file. This file must initially be signed by this repo's inception key, granting these keys the authority to add future commits to this repo including the potential to remove the authority of this inception key for future commits. Once established, any changes to ./.repo/config/verification/allowed_commit_signers must be authorized by one of the previously approved signers."

commit_sha="$(git -C "$target" rev-parse HEAD)"
printf 'Inception commit created at %s\n' "$target"
printf 'did:repo:%s\n' "$commit_sha"
