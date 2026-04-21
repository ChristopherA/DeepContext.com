---
created: 2026-04-19
tagline: Reference filenames carry (Author, Year) parentheticals so the wikilink target is self-citing
brief_summary: A commitment that Reference filenames carry a `(<Author>, <Year>)` citation parenthetical suffix: `<Artifact Name> (<Author>, <Year>).md`. The parenthetical makes the wikilink target self-citing in prose — `[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]` renders as a readable inline citation without extra markup — and makes `(<Author>, <Year>)` a visual marker for Reference-form nodes when scanning a folder or graph listing. The parenthetical is the canonical location for the source's citation form.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Embed Citation Parenthetical in Reference Filenames

Every Reference filename carries a `(<Author>, <Year>)` citation parenthetical as its final component: `<Artifact Name> (<Author>, <Year>).md`. The author component uses the human-readable display form matching the `authored_by::` target (without the `↗` marker): `(Christopher Allen, 2026)`, not `(ChristopherA, 2026)`. Two authors use `(Author One & Author Two, Year)`; three or more use `(Author One et al., Year)` with the full author set enumerated in `authored_by::` predicates. The year refers to the source's publication or last substantive revision, not the node file's creation date. When no year is discoverable, the parenthetical takes the form `(<Author>)`.

## Why

The commitment provides **filename-as-inline-citation**. A wikilink to a Reference node with the parenthetical embedded renders as a readable citation in running prose: "the convention articulated in [[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]] shapes..." becomes a sentence that carries the cited author and year inline without extra markup, parenthetical annotation, or footnote infrastructure. The rendered link reads like a standard academic inline citation; the graph layer sees a wikilink target resolving to the Reference node. Prose and graph participation are satisfied in one mechanism.

The parenthetical makes `(<Author>, <Year>)` a **visual marker** for Reference-form nodes. A reader scanning the Glosses folder, the Decisions folder, or a graph listing sees Reference filenames by their trailing parenthetical — no other form uses the `(<Author>, <Year>)` convention. Filename-shape-carries-form (the rule [[Name Decisions by Action Verb or Role Declarative]] applies to Decisions, the Concept -- definition pattern [[Use Double-Hyphen Separator for Gloss Definitions]] applies to Glosses) extends to Reference: the parenthetical suffix identifies the form at a glance.

The parenthetical is the **canonical citation location**. A Reference body does not need a separate citation line — the filename carries the citation form directly. This avoids two sources of truth: a YAML citation scalar and a filename-level citation would have to be kept aligned; a body-level citation and a filename-level citation would duplicate. The filename is the canonical form; `authored_by::` predicates enumerate authors for graph traversal; the body carries what the source contributes. No duplication.

Specific formatting choices inherit from established citation conventions: `(Author, Year)` is the APA inline-citation shape; `et al.` for three-plus authors matches academic convention; organizational publications use the organization name (`(IETF, 2024)`, `(Wikipedia, 2026)`). Revision-worthy histories may use `(<Author>, <OrigYear>, rev. <RevYear>)` for sources with load-bearing revisions. Each sub-choice follows existing practice rather than inventing new forms; the prototype imports the citation vocabulary the reader population is already literate in.

## Alternatives Considered

**YAML-only citation data.** Carry citation information in YAML frontmatter (`author:`, `year:`) and keep filenames bare. Rejected because citation-as-scalar loses graph participation. A reader wanting the source's citation must open the file to read YAML; a wikilink in prose cannot render the citation inline. The filename-carries-citation pattern keeps the citation graph-participating and prose-inline; YAML citation keeps it file-opening-only.

**Body citation line.** Put a citation string at the top of the body (`Cite as: Christopher Allen (2026).`). Rejected because body-level citation duplicates the filename-level information. When the filename and body citation drift — one updated without the other — neither is authoritative. Single source of truth principle picks the filename, where the citation serves the wikilink-rendering use case the body-line cannot.

**Author-only filenames without year.** Include `(Author)` but drop the year. Rejected because year is part of the citation's disambiguating information. Two artifacts from the same author without year distinction produce wikilink collisions or require awkward disambiguation strings; with year, each artifact is uniquely identified. The year is dropped only when genuinely unknown — the rule is "use what is known, do not guess."

## What Would Change It

The commitment would be revisited under one condition.

**Citation parsing becomes burdensome or informal references dominate.** If most References the project draws from turn out to be informal sources without clear author or year (community discussions, ephemeral posts, unattributed documents), the parenthetical convention would produce awkward filenames with `(Unknown)` or `(Unknown, Unknown)` suffixes. Current References draw from artifacts with clear authorship and publication year; the informal-reference pressure has not arisen. The revisit condition is latent.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine resolves wikilinks by filename. Citation parentheticals in filenames make the wikilink target self-citing — the prose layer and the graph layer agree on what the target says.

- informs::[[Reference Form Contract]]
  - Reference Form Contract's filename pattern Requirement carries the thin enforcement clause pointing at this Decision.
