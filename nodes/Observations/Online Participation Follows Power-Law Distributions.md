---
created: 2026-04-20
tagline: Sustained online communities exhibit power-law distributions of contribution — shape robust across platforms even as absolute percentages vary
brief_summary: An Empirical Observation that sustained online communities consistently show power-law distributions of contribution. A small minority produces most of the content; a larger minority contributes occasionally; the majority lurks. The shape of the distribution is robust across platforms (Nielsen's 90-9-1 formulation, Allen's 99-and-1 refinement for many communities, Wikipedia's measured ~99.8/0.2/0.003, a reported four-tier cascade in a large-scale community from ~300K members to ~30 sustained contributors). Absolute percentages vary with platform, domain, and measurement window; the power-law *shape* is the durable finding, the specific ratios are not.
---

- conforms_to::[[Observation Form Contract]]
- has_epistemic_status::[[Empirical Observation]]
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Online Participation Follows Power-Law Distributions

Sustained online communities exhibit power-law distributions of contribution. A small minority contributes most of the content, a larger minority contributes occasionally, and the majority of the population lurks. The shape of the distribution is robust across platforms; the absolute percentages vary.

## Grounds

Multiple measured sources converge on the power-law shape. Jakob Nielsen's 2006 *Participation Inequality* article formalized the pattern as "90-9-1" — approximately 90% of users lurk, 9% contribute occasionally, 1% contribute most of the content — as a rule-of-thumb drawn from measurement across discussion forums, reviews systems, and early social-web platforms. The ratio is a summary; underlying measurements typically show a smooth power-law curve rather than three discrete tiers, but the three-tier summary is the durable communicable form.

Christopher Allen's 2008 *Power Laws* post refined the ratio for many online communities to a 99-and-1 pattern — roughly one contributor per hundred lurkers rather than one per ten — after observing that Nielsen's 9% tier collapses toward the 1% tier in communities with higher contribution thresholds. Wikipedia's own measured numbers are tighter still: approximately 99.8% read-only, 0.2% occasional editors, and ~0.003% heavy editors at the long tail. The absolute ratios diverge from platform to platform by more than an order of magnitude, but every measured instance shows the power-law shape: a small minority contributes disproportionately, the distribution has a heavy tail, and the gap between the top tier and the rest is large.

A four-tier cascade reported for a large-scale online community (summarized in Allen's 2008 post) supplies a worked example. Approximately 300,000 members produce approximately 30,000 active users, which produces approximately 3,000 regular contributors, which produces approximately 30 sustained contributors over years. Each tier is approximately 10% of the one above it; the scarcity compounds rather than flattens as the filter gets tighter. Four tiers with a consistent ~10× drop-off is the specific shape power-law distributions take when measured with enough dynamic range.

The record's limits are honest: absolute percentages vary with platform, subject domain, and measurement window; power-law *shape* is the durable finding, specific ratios are not. The 90-9-1, 99-and-1, and 99.8-0.2-0.003 formulations are reports from different communities with different thresholds, not competing measurements of the same phenomenon. What they agree on is the distribution's shape; what they disagree on is where the tier boundaries fall for any particular community.

## What Would Revise It

A sustained online community of comparable scale showing a genuinely flat or even contribution distribution — where the top 10% of contributors produce only approximately 10% of the content, or where there is no measurable drop-off between the top contributor tier and the median contributor — would revise the claim that power-law distributions are the robust shape. Small-scale communities (under a few hundred active members) can show flatter distributions because the tail is truncated; the revision would have to come from a community large enough to exhibit a tail and still not show the power-law shape.

A methodological critique that re-interprets observed power laws as measurement artifacts — for example, that the shape appears only because platforms over-count lurkers who would produce if the tooling surfaced their contributions — would also revise the claim at the interpretive layer. The revision would hold if it produced a re-measured distribution, with the measurement artifact corrected, that did not show the power-law shape.

## Sources

- Allen, Christopher. "Power Laws," 2008 — <https://www.lifewithalacrity.com/article/power-laws/>↗. Refines Nielsen's 90-9-1 to 99-and-1 for many online communities; supplies the four-tier cascade worked example.
- Nielsen, Jakob. "Participation Inequality," 2006 — <https://www.nngroup.com/articles/participation-inequality/>↗. Canonical 90-9-1 formulation; draws from measurement across multiple platforms.

## Relations

- informs::[[The Second Cycle of Contribution Happens]]
  - The second cycle occurs against this distribution, not against a flat one. The Aspiration's Current Gap and Progress Recognition sections implicitly assume a power-law shape — a "first-cycle contributor who becomes a second-cycle contributor" is a tier-transition within the distribution, not a movement across a flat population. This Observation makes the distributional assumption explicit.

- informs::[[Wikis Without Curation Drift Toward Write-Only]]
  - The contributor tail below the 1% is the population within which write-only drift compounds. The failure-mode Observation describes what the wiki does without curation; this Observation describes the contributor distribution within which the failure mode unfolds. Write-only drift is not evenly distributed across contributor tiers — it concentrates at the tail.

- informed_by::[[Wikilinks and Named Edges Gist (Christopher Allen, 2026)]]
  - Referenced through Christopher Allen's broader work on collaborative knowledge systems, of which the gist and the 2008 Power Laws post are siblings in the author's corpus.
