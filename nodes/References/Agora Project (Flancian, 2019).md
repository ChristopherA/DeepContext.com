---
created: 2026-04-23
tagline: A software project and running instance aggregating per-contributor git gardens into a federated wikilink namespace — the bring-your-own-garden pattern adopted for a later phase
brief_summary: Flancian's Agora is a three-repo software project (root config, aggregator bridge, renderer server) plus the running instance at anagora.org. Contributors keep their own git-based gardens in whatever tool they prefer; the aggregator collects them via a `sources.yaml` manifest and renders them under a shared namespace where `[[foo]]` resolves to the union of all contributions whose slug matches `foo`. DeepContext adopts the external-sources-list aggregation pattern, the tool-agnostic contribution layer, and the filesystem-as-truth / rendered-graph-as-derived-artifact discipline for a later phase once the single-repo publication model is working. The unit-of-participation difference is load-bearing: Agora's unit is a garden-registered-in-an-aggregator that does not produce its own live site; DeepContext's unit is a scion that publishes itself. The Agora project also names a governance-fork primitive — a community subset may fork the Agora itself when contracts become incompatible — that is distinct from code-level repository forking.
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Federation Model]]
- authored_by::[[Flancian]]↗
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Agora Project (Flancian, 2019)

URL: <https://anagora.org>

## Sources

- Root config, sources manifest, and community contract: <https://github.com/flancian/agora>
- Pull-based aggregator: <https://github.com/flancian/agora-bridge>
- Renderer and web frontend: <https://github.com/flancian/agora-server>

The Agora project is a three-repo software system and its running instance at anagora.org. The root repository holds the `sources.yaml` manifest that names each contributor's git garden and a `CONTRACT.md` naming the community's social agreements; the bridge is a long-running worker that pulls each listed source on a schedule; the server renders the aggregated result under a shared wikilink namespace. A reader encountering `[[foo]]` on the running instance sees the union of contributions whose filename-slug matches `foo`, drawn from many gardens, with each contribution presented as a distinct block attributed to its contributor.

### Adopted for a later phase

- **External sources list as aggregation manifest.** A flat YAML file naming each third-party git repository, with per-entry `url`, `target`, `format`, optional `protocol`, and URL templates for edit links and web views. The pattern is `sources.yaml` at the Agora root; DeepContext's later-phase equivalent would name which external gardens a rendering surface aggregates.
- **Tool-agnostic contribution layer with format tag per source.** Each source declares its flavor (`foam`, `obsidian`, `logseq`, `roam`, `jekyll`, `mycorrhiza`, `markdown`, `org`, `mycomarkup`); format-specific translation happens at ingest. Contributors keep editing in whatever tool they already use.
- **Pull-based aggregation worker with per-source status tracking.** The bridge records last-attempt, last-success, last-error per source so aggregation failure at one garden does not fail the whole surface.
- **Cross-source wikilink resolution as a union, not a merge.** Resolution presents every contribution whose slug matches; it does not normalize or elect a canonical version. This is consistent with [[Translation Over Convergence]] and [[Vocabulary Diversity Is a Feature]] at the rendering layer.
- **No-404 composition.** Every wikilink resolves to something — at minimum, an invitation to contribute. Dead ends become participation surfaces rather than broken links.
- **Filesystem as truth, rendered graph as derived artifact.** The aggregated JSON graph is exported from parsed filesystem content; the filesystem is authoritative.
- **Edit-link delegation via URL templates.** The aggregator links back to each source's upstream editor rather than hosting editing itself. Each entry carries an `edit:` URL template (e.g., `https://github.com/flancian/garden/edit/main/{path}`); the aggregator fills in the path per contribution. This pattern is compatible with [[Adopt Scion Publication Model]]'s first-class Web-UI edit path.
- **Typed sources in one manifest.** The manifest accepts more than one kind of entry: individual authoring gardens and shared collaboration surfaces (named *stoas* upstream) both register through the same API, distinguished by a type tag. DeepContext's later-phase equivalent may name distinct kinds of source while keeping the single-manifest discipline.
- **Governance-fork clause as a social-layer primitive.** The Agora's `CONTRACT.md` names forking as a legitimate response to contract incompatibility — a subset of the community may fork the Agora itself with no presumption of ill intent. This is distinct from code-level repository forking and names an explicit social exit at the conventions layer.

