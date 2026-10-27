# Third-party notices

The authored workflow, adapters, templates and helper code are licensed under the [MIT License](LICENSE), copyright 2026 ToxicityRadius. The package also contains the unmodified third-party files below, under their original terms. The combined package is described by the SPDX expression `MIT AND Apache-2.0`; that expression does not relicense an individual source file.

| Adapter | Preserved source | Original terms |
| --- | --- | --- |
| [workflow-interface-design](skills/workflow-interface-design/SKILL.md) | Anthropic Frontend Design, from anthropics/skills | [Apache-2.0](skills/workflow-interface-design/LICENSE.txt) |
| [workflow-interface-review](skills/workflow-interface-review/SKILL.md) | Vercel Labs Web Interface Guidelines | [MIT, copyright 2025 Vercel Labs](skills/workflow-interface-review/LICENSE.txt) |
| [workflow-mobile-web](skills/workflow-mobile-web/SKILL.md) | Emil Kowalski Mobile Native | [MIT, copyright 2026 Emil Kowalski](skills/workflow-mobile-web/LICENSE.txt) |

The original guidance is stored as `references/upstream.md` inside each adapter. Original license files accompany it; each authored adapter also carries an `ADAPTER_LICENSE.txt`. The [lock record](third-party.lock.json) gives the exact repository, commit, upstream paths, source URLs and SHA-256 values. Source text and licenses are retained byte-for-byte. Renaming their local paths is the only packaging transformation. Application rules live in separate adapter entrypoints; they do not edit the original guidance.

No third-party binary, launcher, installer, browser, MCP server or model account is bundled. Names of optional specialists identify compatible routes; they do not imply endorsement, affiliation, installed availability or redistribution of those specialists. See the [selection research](docs/SKILL_RESEARCH.md) for scope and compatibility decisions.
