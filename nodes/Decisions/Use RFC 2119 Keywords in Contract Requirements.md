---
created: 2026-04-19
tagline: Contract Requirements use RFC 2119 keywords — MUST, MUST NOT, SHOULD, SHOULD NOT, MAY — to state the normative obligation
brief_summary: A commitment that every Contract's Requirements section uses RFC 2119 keywords to carry the normative weight of each rule. MUST and MUST NOT mark unconditional obligations. SHOULD and SHOULD NOT mark strong defaults that may be overridden with stated cause. MAY marks permitted options. The keywords make each rule's weight unambiguous to both human readers and any validator that reads the Requirements section, and they import a well-known normative vocabulary rather than inventing new terms.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Use RFC 2119 Keywords in Contract Requirements

Every Contract's Requirements section uses RFC 2119 keywords — **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY** — to state the normative obligation of each rule. A rule without an RFC 2119 keyword is not a Requirement; it is prose that may belong elsewhere in the Contract (the body above the Requirements section, an annotation on a related edge) but does not carry Requirement-level normative weight.

## Why

The commitment provides **machine-parseable normative weight**. A build-time or curation-time validator reads the `## Requirements` section, extracts each sub-section's rule, and identifies the RFC 2119 keyword to know whether the rule is an unconditional obligation (MUST), a strong default (SHOULD), or a permitted option (MAY). Without the keyword vocabulary, the validator would have to interpret natural-language phrasing ("the filename should end with..." vs. "the filename needs to end with..." vs. "ensure the filename ends with...") — a task that produces false positives and false negatives even with careful pattern matching. RFC 2119 is the solved version of this problem: a small, well-known vocabulary with precise semantics.

Beyond machines, human readers benefit from the same unambiguity. "The filename should be UTF-8 markdown" could mean the author is recommending UTF-8 or stating a hard requirement; "MUST be UTF-8 markdown with `.md` extension" is unambiguous. The cost of learning RFC 2119's five keywords is small (the vocabulary fits in a paragraph); the benefit compounds across every Contract, every Requirement, and every author who reads them. The keywords themselves communicate the weight — a reader scanning a Requirements section for MUST-level rules can filter them at a glance.

Using RFC 2119 rather than inventing new normative terms preserves **interoperability with the wider specification community**. Contracts are a local form of specification; RFC 2119 is the specification-world's standard for normative weight. A reader arriving at a Deep Context Contract with RFC experience recognizes the vocabulary immediately; a validator built on RFC 2119 parsing works without adaptation. Inventing local synonyms (local-MUST, local-MAY, local-SHOULD-unless-X) would produce a vocabulary only Deep Context knows, and every tool that reads Contracts would have to learn it. The standard is cheaper than the invention.

The commitment does not require every sentence in a Contract to contain an RFC 2119 keyword. Bodies, annotations, and explanatory prose use normal English. The keywords appear specifically inside `### <requirement name>` sub-sections to mark the rule each sub-section states. A sub-section may contain multiple MUST/SHOULD/MAY clauses where the requirement has multiple aspects; the keyword vocabulary scales with rule complexity.

## Alternatives Considered

**Prose-only obligation.** Write Requirements in natural English without a fixed keyword vocabulary, relying on authors to make weight clear from phrasing. Rejected because natural-English normative weight is systematically ambiguous. "Must" in English is weaker than RFC 2119's MUST (English "must" is sometimes recommendation); "should" in English is weaker than RFC 2119's SHOULD (English "should" is often a soft suggestion). The vocabulary exists specifically because natural-English weight markers failed the specification-writing community's accuracy standards.

**Locally-invented normative vocabulary.** Define Deep Context-specific weight terms (REQUIRED, RECOMMENDED, PERMITTED) with precise semantics. Rejected because the invented vocabulary would duplicate RFC 2119 without the interoperability benefit. Any tool reading Contracts would have to learn the local vocabulary; any author coming from another specification tradition would have to translate. RFC 2119 is the Pareto-optimal choice — it solves the same problem at zero invention cost.

**Weight-implicit Requirements.** Let the sub-section heading signal weight (e.g., `### filename (required)` vs. `### filename (recommended)`). Rejected because the heading becomes an awkward carrier of normative weight and cannot mark the weight of individual clauses within the sub-section. RFC 2119 operates at clause granularity, which matches how rules are actually written — a single sub-section often mixes MUST clauses (unconditional) with SHOULD clauses (defaults) with MAY clauses (options).

## What Would Change It

The commitment would be revisited under one condition.

**RFC 2119 creates author friction without validator payoff.** If the project produced Contracts consistently and never built a validator that parsed the Requirements section — or if the validator proved impractical because Contract Requirements contained too much natural-language variation to parse reliably — the normative-keyword discipline would be carrying author-time cost without the machine-parseable benefit. The rule would still serve human readers' unambiguity, but the main load-bearing rationale (validator-readable normative weight) would have weakened. The revisit would move toward a softer form — "requirements SHOULD use normative keywords where weight is load-bearing" — rather than removing the keywords entirely. No pressure of this kind has emerged; Contracts accumulate and the RFC 2119 discipline has been cheap to maintain.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The named-edge spine lets Contract Requirements reference their grounding Decisions by typed edge. The keyword discipline works inside a sub-section; the grounding Decision reference lives in the sub-section's body or the Contract's Relations. The two conventions compose — keywords mark obligation, edges mark derivation.

- informs::[[Contract Form Contract]]
  - Contract Form Contract's Requirements section Requirement carries the thin enforcement clause pointing at this Decision.
