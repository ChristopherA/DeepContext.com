# DeepContext

Every collaborative community builds up **deep context** -- the shared
meaning, distinctions, and compressions that make communication efficient
inside the group. A community's hashtags, specialized terms, in-jokes, and
accumulated conventions carry tribal weight an outsider cannot immediately
parse, because insiders co-built the substrate that gives those terms their
implications. That accumulated substrate is deep context, and it is the
thing this project is named for.

Deep context is fragile. Founding vocabularies calcify before later
participants have a chance to shape them. Newcomers experience the
accumulated depth as a debt they owe before contributing. Shared languages
get intimidating as they mature. When the tools that held the deep context
become obsolete, the deep context can die with them -- a decade of
conversation trapped in a wiki engine nobody maintains. Systems that try to
bridge communities often compound the loss by flattening each community's
distinctions to fit a canonical model.

Large language models and agentic tools change what curation, translation,
onboarding, and cross-vocabulary work cost -- not by replacing the people
doing the work, but by making certain kinds of help cheap that used to be
expensive. That shifts what a medium for deep context can plausibly carry.
DeepContext is an experiment in such a medium. Shared meaning accumulates
as typed markdown nodes whose reasoning is part of the record rather than
implicit in oral tradition ([[Capture Reasoning, Not Just Knowledge]]).
Different contributors' distinctions sit alongside each other rather than
being normalized into a canonical vocabulary. The record is plain markdown,
so it outlives the tools that authored it ([[Knowledge Outlives Its Tools]]).
The project's core stance is compact: the author names the relation, and the
software works with that fact afterward -- it does not arrive with an
opinion about what the author's words should mean.

## The stance

Edges stay author-declared, not agent-inferred. The gap between adjacent
vocabularies -- what each author preserves that the other doesn't -- is
often the most valuable content the graph carries, not a friction to
resolve. This matters more the more people are in the graph: a solo graph
can cheat the vocabulary question; a shared graph cannot.

Four commitments carry the stance at the substrate:

- [[Vocabulary Diversity Is a Feature]] -- contributors keep their own
  naming; the graph translates rather than normalizes.
- [[Translation Over Convergence]] -- when two vocabularies meet, both edges
  land in the graph as distinct claims, not one merged claim.
- [[Terms Become Common Through Unanimity, Not Precedent]] -- a term joins
  the shared vocabulary by agreement, never by one contributor's repeated
  usage alone.
- [[Agents Translate, Not Extract]] -- an agent helps authors communicate
  across their choices; it does not decide what their choices should mean.

The substrate claim is simple: software should not default to platform
meaning over authored meaning. Every convention in this graph is built to
carry that principle into a medium many contributors can share without the
medium rewriting their words.

## The founding decision

The project's founding commitment -- the one the three stewards arrived at
before anything else was built -- is [[Deep Context as an Architecture for Captured Reasoning]].
It names what this graph is *for*: representing reasoning as typed markdown
forms with traversable named-edge predicates, not as fine-tuned model weights,
not as retrieval chunks, not as database records, not as tags. The Decision
is grounded in two Convictions -- [[Capture Reasoning, Not Just Knowledge]]
and [[Knowledge Outlives Its Tools]] -- and everything else in the graph
descends from it, directly or through a short chain.

## What the practice is for

The larger practice this architecture supports is
[[Synpraxis Spectrum|synpraxis]] -- a coined term for the full spectrum of
acting together, from coordination (aligning timing) through cooperation
(splitting work and reassembling) to collaboration (work intertwined
throughout). DeepContext is specifically infrastructure for the cooperation
end of that spectrum: not trying to force collaboration in the strict sense
(shared identity, jointly-authored output), but to make cooperation across
diverse contributors work without flattening their distinctions.

## What goes wrong

Collaborative knowledge work has been tried many ways. International
standards bodies. Email lists. Online forums. Private chat groups. Public
and private wikis. Federated and single-author gardens. Each of them runs
into the same failure modes from different angles -- contributors keep
adding, but readers can't find what they need; the people doing the
curation burn out; shared vocabulary accumulates faster than newcomers can
absorb; communities fracture along lines the participants themselves didn't
quite choose. [[Wikis Without Curation Drift Toward Write-Only]] records
the pattern at wiki scale; the same dynamic shows up wherever the
coordination cost exceeds what sustained participation can pay. The graph
carries each dynamic as an Observation with grounds and revision
conditions; three clusters sketch the shape.

