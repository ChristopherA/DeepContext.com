---
created: 2026-04-19
tagline: Reference filenames carry artifact descriptors — Gist, Paper, Repository — to distinguish the specific artifact from the tradition it articulates
brief_summary: A commitment that when multiple external artifacts from the same tradition are captured as separate References, each filename carries an artifact descriptor (`<Name> Gist`, `<Name> Paper`, `<Name> Repository`) before the citation parenthetical. The descriptor distinguishes artifact-level references from concept-level references and prevents conflating the specific instance (a particular gist) with the tradition the instance articulates (the convention-as-a-whole that the gist documents).
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Disambiguate Reference Artifacts from Traditions

When multiple external artifacts from the same tradition are captured as separate References, each filename carries an artifact descriptor — `<Name> Gist`, `<Name> Paper`, `<Name> Repository`, `<Name> Lecture` — before the citation parenthetical. `Wikilinks and Named Edges Gist (Christopher Allen, 2026).md` names a specific artifact (the gist); `Wikilinks and Named Edges.md` would name the concept-as-a-whole. The descriptor distinguishes the instance from the tradition.

## Why

The commitment prevents **conflating the instance with the tradition**. A tradition articulated in a gist is not identical to the gist itself. The gist is one artifact documenting the tradition — a specific URL, a specific version, a specific authored moment. The tradition extends beyond the gist: earlier articulations, later revisions, related work by the same author, adoption by others. When a Reference node captures the gist, the node's scope is the artifact; when a Reference node captures the tradition, the node's scope is broader. Both are legitimate; the filenames must distinguish.

The artifact-descriptor suffix carries the distinction at the filename level. A reader encountering `[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]` knows the citation is to a specific artifact at a specific time; a reader encountering `[[Wikilinks and Named Edges]]` (ghost link or future Gloss) knows the reference is to the tradition-as-a-whole. Pipe form lets the prose read naturally either way — `the [[Wikilinks and Named Edges Gist (Christopher Allen, 2026)|wikilinks and named edges]] convention` cites the artifact while displaying the tradition name. The commitment's filename-level distinction is what makes both citations precise.

The descriptor also handles **ecosystems where multiple artifacts matter**. If the project draws on a paper AND a repository AND a blog post from the same tradition, each is a separate Reference with its own role, its own body, its own adoption account. The descriptors distinguish the three: `Foundational Paper (Author, Year)`, `Reference Implementation Repository (Author, Year)`, `Extended Discussion (Author, Year)`. Without descriptors, the three would collide at the filename level or require awkward disambiguation strings.

The commitment applies specifically when multiple artifacts from one tradition are captured. A single-artifact Reference may use the tradition name as the filename with no descriptor (the descriptor becomes necessary only at the moment of disambiguation). A prudent author anticipates future artifacts — adding the descriptor from the start when the tradition is likely to yield more References — but the rule does not require pre-emptive descriptors; it requires them when disambiguation becomes load-bearing.

## Alternatives Considered

**Lump artifacts under tradition-level References.** Create one Reference per tradition, listing all artifacts inside the body. Rejected because it loses per-artifact graph participation. A Decision that is informed by a specific gist wants to cite the gist, not the tradition-as-a-whole; lumping forces every citation to refer to the tradition and recover specificity through body prose. The graph layer's granularity drops from artifact to tradition; the cost is paid on every citation.

**Author-and-year-only disambiguation.** Let two artifacts from the same author and year be disambiguated by trailing letters (`(Author, 2026a)`, `(Author, 2026b)`). Rejected because letter suffixes carry no semantic information. A reader sees `(Allen, 2026a)` and `(Allen, 2026b)` and knows only that they are two artifacts from the same author and year; they do not know which is the gist, which is the paper, which is the talk. The descriptor approach carries the semantic distinction in the filename directly.

**Disambiguation through body content.** Let filenames remain undifferentiated and distinguish artifacts through body descriptions. Rejected because filename-level identification is the cheapest classification tier. A reader scanning a folder of References does not want to open each file to know what kind of artifact it is. The descriptor convention puts the distinction in the cheap tier; body content handles the deeper semantics.

## What Would Change It

The commitment would be revisited under one condition.

**Most References come as singleton artifacts.** If the project's References remain predominantly single-artifact-per-tradition — where no tradition has yielded two or more Reference-worthy artifacts — the descriptor convention would carry authoring cost without disambiguation benefit. The revisit would soften the rule to "descriptors SHOULD be added when a second artifact from the same tradition arrives, not pre-emptively." Current Reference patterns have not tested this yet; the first tradition to yield two References will be the decisive case.

## Relations

- grounded_in::[[Embed Citation Parenthetical in Reference Filenames]]
  - The citation-parenthetical commitment structures Reference filenames; the disambiguation commitment adds the artifact descriptor in front of the parenthetical when multiple artifacts require disambiguation. The two rules compose at the filename level.

- informs_downstream::[[Reference Form Contract]]
  - Reference Form Contract's filename pattern Requirement carries the thin enforcement clause pointing at this Decision.
