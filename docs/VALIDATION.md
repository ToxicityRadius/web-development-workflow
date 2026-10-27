# Validation scope

The offline validator checks concrete package invariants: manifest and marketplace identity, contained relative paths, referenced local files and page anchors, the complete six-template set, the MIT license, PDF fingerprint, all 16 extracted page fingerprints, and common accidental secret/workstation-path patterns.

Before publication, the public PDF was also compared with the local source using pypdf: all 16 pages retained identical normalized extracted text. Its metadata was replaced for public distribution. The separate portfolio reference and personal project records are excluded.

Skill frontmatter and interface metadata were checked with the bundled Codex skill validator and YAML parser. These tools are not required to use the published plugin or run its standard-library integrity check.

GitHub Actions runs the offline check on Linux and Windows. A green run establishes package integrity on those runners. It does not establish automatic skill activation, a completed interactive plugin installation, model instruction-following accuracy, or the quality of a website built using the workflow.

Representative future behavior checks include a tiny UI fix, a substantial new project, a conflicting historical design prompt, a mocked authentication flow, and a request to prepare a release without permission to publish. Evaluate the resulting actions and evidence rather than matching the wording of the instructions.
