# Web Development Workflow

A Codex plugin for planning, building, reviewing, and preparing web projects for release. It bundles a **16-page planning guide**, searchable page-indexed text, editable templates, and **three small licensed interface adapters**. Optional specialists are selected by task and availability.

```text
Clarify -> Design -> Build -> Verify -> Preview -> Approval -> Publish
```

Start from the project's existing stack and approved design. Build complete user journeys, inspect the rendered result, and keep evidence tied to the actual release candidate. Use only the documentation and checks that the change needs.

## Install in Codex

Add the GitHub repository as a plugin marketplace, then install its plugin:

```powershell
codex plugin marketplace add ToxicityRadius/web-development-workflow --ref v1.1.0
codex plugin add web-development-workflow@toxicityradius-workflows
```

Open a new project chat and invoke the skill:

```text
Use $web-development-workflow to continue this project.
Read the relevant parts of the bundled planning guide, ask only questions
that change the result, preserve the approved design, and prepare a
verified release for my publishing approval.
```

The marketplace reference above pins a release. Use `--ref main` instead if you deliberately want the development branch. Available plugin commands and installation surfaces depend on the installed client; consult [OpenAI's plugin documentation](https://developers.openai.com/plugins/build/plugins). If the same coordinator is already installed as a standalone skill, choose one copy before adding the plugin; duplicate names are not merged.

### Standalone skill

You can also copy the four folders in [skills](skills) into your user skill directory, typically `~/.agents/skills/`. Keep all references, licenses, assets and scripts with their entrypoints. The coordinator alone can use existing specialists and project-native fallbacks; it reports missing adapters instead of installing them. Use one installed copy rather than duplicating the same skill through both methods.

## What's included

| Resource | Purpose |
| --- | --- |
| [Workflow skill](skills/web-development-workflow/SKILL.md) | Stage selection, decision ownership, complete slices, verification and release preparation |
| [Interface design](skills/workflow-interface-design/SKILL.md) | Intentional design grounded in the actual brief; Apache-licensed Anthropic source with an MIT adapter |
| [Interface review](skills/workflow-interface-review/SKILL.md) | Contextual UI/accessibility review using MIT-licensed Vercel guidelines |
| [Mobile web](skills/workflow-mobile-web/SKILL.md) | Scoped phone behavior fixes using MIT-licensed Emil Kowalski guidance |
| [Specialist routing](skills/web-development-workflow/references/skill-routing.md) | Stage selection, capability checks, conflict handling and missing-skill fallbacks |
| [Planning PDF](skills/web-development-workflow/references/planning-guide.pdf) | Six connected planning documents explained across 16 pages |
| [Searchable guide](skills/web-development-workflow/references/planning-guide.md) | Text from every page, with stage-to-page links |
| [Editable templates](skills/web-development-workflow/assets/templates/README.md) | Product, technical, flow, design, data and implementation records |
| [Release checklist](skills/web-development-workflow/assets/templates/RELEASE_CHECKLIST.md) | Candidate, checks, evidence, remaining issues, approval and recovery |
| [Worked example](skills/web-development-workflow/assets/templates/WORKED_EXAMPLE.md) | One hypothetical feature traced through all six documents |

The skill consults the relevant guide pages before planning, flow/design/data decisions, implementation and verification. It reuses material already read in the task instead of loading the whole PDF after every small edit.

## How it works

1. Inspect the repository, instructions, current behavior and working tree. Identify the user task, scope, exclusions and observable acceptance conditions.
2. Resolve only the decisions needed for the next complete slice. Keep one design authority and one current task-status table.
3. Select one primary design workflow: explicit user choice, project preference, a suitable available specialist, then the bundled design adapter. Add review, mobile, motion or technical guidance only for a concrete need.
4. Build relevant success, failure and recovery paths with truthful content, responsive reading order, keyboard/touch access and motion alternatives.
5. Run the existing focused tests and production build. Inspect affected rendered screens, interactions and representative devices. Keep mocks, historical checks and real integrations distinct.
6. Prepare a candidate-specific review packet with preview, results, remaining issues and recovery procedure. Ask for production publishing approval, then check the actual public result after an approved release.

For a small edit, use the relevant parts without creating six documents. A static site does not need an invented backend, account system or analytics. Explicit user instructions and project decisions take precedence over examples.

## Optional specialists and availability

The core works without third-party accounts, launchers or downloaded engines. Advanced routes are conditional:

- Impeccable, Emil Design Engineering or UI-UX Pro Max can be the primary design workflow when selected and usable. Impeccable may require a native engine; UI-UX search may require Python/data and correct root resolution.
- Motion skills run for actual animation work; cinematic Taste is opt-in.
- Vercel React Best Practices runs only for a compatible React/Next.js project with supporting rules present.
- Browser automation uses the project's existing tests or a usable browser integration. Playwright skill files and a package runner do not prove browser readiness.
- API, security, Supabase and database guidance run only at the affected boundary. Library/provider contracts use available documentation tools or current official documentation.

The [routing guide](skills/web-development-workflow/references/skill-routing.md) names fallbacks and evidence requirements. Keep the current installation and report missing selected skills. The workflow does not install or upgrade specialists, execute their downloaders, or rewrite them to fill a gap. Optional sources and installation entrypoints are linked in the [research report](docs/SKILL_RESEARCH.md); choose installations separately.

With an existing Python installation, the read-only helper can inspect known skill locations:

```powershell
python skills/web-development-workflow/scripts/check_skills.py
python skills/web-development-workflow/scripts/check_skills.py --skill-root skills --json
```

Its statuses describe files on disk. Confirm session discovery and successfully exercised tools separately. JSON output can include personal local paths; keep that report private. Missing optional guidance permits an equivalent fallback; missing required execution evidence remains Blocked/Not run with a manual procedure and owner.

## Requirements and boundaries

- The workflow needs a client that supports these skill/plugin files and the tools needed for the actual project.
- The plugin itself has no MCP server, lifecycle hooks, API key requirement or automatic deployment action.
- Advanced skills, browser tools and Jev are optional, not bundled runtime dependencies.
- Production approval is an instruction policy, not a hosting permission lock.
- A completed template or automated accessibility scan does not certify a website. Keep unexecuted checks explicit.

## Validate the package

Python 3.10 or later is sufficient for the repository's offline integrity checks:

```powershell
python scripts/validate.py
python -m unittest discover -s tests -v
```

The validator checks all four skill entrypoints, manifest/catalog consistency, local references, pinned third-party text/licenses, PDF and page-text fingerprints, template presence, and common accidental secret/path patterns. Tests exercise discovery failures and reject damaged package fixtures. CI runs both on Linux and Windows. See [validation scope](docs/VALIDATION.md) and [routing scenarios](docs/ROUTING_SCENARIOS.md) for their limits. These checks do not measure model behavior or website-quality gains.

The public PDF preserves all 16 pages and extracted content. Authoring metadata was replaced for public distribution; the source fingerprint records that transformation. The separate portfolio PDF is not included.

## Sources and contributing

See [sources](docs/SOURCES.md) for the guide's references and the [selection research](docs/SKILL_RESEARCH.md) for the specialist review. This is a curated, source-reviewed workflow, not a claim that one skill set is universally best. To contribute, open an issue with a concrete workflow problem or a small pull request with its validation evidence. Keep examples hypothetical, preserve explicit user choices, and avoid adding mandatory tools or paperwork without a demonstrated need.

Authored material is [MIT-licensed](LICENSE). Bundled sources retain MIT or Apache-2.0 terms; see [third-party notices](THIRD_PARTY_NOTICES.md) and the [pinned lock record](third-party.lock.json).
