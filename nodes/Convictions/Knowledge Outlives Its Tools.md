---
created: 2026-04-21
tagline: Knowledge should outlast the tools used to capture it -- plain markdown, open formats, zero dependencies
brief_summary: A held stance that the graph must survive changes in tools, platforms, and formats. The captured reasoning accumulated over years of conversation cannot be held hostage by the software used to tend it, the platform used to host it, or the encoding used to store it. The commitment produces specific technical constraints -- plain markdown over proprietary formats, file-per-node over database records, predicates as text over plugin-dependent metadata, git for version control over platform-specific sync. The value does not prohibit tooling; it requires that no tooling become a single point of failure for accessing the graph. The zero-tooling floor holds even when tools add value on top of it.
---

- conforms_to::[[Conviction Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Knowledge Outlives Its Tools

Knowledge outlives the tools used to capture it. The graph should survive changes in tools, platforms, and formats. Reasoning accumulated over years of conversation -- the decisions made, the alternatives considered, the convictions named, the observations grounded -- must not be held hostage by the software used to tend it, the platform used to host it, or the encoding used to store it. A platform can disappear, a toolchain can lose support, a markup convention can evolve. The captured reasoning should survive all of those transitions because the reasoning is more valuable than any single tool used to work with it.

The commitment runs deeper than a preference for open formats. It is a stance about the temporal relationship between knowledge and infrastructure: knowledge outlives infrastructure, always. The graph's authoring layer -- its files, its formats, its conventions -- must reflect that.

## Why It Is Held

The value generates specific technical constraints that show up in every subsequent Decision about the graph's pipeline. Plain markdown rather than proprietary formats because markdown works everywhere with no tooling commitment. File-per-node rather than database records because files outlast any particular database engine. Predicates as text (`predicate::[[Target]]` as a literal markdown line) rather than plugin-dependent metadata because plugin-dependent metadata is coupled to the plugin. Git for version control because git is portable and its wire format is durable. Each constraint is a specific bet against a specific failure mode: if the current tooling disappears tomorrow, can the graph still be read, traversed, and edited?

The commitment also makes scioning workable. [[Adopt Scion Publication Model]] requires that a scion produces its own site with no external dependencies; durability is what makes that promise hold at the content layer. A scion inherits the nodes, the conventions, and the pipeline code -- all of which are plain text, all of which can be run, edited, or replaced without contacting any external service. If the template disappears, every scion still works.

The value does not prohibit tooling. Obsidian plugins, shell scripts, agent-mediated curation, specialized editors are all legitimately used by contributors. The requirement is that no tooling become a single point of failure. A reader without the plugins can still read the node; a contributor without the agent can still author the node; the graph's capabilities with tooling are a layer on top, not a foundation under.

## What It Asks

Structural claims live in named edges, not in plugin-specific metadata or platform-specific constructs. When a relationship can be expressed as `predicate::[[Target]]` in body markdown, it MUST be expressed that way rather than as a YAML tag, a plugin property, or a platform annotation. [[Adopt Wikilinks and Named Edges]] records the Decision; this Conviction is one of the values that makes the Decision load-bearing.

File organization mirrors human legibility, not tool convenience. [[Folders Serve Human Legibility, Not the Graph]] names the stance; this Conviction supports it at the durability layer. A folder structure that only makes sense through the current tool's view becomes unreadable when the tool disappears; a folder structure legible at the filesystem layer survives tool changes.

The pipeline stays minimum-viable. Every pipeline dependency is a coupling that could break in a future environment. [[Adopt Minimum-Viable-Architecture Stance]] records the stance at the project level; this Conviction is one of the durability reasons for holding it.

## Drift Recognition

The value has drifted when the graph starts requiring specific tools to be legible. A reader opening a node file in a plain text editor and finding the reasoning illegible -- because predicates have been encoded in a plugin's proprietary syntax, because wikilinks have been replaced by tool-resolved IDs, because metadata lives in a database the reader cannot query -- is the visible form of the drift.

The drift also shows up at the pipeline layer. A build script that requires a specific Node version or a specific package registry is a coupling; a dependency tree that needs lockfile regeneration on every contributor's machine is a coupling; a deployment mechanism that depends on a single hosting provider is a coupling. Each of these can be justified individually; together, they produce a graph that can be scioned in theory but not in practice.

The subtlest drift is in the authoring experience. A contributor who cannot contribute without a specific editor, a specific agent, or a specific workflow is filtered by tooling -- whether or not that filtering was intended. Fidelity to the durability commitment asks that the baseline authoring path stay tool-free: plain text, any editor, any git client.

## Sources

- Allen, Christopher. "Knowledge Durability" value in personal knowledge garden (2026-03) -- the original framing this Conviction adapts.

## Relations

- informs_downstream::[[Deep Context as an Architecture for Captured Reasoning]]
  - The Decision's zero-tooling floor is a direct implementation of this Conviction. The Decision now grounds in this local Conviction rather than in the external value; the grounding lives inside the graph.

- informed_by::[[Capture Reasoning, Not Just Knowledge]]
  - Captured reasoning that doesn't survive tool changes loses its fidelity over time. Durability is a precondition for sustained fidelity; the two values compose.

- informs_downstream::[[Adopt Scion Publication Model]]
  - The scion publication model depends on durability at the content layer. A scion inherits durable content and a durable pipeline; without durability, scioning is formal rather than substantive.

- informs_downstream::[[Adopt Minimum-Viable-Architecture Stance]]
  - Every pipeline dependency is a coupling that could break in a future environment. The MVA stance keeps the durability surface tractable.

- informs_downstream::[[Adopt Wikilinks and Named Edges]]
  - Structural claims as text rather than as tool-specific metadata -- the author-declared wikilink convention is what makes the graph's structure survive tool changes.

- informs_downstream::[[Folders Serve Human Legibility, Not the Graph]]
  - A folder structure legible at the filesystem layer survives tool changes; one that only makes sense through a specific tool's view does not.
