# Web Development Workflow

A Codex plugin for planning, building, reviewing, and preparing web projects for release. It bundles a **16-page planning guide**, a searchable page-indexed version, and editable templates with the workflow skill.

```text
Clarify -> Design -> Build -> Verify -> Preview -> Approval -> Publish
```

Start from the project's existing stack and approved design. Build complete user journeys, inspect the rendered result, and keep evidence tied to the actual release candidate. Use only the documentation and checks that the change needs.

## Install in Codex

Add the GitHub repository as a plugin marketplace, then install its plugin:

```powershell
codex plugin marketplace add ToxicityRadius/web-development-workflow --ref v1.0.0
codex plugin add web-development-workflow@toxicityradius-workflows
```

Open a new project chat and invoke the skill:

```text
Use $web-development-workflow to continue this project.
Read the relevant parts of the bundled planning guide, ask only questions
that change the result, preserve the approved design, and prepare a
verified release for my publishing approval.
```

The marketplace reference above pins the first release. Use `--ref main` instead if you deliberately want the development branch. Available plugin commands and installation surfaces depend on the installed client; consult [OpenAI's plugin documentation](https://developers.openai.com/plugins/build/plugins).

### Standalone skill

You can also copy the entire [skills/web-development-workflow](skills/web-development-workflow) folder into your user skill directory, typically `~/.agents/skills/`. Keep its `references/` and `assets/` folders alongside `SKILL.md`. Use one installed copy rather than duplicating the same skill through both methods.

## What's included

| Resource | Purpose |
| --- | --- |
| [Workflow skill](skills/web-development-workflow/SKILL.md) | Stage selection, decision ownership, complete slices, verification and release preparation |
| [Planning PDF](skills/web-development-workflow/references/planning-guide.pdf) | Six connected planning documents explained across 16 pages |
| [Searchable guide](skills/web-development-workflow/references/planning-guide.md) | Text from every page, with stage-to-page links |
| [Editable templates](skills/web-development-workflow/assets/templates/README.md) | Product, technical, flow, design, data and implementation records |
| [Release checklist](skills/web-development-workflow/assets/templates/RELEASE_CHECKLIST.md) | Candidate, checks, evidence, remaining issues, approval and recovery |
| [Worked example](skills/web-development-workflow/assets/templates/WORKED_EXAMPLE.md) | One hypothetical feature traced through all six documents |

The skill consults the relevant guide pages before planning, flow/design/data decisions, implementation and verification. It reuses material already read in the task instead of loading the whole PDF after every small edit.

## How it works

1. Inspect the repository, instructions, current behavior and working tree. Identify the user task, scope, exclusions and observable acceptance conditions.
2. Resolve only the decisions needed for the next complete slice. Keep one design authority and one current task-status table.
3. Use a suitable primary design workflow. Add a specialist for a concrete need, while preserving approved project choices.
4. Build relevant success, failure and recovery paths with truthful content, responsive reading order, keyboard/touch access and motion alternatives.
5. Run the existing focused tests and production build. Inspect affected rendered screens, interactions and representative devices. Keep mocks, historical checks and real integrations distinct.
6. Prepare a candidate-specific review packet with preview, results, remaining issues and recovery procedure. Ask for production publishing approval, then check the actual public result after an approved release.

For a small edit, use the relevant parts without creating six documents. A static site does not need an invented backend, account system or analytics. Explicit user instructions and project decisions take precedence over examples.

## Requirements and boundaries

- The workflow needs a client that supports these skill/plugin files and the tools needed for the actual project.
- The plugin itself has no MCP server, lifecycle hooks, API key requirement or automatic deployment action.
- Named design tools and Jev are optional examples, not bundled dependencies.
- Production approval is an instruction policy, not a hosting permission lock.
- A completed template or automated accessibility scan does not certify a website. Keep unexecuted checks explicit.

## Validate the package

Python 3.10 or later is sufficient for the repository's offline integrity checks:

```powershell
python scripts/validate.py
```

The validator checks manifest/catalog consistency, local references, PDF and page-text fingerprints, template presence, and accidental secret/path leakage. CI runs the same checks on Linux and Windows. See [validation scope](docs/VALIDATION.md) for the limits of those checks.

The public PDF preserves all 16 pages and extracted content. Authoring metadata was replaced for public distribution; the source fingerprint records that transformation. The separate portfolio PDF is not included.

## Sources and contributing

See [sources](docs/SOURCES.md) for the guide's references. To contribute, open an issue with a concrete workflow problem or a small pull request with its validation evidence. Keep examples hypothetical, preserve explicit user choices, and avoid adding mandatory tools or paperwork without a demonstrated need.

Licensed under the [MIT License](LICENSE).