### Not adopted

- **Aggregator as a separate always-on service.** The bridge is a worker; the server is a Flask application; the full stack requires deployment infrastructure (uWSGI, SystemD, caching, optional Forgejo hosting). DeepContext's model is self-contained publication: a scion produces its own live site on GitHub Pages with no external service required. The aggregator-as-service model is incompatible with the friction floor [[Adopt Scion Publication Model]] commits to.
- **Federation as the primary unit.** Agora treats the aggregated namespace, not the individual garden, as what a reader visits. A contributor's garden is source material for someone else's rendered surface rather than a published site in its own right. DeepContext's current scope is single-repo canonical publication; a scion is a first-class live site, not a feeder.
- **Per-contributor does not publish.** A contributor registering a garden in someone else's Agora does not get their own rendered surface from that registration. This differs from DeepContext's commitment that a scion's first push builds the scion's own site.
- **ActivityPub federation.** Agora's server publishes per-user ActivityPub actors with signed Create activities for new subnodes. DeepContext has no federation commitment; the pattern is named here because it may become relevant if a later phase touches cross-graph aggregation.

### Key moves to remember

- The governance-fork primitive and the code-level repository fork are distinct moves. The former is a community exit when agreements become incompatible; the latter is a technical operation on a git repository. Both are relevant to DeepContext, but they answer different questions.
- Agora's unit of participation is a garden registered in an aggregator's manifest; the garden does not produce a live site on its own. This is the structural contrast with DeepContext's scion-publishes-itself commitment that [[Adopt Scion Publication Model]] makes.
- The aggregator-plus-many-gardens model and the scion-as-single-repo model are not competitors — they address different scales. Agora's patterns are worth naming for the later phase where cross-graph aggregation becomes load-bearing; the MVA Stance defers building until that need surfaces.
- Translation happens at ingest (format-to-format), at resolution (cross-source union), and at contract (the governance-fork exit when vocabularies cannot be reconciled).

## Relations

- informs_downstream::[[Adopt Scion Publication Model]]
  - The Decision commits to a scion-publishes-itself unit of participation that differs structurally from Agora's aggregator-plus-gardens model. This Reference is one of the precedents the Decision contrasts with — Agora's model shows what aggregation-first federation looks like, and the Decision names why DeepContext's current scope chose self-contained publication instead.

- informs_downstream::[[Adopt Minimum-Viable-Architecture Stance]]
  - The MVA Decision defers cross-garden aggregation, translation at the aggregator, and interactive federation surfaces. The Agora project is a precedent the deferred capabilities draw their specific shape from; this Reference is the study substrate for if and when those capabilities become load-bearing.

- informs_downstream::[[Wikis Without Curation Drift Toward Write-Only]]
  - The Observation's Grounds name Agora and Anagora as one of the traditions the write-only drift appears in — sustained contributor enthusiasm for a period followed by a slowdown as link-integrity and ontology-reconciliation work outpaces contributor willingness to do bookkeeping. This Reference is the specific source that grounding reconstructs from.

- informs_downstream::[[Translation Over Convergence]]
  - Agora's cross-source wikilink resolution presents multiple gardens' contributions as a union rather than a merge, consistent with the Conviction's commitment to holding distinct claims as distinct claims. The resolution layer's translation is thinner than the cross-vocabulary translation the Conviction asks agents to do, but the architectural direction is the same: preserve difference, do not normalize.

- contrasts_with::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The gist specifies the per-node convention layer — wikilinks, named-edge predicates, annotated edges, form contracts. The Agora Project addresses the complementary cross-node-set layer — how many gardens' contributions aggregate into a shared namespace. The two References occupy adjacent territory at different scales: the gist is primary convention source; this Reference is federation model.
