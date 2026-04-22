---
created: 2026-04-21
tagline: When two contributors' vocabularies meet, write the glossary entry that names what each term preserves — translation as the move at the contact surface, not rename to canonical
brief_summary: "A recurring move at the contact surface between vocabularies. When a new contributor's predicate, term, or classification meets an existing one whose meaning overlaps but is not identical, the practical move is to write a Gloss that names each term, cites the tradition each comes from, and names the distinction each preserves. The Gloss is the translation layer; without it, the two terms either collapse silently into one (convergence by precedent) or sit as apparent synonyms whose encoded distinctions are invisible to later readers. The move is operationally cheap (one Gloss per pairing) and architecturally load-bearing — it is what makes the project's vocabulary-sovereignty commitments observable at the predicate layer."
---

- conforms_to::[[Pattern Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Gloss the Translation Surface

## Heart

When a new contributor arrives with a predicate, term, or classification that overlaps with an existing one but does not collapse into it, write a Gloss that names each term, cites the tradition each comes from, and names the distinction each preserves. The Gloss is the translation layer at the contact surface — the concrete move that turns `[[Translation Over Convergence]]` from stance into practice.

## Problem

Two contributors' vocabularies meet. One author writes `critiques::[[X]]`; another writes `challenges::[[X]]`. One calls a node a *Predicate*; another calls it a *Relation Type*. One's `gardener` serves the same role the other's `content curator` does. The overlap is real — both mean something in the neighborhood — and the distinction is also real: each term encodes a prior choice about what matters. Collapsing the two predicates into a canonical form erases the distinction; leaving them unlabeled in the graph hides the distinction from later readers who encounter one term without context for the other.

The default move is to rename to a canonical term. A reviewer suggests "use the standard one"; an agent summarizing the graph silently maps both to its preferred form; a curator consolidating the vocabulary list picks the term that appears more often. Each individual move is small, and the cumulative effect is convergence by precedent — the graph's vocabulary narrows without anyone explicitly deciding to narrow it.

The difficulty is recognition and discipline, not mechanics. Once the two terms are named as distinct, writing the Gloss is straightforward editorial work. The craft this Pattern teaches is *noticing that the two terms are not interchangeable* and intervening with translation before normalization becomes the path of least resistance.

## Forces

- **Convergence pressure is the path of least resistance.** Every tool, every review, every traversal nudges toward a single canonical form. The reviewer who suggests "use the standard term" is not being adversarial — the suggestion feels like hygiene. Holding the translation stance against this drift requires explicit intervention at every contact surface, not just at the first one.
- **Each vocabulary encodes decisions.** `critiques::` and `challenges::` are not synonyms — the first names a stance of engaged disagreement that expects response; the second names a confrontation that may or may not invite response. A contributor who wrote `challenges::` in their own tradition was making a claim about what the edge carries. Flattening the two loses the claim; the reader two weeks later sees a single predicate and cannot tell which sense the author meant.
- **The glossary cost is local; the convergence cost is global.** Writing a Gloss entry takes a few minutes. Converging two predicates into one affects every node using either. Translation is the cheap move, not the disciplined one — but cheapness is not obvious at the moment of decision, because the Gloss is extra work while normalization feels like simplification.
- **Emerging distinctions often appear under convergence pressure.** A contributor's predicate may initially look like a synonym and only later reveal a distinction the original author was preserving. The Pattern must be applied when the distinction is uncertain as well as when it is obvious — writing the Gloss is how the distinction gets named and made available for later evaluation, rather than lost to a premature rename.

## Solution

When authoring, reviewing, or curating, watch for the moment two vocabularies meet. Trigger signals: a new contributor's predicate that overlaps with an existing one; a proposed rename from one term to another; a summarization pass that maps distinct predicates to the same canonical form; a review comment suggesting "use the standard term."

At the trigger, write a Gloss entry with this shape:

1. **Name each term** as its own Gloss node, following the Gloss Form Contract's `<Concept> -- <definition>.md` filename shape. `critiques -- engaged disagreement expecting response.md` and `challenges -- confrontation not assuming response.md` as peers.
2. **Cite the tradition** for each term in the body. A predicate's provenance — an adjacent plural-contributor corpus, a particular author's practice, a field's established usage — is part of what the term carries.
3. **Name the distinction each preserves.** The load-bearing sentence names what the first term says that the second does not, and vice versa. The distinction may be axis ("engagement stance" vs "confrontation mode"), scope ("between two individuals" vs "to a group"), or register ("technical" vs "colloquial"). What matters is that the distinction is named explicitly, not implied.
4. **Cross-reference in Relations.** Each Gloss carries `contrasts_with::` to the other, with an annotation naming the load-bearing distinction.
5. **Leave both terms in the graph.** The Gloss is the translation layer; the original authors' predicates stay in their nodes. Readers encounter the Gloss when they ask "what is the difference between these?"

Do not write the Gloss as a choice-of-vocabulary recommendation. The Gloss is a translation, not a vocabulary review — it does not recommend one term over the other, it makes both legible to readers and agents working across them.

## Consequences

- **Vocabulary-plurality survives at the predicate layer.** Each contributor's terms remain in their nodes; readers encounter the distinctions through the Gloss rather than through silent normalization. The graph's vocabulary grows by accretion rather than converging under review pressure.
- **Convergence pressure becomes visible as a drift signal.** A reviewer who proposes rename-without-Gloss is making a vocabulary-arbitration move. Writing the Gloss instead surfaces the move as a decision the community can evaluate, rather than a hygiene step that slides through.
- **Glossary grows in proportion to divergence, not node count.** A single-contributor garden has few Glosses; a multi-contributor garden accumulates Glosses as contact surfaces emerge. The glossary's shape is a measurement of the graph's vocabulary plurality, visible in the `prototype/nodes/Glosses/` folder's own growth curve.
- **Translation work is bounded and local.** Each Gloss addresses one pairing. The cost does not compound across the whole corpus — a Gloss for `critiques`/`challenges` does not need to wait for every other pairing to be named. The work accumulates incrementally, each Gloss independently useful.
- **Agents reading across vocabularies have a translation substrate to consult.** An agent summarizing the graph can traverse `critiques::` edges AND `challenges::` edges and, at the point of summary, consult the Gloss to present the distinction to a reader rather than collapse the two. The Gloss is what makes agent translation operationally viable, not merely aspirational.

## Instances

- **The adjacent plural-contributor corpus's translation predicates.** `source_voice`, `responds_to`, and `assists_by` were translated into this graph from an adjacent corpus's practice. Each became its own Predicate node with `Carries` and `Crescent` sections naming the distinction against existing predicates. The Predicate form's Crescent structure is the Pattern applied at the Predicate layer specifically — one Predicate per axis, each with an explicit distinction against its neighbors.
- **Gloss files for compound-node terms.** The project's Gloss form was seeded with terms like `Named Edge` and `Markdown Node` where the project's usage overlapped with but did not identically match usages in adjacent traditions. Each Gloss cites the tradition and names the project's specific framing — the same move the Pattern names at the predicate layer applied at the concept layer.
- **Future instance: second contributor's first predicate.** The Pattern has not yet run at full contact-surface pressure because the graph has one principal author. The first instance where a new contributor brings a divergent predicate — whether `gardener` versus `curator`, or some other pairing — is the Pattern's canonical execution. The Gloss written at that moment is load-bearing for whether the project holds its translation commitments when the pressure arrives.

## Also Known As

- **Translation layer** — the infrastructure framing; the Gloss is the concrete unit, "translation layer" names the aggregate.
- **Don't normalize, gloss** — the imperative version; useful as a slogan mid-review when a rename is being proposed.
- **Peer-predicate documentation** — framing from an adjacent corpus; emphasizes that the glossed terms remain peers rather than one becoming canonical.

## Relations

- grounded_in::[[Translation Over Convergence]]
  - The Conviction that names the stance this Pattern operationalizes. Translation Over Convergence says "when vocabularies meet, both stay intact and translation bridges them"; this Pattern names the concrete move a contributor or curator runs at the moment two vocabularies actually meet. Without the Conviction, the Pattern is a style preference; with it, the Pattern is the stance-in-practice.

- grounded_in::[[Vocabulary Diversity Is a Feature]]
  - The substrate Conviction. The Gloss-as-translation move only makes sense if vocabulary diversity is the property the graph is committed to preserving. Under a convergence commitment, the Gloss would be busywork; under diversity, the Gloss is the operational mechanism.

- grounded_in::[[Terms Become Common Through Unanimity, Not Precedent]]
  - The Conviction that governs when a term moves from contributor-local to Common vocabulary. This Pattern operates one layer down — at the contact surface where contributor-local terms meet without (yet) traveling into Common. The Gloss keeps both terms local and legible; Terms Become Common governs whether either later enters shared vocabulary.

- informs::[[Agents Translate, Not Extract]]
  - The Conviction at the agent layer depends on this Pattern at the authoring layer. Agents translate rather than extract because contributors have written Glosses that make the distinctions available to agent reading; without the Glosses, an agent has only the raw predicates and must infer the distinction or normalize. The Pattern is what makes the agent-posture commitment executable.

- composes_with::[[Treat Objection as Structural Contribution]]
  - Both Patterns surface the move that keeps contributor sovereignty intact under review pressure. When a reviewer proposes rename-to-canonical, the objection names a distinction the proposer missed; writing a Gloss is one form the objection's structural contribution takes. The two Patterns compose: the objection surfaces the distinction; the Gloss records it.

- composes_with::[[Refactor the Predicate's Axes]]
  - Both are predicate-layer craft moves. Refactor the Predicate's Axes addresses the single-contributor case where one predicate carries two axes (split into single-axis predicates in the same vocabulary). This Pattern addresses the cross-contributor case where two predicates in different vocabularies overlap (translate between them, keep both). Applied together, they keep each contributor's vocabulary internally atomic and preserve distinctions across contributors.
