---
created: 2026-03-05
tagline: The wiki augments human capability — humans retain authority at every level
brief_summary: A held stance that wikis built for augmentation must preserve human authority — legibility (what the agent does), boundary-setting (what the agent may do), and override capability (when humans intervene). Specializes the broader commitment that authority flows from the humans who author the graph, and extends the commitment that content must not be subordinated to its container by treating the authors' reasoning as the content in an augmentation system.
---

- conforms_to::[[Conviction Form Contract]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Human Authority Over Augmentation Systems

A wiki built as a Deep Context graph exists to augment the reasoning of the humans who author it, not to replace it. The stance has concrete consequences: every mechanism that delegates work to an AI agent must preserve authors' ability to see what happens (legibility), define what may happen (boundaries), and change what is happening (override).

Agency erosion in AI systems happens through convenience, defaults, and invisible delegation — not through force. Contributors edit the AI's choices rather than making their own. The system produces outputs contributors accept without understanding. The feedback loop between human judgment and system behavior attenuates until humans are nominally in charge but structurally irrelevant.

What the stance asks of the project shows up at three levels:

**Session level** — Every session begins by reading state files humans can inspect. Every commit requires human approval. Decision surfaces (`AskUserQuestion` and its equivalents) raise choices to contributors rather than resolving them silently. Session logs and learning loops make the agent's reasoning visible after the fact.

**Architecture level** — Rules, skills, and processes are the conferral mechanism. They are plain-text files humans can read, edit, and version-control. Contextual trigger systems (path-scoped rules, skill frontmatter) load constraints where they apply rather than applying blanket permissions. Contributors can change any conferral by editing a file.

**Knowledge level** — The graph's form types, structural contracts, and typed relations encode the authors' reasoning in a format that survives the agent that helped create it. If the current AI harness were replaced tomorrow, the wiki's content retains its structure and meaning. The knowledge belongs to the humans who authored it, not to the tool.

The difference between augmentation and substitution is testable: remove humans from the loop and observe what changes. If nothing changes, the system has substituted; if the system cannot proceed, human authority is real. That test is how drift from this conviction would be recognized — a wiki whose generation continues unchanged when its authors are absent has subordinated their reasoning to the system that helps produce it, and the stance has weakened whether or not the project still names the commitment.

## Why Authority Cannot Be Delegated Away

Authority cannot be delegated away because authorship carries consequence and machines do not bear it. Deb Roy argues that speech without a speaker who bears consequence is "words without consequence" — a machine can produce fluent text but cannot risk being wrong, cannot be embarrassed by a weak argument, cannot have its reputation shaped by what it publishes. That vulnerability is what makes authorship real. A wiki whose content is entirely agent-produced has no author in this sense, regardless of how coherent the prose appears. The human role is not performance but responsibility: standing behind the result, having genuinely shaped it, being accountable for its claims. Augmentation tools research, draft, restructure, and critique — but they cannot bear the consequence of the output. The wiki's authors can.

## Generation-Verification Asymmetry

The P-vs-NP intuition from computational complexity maps onto agent engineering: verifying a solution is cheaper than generating one. Humans out-evaluate agents but do not out-implement them. Generation is cheap — an agent can produce a hundred candidate restructurings of a wiki section in seconds. Verification is expensive and requires domain judgment the agent lacks: does this restructuring preserve authors' intent? Does it break a relationship authors value? Does it introduce a claim authors would not endorse?

This asymmetry is what makes human authority over augmentation systems operationally viable rather than merely asserted. Authors do not need to produce every output — only to evaluate whether each output meets the standard. Three historical examples trace the pattern across engineering domains. James Watt's centrifugal governor (1788) maintained steam engine speed through a mechanical feedback loop: the system generated continuous adjustments while a physical constraint verified acceptable range. Kubernetes applies the same logic to infrastructure: operators declare desired state, and the system generates whatever actions converge toward it — humans verify by specifying what "correct" looks like, not by implementing each step. Agent harnesses like Claude Code's rules, hooks, and approval gates represent the current frontier of this pattern, where humans define boundaries and the agent generates within them.

The operational consequence for a Deep Context graph: design every agent interaction so the expensive part — judgment, verification, consequence-bearing — stays with the humans, while the cheap part — generation, search, restructuring — goes to the agent.

## Sources

- Allen, Christopher. "Principal Authority," 2021 — the Self-Sovereign Identity framing that authority originates with the person.
- Roy, Deb. "Words Without Consequence," *The Atlantic* — speech without a speaker who bears consequence erodes the moral structure of language.
- George. "Harness Engineering Is Cybernetics," 2026 — generation-verification asymmetry and the cybernetics lineage from Watt's governor through Kubernetes through agent harnesses.

## Relations

- grounded_in::[[Authority Flows from the Person]]↗
  - The Self-Sovereign Identity principle that authority originates with the person grounds this wiki-level stance. Specialization direction: Authority Flows from the Person is the general claim; this conviction is the specialization to augmentation systems, carrying the specific session/architecture/knowledge asks. The grounding principle's full statement lives in the estate. (The grounding principle speaks of authority at the level of the individual person; this specialization applies that authority to the humans — one or more — who author a given graph.)

- grounded_in::[[Content Over Container]]↗
  - This conviction extends Content Over Container by treating the authors' reasoning as the content. Where Content Over Container says knowledge must not be subordinated to its container, this conviction says human reasoning must not be subordinated to the system that helps produce it. Specialization direction: the authors' reasoning is the content; the augmentation system is the container.

- informed_by::[[George (2026) Harness Engineering Is Cybernetics]]↗
  - George grounds the operational-viability claim in the P-vs-NP intuition — humans out-evaluate but do not out-implement. The cybernetics lineage (Watt's governor, Kubernetes, agent harnesses) provides the historical evidence that generation-verification asymmetry is a robust engineering pattern, not a convenient rationalization.

- informs_downstream::[[Deep Context as an Architecture for Captured Reasoning]]
  - The architecture decision names "expressible agent-versus-human authority boundaries" as one of the requirements that rules out fully autonomous alternatives. This conviction is the standing stance that requirement serves — the architecture is the structural move that takes the stance seriously.

- informs_downstream::[[Adopt Wikilinks and Named Edges]]
  - The wikilinks-and-named-edges decision commits the graph's semantic layer to author-declared predicates rather than tool-inferred similarity. Taking human authority seriously structurally requires that the graph's meaning is author-declared: every named edge is an act of authorship a human contributor can inspect, edit, and version-control.

- informs_downstream::[[Agents Translate, Not Extract]]
  - Agents Translate specializes this Conviction at the graph-interaction layer. Human authority over outputs is operationally incomplete without a translating-mode commitment — an extracting agent can respect every approval gate and still enroll contributors as subjects of its schema. The specialization names what human authority requires of the agent's posture toward the graph's predicates.
