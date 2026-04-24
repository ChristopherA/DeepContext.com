---
created: 2026-04-20
tagline: Contributor vocabularies carry design decisions the graph is committed to preserving rather than flattening
brief_summary: A held stance that different contributors' naming traditions encode meaning the graph wants to preserve. Each tradition is a design decision about what distinctions matter — choosing `estate` over `workspace` encodes stewardship; choosing `gardener` over `content curator` encodes a living-systems relation to knowledge; choosing `critiques::` over `challenges::` encodes a particular stance toward disagreement. Convergence pressure destroys the encoded meaning. The project holds that vocabulary diversity across contributors is not a friction to resolve but a feature of the graph — carried by author-declared named edges that let multiple vocabularies sit in the same corpus without being normalized at read time.
---

- conforms_to::[[Conviction Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Vocabulary Diversity Is a Feature

When contributors from different naming traditions meet in a shared graph, the differences in their predicates, their classification names, and their typed relations are not noise to normalize. They are design decisions each tradition made about what distinctions matter. The project holds that vocabulary diversity across contributors is a feature of the graph and a property the graph is committed to preserving, not a friction to resolve.

## Why It Is Held

Each naming tradition encodes decisions that would be destroyed by flattening. Choosing `estate` over `workspace` encodes stewardship and generational continuity; choosing `gardener` over `content curator` encodes a living-systems relation to knowledge; choosing `critiques::` over `challenges::` encodes a particular stance toward disagreement. The names are not cosmetic labels on interchangeable concepts — the names *are* the concepts, and the web of associations each name activates is the context through which every subsequent inference runs. Collapsing multiple naming traditions into a single shared vocabulary erases the distinctions that made each tradition legible to the communities it came from.

Convergence pressure carries costs that are not evenly distributed. When a community converges on a shared vocabulary, the participants who helped create it acquire natural authority, and newcomers face a choice between learning an ontology they did not shape or creating a parallel community with its own vocabulary. Standardized language stops evolving with the understanding of practitioners doing the work. Flattening three distinct predicates into one merged term produces an impoverished vocabulary less precise than any of the originals. The alternative — keeping each vocabulary intact and translating between them — preserves what each tradition built.

The stance is what makes author-declared edges load-bearing. When one contributor writes `critiques::[[X]]` and another writes `challenges::[[X]]`, both edges land in the graph as distinct claims. An agent reading across them translates rather than normalizing, and the contributors remain participants in their own naming rather than subjects of the system's extraction. Without the stance, author-declared edges drift toward agent-normalized edges at read time, and the graph silently converges on whichever vocabulary the normalizing agent prefers.

## What It Asks

Authors translate between vocabularies rather than normalize them. When a contributor brings naming that differs from existing conventions, the first response is to understand what distinction the new naming encodes — not to route it back to an existing predicate.

New predicates join the local vocabulary rather than being turned back at the door. A predicate unique to one contributor's tradition is seeded as a Predicate node in `nodes/Predicates/` and used. A predicate that overlaps with existing ones is kept as distinct whenever the contributor's distinction is load-bearing, with a glossary entry documenting the overlap and the difference.

Reviews flag convergence pressure as a drift signal. When a reviewer suggests "use the standard predicate" without asking what distinction the original carried, the suggestion is itself a sign that the reviewer is treating vocabulary variation as error rather than as preserved distinction. The review surface for vocabulary is translation, not normalization.

Cross-system collaboration adds translation layers rather than shared vocabularies. When the graph interoperates with another graph whose predicates differ, the response is a gloss document or a typed cross-reference — not schema alignment. Mutual intelligibility through translation is the target; a single shared ontology is not.

## Drift Recognition

The stance has drifted when the project starts treating contributor vocabularies as problems to resolve rather than as distinctions to preserve. Convergence pressure appears in reviews without being flagged; new predicates stop being added to the local vocabulary because authors default to existing terms; `nodes/Predicates/` stops growing by accretion.

A reader scanning the graph after drift would see convergence toward a single vocabulary — redundant predicates merged without preserving the merged distinction, contributor-specific terms replaced silently during review, glossary entries for the project's local dialect disappearing from the vocabulary section rather than being kept as translation anchors. A cross-system interop attempt that reaches for a shared schema rather than a translation layer is a louder signal of the same drift. None of these require a structural Requirement to fail; they accumulate as cultural erosion.

## Sources

- Allen, Christopher. "Wikilinks and Named Edges," 2026 — the "Why vocabulary diversity matters across systems" section develops the argumentative substrate, including the three costs of convergence (consensus creates priesthoods, standardized language becomes dogma, flattening destroys encoded meaning).

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The substrate Decision that makes author-declared edges the graph's spine. Vocabulary diversity only survives structurally if each contributor's edges are author-declared rather than agent-inferred; the Decision is what makes the stance viable in plain markdown.

- informed_by::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The gist's "Why vocabulary diversity matters across systems" section supplies the direct argument this Conviction compresses — the three-cost analysis of convergence and the alternative of mutual intelligibility through translation.

- informed_by::[[Deep Context Shared Languages Post (Christopher Allen, 2014)]]
  - The 2014 post that framed shared languages as layered machinery carrying community-specific meaning — the philosophical substrate under this Conviction's claim that adjacent vocabularies' distinctions are load-bearing content.

- informed_by::[[Creating Shared Language and Shared Artifacts Post (Christopher Allen, 2009)]]
  - The earlier 2009 post that framed meaning as provided by users rather than inherent in words. The sovereignty argument in this Conviction rests on that substrate: author-declared edges preserve distinct claims because meaning is not reducible to a canonical vocabulary's terms.

- informed_by::[[Synpraxis Spectrum -- acting together across the coordination-cooperation-collaboration spectrum]]
  - The Gloss naming the coordination-cooperation-collaboration spectrum. Vocabulary diversity is the cooperation-side discipline that distinguishes cooperation (each contributor keeps their own vocabulary) from collaboration (shared identity, jointly-authored output requiring vocabulary convergence). The Gloss provides the wider framing this Conviction's stance occupies a specific position within.

- informed_by::[[Consensus Creates Priesthoods]]
  - The Observation supplies the empirical grounding for one of the three convergence costs the Why rests on.

- informs_downstream::[[Translation Over Convergence]]
  - Translation Over Convergence specializes this stance into a concrete operational rule for what happens when vocabularies meet. This Conviction names the feature; Translation Over Convergence names what the feature asks of the project at the contact surface between vocabularies.

- informs_downstream::[[Document Predicate Crescents Against Adjacent Predicates]]
  - The Decision that operationalizes this Conviction at the predicate layer. Per-neighbor Crescent subsections are the structural enforcement that keeps adjacent predicates' distinctions from being silently merged under convergence pressure.

- informs_downstream::[[Require Carries Section in Predicate Nodes]]
  - The Decision that pairs with the Crescent Requirement at the predicate layer. A dedicated positive-sense Carries section gives each Predicate an independent account of itself — Crescent's contrast work is what it is not, and Carries is what it is.

- informs_downstream::[[Adopt Scion Publication Model]]
  - The scion publication model is load-bearing for this Conviction at the architecture layer. Without scioning, a contributor whose vocabulary diverges would have to converge on the parent's vocabulary or stop participating; with scioning, they continue the practice under their own cryptographic identity while holding their own vocabulary. The Conviction commits the graph to preserving diversity at the edge-and-annotation layer; the scion Decision is what preserves it at the graph-instance layer.