**Vocabulary accumulates asymmetrically.** The terms founders choose become
the group's terms before later participants have a chance to shape them
([[Founding Vocabularies Constrain Later Participants]]). As the shared
vocabulary grows, newcomers experience the breadth as a debt they owe
before contributing ([[Shared Languages Get Intimidating Over Time]]).
Converged vocabularies then produce authority asymmetries that make
reshaping harder still ([[Consensus Creates Priesthoods]]).

**Participation follows power-law distributions.** A small fraction of
participants produce most of the contribution across every online
collaborative platform studied. The bottleneck is not first-cycle entry
but second-cycle continuation, where roughly one in four first-cycle
contributors continues ([[Second-Cycle Contributors Are the Scarce Resource]],
which carries the power-law distributional finding in its Grounds). Tooling
improvements that lower the surface barrier have not shifted the curve
alone ([[Markup Simplification Does Not Flatten Participation]]), and
volume-only measures miss contributors whose work takes the form of
responding or curating rather than authoring
([[Participation Takes Different Forms Not Different Levels]]). Critical
mass -- enough sustained participation for a practice to feed itself -- is
hard to reach against that shape, and harder still to keep.

**Contribution requires an unusual trait combination.** Meaningful
contribution demands someone who simultaneously believes the contribution
is worthwhile (pride) and accepts that others can improve it (humility) --
a combination rarer than either trait alone, and one the surface of most
collaborative tools does not specifically cultivate
([[Meaningful Wiki Contribution Requires Both Pride and Humility]]).

These clusters compose into a predictable cycle: founders seed vocabulary;
the vocabulary calcifies into authority; later participants either adopt
it, stay silent about their own framings, or leave to form parallel
communities; participation concentrates among early arrivers; and the
reinvention of the same concepts under different names becomes the visible
symptom each decade. Deep context built under those dynamics accumulates
unevenly, ages badly, and frequently ends up trapped in whichever tool
happened to hold it.

The stewards do not believe any of this can be wholly overcome. The power
law is robust across platforms. Accumulated vocabulary cannot be made
weightless. Founding choices do shape what comes after. The rare trait
combination remains rare. Honest attention to the ways tool adoption can
widen the gaps it was meant to close stays part of the work --
[[LLM Assistance Widens the Participation Gap]] holds the sharpest version
of that worry as a Contested Observation. This project is the experiment
for whether the specific moves recorded in its stance and architecture,
composed, add up to something that survives its own growth better than
what came before.

## Where to start

Different entry points by what you want to understand.

**The conventions** -- [Contracts](/nodes/contracts/) specify node shapes
(Contract, Decision, Conviction, Gloss, Observation, and so on) with RFC 2119
compliance rules. Start with [[Markdown Node Contract]] for the base shape,
then [[Contract Form Contract]] for how contracts themselves are structured.

**The choices and their reasoning** -- [Decisions](/nodes/decisions/) each
record what was chosen, what was considered, and what would change the call.
[[Adopt Wikilinks and Named Edges]] is the foundational one.

**The stance** -- [Convictions](/nodes/convictions/) are normative positions
the practice holds. [[Human Authority Over Augmentation Systems]],
[[Vocabulary Diversity Is a Feature]], and [[Translation Over Convergence]]
are the current six.

**The direction** -- [Aspirations](/nodes/aspirations/) name what the
project pulls toward with honest acknowledgement of the gap.
[[The Second Cycle of Contribution Happens]] is the core success metric.

**The open questions** -- [Observations](/nodes/observations/) record
descriptive claims with epistemic grounds (Empirical, Retrospective,
Contested). Contested observations like
[[LLM Assistance Widens the Participation Gap]] are claims the project takes
seriously but does not yet have a definitive answer to.

**The predicates** -- [Predicates](/nodes/predicates/) document the typed
edges themselves. [[conforms_to]], [[grounded_in]], [[informed_by]], and
[[contrasts_with]] are the most load-bearing.

## Link legend

The graph is held together by `[[wikilinks]]` and `predicate::[[Target]]` named
edges. Six surface forms appear in node bodies.

**Resolved wikilink** -- source `[[Target]]`; rendered as a working link that
preserves the brackets, so the source pattern stays legible on the site.
[[Atomic Node]] is a live example; clicking it opens the Gloss. Brackets are
kept deliberately ([see the Decision](/nodes/decisions/render-bare-wikilinks-with-visible-brackets/)).

**Pipe wikilink** -- source `[[Target|Display]]`; rendered as the display text
only so it reads naturally in prose. The full filename stem on a Gloss like
Compound Node is long; the pipe lets a reference read as
[[Compound Node -- a folder of markdown nodes with a designated lead|Compound Node]]
(displayed as "Compound Node", linked to the Gloss).

