---
created: 2026-04-22
tagline: An agent-invocable capability is a graph node like any other, authored under nodes/Skills/ and conforming to a Skill Form Contract
brief_summary: The meta-commitment that skills are first-class graph nodes rather than auxiliary tooling, user-level-only artifacts, or content hosted in a separate repository. Each skill lives under nodes/Skills/ as a compound node carrying the same identity predicate block and annotated Relations edges every other node form uses, so the skill's grounding in the Decisions it enforces, its composition with adjacent skills, and its contrasts against skills with overlapping triggers all travel with the skill itself. The commitment is the prior claim that makes the Skill Form Contract worth writing and that makes scions inherit their maintenance capabilities alongside the graph they maintain. Rejected alternatives: Claude-Code-only skills at user level; flat single-file skills; skills hosted in a separate repository.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-22
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Adopt Skills as Graph Nodes

An agent-invocable capability is a graph node. Each skill lives under `nodes/Skills/` as a compound node with a lead file conforming to [[Skill Form Contract]], carrying the same identity predicate block and annotated Relations edges every other node form uses. The skill's reasoning, its grounding in the Decisions it enforces, its composition with adjacent skills, and its contrasts against skills with overlapping triggers are all visible on the skill itself rather than scattered across agent-runtime configuration or user-level dotfiles. The commitment is what makes the Skill Form Contract worth writing: without the commitment, skills would be files in an agent runtime's directory and a Contract describing their shape would have no home in the graph.

## Why

The commitment provides **reasoning traversability from skills outward**. An agent or reader encountering a skill should be able to discover why the skill does what it does through the same graph-traversal moves used on any other node -- the `grounded_in::` edge names the Decision the skill enforces, the `composes_with::` edge names the adjacent skill it coordinates with, the `contrasts_with::` edge names the skill whose trigger overlaps. The traversability is what keeps skills from drifting away from the reasoning they were written to realize. When the Decision changes, the skill reads as stale; when the skill would dilute its scope, the `contrasts_with::` edge names the neighbor whose territory it would blur. This is the same property every other node form in the graph carries, applied to the operations an agent performs against the graph.

The commitment is the direct consequence of [[Adopt Wikilinks and Named Edges]] extended to agent operations. Once the graph's spine is author-declared named edges, a capability whose reasoning sits outside that spine cannot be audited, cannot be cited by other nodes, and cannot participate in the `grounded_in::` chain that connects form to Decision to Conviction. Treating skills as something other than graph nodes would be a category exception to the wikilinks-and-named-edges commitment for the specific operations that write and validate the graph -- the exact operations the commitment most needs to cover.

The commitment also follows from [[Adopt Scion Publication Model]]. A scion inherits the template's graph; if skills live outside the graph, the scion inherits a graph whose maintenance workflows live somewhere the scion owner has to assemble separately. Putting skills inside the graph makes the scion self-contained at the capability layer the same way the scion commitment makes it self-contained at the publication layer. A scion inheriting the repository inherits the skills that maintain it, without external dependencies.

The skill-as-node commitment does not preclude agent runtimes emitting their own layouts. Anthropic Agent Skills expects a particular directory shape with `SKILL.md` as the lead file under `.agents/skills/<runtime-name>/`; that shape is a rendering target, not the source of truth. The commitment is about where the canonical skill lives and what contract it conforms to, not about which runtime formats the build can emit. The runtime-alias question is taken up separately in [[Emit Skill Runtime Aliases at Build Time]].

## Alternatives Considered

**Claude-Code-only skills at user level under `~/.claude/skills/`.** Keep skills as Claude Code user-level artifacts that travel with a contributor's configuration rather than with any particular repository. Rejected because it breaks the scion commitment at the capability layer -- a scion of DeepContext.com inherits the graph without inheriting the skills that read, write, or validate it, and every scion owner would have to reproduce the skill set in their own user configuration or do without. It also breaks reasoning traversability: the skill's grounding in the graph's Decisions cannot be expressed as a named edge when the skill lives outside the graph, so the grounding becomes prose documentation at best and lore at worst.

**Flat single-file skills as `<skill-name>.skill.md` directly under `nodes/Skills/`.** Treat each skill as one markdown file carrying both the reasoning and the workflow, without the compound-node folder layout. Rejected because the Anthropic Agent Skills runtime model expects skill-supporting assets alongside the lead file -- scripts the skill invokes, references the agent loads on demand -- and flat files cannot carry those without either bundling them into another location or committing to a skill model that forbids them. The compound-node layout matches both the runtime shape and the content the skills actually need to carry; forgoing it would force a split between the source and the runtime that the alias emission deliberately avoids.

**Skills hosted in a separate repository from the graph.** Keep the graph repository focused on content (nodes, conventions, Contracts) and move skills into their own repository that the graph repository references or depends on. Rejected because it recreates the external-dependency pattern [[Adopt Scion Publication Model]] is designed to prevent. A graph repository that depends on a separate skills repository forces every scion owner either to scion both or to accept an external dependency that can change out from under the scion. The skills are part of the practice the graph encodes; splitting them into a separate repository would put the practice's maintenance operations outside the practice's publication unit.

## What Would Change It

**Skills stop benefiting from graph-node properties.** If the skills written under this commitment consistently fail to carry meaningful `grounded_in::` edges, fail to compose with other nodes through the graph's edge vocabulary, or are never cited from other nodes, the cost of treating them as graph nodes is not being paid back in traversability. The revisit would ask whether the skill shape has drifted away from what the graph form was designed to carry, and whether a simpler runtime-only representation would serve the practice better.

**An agent runtime contract emerges that graph-node skills cannot satisfy.** If Anthropic Agent Skills or a successor runtime grows a requirement the compound-node layout cannot meet without violating the graph's other conventions -- required fields that conflict with the identity predicate block, required lead filenames that cannot be aliased from Title Case, or required subdirectory layouts that break compound-node rules -- the commitment's implementation would have to change. The question would be whether a build-emitted adaptation can preserve the source-of-truth-in-graph property, or whether the runtime contract forces the source of truth into the runtime layout.

**A scion's skills diverge from the template's so substantially that co-location ceases to matter.** If scions consistently replace most of the template's skill set rather than extending it, the benefit of skills traveling with the repository is weaker -- what the scion inherits is not being used. The revisit would ask whether skills should be scion-specific artifacts declared separately rather than graph-resident nodes shared across scions by default.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The spine commitment that makes skills' reasoning traversable. Without author-declared named edges, a skill's grounding in the Decisions it enforces could not be expressed as a typed relation and would have to live in prose documentation. The skill-as-node commitment extends the wikilinks-and-named-edges discipline to the operations that write and validate the graph -- the category of content that most needs the discipline applied.

- grounded_in::[[Adopt Scion Publication Model]]
  - The scion commitment that makes co-locating skills with the graph load-bearing. A scion inherits what the template carries; putting skills in the repository means a scion inherits the maintenance capabilities alongside the content, without external dependencies. The skill-as-node commitment is the capability-layer expression of the scion discipline.

- informs_downstream::[[Skill Form Contract]]
  - This Decision is the commitment that makes the Skill Form Contract worth writing. The Contract specifies what skill nodes look like structurally; this Decision records the prior claim that skills are graph nodes in the first place. A graph in which skills were external artifacts would not need a Skill Form Contract at all.

- informs_downstream::[[Emit Skill Runtime Aliases at Build Time]]
  - The downstream Decision that resolves the runtime-emission question this Decision deliberately leaves open. This Decision locates source-of-truth in the graph; the downstream Decision specifies how runtime aliases are emitted from that source.
