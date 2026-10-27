# Validation scope

The standard-library offline validator checks manifest/marketplace identity, contained paths, relative links and guide-page anchors, all four skill entrypoints and interface files, discoverable adapter policies, routing aliases/resources, the six-template set, original third-party licenses/text against the pinned lock record, adapter MIT licenses, the combined SPDX expression, PDF fingerprint, all 16 extracted page fingerprints, and common accidental secret/workstation-path patterns. Hash validation detects drift from the reviewed record; it is not independent proof of upstream authenticity or a comprehensive secret scanner.

Before publication, the public PDF was also compared with the local source using pypdf: all 16 pages retained identical normalized extracted text. Its metadata was replaced for public distribution. The separate portfolio reference and personal project records are excluded.

Skill frontmatter and interface metadata were checked with the bundled Codex skill validator and YAML parser. These tools are not required to use the published plugin or run its standard-library integrity check.

The unit tests exercise missing skills without installation, directory aliases, duplicate roots/copies, absent supporting resources, wrong frontmatter names, unreadable files and Windows-compatible text encodings. Isolated negative package fixtures remove a license, alter pinned source, escape a routing directory and add a broken link. They do not mutate the checkout. The availability helper never tests activation or tools; its runtime field remains `not_tested` even for present files.

GitHub Actions runs the validator and tests on Linux and Windows. A green run establishes those checks on the specific revision and runners. It does not establish automatic skill activation, a completed interactive plugin installation, model instruction-following accuracy, a working specialist engine/browser, or the quality of a website built using the workflow.

The [routing scenarios](ROUTING_SCENARIOS.md) define expected behavior for later agent-level evaluation. They were reviewed against the instructions during authoring; they are not executed model trials. No comparative performance gain or accessibility certification is claimed. A fresh-chat invocation and an actual project run are needed to assess behavioral results.
