---
created: 2026-04-19
tagline: Filenames use ASCII hyphens only; typographic em-dashes and en-dashes are prohibited; the double-hyphen separator is two ASCII hyphens
brief_summary: A bundled commitment that filenames carry only ASCII hyphens — no typographic em-dashes or en-dashes, and where a visual dash is needed in a filename, the double-hyphen separator `--` is used. The two rules share a Why about filename portability across shells, grep, cross-platform filesystems, and wiki tooling. The bundle includes the Gloss Form Contract's `<Concept> -- <definition>` separator pattern, which is a specific application of the double-hyphen rule.
---

- conforms_to::[[Decision Form Contract]]
- has_commitment::[[Firm Commitment]]
- decided_on::2026-04-19
- in_domain::[[Deep Context Architecture]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]

# Use ASCII Dashes in Filenames

Every filename in the node graph uses ASCII hyphens (`-`) only. Typographic em-dashes (`—`) and en-dashes (`–`) MUST NOT appear in filenames. Where a visual dash is needed in a filename — between a concept and its gloss definition, between parts of a compound title, or as any author-chosen separator — the form is a double ASCII hyphen (`--`). The commitment covers both the exclusion of Unicode dashes and the adoption of `--` as the canonical visual-dash substitute.

## Why

The commitment provides **cross-tool portability** for the filename layer the graph's wikilink resolution depends on. Filenames travel through shells, grep, cross-platform filesystems, wiki tooling, build pipelines, and version-control surfaces. ASCII hyphens pass through every layer unchanged; typographic dashes do not. The failure modes are concrete:

**Shell escaping.** Unicode dashes require UTF-8-aware quoting in zsh, bash, and most shells. A filename with `—` in it must be single-quoted or escaped — a mismatch between the user's editor (which inserts the Unicode character) and the shell's quoting rules produces commands that either fail silently or operate on the wrong file. The double-ASCII-hyphen alternative has no escaping requirement.

**Grep and content search.** `grep`, `ripgrep`, and similar tools match filenames and content by byte sequence. A user searching for a concept by its filename types `-` on the keyboard; the tool's match against `—` in the filename fails unless the user knows to type the Unicode character. The common case — someone looking for a node by name — hits a false negative every time.

**Cross-platform filesystem case.** Some filesystems normalize Unicode inconsistently (macOS HFS+ and APFS normalize NFC vs NFD differently than Linux filesystems); a filename created with `—` on one platform may appear with a different byte sequence when cloned or synced to another. Git usually catches these, but edge cases produce phantom files. ASCII hyphens avoid the normalization layer entirely.

**Wiki-tool rendering and link resolution.** Obsidian, GitHub's markdown renderer, and most wiki tooling handle Unicode dashes in filenames but not uniformly. A user typing `[[Concept — definition]]` may or may not resolve to `Concept — definition.md` depending on the tool's input-normalization rules; the resulting ghost-link confusion is indistinguishable from the file genuinely not existing.

The double-hyphen separator (`--`) is the canonical substitute. It is visually clear — a reader scanning a folder sees `--` as a separator, not as two accidental hyphens — and it collides with no other filename convention in use. The Gloss Form Contract's `<Concept> -- <one-clause definition>.md` pattern is a specific application: the separator makes the definition visible in the filesystem without opening the file, and the space-hyphen-hyphen-space (` -- `) spacing prevents collision with hyphenated words on either side.

The two rules bundle because they share this Why — filename portability — and because rollback is bundled. Reversing the exclusion of Unicode dashes without also reversing the adoption of `--` would leave the Gloss Form's separator orphaned; reversing `--` without reversing the exclusion would leave the graph needing a separator and having nothing portable to use. They are adopted and revisited together.

## Alternatives Considered

**Accept typographic dashes in filenames.** Let authors use `—` or `–` where they want visual emphasis. Rejected because the portability failures are not hypothetical — they show up in every user's first week of shell interaction with the graph. The typographic benefit (a visually elegant separator in folder listings) is consumed only by the reader who is already inside their editor; the cost is paid by every shell, search, and sync interaction. The cost-benefit is one-way.

**Single hyphen as separator.** Use a single `-` as the concept-definition separator in Gloss filenames. Rejected because it collides with hyphenated words. A gloss for "well-being" or "self-sovereign identity" would produce `Well-Being -- concept about wellbeing.md` or, with a single-hyphen separator, `well-being - concept.md` — and the renderer, grep, and reader cannot reliably tell which hyphen is the separator. The double hyphen is visually distinct and collision-free.

**Unicode dash with a build-step normalization.** Allow typographic dashes in source and normalize them to ASCII at build or sync time. Rejected because it violates plain-markdown expressibility — the filename in the working tree differs from the filename the build produces, and any reader who does not run the build sees the wrong filename. The [[Adopt Wikilinks and Named Edges]] commitment's plain-markdown floor forbids build-step-dependent structural identity.

## What Would Change It

The commitment bundles two rules; the revisit conditions converge.

**Shells and grep reliably handle Unicode dashes.** If zsh, bash, and POSIX-compatible tools adopted transparent Unicode-dash handling across their quoting, pattern-matching, and glob-expansion surfaces — and if cross-platform filesystems converged on a single normalization — the portability failure that motivates the exclusion would weaken. This is a shift at the tooling layer the graph cannot drive; no current pressure indicates the shift is coming.

**Wiki-tool link resolution normalizes dashes in wikilink input.** If Obsidian, Logseq, and the common GitHub-style wiki renderers all adopted consistent input-normalization such that `[[Concept — definition]]` and `[[Concept -- definition]]` resolved to the same file, one class of failure would disappear. The shell-interaction failure would remain — tooling cannot fix what the user sees when they run `ls`.

The double-hyphen separator half of the commitment would be revisited if `--` ever became reserved or reinterpreted by a tool in the path (shell, wiki renderer, filesystem). No current conflict exists; the separator is uncommon enough in other conventions that collision is unlikely.

## Relations

- grounded_in::[[Adopt Wikilinks and Named Edges]]
  - The wikilink spine resolves by filename. Filename portability is substrate for that resolution — every layer between the user and the graph must read the filename consistently. This Decision is the specific filename-portability commitment the substrate requires.

- informs_downstream::[[Markdown Node Contract]]
  - Markdown Node Contract's file-form Requirement carries the thin enforcement clause pointing at this Decision.

- informs_downstream::[[Gloss Form Contract]]
  - Gloss Form Contract's filename pattern (`<Concept> -- <one-clause definition>.md`) is a specific application of the double-hyphen separator rule. The Gloss contract's filename requirement is grounded in this Decision; the double-hyphen separator is what makes the definition-in-filename visible in folder listings while remaining portable across tools.
