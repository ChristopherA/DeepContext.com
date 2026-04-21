---
created: 2026-04-19
tagline: YAML carries scalar metadata about the file; graph-participating predicates live in the identity block and Relations; new Deep Context keys are snake_case
brief_summary: A bundled commitment covering three co-specifying rules about YAML frontmatter. YAML carries only scalar metadata (`created`, `tagline`, `brief_summary`, and tool-required fields like `aliases`). Named-edge predicates — both graph-participating ones and their scalar mirrors — MUST NOT live in YAML. New Deep Context-specific YAML keys use `snake_case`, matching the named-edge predicate discipline; established single-word scalars and tool-reserved fields keep their names. The three rules share one Why — the separation between file-level curation data and graph-level structural claims.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Restrict YAML to Scalar Metadata

YAML frontmatter is optional. When present, it carries only scalar metadata about the file — `created` (ISO date of file creation), `tagline` (a pithy one-liner), `brief_summary` (a paragraph-length summary), and tool-required or convention-respecting fields such as `aliases` (Obsidian's autocomplete hint) and `tags`. Named-edge predicates MUST NOT appear in YAML, whether as graph-participating predicates (`conforms_to::`, `in_domain::`, `authored_by::`) or as their scalar mirrors (`author: Christopher Allen` duplicating `authored_by::[[Christopher Allen]]↗`). New Deep Context-specific YAML keys are multi-word `snake_case`, matching the named-edge discipline.

## Why

The commitment draws the boundary between **file-level curation data and graph-level structural claims**. A node file carries both: a document that tools index and render (its creation date, its summary, its tagline for a build pipeline) and a concept in the graph that the predicate vocabulary traverses (its conformance, its domain, its authorship, its relations). Letting both live in the same structural container — YAML — forces every reader to know which fields participate in the graph and which do not. The separation removes the ambiguity: YAML is unambiguously for scalar metadata, and the identity block above the H1 plus the Relations section below the body are unambiguously for graph-structural claims.

Named-edge predicates cannot live in YAML without losing their semantics. `conforms_to::[[Decision Form Contract]]` is a typed edge to a wikilink target, annotatable with an indented sub-bullet explaining why the relationship matters. A YAML scalar `conforms_to: Decision Form Contract` is a string — the graph layer cannot traverse from the YAML string to the `[[Decision Form Contract]]` node without either a syntactic convention the YAML spec does not provide or tooling that re-parses YAML as predicate assertions. Wiki tooling does not do this by default. The [[Adopt Wikilinks and Named Edges]] commitment places graph-participating claims where the wiki layer already sees them — in running markdown body, as bullet-form named edges — and excludes them from YAML for the same reason.

Scalar mirrors fail the same test. An `author:` YAML scalar that duplicates `authored_by::[[Person]]↗` creates two sources of truth for one claim; when they disagree, neither is authoritative. The graph traverses the named edge; the scalar is a free-floating metadata string that participates in nothing. The canonical claim is the named edge in the identity block; YAML scalars that mirror predicates either mislead or go stale, and the commitment is to prevent both by excluding them.

`snake_case` for new Deep Context-specific YAML keys matches named-edge predicate discipline (`lower_snake_case`, multi-word). Two classes of exception keep their established names: tool-reserved fields like `aliases` and `tags` (Obsidian and other tooling hardcode these spellings; renaming breaks interop), and fused compound words like `tagline` and `brief_summary` that operate as single concepts in English rather than as compressions of multi-word phrases. The multi-word predicate rule targets compression ambiguity (`[[MIT]]↗` vs `[[MIT License]]↗`), which fused compounds do not carry.

The three rules bundle because they share this Why — the separation between file metadata and graph structure — and because rollback is bundled. Reversing any one of them (letting predicates into YAML, letting YAML keys use predicate casing while predicates stay in the identity block, letting scalar mirrors proliferate) would reopen the same ambiguity the others close. They are adopted and revisited together.

## Alternatives Considered

**Predicate-carrying YAML.** Encode identity predicates and relation predicates as YAML scalars or lists. Rejected because YAML cannot carry the semantics without tooling. A YAML list of wikilink targets looks like a set of strings; extracting typed edges from it requires convention-specific re-parsing that the plain-markdown floor forbids. Even if the re-parsing were reliable, annotations — indented sub-bullets explaining why an edge matters — have no YAML equivalent. The named-edge convention and YAML serve different jobs; mixing them forces one to imitate the other badly.

**YAML as the single structural container.** Put everything structural in YAML and let the body be pure prose. Rejected because it collapses the identity-block/Relations tier architecture into a single flat dictionary and loses annotations. The [[Adopt Layered Node Structure]] commitment requires cheap structural tiers bracketing the prose; compressing both tiers into YAML would lose the Relations-after-body semantics and defeat the cost gradient the layering provides. Plus, annotations would disappear.

**Permit scalar mirrors as a convenience.** Allow `author:` alongside `authored_by::[[Person]]↗` so tooling that reads only YAML still gets the author. Rejected because two sources of truth drift. A mirror that starts consistent becomes inconsistent the first time the named edge updates without the scalar being updated with it, and no reader can tell which to trust. The cost of the mirror is paid continuously; the benefit is a one-time tooling convenience that could be provided by a build step extracting named edges into a YAML adapter when truly needed.

## What Would Change It

The commitment bundles three rules; the revisit conditions split by part.

**Scalar-only YAML.** The scalar-only rule would be revisited if YAML-native named-edge syntax became standard across wiki tooling — a typed-list convention that preserved annotations, target resolution, and query participation. No such standard exists at the plain-markdown floor; existing proposals require tooling to re-parse.

**Named edges out of YAML.** Revisit conditions here track the scalar-only rule — if predicates could live in YAML with full graph semantics, the exclusion rule would lose its ground. Separately, the rule would weaken if authored-declared named edges stopped being the spine of the graph — which would itself require revisiting [[Adopt Wikilinks and Named Edges]], a prior substrate.

**`snake_case` for new Deep Context keys.** This rule would be revisited if the named-edge predicate discipline itself changed casing — if `lower_snake_case` were replaced by `kebab-case` or CamelCase across the predicate vocabulary, the YAML-key rule would follow. No pressure to change predicate casing exists; the rule is firm in parallel with the predicate discipline.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The Decision that makes named edges the graph's structural spine. YAML exclusion of predicates is the mirror constraint: the spine lives in the body, YAML carries curation metadata only. Without the substrate Decision, the exclusion rule would have no direction.

- grounded_in::[[Adopt Layered Node Structure]]
  - The layered-structure commitment places graph-structural claims in the identity block above the H1 and the Relations section below the body. This commitment is the mirror: YAML carries scalar metadata about the file; the identity block and Relations carry graph-structural claims. The separation between file-metadata tier and graph-structural tiers depends on both commitments.

- informs::[[Markdown Node Contract]]
  - Markdown Node Contract's YAML-frontmatter Requirement is the thin enforcement clause pointing at this Decision. The Contract carries the compliance rule; this Decision carries the reasoning and the revisit conditions.
