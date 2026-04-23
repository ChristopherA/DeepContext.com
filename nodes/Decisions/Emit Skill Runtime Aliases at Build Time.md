---
created: 2026-04-22
tagline: Source-of-truth lives at nodes/Skills/<Title Case>/<Title Case>.md; the Anthropic runtime layout at .agents/skills/<lowercase-hyphenated>/ is emitted as committed symlinks
brief_summary: A Decision resolving the dual-residence of skills -- as graph nodes under Title Case compound-node folders and as runtime-invocation targets under lowercase-hyphenated directories -- by making the graph layout source-of-truth and the runtime layout a build-emitted symlink tree committed to the repository. Symlinks preserve the single-source property without content duplication, so a Web-UI edit to a lead file appears immediately at the runtime path without any build step. Committing (rather than gitignoring) the runtime directory means a fork or a fresh clone inherits a working runtime layout without having to run build.py locally. Rejected alternatives: SKILL.md as the source lead filename; lowercase-hyphenated source filenames; committed copies instead of symlinks; gitignored aliases regenerated locally.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-22
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Emit Skill Runtime Aliases at Build Time

A skill's source of truth is its compound-node folder under `nodes/Skills/<Title Case>/`, with the lead file named to match the folder (`nodes/Skills/Node Create/Node Create.md`). The Anthropic Agent Skills runtime layout at `.agents/skills/<runtime-name>/SKILL.md` is build-emitted: `.scripts/emit_skills.py` reads each source folder, derives the runtime name from the folder's Title Case name (`Node Create` -> `node-create`) or from the lead file's `runtime_name` frontmatter field, and writes symlinks at the runtime path pointing back at the source (`SKILL.md` -> `../../../nodes/Skills/Node Create/Node Create.md`). The runtime directory is committed to the repository; hand-editing files under `.agents/skills/` is forbidden; the emission is idempotent and regenerates the tree from source.

## Why

The commitment provides **single-source-of-truth across dual-residence layouts**. A skill has to be two things at once: a graph node conforming to the filename conventions every other node form carries (Title Case, wikilink-resolvable stem, compound-node lead matching folder name), and an agent-runtime artifact conforming to the Anthropic Agent Skills spec (lowercase-hyphenated directory name, `SKILL.md` lead, predictable paths for `scripts/` and `references/` subdirectories). The two conventions conflict directly -- the graph's wikilink resolver is looking for `[[Node Create]]` at `nodes/Skills/Node Create/Node Create.md`, while the agent runtime is looking for `SKILL.md` under `.agents/skills/node-create/`. The symlink emission resolves the conflict by making one layout canonical and the other a view: the source layout is what authors edit and what other nodes link to; the runtime layout is what the agent runtime reads.

Symlinks are the mechanism because they preserve the single-source property without any content duplication. A Web-UI edit to `nodes/Skills/Node Create/Node Create.md` is immediately reflected at `.agents/skills/node-create/SKILL.md` -- no build step is needed to propagate the edit, because the symlink resolves to the edited file at read time. The same property holds for `scripts/` and `references/` subdirectories: the symlink points at the source folder, so anything added or edited in the source is visible at the runtime path without regeneration. A Web-UI contributor editing a fork's skill gets correct runtime behavior after a single commit, with no intermediate tooling step.

The runtime directory is committed rather than gitignored because the forkability commitment requires the runtime layout to be present after a clone or fork without any local build. A fork owner whose first contribution is a Web-UI edit never runs `build.py`; if `.agents/skills/` were generated locally and gitignored, an agent running in the fork's context would find an empty runtime directory until someone pushed a build. Committing the symlinks makes the runtime layout part of the repository's shipped shape, matching the forkable-publication property at the capability layer.

Idempotent regeneration is what keeps the emission safe under authoring churn. The emission clears the runtime directory and recreates it from the current source layout; a skill renamed, removed, or added updates the runtime directory mechanically on the next build. Hand-editing under `.agents/skills/` is forbidden because any hand edit is lost on the next regeneration -- a hand edit is a symptom of reaching for the wrong layer. The correct layer is always the source lead file.

## Alternatives Considered

**SKILL.md as the source lead filename.** Author each skill as `nodes/Skills/<Folder>/SKILL.md` directly, eliminating the need for the symlink. Rejected because it would make skills the only node form whose compound-node lead file does not match its folder name. The compound-node convention across the graph is `<Folder>/<Folder>.md` -- the lead file carries the concept the folder names; breaking it for skills would force every reader, every tool, and every wikilink resolver to treat the Skills taxonomy specially. Wikilink resolution would have to carry a skill-specific exception: `[[Node Create]]` would resolve to `SKILL.md` for skills and to `Node Create.md` for every other form. The naming exception radiates outward; the symlink does not.

