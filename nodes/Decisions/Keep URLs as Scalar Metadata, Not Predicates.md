---
created: 2026-04-19
tagline: URLs appear as body URL: lines or Sources section entries; they are never encoded as named-edge predicate values
brief_summary: A commitment that URLs for external source artifacts appear as scalar content — a `URL:` line in the body or bulleted entries in a `## Sources` section — not as named-edge predicate values. URLs are scalar data; graph-structural claims about sources (what role the source plays, what it informs, what it is superseded by) live in named edges (`serves_as::`, `informs::`, `supersedes::`). Conflating the two would either misuse predicate syntax for flat data or push structural claims into scalar-only formats.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Keep URLs as Scalar Metadata, Not Predicates

URLs preserving the external location of a source appear as scalar body content — a `URL:` line in the body (preferred for a single canonical URL) or bulleted entries inside a `## Sources` section (when multiple URLs are material). URLs MUST NOT be encoded as named-edge predicate values: no `external_url::https://...`, no `source_location::[[https://...]]↗` wrapping a URL as a pseudo-wikilink target. Graph-structural claims about the source (what role it plays, what it informs, what supersedes it) live in named edges; the URL lives in body scalar form.

## Why

The commitment preserves **graph spine clean of flat data**. Named-edge predicates carry graph-structural semantics — they connect nodes by typed relations that the graph's reader traverses for meaning. URLs connect nodes to external resources, but the connection's shape is different: a URL is a flat pointer to a document, not a typed relation between two graph vertices. Encoding URLs as predicate values would either misuse the predicate vocabulary (predicates become dual-purpose — some carry structural claims, others carry flat data) or force wiki-style wrapping of URLs as pseudo-targets (`[[https://example.com]]↗`), which the wiki layer does not resolve as a node.

The separation makes **structural and flat data legible at the tier layer**. A reader scanning a Reference's body for the external location finds the `URL:` line or the `## Sources` section — predictable placements that carry URLs specifically. A reader traversing the Reference's graph relations finds `serves_as::`, `informs::`, `supersedes::` — predicate edges that carry structural claims. The two readers have different jobs; keeping URLs in scalar form and structural claims in predicate form lets each reader find what they need at the tier the prototype's vocabulary reserves for it.

The rule applies specifically to URLs-as-artifact-locations. A Reference's canonical URL (where the artifact lives) is scalar. A typed edge to another graph node by wikilink is not — `serves_as::[[Primary Convention Source]]` is a named edge whose target is a graph node, not a URL. The rule distinguishes URLs (flat, scalar, body content) from wikilinks (typed, graph-participating, named edges). Wiki tooling's `↗` marker applies to external-tradition wikilink targets (nodes in other wikis), not to URLs — the marker signals "this target lives elsewhere in wiki space," not "this is a URL."

The prototype's `## Sources` convention handles multi-URL cases. When a Reference has a primary URL plus a mirror, a running instance, or a supplementary file, the `## Sources` section lists each with a brief annotation. The section is scalar body content; its entries are not typed edges. If a source becomes load-bearing enough to warrant its own Reference node, it is promoted to a stub node under `sources/` (a future folder), and the Reference cites the stub by wikilink via a typed predicate — which re-enters graph participation appropriately.

## Alternatives Considered

**`external_url::[[https://...]]` predicate.** Wrap URLs as pseudo-wikilink targets on a predicate edge. Rejected because the wrapping breaks wikilink resolution. `[[https://example.com]]` resolves by filename — a file named `https://example.com.md` — not by URL fetch. The predicate becomes a named-edge that points at a ghost link for every external URL, polluting the ghost-link signal (which should mean "intended future node") with "this is actually a URL, not a node." The wikilink convention is wrong for URLs.

**Predicate URLs without wikilink wrapping.** Let URLs appear as bare predicate values: `external_url::https://example.com`. Rejected because predicates are the graph's typed-edge syntax; non-wikilink values violate the convention that predicates target nodes. Mixing URL values and wikilink values in the predicate vocabulary would produce traversal ambiguity — a reader filtering on `external_url::` would need to check whether each value was a URL or a wikilink.

**YAML-encoded URLs.** Carry URLs in YAML frontmatter (`url: https://...`). Rejected by [[Restrict YAML to Scalar Metadata]] for named-edge predicates, but URLs-as-scalars could live in YAML. The body placement is preferred because References' URLs are load-bearing reading content — a reader opening the Reference expects the URL visible in the body near the top, not buried in frontmatter. The rule does not strictly forbid YAML URLs; it establishes body placement as canonical.

## What Would Change It

The commitment would be revisited under one condition.

**URL-as-predicate proves valuable for traversal queries.** If a compelling query use case emerges — traverse the graph, collect all external URLs for citation, filter by URL pattern — and the scalar body placement makes the query awkward, the convention could weaken to permit URL-predicates. The alternative is a build step that extracts URLs from body `URL:` lines into a query index, which preserves the scalar-body convention while enabling the traversal. Current use patterns have not surfaced the need; the revisit condition is latent.

## Relations

- grounded_in::[[Restrict YAML to Scalar Metadata]]
  - The YAML-scalars commitment establishes the scalar/predicate separation. URLs-as-scalar-body-content extends the same separation: structural claims use predicates, flat data (YAML keys and body URLs) uses scalars.

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine is what URLs-as-predicate would colonize if permitted. Keeping URLs out of predicate vocabulary preserves the spine for graph-structural claims.

- informs::[[Reference Form Contract]]
  - Reference Form Contract's URL-preservation Requirement carries the thin enforcement clause pointing at this Decision.
