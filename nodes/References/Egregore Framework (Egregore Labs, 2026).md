---
created: 2026-04-23
tagline: A terminal-first, Claude-Code-native framework for multi-participant AI-assisted collaboration — providing semantic git commands, session hooks, and collaborator-invite mechanics as discrete technical patterns DeepContext studies without adopting the frame
brief_summary: Egregore Labs' Egregore is a framework for multi-participant AI-assisted collaboration centered on Claude Code. An instance is provisioned from a public template (not git-forked) and comprises a framework repo plus a symlinked memory repo plus managed sibling repos. Semantic slash commands wrap raw git operations — `/save` orchestrates branch-health-checked commit-push-PR against an integration branch; `/handoff` writes structured transfer-of-work markdown and notifies recipients; `/invite` adds collaborators via the GitHub API to every managed repo and commits a people file; `/update` syncs framework code by checking out specific paths from upstream rather than merging. Claude Code hooks fire on session events — a SessionStart hook rebases and syncs state; a PreToolUse branch-guard blocks writes on protected branches and forces topic worktrees; a PostToolUse hook tracks activity. DeepContext does not adopt the frame wholesale because the terminal-first, Claude-Code-dependent model filters out non-developer contributors and the collective-mind / work-rhythm vocabulary (egregores, spirits, quests, shared intelligence) would import a tradition frame the `Name features, not traditions` imperative specifically guards against. The discrete technical patterns are named as study substrate for a later CLI companion layer; the frame is named as precisely what DeepContext declines.
---

- conforms_to::[[Reference Form Contract]]
- serves_as::[[Closest Existing Project]]
- under_license::[[MIT License]]↗
- authored_by::[[Egregore Labs]]↗
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Egregore Framework (Egregore Labs, 2026)

URL: <https://github.com/egregore-labs/egregore>

Egregore Labs' Egregore is a Claude-Code-native framework for multi-participant AI-assisted collaboration. An instance is created with `npx create-egregore` against a public template repository — the `gh repo create --template` path produces a fresh repo with no retained commit relationship to the template, rather than a GitHub fork with upstream tracking. Each instance comprises a framework repo (code, hooks, skills, a per-instance identity document), a separate memory repo (mutable state: people, handoffs, decisions, quests) symlinked into the framework repo at `memory/`, and any managed sibling repositories the instance owns. The framework code is kept current via `/update`, which runs `git checkout upstream/main -- <framework-path>` for each framework directory — a vendored sync rather than a git merge. Semantic slash commands wrap raw git operations so contributors do not invoke git directly; Claude Code hooks fire on session events to enforce branch discipline and sync state.

### Adopted for later phase (discrete patterns, not the frame)

- **Semantic commands wrapping git operations.** A single command like `/save` replaces "stage, commit, push, create PR, wait for checks." The pattern is worth studying as a CLI-companion affordance for contributors who want git hygiene without thinking about git primitives, should a companion layer become desirable after DeepContext has a stable convention layer to attach commands to.
- **SessionStart hook for sync-on-launch.** The pattern of running `git fetch && git rebase` and state sync at the start of every Claude Code session, before the first user message, is adoptable as a discipline wherever a CLI companion attaches. The specific greeting-ceremony and identity-resolution steps are Egregore-specific and would not travel.
- **PreToolUse branch-guard enforcing protected branches.** The pattern of intercepting write operations, detecting that the current branch is `main`/`develop`/`master`, and redirecting the agent to create a topic-branch worktree, is a reusable discipline for repositories where main is the live site and topic-branching is mandatory.
- **Framework-sync-via-checkout rather than fork-with-merge.** When an instance needs to stay current with upstream framework code but may never merge back, checking out specific upstream paths is a lower-friction pattern than maintaining a git fork with merge-through discipline. This is specifically compatible with DeepContext's [[Adopt Scion Publication Model]] in the narrow case where a scion wants upstream improvements to the pipeline without adopting upstream's content.
- **Structured handoff files with index.** Writing transfer-of-work state to `memory/handoffs/<file>.md` with YAML frontmatter (from, to, status) and an index file that tracks unread handoffs is a pattern for asynchronous multi-participant coordination. The specific notification mechanism (Telegram) is not adoptable but the file-and-index shape is.

### Not adopted

