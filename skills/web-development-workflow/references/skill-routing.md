# Specialist routing

Read only the rows relevant to the current stage, then the selected specialist's entrypoint and required references. Explicit user instructions and approved project decisions govern the work. One specialist drives the design; review and technical checks complement it. A list of skills is not a requirement to run all of them.

## Select by changed behavior

| Need | Preferred route when available | Bundled or project-native fallback | Completion evidence |
| --- | --- | --- | --- |
| Tiny copy, spacing or isolated bug fix | Existing project patterns; skip broad design skills | Direct focused edit | Affected behavior and rendered area checked |
| New visual direction or substantial UI refinement | Explicit choice, project preference, or suitable existing `impeccable`, `emil-design-eng` or `ui-ux-pro-max`; choose one | `workflow-interface-design`; otherwise actual brief, DESIGN.md and a bounded rendered prototype | Approved direction, realistic content and responsive screenshots |
| Interface/accessibility review | `workflow-interface-review`, or existing `web-design-guidelines` when its source is available | Semantic HTML, keyboard/focus, contrast, zoom/reflow, states and content checks against project requirements | File/element findings plus rendered and interaction checks; scan limits stated |
| Mobile web/PWA behavior | Existing `mobile-native` or bundled `workflow-mobile-web` | Target relevant viewport, touch, keyboard, safe-area and scrolling issues directly | Emulation plus actual-device evidence for device-specific claims |
| Requested animation | `animate` for implementation; `review-animations` for critique; `animation-performance` for observed jank | Existing CSS/motion tokens and reduced-motion path | Purpose, interruption, reduced-motion and observed performance |
| Requested cinematic composition | `gpt-taste` only when the actual brief calls for its style | Primary design route | Fit with approved density, content, motion and access needs |
| React/Next.js performance | `vercel-react-best-practices` with its supporting rules and compatible framework version | Project profiler, production bundle and official framework docs | Measured bottleneck and result; skip on other stacks |
| Browser verification | Usable existing browser integration, project E2E setup, `playwright` or `playwright-interactive` | User-operated preview with exact steps and evidence owner | Actual navigation/interactions on the named candidate; installed files alone prove nothing |
| Uncertain library/provider contract | Available Context7 integration or current official docs | Official documentation in a browser/search tool | Applicable version and source; a configured server is not proof of a successful query |
| API/backend boundary | Relevant `api-design` or `backend-patterns`; `security-review` for auth, permissions, uploads, secrets or sensitive data | Inspect project contracts, validate trusted inputs and exercise positive/denied paths | Actual runtime, persistence and access behavior |
| Supabase/database work | Available Supabase product skill; Postgres guidance only for actual database changes | Current official provider docs and project migrations/policies | Authorized and denied access, persistence and recovery on the intended environment |

The public plugin bundles three namespaced adapters with licensed source references. Their source snapshots and scope are documented in the package's third-party notices. Advanced skills are optional and are not automatically installed. A standalone coordinator may have none of the adapters; use its existing catalogue and report gaps.

## Verify availability without changing the setup

1. Check the current session catalogue for the selected name. Duplicate names are not merged; identify which copy and resources will be used. Existing disk files may require a new chat to appear in discovery.
2. Read the selected entrypoint and check its referenced resources. Resolve a skill's own root correctly; do not execute a path containing an unresolved plugin-root placeholder.
3. Verify the relevant tool/runtime separately. A launcher can download an engine, and a Playwright wrapper can invoke a package runner. Do not run a downloader or installer just to test availability. Prefer the project's installed tools or an already usable browser. A required runtime is untested until it actually succeeds on this task.
4. Report a missing selected skill with its intended role and fallback. Missing optional guidance does not block equivalent project-native work. Missing required execution evidence stays Blocked/Not run; do not convert it to Passed because a build or mock passed.

If Python is already available, run `scripts/check_skills.py --json` from this skill's directory to inventory known candidates. It checks bundled siblings, `~/.agents/skills/` and `~/.codex/skills/`. Supply repeated `--skill-root` paths to inspect only specified roots. It reads registered candidate files and prints a report; it performs no network access, installation or tool execution. Output includes local paths, so keep the report private unless deliberately redacted. Disk status, session visibility and runtime evidence are separate fields; the last two remain unknown/not tested in this helper.

## Apply source guidance in context

- Read one primary design entrypoint, then only supporting references needed for that task. Do not load every style database or motion skill.
- The bundled adapters define how their preserved upstream text applies. Do not infer a real client's history, force an aesthetic, invent content or add a backend from an example.
- Native buttons/links already have keyboard behavior. Preserve useful autofill, user zoom, selectable content and native navigation. Scope touch/scroll overrides to an observed need. Treat list-size thresholds and style conventions as heuristics.
- An existing Impeccable installation may require its native engine and platform launcher. Use its documented fallback when the runtime is unavailable, and state that its context step did not run. Do not replace the installation or pretend a fallback executed the engine.
- UI-UX Pro Max can require local Python/data and root resolution. React advice requires the actual React version. Browser automation requires a successful browser operation. Skill presence establishes none of these.
- Use current official documentation when a changing API or standard matters. Record whether a review used a pinned source snapshot or a freshly retrieved source. Do not call the bundled snapshot the latest without verification.
- Jev is optional for a bounded semantic judgment. Deterministic rules, calculations, execution and publication permission remain with code and the user; no advisory score substitutes for a browser or access-control check.

## Record only useful routing evidence

For substantial work, add a short note to the existing verification record: selected role and skill/copy, missing requirements and fallback, tools actually exercised, and any blocked check with its owner. Keep task progress in the existing task table. For a small fix, the final result and check summary are enough. Do not create a second skill-status ledger per project.
