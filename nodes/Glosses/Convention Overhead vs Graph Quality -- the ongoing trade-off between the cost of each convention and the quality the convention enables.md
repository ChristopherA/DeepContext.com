---
created: 2026-04-22
tagline: The ongoing trade-off between the cost each convention imposes on contribution and the quality that convention enables
brief_summary: A named tension the project holds open rather than collapses. Every new Contract, Decision, or predicate raises the bar for contribution; every absence of structure admits more drift. No general rule resolves the trade-off; the judgment is made per convention, weighing the overhead the convention imposes (authoring friction, cognitive load, machinery to maintain) against the quality it enables (legibility, drift prevention, navigability). Contracts and other structural nodes carry `contends_with::[[Convention Overhead vs Graph Quality]]` edges when their existence visibly navigates this trade-off -- the edge declares the tension as acknowledged rather than ignored.
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Convention Overhead vs Graph Quality

The ongoing trade-off between the cost of each added convention -- the authoring friction it imposes on contributors, the cognitive load it adds to readers, the machinery it introduces that must be maintained -- and the quality improvement the convention is meant to produce -- the legibility it adds, the drift it prevents, the navigability it preserves. Each convention the project considers sits somewhere on this trade-off; the project's practice of deciding when to add, revise, or retire a convention is the working-out of this tension case by case.

The phrase captures a tension the project holds open rather than collapses. Every new Contract, Decision, or predicate raises the bar for contribution; every absence of structure admits more drift. No general rule resolves the trade-off; the judgment is made per-case, weighing the specific convention's overhead against the specific quality gain it is expected to produce. Contracts and other structural nodes carry `contends_with::[[Convention Overhead vs Graph Quality]]` edges when their existence visibly navigates this trade-off -- the edge declares the tension as acknowledged rather than ignored.

The project does not treat one side of the trade-off as paramount. The scion publication model depends on the repository's surface staying small enough to understand; the practice's durability depends on the conventions being strong enough to survive drift. Both pressures are real. The trade-off is where the project does its architectural thinking -- every Contract with a `contends_with::` edge to this concept is a node whose author considered the cost alongside the benefit and decided the benefit carried the day, with the `contends_with::` edge acknowledging that a future reader may weigh the same trade-off differently.

## Relations

- grounded_in::[[Adopt Minimum-Viable-Architecture Stance]]
  - The MVA stance operationalizes this trade-off at the capability layer: ship the minimum architecture that lets the practice run, defer until use surfaces what to add. This Gloss names the underlying tension the stance navigates; the Decision names the discipline the project applies to the trade-off in first-cycle work.
