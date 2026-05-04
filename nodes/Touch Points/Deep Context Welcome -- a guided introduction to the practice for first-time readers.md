---
tagline: A guided introduction to the Deep Context practice — for first-time readers and returning ones wanting a fresh framing
created: 2026-05-03
is_home: true
hide_identity_block: true
---

- conforms_to::[[Touch Point Form Contract]]
- frames_lens_on::[[Deep Context Architecture]]
- frames_lens_on::[[Deep Context as an Architecture for Captured Reasoning]]
- in_practice_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Growth Stage]]
- has_curation::[[Working Draft]]

# Deep Context Welcome

![[Attachments/Where Our Vocabularies Don't Match.png]]

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
DeepContext is an experiment in such a medium. Different contributors'
distinctions sit alongside each other rather than being normalized into a
canonical vocabulary. The record is plain markdown, so it outlives the
tools that authored it ([[Knowledge Outlives Its Tools]]). Nodes carry
their reasoning alongside their claims, so the *why* each contributor
carried is legible to later readers rather than implicit in oral tradition
([[Capture Reasoning, Not Just Knowledge]]). The project's core stance is
compact: the author names the relation, and the software works with that
fact afterward -- it does not arrive with an opinion about what the
author's words should mean.

This page is a **Touch Point** -- a guided introduction for someone
arriving for the first time (or remembering as if for the first time) what
this graph is for and how to enter it. It is not a summary; the substance
lives in the linked nodes. It is a curated welcome that gives you a way of
looking at what's here.

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

## Entry Points

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
are three of the most load-bearing.

**The direction** -- [Aspirations](/nodes/aspirations/) name what the
project pulls toward with honest acknowledgement of the gap.
[[The Second Cycle of Contribution Happens]] is the core success metric.

**The open questions** -- [Observations](/nodes/observations/) record
descriptive claims with epistemic grounds (Empirical, Retrospective,
Contested). Contested observations like
[[LLM Assistance Widens the Participation Gap]] are claims the project takes
seriously but does not yet have a definitive answer to.

**The craft moves** -- [Patterns](/nodes/patterns/) name recurring moves
an author makes by hand, each stated at card scale with a Heart, the Forces
it navigates, and the tension it resolves. [[Refactor the Predicate's Axes]]
and [[Let the Exercise Audit the Contract]] are two.

**The predicates** -- [Predicates](/nodes/predicates/) document the typed
edges themselves. [[grounded_in]], [[conforms_to]], [[informs_downstream]],
[[informed_by]], and [[contrasts_with]] are the most load-bearing.

**The term definitions** -- [Glosses](/nodes/glosses/) frame terms used
elsewhere in the graph, with the working definition carried in the filename
so a reader encounters it without opening the file. [[Atomic Node]] and
[[Compound Node]] are short examples.

**The external sources** -- [References](/nodes/references/) point at the
published material this graph draws on, with an Adopted / Not-adopted split
per source. [[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]] is
the most load-bearing for this project's structural spine.

**The agent capabilities** -- [Skills](/nodes/skills/) are agent-invocable
workflows that operate on the graph -- reading, authoring, validating,
auditing. [[Node Create]] is the entry point for writing new nodes;
[[Graph Orient]] is the entry point for agents arriving at the graph
for the first time.

**The reader-orientation pages** -- [Touch Points](/nodes/touch-points/)
(this page lives there) are guided introductions to specific regions of
the graph; this Touch Point welcomes you to the practice as a whole.

## Out of Scope

This Touch Point's lens does not cover:

- **A summary of the graph's content.** The substance lives in the linked nodes; this page is orientation, not synopsis. Follow the Entry Points above to read the substance.
- **A how-to guide for collaborative-knowledge tooling.** This graph is not a manual for using wiki engines, knowledge-graph databases, or LLM-application frameworks. The practice is about *what to record about reasoning*, not *which tool to use*.
- **A library-science classification of all human knowledge.** The graph is the deep context of *this* practice's contributors; it is not an attempt to organize knowledge in general. Other graphs (Self-Sovereign Identity, Synpraxis, etc.) carry their own deep contexts via their own conventions.
- **A pitch for adoption.** The practice does not assume readers will adopt it. The home page is here to receive readers well; what they do next is theirs to decide.

Readers looking for any of those should look elsewhere; the Entry Points above route to what this graph does cover.

## Link legend

The graph is held together by `[[wikilinks]]` and `predicate::[[Target]]` named
edges. Six surface forms appear in node bodies.

**Resolved wikilink** -- source `[[Target]]`; rendered as a working link that
preserves the brackets, so the source pattern stays legible on the site.
[[Atomic Node]] is a live example; clicking it opens the Gloss. Brackets are
kept deliberately per [[Render Bare Wikilinks with Visible Brackets]].

**Pipe wikilink** -- source `[[Target|Display]]`; rendered as the display text
only so it reads naturally in prose. The full filename stem on a Gloss like
Compound Node is long; the pipe lets a reference read as
[[Compound Node -- a folder of markdown nodes with a designated lead|Compound Node]]
(displayed as "Compound Node", linked to the Gloss).

**Ghost link** -- a named but unseeded concept. The target has no node yet, so
the graph shows the name in ghost styling. Every identity block in this graph
currently carries `authored_by::[[Deep Context Community]]`, but [[authored_by]]
itself is a ghost -- the predicate is named in use but not yet seeded as a
Predicate node.

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

Each node conforms to one of the [[Form Contract]]s. Each contract names a
shape and a compliance rule; the Decisions that ground each contract carry the
reasoning. The forms group by the role they play -- the reasoning the graph
captures, the vocabulary that makes the reasoning legible, and the
infrastructure the graph runs on. Each form name links to its taxonomy index.

**Reasoning the graph captures.**

- **[Decision](/nodes/decisions/)** -- what was chosen, why, and what would change it. Example: [[Adopt Wikilinks and Named Edges]].
- **[Conviction](/nodes/convictions/)** -- a normative stance the project holds. Example: [[Human Authority Over Augmentation Systems]].
- **[Aspiration](/nodes/aspirations/)** -- a direction the project pulls toward, with acknowledged gaps. Example: [[The Second Cycle of Contribution Happens]].
- **[Observation](/nodes/observations/)** -- a descriptive claim with epistemic grounds (Empirical, Retrospective, Contested). Example: [[Wikis Without Curation Drift Toward Write-Only]].
- **[Pattern](/nodes/patterns/)** -- a recurring craft move that resolves a tension. Example: [[Refactor the Predicate's Axes]].

**Vocabulary that makes the reasoning legible.**

- **[Gloss](/nodes/glosses/)** -- an interpretive definition that frames a concept. Example: [[Atomic Node]].
- **[Predicate](/nodes/predicates/)** -- a typed edge with Carries, Crescent, and Typing sections. Example: [[conforms_to]].
- **[Reference](/nodes/references/)** -- an external source the graph draws on. Example: [[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]].

**Infrastructure the graph runs on.**

- **[Contract](/nodes/contracts/)** -- what a node of a given form looks like; every node declares which Contract it conforms to. Example: [[Gloss Form Contract]].
- **[Skill](/nodes/skills/)** -- an agent-invocable workflow grounded in the Decisions it enforces. Example: [[Node Create]].

**Reader orientation.**

- **[Touch Point](/nodes/touch-points/)** -- a guided introduction that frames a reader's lens onto a region of the graph. Example: this page.

## For agents

Agents collaborating on this graph should start with
[AGENTS.md](https://github.com/ChristopherA/DeepContext.com/blob/main/AGENTS.md),
which names the curator stance (suggest, flag, translate -- do not rewrite a
contributor's vocabulary without confirmation) and points at the taxonomy
entry points. Agents joining a graph that grafted from this one should read
that graph's AGENTS.md first; each graph customizes the stance.

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

- **Read first.** Browse the taxonomies or follow the Entry Points above.
  The graph is in its seed stage; not every node you want to reference will
  exist yet. Ghost links mark where gaps are.
- **Open an [Issue](https://github.com/ChristopherA/DeepContext.com/issues)
  or [Discussion](https://github.com/ChristopherA/DeepContext.com/discussions)**
  to propose a node, flag a conflation between two concepts, suggest a predicate,
  or ask a question about the conventions.
- **Edit directly in the GitHub Web UI.** Any node under `nodes/` can be
  edited in-browser; clicking "Commit changes" opens a pull request.
- **Stand up your own graph.** Run the local [[Graph Inception]] ceremony
  to produce a fresh Open Integrity inception commit and DID, signed with
  your own SSH key — the new graph's cryptographic identity is yours, not
  GitHub's and not this graph's. You can start from a clone of this
  repository, from any other Deep Context graph, or from an empty
  directory; the ceremony is the same. The new graph stands on its own;
  it may optionally claim `scion_of:` lineage back to a donor when you
  want upstream tracking visible, or carry no lineage claim at all and
  diverge freely. See
  [README.md](https://github.com/ChristopherA/DeepContext.com#readme) for
  the setup procedure, [[Graph Inception]] for the agent-invocable
  ceremony, and [[Adopt Self-Sovereign Graph Publication]] for the why.

The practice publishes as self-sovereign graphs — anyone can stand up
their own graph carrying its own cryptographic identity, collaboratively
editable, with no single editorial gatekeeper. Most graphs are not
scions; scion-of is reserved for the parallel-fork case where upstream
tracking is wanted. The curation discipline lives in the conventions,
not in permissions. See [[Adopt Self-Sovereign Graph Publication]] for
the specific commitments this implies.

## Relations

- conforms_to::[[Touch Point Form Contract]]
  - The first Touch Point in this graph; serves as the home page (`is_home: true` in YAML frontmatter).

- frames_lens_on::[[Deep Context Architecture]]
  - The Practice Domain Gloss this Touch Point welcomes readers to. Deep Context Architecture is the shared language community whose conventions this graph documents; the Touch Point's lens names the welcoming entry into that community's vocabulary and reasoning.

- frames_lens_on::[[Deep Context as an Architecture for Captured Reasoning]]
  - The founding Decision the practice rests on. The Touch Point also frames the reader's encounter with this Decision specifically, since everything in the graph descends from it directly or through a short chain.
