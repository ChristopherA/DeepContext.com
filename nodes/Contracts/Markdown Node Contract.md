- conforms_to::[[Contract Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Markdown Node Contract

The base contract every Markdown Node in this project conforms to. It specifies the file-level form: encoding, filename rules, YAML frontmatter scope, the predicate block above the H1, the Relations section, and the named-edge syntax. More specific contracts (Gloss, Contract, Reference, Decision, Pattern, Observation, Conviction, Aspiration Form Contracts) extend this one by adding structural requirements on top of the base form.

The Requirements below are thin enforcement clauses; their reasoning, alternatives, and revisit conditions live in the Decisions they ground in. The grounding edges are named in each Requirement and listed in the Relations section.

## Requirements

### File form

Enforces [[Use ASCII Dashes in Filenames]].

- The file MUST be UTF-8 markdown with `.md` extension.
- The filename MUST NOT contain em-dashes (`—`) or en-dashes (`–`). Use ASCII hyphens.
- Where a visual dash is needed in a filename, the form MUST be a double ASCII hyphen `--`.
- The filename MUST be either `<wikilink target>.md` or `<wikilink target> -- <description>.md` (the latter reserved for Gloss Form per its own contract).
- Referencing this file from another node depends on whether the filename carries a ` -- <description>` suffix. When the filename has no suffix, other nodes reference it using the bare wikilink `[[<filename>]]`. When the filename has a ` -- <description>` suffix, references MUST use the pipe form `[[<full filename>|<concept>]]` per [[Use Pipe Wikilinks for Display-Target Divergence]].

### Node atomicity

Enforces [[Adopt Node Atomicity]].

- A file MUST address exactly one concept. One node names one concept, and one concept has one node.
- A file whose body would legibly split into two independent sections serving two different concepts MUST be split into two files, each naming one concept.
- Compound nodes follow node atomicity: a compound names one concept; its sub-files are supporting material, not sub-concepts or facets. A sub-file that reads as a node in its own right — cited by other nodes under its own name, carrying its own identity predicates — MUST be promoted to an atomic node, and the compound split.
- Decisions MAY bundle multiple logically-related commitments under the narrow conditions in [[Decision Form Contract]]. A bundled Decision still names ONE concept — the bundle itself.

### YAML frontmatter

Enforces [[Restrict YAML to Scalar Metadata]].

- YAML frontmatter is OPTIONAL.
- When present, YAML MUST contain only scalar metadata (e.g., `created`, `tagline`, `brief_summary`).
- YAML keys for Deep Context-specific scalars MUST be multi-word `snake_case`, matching named-edge predicate discipline. Two classes of exception: tool-reserved or convention-respecting fields (`aliases`, `tags`, `created`) keep their established names, and fused compound words (`tagline`, `wikilink`) operate as single concepts.
- Named-edge predicates MUST NOT live in YAML. This applies to graph-participating predicates and to their scalar mirrors.
- An `aliases:` field MAY appear as a tool-level convenience; it is graph-non-participating.

### Identity predicate block

Enforces [[Adopt Layered Node Structure]].

- The body MUST begin with a bullet list of identity predicates before the H1.
- This block MUST include `conforms_to::[[<Form> Contract]]` or `conforms_to::[[<Form> Form Contract]]`.
- This block SHOULD include `in_domain::[[<Domain>]]`.
- This block MAY include `has_lifecycle::[[<X> Stage]]`, `has_curation::[[<descriptive phrase>]]`, and `authored_by::[[<Person>]]`.
- Identity predicates describe what the node IS; they do not describe its relationships to other nodes.

### H1

- The file MUST contain exactly one H1.
- The H1 MUST be the concept name — not the full filename, not a definition, not a sentence.

### Body

- Prose body follows the H1.
- Prose MAY contain inline wikilinks; inline links are readable references, not structural edges.

### Layered structure

Enforces [[Adopt Layered Node Structure]].

- A node MUST be arranged in layers that differ in cost to read, and each layer MUST be complete at its own scale.
- The minimum layering is: (a) the identity predicate block above the H1 (cheap, structural, machine-readable), (b) the H1 and its opening prose — or the opening designated section such as a Heart — stating the node's claim at card scale, (c) the elaboration body carrying reasoning, consequences, or instances, and (d) the Relations section (cheap, structural, machine-readable). Specific form contracts MAY extend or refine this shape; they MUST NOT collapse it below the minimum.
- Each layer MUST carry what its scale claims to carry. A claim layer MUST state the claim, not tease it; a structural layer MUST carry authoritative data, not preview text; an elaboration layer MUST reason about the claim, not re-introduce it.
- The cheapest structural layer MUST appear before the expensive prose.

### Relations section

Enforces [[Annotate Edges With Why-They-Matter]] and [[No Generic relates_to Predicate]].

- If the node has relational edges, they MUST appear in a section headed `## Relations` after the body.
- Each relational edge MUST be a top-level bullet in the form `- predicate::[[Target]]` or `- predicate::[[Target]]↗`.
- Each relational edge SHOULD carry an indented sub-bullet annotation explaining why the relationship matters.
- The `relates_to::` predicate MUST NOT be used. Choose a specific predicate (`extends_contract::`, `has_component::`, `composed_of::`, `grounded_in::`, `built_on::`, `informed_by::`, `contrasts_with::`, `contends_with::`, and so on) or add one to the local vocabulary.

### Named-edge syntax

Enforces [[Adopt Wikilinks and Named Edges]].

- Predicates MUST be multi-word, lower-case, joined by underscores (`has_component::`, not `includes::`).
- Wikilink targets MUST be multi-word. Single-word targets are not permitted (`[[Wikilink Syntax]]`, not `[[Wikilink]]`).
- A target whose referent belongs to a different wiki or to an external tradition MUST be marked with a trailing `↗`. The `↗` marks the referent's provenance, not a URL. URLs, when recorded, live in a stub node under `sources/`.
- Ghost links (wikilinks to targets that do not yet exist) are permitted and signal intended future nodes.

### Predicate atomicity

Enforces [[Adopt Predicate Atomicity]].

- Each predicate MUST answer exactly one question — one axis of distinction, not multiple.
- A predicate's values MAY span many points along that one axis. What MUST NOT occur is values that cluster into subgroups answering different questions.
- When a predicate is found carrying two or more axes, the remedy MUST be a predicate family — each member a single-axis predicate — not a revised but still-overloaded name. The recurring craft move is [[Refactor the Predicate's Axes]].
- A new axis of distinction MUST earn a new predicate; retrofitting existing predicates to carry a new axis is forbidden.

## Relations

- built_on::[[CommonMark Markdown]]↗
  - A node conforming to this contract is valid CommonMark; the contract adds reading and authoring discipline on top of the file format.

- grounded_in::[[Wikilinks and Named Edges]]↗
  - The canonical reference for the underlying wikilinks-plus-named-edges convention this contract specializes.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The project-level Decision that commits to the wikilinks-and-named-edges spine. Node atomicity, predicate atomicity, and layered structure all presuppose this Decision.

- grounded_in::[[Adopt Node Atomicity]]
  - The Decision grounding the node-atomicity Requirement.

- grounded_in::[[Adopt Predicate Atomicity]]
  - The Decision grounding the predicate-atomicity Requirement.

- grounded_in::[[Adopt Layered Node Structure]]
  - The Decision grounding the layered-structure Requirement and the identity-predicate-block placement.

- grounded_in::[[Restrict YAML to Scalar Metadata]]
  - The Decision grounding the YAML-frontmatter Requirement.

- grounded_in::[[Use ASCII Dashes in Filenames]]
  - The Decision grounding the filename-dash rules in the File form Requirement.

- grounded_in::[[Annotate Edges With Why-They-Matter]]
  - The Decision grounding the Relations-section annotation requirement.

- grounded_in::[[No Generic relates_to Predicate]]
  - The Decision grounding the `relates_to::` prohibition in the Relations-section Requirement.

- extended_by::[[Gloss Form Contract]]
  - Gloss Form Contract extends this contract with filename-carries-definition and body-shape allowances.

- extended_by::[[Contract Form Contract]]
  - Contract Form Contract extends this contract with requirements for parseable `## Requirements` sections and the self-conformance pattern.

- informs::[[Compound Node -- a folder of markdown nodes with a designated lead|Compound Node]]
  - The compound-node pattern realizes node atomicity for concepts whose supporting material warrants its own sub-files: the compound names one concept, the sub-files are supporting material, and the node-atomicity Requirement's split criterion is what tells the author whether a prospective sub-file is supporting material (stays compound) or an independent concept (promote to atomic).

- informs::[[Progressive Summary Before Substance]]
  - The Pattern that realizes the layered-structure Requirement in the prototype's specific vocabulary. The Requirement states the standing structural rule; the Pattern names the move an author makes composing a node in practice.

- informs::[[Refactor the Predicate's Axes]]
  - The Pattern that realizes or restores predicate atomicity when a predicate is found carrying multiple axes. The Requirement states the rule; the Pattern names the craft applied when the rule is violated in the wild.

- informed_by::[[Use Pipe Wikilinks for Display-Target Divergence]]
  - Bare `[[Concept]]` does not resolve to a file whose name carries a ` -- <description>` suffix; the pipe form Decision specifies the canonical way to reference gloss nodes and other disambiguated filenames from both prose and named edges.