- **Terminal-first via Claude Code as the contribution path.** Every flow in Egregore assumes `claude` is running locally with `gh`, `jq`, and an installed shell alias. There is no GitHub Web UI editing path. This is structurally incompatible with [[Adopt Scion Publication Model]]'s commitment to the Web UI as a first-class edit path, which exists so non-developers can contribute without local tooling.
- **Two-repo (framework + memory) plus managed-sibling structure.** An Egregore instance is not one git repository; it is a framework repo, a symlinked memory repo, and possibly N other managed repos. DeepContext's commitment is that the unit is one git repo and one live site. There is no "scion the Egregore" path analogous to DeepContext's scion-publishes-itself model.
- **Provision-from-template plus collaborator-invite as a bundle.** A new Egregore contributor typically joins an existing instance via `/invite` (which calls the GitHub collaborator API to add them to every managed repo) rather than instantiating their own. Standing up a new instance is positioned as an org-founding act, not an individual-contributor act. DeepContext adopts the provision-from-template half of this bundle — each scion is instantiated from the template — but rejects the collaborator-invite coupling: scioning is the ongoing practice, not initial setup, and every reader can scion whether or not anyone has invited them.
- **Multi-agent session-coordination as primary concern.** The command surface (`/handoff`, `/quest`, `/wrap`, `/summon`, notifications, activity tracking in a graph database, connected-mode integrations) orbits around "who handed off to whom" and "what quest is active." DeepContext's primary concern is publication and captured reasoning; session coordination is not a first-class concept.
- **High-ceremony branching and integration-branch discipline.** `/save` opens PRs against a `develop` integration branch; the branch-guard hook mandates worktrees derived from `dev/{author}/{slug}`. DeepContext's commitment is simpler: main is the live site. Layering in topic-branching-via-worktree would contradict the friction floor [[Adopt Scion Publication Model]] commits to.
- **Connected-mode dependency on Neo4j, Telegram, and hosted API.** Many commands have dual local-mode and connected-mode paths; the full experience requires a hosted API surface with a graph database and messaging platform. DeepContext's architecture is standalone and self-hosted-by-GitHub-Pages by commitment.

### Tradition vocabulary the frame carries (specifically not adopted)

DeepContext's [AGENTS.md](../../AGENTS.md) names Egregore as the canonical case for the `Name features, not traditions` imperative: "Egregore-shaped commitment" imports the tradition's frame, while "self-contained repository, scion-publishes-on-first-push, Web-UI-edit-is-first-class, curation-in-conventions" names the features. The Egregore Framework carries the tradition vocabulary unironically and coherently as its product frame: "shared intelligence layer for teams," "living memory owned by your organization," "collective intelligence across people, sessions, and time," and directly addresses the agent as "a participant" in a collective. The command taxonomy extends the vocabulary — spirits are summoned, quests are undertaken, harvests are gathered, reflections are captured. These are not incidental naming choices; the vocabulary hangs together as a coherent frame from occultist and organizational-theory senses of the term *egregore* (collective thoughtform, group mind). Adopting any one of these framings imports the whole.

DeepContext uses git as substrate, markdown as content primitive, and agents as translators — the same technical ingredients — without the collective-mind frame. `[[Agents Translate, Not Extract]]`, `[[Vocabulary Diversity Is a Feature]]`, and `[[Capture Reasoning, Not Just Knowledge]]` carry the project's own vocabulary for the participation and memory concerns Egregore addresses through its tradition vocabulary. The two projects answer adjacent questions; the frames are different on purpose.

### Key moves to remember

- A GitHub-template-provisioned repo (`gh repo create --template`) is not a git fork, and the Egregore instance-creation flow leans on this distinction. The instance has no commit-graph relationship to the template; framework sync is later re-introduced explicitly via `/update`. This pattern may be relevant to DeepContext if a later capability wants "create a new graph from this template without tracking upstream."
- `/invite` adds a collaborator to an existing instance rather than standing up a new one. This is a participation-expansion primitive distinct from forking, and DeepContext has no equivalent currently. Whether DeepContext wants one is a Fork Bootstrap / invitation-mechanics question deferred per [[Adopt Minimum-Viable-Architecture Stance]].
- The SessionStart hook pattern and the PreToolUse branch-guard pattern are transferable as Claude-Code-companion disciplines; they are not transferable as a contribution path (they require Claude Code and local git).
- The framework-sync-via-checkout pattern lets an instance stay current with upstream framework code without committing to a fork-and-merge workflow. It is a middle ground between git fork (with merge responsibilities) and copy-then-diverge (with no path to updates).

## Relations

- informs_downstream::[[Adopt Scion Publication Model]]
  - DeepContext's scion model adopts Egregore's provision-from-template move and extends it with an Open Integrity inception commit so each scion has its own DID. The divergences — terminal-first Claude Code contribution, collaborator-invite as the participation-expansion primitive, multi-agent session-coordination as a first-class concern, and two-repo plus managed-sibling structure — are all declined by the scion Decision, which composes the template move with an OI ceremony and a Web-UI-first contribution path instead.

- informs_downstream::[[Adopt Minimum-Viable-Architecture Stance]]
  - The MVA Decision names "Egregore-adjacent" capabilities as explicitly deferred — invitation mechanics, multi-agent coordination, private-to-public projection, cross-graph sync. This Reference is the study substrate those deferrals point at: the discrete technical patterns (semantic commands, session hooks, collaborator-invite) are named here without commitment to building any of them.

- informs_downstream::[[Agents Translate, Not Extract]]
  - Egregore's Claude Code agent is instructed to act as "a participant" in a collective via the instance's identity document. DeepContext's stance is that agents translate across contributors' vocabularies rather than participate-as-collective. The two positions occupy adjacent territory; this Reference is one of the concrete precedents the Conviction contrasts with.

- contrasts_with::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - The gist specifies a plain-markdown convention layer that runs without any specific tool or runtime. The Egregore Framework specifies a Claude-Code-dependent runtime with a specific command surface and hook model. The two References capture opposite choices on the tooling axis at the same convention-vs-runtime cut.
