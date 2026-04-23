---
created: 2026-04-21
tagline: A term becomes shared only when every participant agrees to it; one contributor's usage does not establish it as the group's term
brief_summary: A held stance about how vocabulary becomes shared in this project. A term is part of the Common vocabulary when participants actively affirm it, or at minimum decline to object to it, after it has been proposed. One person's repeated use, the project founder's choice of a word, or precedence-by-first-author does not by itself make a term the group's term. The stance protects contributors from having frames folded onto them silently -- even helpful-sounding ones -- and gives the project a mechanism for adding common vocabulary deliberately rather than by accretion. The Wilderness group developed an explicit three-state process (Affirm / No objection / Object); Deep Context adopts the stance at the abstraction level, leaving forks free to implement it however fits their context.
---

- conforms_to::[[Conviction Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Terms Become Common Through Unanimity, Not Precedent

A term is part of the project's Common vocabulary only when every participant in the conversation has either affirmed it or declined to object to it. One contributor's repeated use, the founder's initial choice, or the precedent of a term appearing first in the corpus does not by itself make the term common. The stance applies at the layer where a term is about to carry shared meaning across contributors; contributor-local vocabulary stays local by default.

## Why It Is Held

The stance is held because shared vocabulary is a genuine commitment, and commitments silently incurred are contributor sovereignty problems. When a term slides from "one person's word" into "the group's word" through usage alone, the participants who encounter it later inherit a frame they never chose, and the participants who could have proposed a different term lose the chance to do so. The asymmetry favors whoever spoke first, which for most projects is the founder. The project takes the position that this is a problem even when the founder's term is good -- the load-bearing thing is not whether the term is correct but whether the other participants had a chance to shape it.

The risk is most concrete at the beginning of a project, when the graph's founding vocabulary gets chosen. [[Founding Vocabularies Constrain Later Participants]] records the dynamic: architects who pick terms early end up constraining users later, and the constraint is often invisible until a newcomer encounters the vocabulary and finds no way to reshape it. The Wilderness group the project draws on took this directly into its process: a term moves from one participant's Vocabulary into the shared Common folder only through an explicit process where each participant chooses Affirm, No objection, or Object. A single Object blocks the move; Affirm and No objection both count toward adoption. The mechanism treats silence-as-consent as insufficient -- a term becoming common requires participants to at least not object, which is a weaker bar than affirmation but stronger than precedent.

Deep Context adopts the stance at the abstraction level rather than the specific mechanism. Unanimity-over-precedent is the commitment; the three-state Wilderness process is one way to implement it. A fork operating at a different scale, or in a different cultural context, could implement the commitment through a different mechanism -- periodic Common-vocabulary reviews, explicit proposals in a dedicated location, or a convention that new common terms must be proposed by someone other than the term's originator. The fork pattern itself depends on this -- a fork inherits the vocabulary the parent already converged on, but the fork's own new common terms are the fork's participants' to establish, not the parent project's to project downstream.

## What It Asks

Treat founder vocabulary as provisional until unanimity establishes it. The project's early terms -- the ones that appeared in the Founding Conversation or seeded the first Contract -- do not automatically become part of the Common vocabulary. They are the starting draft of the Common vocabulary that later participants still have standing to revise. Marking a term as provisional until reviewed is an acknowledgement that the convergence work has not yet been done.

Propose, do not assume. When a term looks like it could become common, make the proposal explicit rather than letting the term accrete through repeated use. An explicit proposal lets other participants choose a position; accretion does not. The proposal can be brief -- a line in a Decision note, a commit message, a Discussion thread -- as long as it names the term and asks participants to respond.

Let contributor-local vocabulary stay local. A term used by one contributor in their own node does not need to be proposed for Common unless the term is about to travel into cross-contributor work. The author-declared edge convention is what makes this tolerable: each contributor's vocabulary stays in their own nodes, marked by `authored_by::`, and agents translate between vocabularies rather than normalizing. See [[Vocabulary Diversity Is a Feature]] and [[Translation Over Convergence]].

Treat Objection as a structural contribution. When a participant objects to a term moving to Common, the objection is a contribution to the shared vocabulary's shape, not a failure of collaboration. The objection names a distinction the proposer did not see, or a frame the term would impose that the objector rejects. The response is to understand the distinction the objection carries, not to re-argue the term.

## Drift Recognition

The stance has drifted when common vocabulary starts appearing without the proposal-and-affirmation step. A new predicate gets into the convention list because it appeared in three nodes first; a Contract acquires a new Requirement because the founder wrote it that way; a Gloss gets renamed because a curator thought the new name read better. Each of these can be done for good reasons, but none of them is the same as participants choosing the new term.

A reader scanning the project after drift would see a growing Common vocabulary that no one specifically remembers agreeing to. Repeated-use-becomes-canonical starts showing up as a visible pattern -- "X is what we've been calling it" rather than "X is what we agreed to." Contributors with different naming traditions stop proposing their terms, because the project's vocabulary has gained enough momentum that proposing feels like asking for a change. The silent drift is most visible at the point where a contributor stops writing something they would have written in their own dialect, because they've absorbed the project's vocabulary as given.

The stance also drifts in the opposite direction -- toward unanimity-as-paralysis, where no term ever moves to Common because agreement is too expensive to gather. A healthy implementation keeps the threshold accessible: No objection counts, silence-after-explicit-ask counts, the proposal-and-affirmation step is lightweight. The drift to watch is the stance functioning as a blocker on vocabulary growth, which would turn the commitment into a reason nothing shared ever gets named.

## Sources

- Allen, Christopher. "On How Terms Become Common," 2026 -- the essay from the IFP Wilderness Comms folder that supplies the Affirm / No objection / Object framework this Conviction adapts. The essay argues that "common vocabulary is a deliberate act, not a side effect of use."

## Relations

- grounded_in::[[Founding Vocabularies Constrain Later Participants]]
  - The Observation that founders' terms tend to calcify into the group's terms without deliberate review. This Conviction is the project's response to that dynamic: a commitment that precedent does not carry the same weight as participant agreement.

- informed_by::[[Consensus Creates Priesthoods]]
  - The Observation that converged vocabularies acquire authority over the participants who helped create them, leaving newcomers with a learn-or-leave choice. This Conviction names a process that intervenes before convergence calcifies, so the newcomer's position is proposer rather than supplicant.

- informs_downstream::[[Vocabulary Diversity Is a Feature]]
  - Vocabulary Diversity Is a Feature names the property the graph preserves (contributor-local vocabulary as design decision); this Conviction names the process that decides when a term is allowed to leave contributor-local scope and become shared. The two compose: most vocabulary stays local; the vocabulary that travels to Common does so only through unanimity.

- informs_downstream::[[Translation Over Convergence]]
  - Translation Over Convergence specializes the diversity stance into an operational rule for what happens when vocabularies meet. This Conviction specifies when that rule applies: whenever a term is about to travel from one contributor's dialect into shared vocabulary without explicit cross-contributor agreement.

- contrasts_with::[[Consensus Creates Priesthoods]]
  - The Observation describes how convergence calcifies into authority; this Conviction prescribes a mechanism for convergence that resists that calcification. The contrast is pattern-versus-intervention rather than opposition.