**Ghost link** -- a named but unseeded concept. The target has no node yet, so
the graph shows the name in ghost styling. Every identity block in this graph
currently carries `has_lifecycle::[[Seed Stage]]`, but [[Seed Stage]] itself
is a ghost -- the lifecycle vocabulary is named but not yet seeded as nodes.

**External marker** -- a concept named in another graph. The `↗` suffix is
the source-form convention -- the target is recognized as living in another
graph or tradition rather than being ghost or broken. A node can include an
external reference like `engages_with::[[Some Adjacent Idea]]↗` without
committing to importing the other graph's frame.

**Plain URL** -- a link to the web outside this graph. For example,
https://www.lifewithalacrity.com/2014/12/deep-context.html.

**Named edge** -- a typed relation in bullet form, e.g.
`conforms_to::[[Gloss Form Contract]]`. The predicate to the left of `::`
names the relation; the wikilink to the right names the target. Each
[Predicate](/nodes/predicates/) is itself a node specifying what the
predicate carries, what it distinguishes itself from, and the node shapes
it connects.

Unresolved and external targets render with visibly-distinct styling so a
reader can see where the graph ends.

## Form types

Each node conforms to one of nine Form Contracts. Each contract names a shape
and a compliance rule; the Decisions that ground each contract carry the
reasoning.

- **Contract** -- what a node of this form looks like. Example: [[Gloss Form Contract]].
- **Decision** -- what was chosen, why, and what would change it. Example: [[Adopt Wikilinks and Named Edges]].
- **Conviction** -- a normative stance the project holds. Example: [[Human Authority Over Augmentation Systems]].
- **Aspiration** -- a direction the project pulls toward, with acknowledged gaps. Example: [[The Second Cycle of Contribution Happens]].
- **Observation** -- a descriptive claim with epistemic grounds (Empirical, Retrospective, Contested). Example: [[Wikis Without Curation Drift Toward Write-Only]].
- **Pattern** -- a recurring craft move that resolves a tension. Example: [[Refactor the Predicate's Axes]].
- **Predicate** -- a typed edge with Carries, Crescent, and Typing sections. Example: [[conforms_to]].
- **Gloss** -- an interpretive definition that frames a concept. Example: [[Atomic Node]].
- **Reference** -- an external source the graph draws on. Example: [[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]].

## Browse by taxonomy

- [Contracts](/nodes/contracts/)
- [Decisions](/nodes/decisions/)
- [Convictions](/nodes/convictions/)
- [Aspirations](/nodes/aspirations/)
- [Observations](/nodes/observations/)
- [Patterns](/nodes/patterns/)
- [Predicates](/nodes/predicates/)
- [Glosses](/nodes/glosses/)
- [References](/nodes/references/)

## For agents

Agents collaborating on this graph should start with
[AGENTS.md](https://github.com/ChristopherA/DeepContext.com/blob/main/AGENTS.md),
which names the curator stance (suggest, flag, translate -- do not rewrite a
contributor's vocabulary without confirmation) and points at the taxonomy
entry points. Agents joining a fork should read their own fork's AGENTS.md
first; forks may customize the stance.

## About this repository

This repository is where the practice is being worked out in public. The
conventions, the node drafts, and the conversation all live here on GitHub.

The stewards carry decades of experience with online collaboration, across
both what has worked and what has fallen apart. The commitments encoded in
these conventions are drawn from that experience -- small-group
shared-thinking spaces that succeeded, larger ones that fractured, wikis
that sustained and wikis that drifted to write-only. The motivation is
shared: to make collaborative knowledge work easier to sustain, not to
relitigate any one prior attempt.

## How to contribute

This repository is the source of truth for the published graph. Contributions
are welcome through GitHub.

- **Read first.** Browse the taxonomies or follow the reading paths above.
  The graph is in its seed stage; not every node you want to reference will
  exist yet. Ghost links mark where gaps are.
- **Open an [Issue](https://github.com/ChristopherA/DeepContext.com/issues)
  or [Discussion](https://github.com/ChristopherA/DeepContext.com/discussions)**
  to propose a node, flag a conflation between two concepts, suggest a predicate,
  or ask a question about the conventions.
- **Edit directly in the GitHub Web UI.** Any node under `nodes/` can be
  edited in-browser; clicking "Commit changes" opens a pull request.
- **Fork the repository** to build your own garden on these conventions. A
  fork publishes to its own Pages site on first push -- see
  [README.md](https://github.com/ChristopherA/DeepContext.com#readme) for
  setup.

The practice is forkable, collaboratively editable, and has no single
editorial gatekeeper. The curation discipline lives in the conventions, not
in permissions. See [[Adopt Forkable Publication Model]] for the specific
commitments this implies.
