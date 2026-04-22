- conforms_to::[[Contract Form Contract]]
- extends_contract::[[Markdown Node Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Skill Form Contract

A Skill is a node that encodes an agent-invocable capability — a named workflow or capability an agent runs to read, write, validate, or maintain the graph. It carries the invocation name, the trigger conditions, the numbered steps the agent follows, and any supporting scripts or reference material the workflow depends on. Skill nodes are the structural home for every repeatable operation an agent performs against this graph.

A Skill is not a Pattern (which names a craft move an author makes by hand) and not a Decision (which records a commitment). What distinguishes a Skill is that it is designed to be executed by an agent on demand — its body is a workflow, not a claim — and its presence at a runtime path lets an agent runtime discover and invoke it by name. The invocation surface is what forces the structural additions in this contract: a runtime-visible scalar name, an Anthropic-style `description` block, and a compound-node layout that can carry scripts alongside the lead file.

The Skill Form Contract is Seed Stage. The project committed to skills-as-nodes ahead of any skill nodes existing, so this contract codifies expected shape in advance of the 2-to-3-conforming-nodes-already-exist threshold that `Contract Form Contract` would usually prefer. The first skills drafted under this contract are expected to reveal gaps that revise it.

## Requirements

### Inherits Markdown Node Contract

- All requirements of [[Markdown Node Contract]] apply.
- Filename case follows the base contract — Title Case, ASCII dashes only. The lowercase-hyphenated runtime form is derived at build time, not carried in the filename.
- The requirements below are additions or refinements, not overrides.

### Compound-node layout

- A Skill MUST be a compound node: a folder under `nodes/Skills/` whose lead file matches the folder name (`nodes/Skills/Node Create/Node Create.md`).
- The folder MAY contain a `scripts/` subdirectory for executable supporting code.
- The folder MAY contain a `references/` subdirectory for supporting documentation loaded on demand by the agent.
- The folder MUST NOT contain a `SKILL.md` file in source — `SKILL.md` is reserved for the build-emitted runtime alias.

### Filename pattern

- The folder name MUST be a Title Case phrase matching the concept the skill performs. The user-facing naming convention is object-first (`Node Create`, `Node Read`, `Graph Audit`) for skills users invoke directly; skills invoked only by other skills or by the repository MAY use alternative phrasings.
- The folder name MUST NOT carry a definition in the `<Concept> -- <definition>` pattern; a Skill's purpose is captured in its `description` YAML field, not its filename.

### YAML frontmatter

- The lead file MUST carry YAML frontmatter. This is an exception to `Markdown Node Contract`'s OPTIONAL rule for YAML; the Anthropic Agent Skills runtime requires structured frontmatter to discover and invoke skills.
- Required scalar keys:
  - `runtime_name` MUST be the lowercase-hyphenated form of the folder name (`Node Create` → `node-create`). It matches Anthropic's `name` field and becomes the invocation name (`/node-create`).
  - `description` MUST carry an Anthropic-spec-compliant description: a brief third-person statement of what the skill does, followed by a WHEN line listing trigger conditions and a WHEN NOT line listing non-invocation cases.
- Optional scalar keys inherited from `Markdown Node Contract`: `created`, `tagline`, `brief_summary`.
- YAML MUST NOT carry named-edge predicates. Identity predicates live in the body above the H1 per the base contract.

### Identity predicate block

- The body MUST begin with an identity predicate block before the H1 per `Markdown Node Contract`'s Identity predicate block Requirement.
- The block MUST include `conforms_to::[[Skill Form Contract]]`.
- The block SHOULD include `authored_by::`, `has_lifecycle::`, `has_curation::`, and `in_domain::`.

### H1

- The H1 MUST match the folder name (and the lead filename, minus the `.md` extension).

### Body: Opening orientation

- The body MUST begin with prose that states what the skill does and when an agent should invoke it.
- The opening MAY restate the WHEN and WHEN NOT lines from the YAML description, but SHOULD elaborate beyond them.

### Body: Steps

- The body MUST include numbered steps stating the workflow the agent follows.
- Steps MAY be grouped under H2 subsections when the workflow is long enough to benefit from phases.
- When a step depends on a supporting script, the step MUST name the script path and what the step does with its output.

### Body: Scripts

- A Skill whose folder carries a `scripts/` subdirectory MUST include a `## Scripts` section documenting each script, its purpose, and its inputs and outputs.
- Scripts MUST be POSIX-portable and follow the project's shell conventions.
- LLM instructions MUST live in the skill body, not in script comments — an agent does not read the script's source during execution.

### Relations section

- The Relations section follows the base `Markdown Node Contract`.
- A Skill SHOULD declare `grounded_in::[[Decision]]` for each Decision it enforces at write time or validation time. The grounding edge makes the skill's purpose traceable to the commitment it realizes.
- A Skill MAY declare `informs::[[Contract]]` for each Contract whose Requirements the skill helps authors satisfy.
- A Skill MAY declare `composes_with::[[Other Skill]]` when two skills are routinely invoked together or one invokes the other.
- A Skill MAY declare `contrasts_with::[[Adjacent Skill]]` to mark the distinction between skills whose triggers overlap.

### Runtime alias emission

- Skills are source-of-truth at `nodes/Skills/<Folder>/<Folder>.md`. The Anthropic runtime layout at `.agents/skills/<runtime_name>/SKILL.md` is build-emitted output.
- `.scripts/build.py` MUST create `.agents/skills/<runtime_name>/` as a directory containing symlinks pointing back to the compound-node contents: `SKILL.md` → `<Folder>.md`, and directory symlinks for `scripts/` and `references/` when present.
- `.agents/skills/` is regenerated by `build.py` and MUST be idempotent. Hand-editing files under `.agents/skills/` is forbidden.

## Relations

- extends_contract::[[Markdown Node Contract]]
  - Inherits all base file-form requirements; adds compound-node layout, required YAML frontmatter carrying runtime-invocation metadata, and the runtime-alias-emission clause that makes skills dual-resident in the graph and in the agent runtime layout.

- conforms_to::[[Contract Form Contract]]
  - This file is itself a Contract; it conforms to the meta-contract that specifies what Contract nodes look like.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The commitment that makes named-edge predicates the structural spine. Skills are graph nodes like any other; their Relations edges let an agent reading one skill discover the Decisions it enforces and the skills it composes with.

- contends_with::[[Convention Overhead vs Graph Quality]]
  - Introducing a Contract ahead of the two-or-three-conforming-nodes threshold raises the bar for skill authoring speculatively. The Seed Stage lifecycle and Working Draft curation mark the contract as provisional; the first skills drafted under it are expected to revise it.

- contrasts_with::[[Pattern Form Contract]]
  - A Pattern names a craft move an author makes by hand; a Skill encodes an agent-invocable workflow. Both shape practice, but Patterns address human authorship and Skills address agent execution. The distinction is load-bearing because some operations warrant both — a Pattern describing how an author should think, and a Skill encoding the agent-side execution.
