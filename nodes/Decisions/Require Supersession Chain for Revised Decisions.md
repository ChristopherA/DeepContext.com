---
created: 2026-04-19
tagline: A revised Decision gets a new filename and a supersession edge; the old filename is never renamed
brief_summary: A commitment that when a Decision is revised, a new Decision node is created with a new filename reflecting the new commitment. The older Decision's filename MUST NOT change — renaming would break existing wikilinks. The new Decision declares `supersedes::[[Old Decision]]`; the old Decision is updated to include `superseded_by::[[New Decision]]`. Both remain in the graph; the supersession chain is how the commitment's evolution is recorded. The commitment preserves wikilink citation stability and keeps the historical trace traversable.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Require Supersession Chain for Revised Decisions

When a Decision is revised, a new Decision node is created with a new filename reflecting the new commitment. The older Decision's filename does not change; it remains where it was, with its content intact, and gains a `superseded_by::[[New Decision Name]]` edge in its Relations section. The new Decision declares `supersedes::[[Old Decision Name]]`. Both Decisions remain in the graph. The supersession chain — a linked sequence of `supersedes::` / `superseded_by::` edges — is the record of how the commitment evolved over time.

## Why

The commitment **preserves wikilink citation stability** across revision. Every node that cited the old Decision by wikilink continues to resolve; the citing nodes are not touched by the revision. The old Decision's body is not edited to reflect the revision — a reader following an old citation arrives at the historical commitment as it was made, and the `superseded_by::` edge tells them a successor exists. Renaming the old Decision would silently break every citing wikilink (wiki tooling does not track renames universally), and editing the old Decision's body to reflect the new commitment would erase the historical record.

The commitment **keeps the historical trace traversable**. Supersession chains are first-class graph structure: any reader can follow `supersedes::` backward from the current commitment to the original, reading the evolution of the project's thinking on an issue. The chain carries the project's memory of how its commitments have changed — which alternatives were weighed and rejected at the time, what forcing cases prompted revisits, what conditions proved to have triggered. A rename-based approach would collapse the chain into a single file whose history lives only in git log; a supersession-based approach puts the history in the graph itself, where it is as navigable as any other relation.

The commitment distinguishes Decision revision from other forms of update. A typo fix, a clarification, an improved annotation — these are edits to the existing Decision, not revisions to its commitment. The commitment that distinguishes the two is: "Does this change what the Decision commits to?" If yes, it is a supersession; a new Decision is seeded and the old one is updated with `superseded_by::`. If no, it is an edit to the existing file. The supersession-vs-edit distinction is what keeps the chain's signal clean — it tracks commitment changes, not textual changes.

The commitment applies even when the new commitment narrows or splits the old. If a bundled Decision is later understood to have been two commitments with asymmetric revisit criteria, the correct response is a new Decision that supersedes the bundled one plus two sibling Decisions, each conforming to Decision Form Contract. The bundled Decision remains in the graph with its `superseded_by::` edge pointing at the new structure; the split is recorded, not erased. Splitting by editing the old Decision into one of the two new roles would strand the other role.

## Alternatives Considered

**Rename the old Decision to mark obsolescence.** When revising, rename the old file (`<Old Commitment>.md` → `<Old Commitment> (superseded).md`) and write the new Decision under the old file's previous name. Rejected because renaming breaks every existing wikilink citation. Wiki tooling does not track renames across the wiki-graph boundary; a link from a Pattern or Conviction to the old Decision's previous name produces a ghost link after the rename. The renaming-as-obsolescence-marker approach trades citation stability for a small filename-level signal that the `superseded_by::` edge provides better.

**Edit the old Decision in place to reflect the revision.** Keep one file per commitment — when the commitment changes, update the file. Rejected because it erases the historical record. A reader encountering the file after the edit sees the new commitment with no trace of the old; the project's thinking becomes a single point-in-time rather than an evolution. The supersession chain's value is the traceability — the ability to see what was committed, when, and what replaced it — which in-place editing destroys.

**Soft deletion of superseded Decisions.** Move superseded Decisions to an `archived/` subfolder and break their wikilink resolution deliberately, to signal that the commitment is no longer active. Rejected because active wikilink resolution is load-bearing for historical reference. A reader following an old citation needs to arrive at the historical commitment; a reader following the supersession chain forward from a current Decision needs to find the predecessors. Deliberately broken resolution would serve neither use case, and the `has_curation::[[Superseded]]` annotation inside the file (when the curation vocabulary grows to include it) already carries the state information the folder move would signal.

## What Would Change It

The commitment would be revisited under one condition.

**Historical supersession chains become noise.** If the graph accumulates so many superseded Decisions that the chains dominate the Relations tier — where a reader traversing a Decision's edges spends disproportionate attention on superseded ancestors rather than on current relations — the commitment's record-keeping benefit would trade off against its readability cost. A mitigation (`has_curation::[[Superseded]]` enabling filtered views, curation passes collapsing long chains into summary nodes) would likely arrive before the commitment itself is revisited. The current corpus has zero supersession chains; no pressure exists. The revisit condition is latent, not current.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine is what makes `supersedes::` and `superseded_by::` traversable structural edges rather than prose claims about Decision evolution. Without the spine, supersession would live in git history or file comments; with it, the chain is first-class graph structure.

- grounded_in::[[Name Decisions by Action Verb or Role Declarative]]
  - The filename-shape commitment is what makes the new Decision's filename differ from the old one's. A revised Decision's new commitment is phrased as a new action-verb lead or declarative; the filename reflects the commitment. The filename-shape rule and the supersession rule compose — the shape ensures the new name differs meaningfully from the old.

- informs::[[Decision Form Contract]]
  - Decision Form Contract's Superseding Requirement carries the thin enforcement clause pointing at this Decision.
