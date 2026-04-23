---
created: 2026-04-19
tagline: A Reference body distinguishes what this project adopts from the source from what it deliberately doesn't
brief_summary: A commitment that every Reference body distinguishes what this project has adopted from the source from what it has deliberately declined to adopt. The distinction may appear as explicit sub-headings (`### Adopted`, `### Not adopted`) or as prose paragraphs whose role is clear from context. The rule makes adoption an active choice the Reference records, not vague acknowledgment that the source influenced the project. A Reference that gestures at the source without naming the adoption is a bibliography entry, not a load-bearing Reference.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Provisional Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Distinguish Adopted from Not-Adopted in References

Every Reference body distinguishes **what this project has adopted from the source** from **what it has deliberately not adopted**. The distinction may appear as explicit sub-headings (`### Adopted`, `### Not adopted`) or as prose paragraphs whose role is clear from context. The adoption side names the specific moves, ideas, predicates, or structural choices the project has drawn forward; the not-adoption side names the specific moves the project weighed and declined, with a one-sentence reason. Active adoption is the Reference's claim; passive acknowledgment ("we were influenced by this source") is not.

## Why

The commitment makes **adoption an active choice**, not vague acknowledgment. A Reference exists because the project draws specific content from the source — predicates, naming conventions, body structures, grounding arguments. The Reference's body is where the drawing is recorded: what was adopted, in what form, how it landed in this graph. A Reference that summarizes the source without naming the adoption is functionally a bibliography entry — it tells the reader the source exists but not what the project took from it.

The not-adopted side is **equally load-bearing**. A source that shaped the project's thinking by influencing some choices and not others is legible only when both sides are named. A Reference recording only the adopted content leaves the reader to guess whether the project adopted the source wholesale; the explicit not-adopted side prevents the guess. "We adopted the filename-carries-definition pattern; we did not adopt the fixed global vocabulary approach" tells the reader both what the source contributed and what the project chose to do differently. Each half sharpens the other.

The distinction makes the Reference **accountable to the source's actual content**. An author drafting a Reference without the distinction can produce a body that sounds like adoption but describes influence generally. Forcing the explicit split requires the author to look at the source's specific claims, decide which ones the project took, which ones it did not, and say so. The discipline produces Reference bodies that name concrete moves rather than rhetorical acknowledgments.

The rule does not require a specific section structure. A short Reference where both sides are clear in context may use prose paragraphs. A long Reference with many adopted and not-adopted moves may use `### Adopted` and `### Not adopted` sub-headings. A Reference that is near-full adoption may frame the body as adoption with a brief "the project does not follow X from the source" paragraph; a Reference that is largely not-adopted may frame it the other way. The structural flexibility is deliberate — the discipline targets the distinction, not a template.

## Alternatives Considered

**Adoption-only bodies.** Let References name what the project adopts without also naming what it declines. Rejected because one-sided adoption bodies drift toward influence-acknowledgment. A Reference saying "this source shaped our thinking on X" can cover any amount of actual adoption, from wholesale import to incidental influence; the reader cannot tell what specifically the project took. Requiring the not-adopted side forces the author to draw a specific line.

**Adoption in body, not-adopted in Alternatives of downstream Decisions.** Let adoption live in the Reference body, and push "what the source suggests but we didn't do" into the Alternatives Considered sections of specific downstream Decisions. Rejected because the structure fragments the source's contribution across many Decision nodes, and each Decision names only what that Decision rejected. A reader wanting the full picture of what the project took from and declined from one source has to read every downstream Decision. The Reference body is the right place to give the full picture in one location.

**Implicit not-adopted via omission.** Let References describe only adoption; treat everything not described as implicitly not-adopted. Rejected because omission is ambiguous. A reader cannot distinguish "the source argued for X but the project declined" from "the source argued for X but the Reference body didn't mention it, not because the project declined but because the author didn't consider X load-bearing." Explicit not-adopted content resolves the ambiguity.

## What Would Change It

The commitment would be revisited under one condition.

**Pure inspiration References become common.** If the project accumulates References to sources that genuinely inspired without being drawn from — philosophical influences, aesthetic precursors, motivational corpora — and the "what did we adopt" question has no concrete answer, the rule would force authors to manufacture adoption claims. The revisit would add a third mode: an "influence-only Reference" form where the body narrates the source's role as inspiration without claiming specific adoption. Current References draw specific content from specific sources; the inspiration-only pattern has not emerged.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine lets References inform Decisions, Contracts, and other downstream nodes through `informs_downstream::` edges. The adopted-vs-not-adopted body structure is what makes the `informs_downstream::` edges specifiable — the body names what the Reference informs (the adopted side) and what it does not (the not-adopted side).

- informs_downstream::[[Reference Form Contract]]
  - Reference Form Contract's Body-shape Requirement carries the thin enforcement clause pointing at this Decision.
