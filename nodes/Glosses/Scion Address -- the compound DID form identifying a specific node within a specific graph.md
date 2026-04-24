---
tagline: The compound DID form identifying a specific node within a specific graph
---

- conforms_to::[[Gloss Form Contract]]
- authored_by::[[Deep Context Community]]
- has_lifecycle::[[Seed Stage]]
- has_curation::[[Working Draft]]
- in_domain::[[Deep Context Architecture]]

# Scion Address

A compound DID of the form `did:repo:<sha1>/<repo-relative-path>` that identifies a specific node within a specific DeepContext graph. The `<sha1>` is the graph's own DID — derived from its Open Integrity inception commit and therefore stable across any git host — and the path segment uses the W3C DID-URL path syntax rather than any git-forge's URL convention, so a Scion Address does not embed `/blob/main/` or other host-specific segments.

Concrete examples on this repository:

- The landing page: `did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae/landing.md`
- A specific Decision: `did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae/nodes/Decisions/Adopt%20Scion%20Publication%20Model.md`
- The repo as a whole (no path segment): `did:repo:7eac0b30ce47538930800f563ecfb3cec6e3c5ae`

A Scion Address is not a URL. Browsers today do not resolve `did:repo:` — the Scion Address sits as a canonical identifier waiting for a resolver that walks from the DID to one or more host URLs (GitHub, GitLab, Radicle, self-hosted). Two places in this graph already emit Scion Addresses in anticipation of such resolvers:

- Every rendered page's footer carries the page's own Scion Address in the DID widget, abbreviated for display and full in the `href` and `title` attributes.
- External-link reference definitions may carry a Scion Address in the link's `title` attribute alongside an HTTP URL in `href`, so a reader clicking the link navigates to a working host URL today while the DID sits in the title for a future citation or resolver tool to read:

  ```markdown
  See the Open Integrity inception spec[oi-readme] for the canonical ceremony.

  [oi-readme]: https://github.com/OpenIntegrityProject/core/blob/main/README.md "did:repo:69c8659959f1a6aa281bdc1b8653b381e741b3f6/blob/main/README.md"
  ```

  Both live in the same markdown element; the URL works today, the Scion Address waits for tooling. Neither depends on the other being present.

The Scion Address differs from the plain `did:repo:<sha1>` in scope: the plain form identifies a repository-as-whole (the graph), while the Scion Address identifies a specific node within that graph. When [[Adopt Scion Publication Model]] says a scion "carries one DID across any git host," that DID is the plain form; when a node needs to be cited at page granularity, the Scion Address is the form.

Limitations are named rather than hidden. A Scion Address uses the file's current path; if the file is renamed or moved, the old address no longer resolves to the file at its new location. For most references this is acceptable because paths are stable in practice, but a rename-survives form would need to use the file's blob SHA1 rather than its path. The graph does not commit to that more principled form today; if rename fragility becomes a real problem, the Address syntax may extend.

## Relations

- grounded_in::[[Adopt Scion Publication Model]]
  - The Decision that names the did:repo scheme and makes a scion's DID content-derived. Scion Address is the natural extension to page granularity — if the graph's DID is the SHA1 of the OI inception commit, each page's addressability follows from the repo-relative path within that graph.

- grounded_in::[[Open Integrity Project (Blockchain Commons, 2025)]]
  - The cryptographic specification that makes the repo-level DID content-addressable. Scion Address composes the OI DID with a repo-relative path to produce node-level addressing without importing any specific git-forge's URL conventions.

- composes_with::[[External Node]]
  - When a node in this graph wants to cite a node in another graph, the reference target is an External Node; a Scion Address is one of the forms that target can take (alongside the `[[target]]↗` wikilink with external marker).