**Lowercase-hyphenated source filenames.** Author skills as `nodes/Skills/node-create/node-create.md` to match the Anthropic runtime's case convention directly, eliminating the runtime-rename step. Rejected because Title Case is the filename convention across every node form in the graph, enforced by `Markdown Node Contract` and relied on by wikilink-stem resolution. A `[[Node Create]]` wikilink from any other node expects to resolve to a Title Case stem; a lowercase-hyphenated filename would fail to resolve or force the resolver to carry a taxonomy-specific casing rule. The authoring convention and the runtime convention have legitimately different optimizations -- the authoring convention optimizes for cross-node wikilinks and human readability, the runtime convention optimizes for shell-friendly invocation names -- and each is correct in its own layer.

**Committed copies of the skill body at the runtime path.** Have the emission write the skill body into `.agents/skills/<runtime>/SKILL.md` as a regular file rather than as a symlink. Rejected because a copy drifts silently from its source whenever an author edits one layer and not the other. The symlink cannot drift -- it dereferences to the source every time it is read. Silent drift between a source and a committed copy is the same failure [[Publish via Actions Artifact Deploy]] cited when removing committed build output from the publication pipeline; the same reasoning applies at the runtime-alias layer.

**Gitignored aliases regenerated locally.** Gitignore `.agents/skills/` and expect every developer, fork owner, and CI runner to regenerate it locally before running an agent. Rejected because it breaks the forkability commitment's capability layer. A Web-UI contributor editing a fork's skill never runs the build locally; an agent running in that fork's context would find an empty runtime directory. Committed aliases make the runtime layout part of what a clone or fork receives, consistent with the self-contained-repository shape the forkability commitment names.

## What Would Change It

**Committed symlinks become unreliable on target surfaces.** If a fork's CI runner, a clone-over-HTTPS path, or the GitHub Web-UI-edit round trip stopped preserving committed symlinks reliably -- on a platform that lacks symlink support, or through a tool that flattens them -- the committed-symlink approach would break. The revisit would reconsider committed copies with a drift-detection check in the build, or move to a runtime that accepts the source layout directly.

**The Anthropic Agent Skills runtime absorbs compound-node layouts directly.** If the runtime grew the ability to discover skills from `nodes/Skills/<Folder>/<Folder>.md` directly -- reading the folder's lead file and tolerating Title Case and space-separated names -- the alias emission would become redundant. The revisit would remove `.agents/skills/` and point the runtime at the source layout.

**The source and runtime layout conventions converge.** If the graph's filename conventions shifted toward lowercase-hyphenated filenames across node forms (unlikely, and the current state of `Use ASCII Dashes in Filenames` specifically preserves Title Case), the source and runtime conventions would converge and the rename step would drop out. The revisit would be a cascade from a larger filename-convention change, not a skill-specific reconsideration.

**A fork adopts a different agent runtime with a conflicting layout.** If a fork adopts an agent runtime whose expected layout conflicts with the Anthropic one the parent emits, the build would have to grow emission targets per runtime, or the fork would maintain its own emission alongside (or instead of) the parent's. The commitment survives; the emission set grows.

## Relations

- grounded_in::[[Adopt Skills as Graph Nodes]]
  - The upstream commitment that locates source-of-truth in the graph. This Decision is the downstream resolution: given that skills live in the graph, how the agent runtime's layout is derived from the graph layout. Without the upstream commitment, the question would not arise -- a skill that was primarily a runtime artifact would have no source-in-graph to emit from.

- grounded_in::[[Adopt Forkable Publication Model]]
  - The forkability commitment that forces the runtime aliases to be committed rather than built-locally-and-gitignored. A fork owner or a Web-UI editor does not run the build locally; the runtime layout has to be part of the repository's shipped shape for the fork's agent runtime to find skills after clone.

- informed_by::[[Publish via Actions Artifact Deploy]]
  - The sibling Decision that names the same drift concern at the site-rendering layer. Committed build output doubles the diff and drifts silently from its source; Actions-deploy regenerates from source each push. Symlinks are the same answer at the runtime-alias layer -- a view of the source rather than a committed copy -- adapted to the constraint that the runtime layout has to be present in the cloned repository.

- informs_downstream::[[Skill Form Contract]]
  - The Contract carries the runtime-alias-emission clause as a Requirement; this Decision is the commitment the Requirement points at. The Contract states the rule (source-of-truth in `nodes/Skills/`, runtime-emitted at `.agents/skills/`, idempotent regeneration, no hand edits); this Decision records the reasoning and the revisit conditions.
