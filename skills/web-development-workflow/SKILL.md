---
name: web-development-workflow
description: Coordinate substantial website or web app work using the bundled PDF planning guide, from project decisions through implementation, rendered verification, and a reviewable release. Use for building or continuing a web project, a multi-step feature, or release preparation. For a small isolated edit, use the relevant parts without creating planning documents. Preserve the project's stack and approved design.
---

# Web development workflow

The default is careful, polished work with checks proportional to the change. Prepare and verify a concrete release, then ask the user before production publication. A current explicit user instruction can change that policy. This skill organizes work; it does not grant permission to publish, merge a deployment-triggering branch, send messages, or change accounts.

## Consult the bundled planning guide

The primary reference is the bundled [Website & Web App Planning Toolkit PDF](references/planning-guide.pdf). Its [searchable page-by-page version and page map](references/planning-guide.md) are bundled with this skill; no old chat, external folder or download is needed to read the guide. The six-document toolkit is the only PDF reference for this workflow.

At the start of a substantial new project, read pages 1-2 for document ownership and minimum useful depth. Before making or changing decisions in a stage below, read its relevant source pages through the searchable version. Reuse unchanged material already read in the current task; do not reload the whole PDF for every small edit. For isolated fixes, consult only guidance relevant to the changed behavior. Use the original PDF when diagrams, table alignment, layout or exact source presentation matters.

| Stage | Guide sections |
| --- | --- |
| Plan product scope and acceptance | [Pages 3-4](references/planning-guide.md#pdf-page-03) |
| Resolve technical choices and contracts | [Pages 5-6](references/planning-guide.md#pdf-page-05) |
| Define flows, states and recovery | [Pages 7-8](references/planning-guide.md#pdf-page-07) |
| Design or refine the interface | [Pages 9-10](references/planning-guide.md#pdf-page-09) |
| Define data handling and permissions | [Pages 11-12](references/planning-guide.md#pdf-page-11); a static site can use a short applicability statement |
| Implement, verify and prepare release | [Pages 13-14](references/planning-guide.md#pdf-page-13) |
| Work through a connected example | [Pages 15-16](references/planning-guide.md#pdf-page-15) when useful |

Apply the relevant guidance to the actual project. Explicit user instructions and approved project decisions take precedence over hypothetical examples; a template does not mandate six new documents, a backend, a style system, or an unrequested feature. The guide's examples are not executed evidence. Keep its distinction between implemented and verified. Preserve the bundled PDF content; if its edition changes, regenerate the text/page map and update the [source fingerprint](references/guide-source.json) together.

## Establish the task

Inspect repository instructions, Git status, existing commands, the current brief, and the actual preview or implementation. Preserve unrelated local work. Identify the audience, user decision, smallest complete result, exclusions, and observable acceptance conditions. Infer settled choices; ask early only for missing decisions that change the result. Continue independent work while waiting.

Use the existing document structure. Six planning documents are a reference model, not a prerequisite to editing code. Keep a small fix in the task description. For substantial work, update the existing project records instead of starting parallel plans.

| Decision | Authoritative home, unless the project already specifies another |
| --- | --- |
| Audience, behavior, priorities and acceptance | PRD.md or existing product brief |
| Stack, contracts, runtime and hosting constraints | TECHNICAL_REQUIREMENTS.md |
| Routes, interaction order, states and recovery | APP_FLOW.md |
| Visual tokens, density, references and motion intent | One designated DESIGN.md |
| Actual data, ownership, permissions and retention | BACKEND_SCHEMA.md; brief applicability statement for static sites |
| Current task status, blockers and next actions | One IMPLEMENTATION_PLAN.md task table |
| Executed checks and their limits | Existing verification record; link it from the plan |

Resolve a consequential conflict in its owning document before dependent changes. Make other documents and reusable prompts link to that decision; do not copy competing values. Preserve important history outside the active instructions. A handoff is a pointer to current status, not a second status table.

Optional [starter templates](assets/templates/README.md) are bundled in `assets/templates/`. Copy only missing, useful templates and adapt them to the project. Never overwrite project decisions with blank starters.

## Choose design and tools deliberately

Use one primary design workflow that fits the task and the existing DESIGN.md. Add a specialist only for a concrete gap. Impeccable can guide general UI refinement; motion skills can handle a specified interaction. Taste is appropriate when its cinematic composition is wanted and compatible with the brief. Conflicting skill aesthetics do not override approved project decisions.

A new or ambiguous visual direction deserves a bounded prototype or a few genuinely different options before site-wide implementation. Routine refinements within an approved direction do not need a new approval step. Inspect rendered results and give the user a concrete visual checkpoint when a consequential design choice needs their decision.

Use available tools and existing dependencies first. Check relevant current official provider/library documentation when contracts are uncertain. Keep research proportional; do not migrate the stack or install tools for their own sake. Distinguish configured, available, authenticated, and successfully tested integrations. Jev may advise a bounded semantic judgment; code and observed evidence own exact checks, execution, and permissions.

## Build complete slices

Implement one user-visible journey at a time, including relevant loading, empty, error, success and recovery states. Reuse established components. Keep semantic HTML, keyboard/touch paths, responsive reading order, and static or reduced-motion alternatives intact. Use truthful content and sourced or authorized assets; mark missing content honestly.

For persistent or protected features, include trusted validation, positive and denied access, failed saves, and persistence/recovery checks. For a static site, do not invent a backend, authentication, form, analytics, or schema to fill a template.

## Verify the candidate

Select checks from changed behavior and the intended release, using existing commands. Maximum quality means closing material risks, not adding tests that only mirror implementation. Stop repeating successful checks unless new changes or unresolved concerns justify it.

- Run relevant logic tests and a production build. For deployment changes, check runtime version, production configuration, CI commands and the actual built artifact.
- Inspect affected rendered screens and interactions at representative wide, narrow and short sizes. Include realistic content, required themes and failure states. Compare against the approved reference, fix visible defects, and recheck the changed area.
- Before a substantial UI release, name applicable keyboard/focus, contrast, zoom/reflow, motion-preference, assistive-technology, browser/device and performance checks. Include a real phone for a phone-facing experience. Record a reason for any inapplicable check.
- Exercise at least the critical user journey on the intended candidate. Mocks, public sample flows and component tests do not prove actual authenticated or external-provider behavior.
- If a tool lacks a required capability, name a concrete alternative or manual procedure and its owner. Do not silently lower the requirement or retry unchanged tools indefinitely.
- Check product understanding as well as mechanics: can a representative visitor identify the offer, find evidence, and complete the primary action? Use a lightweight observed task when practical; do not add analytics without a reason.

For each material result record the tested revision or working-tree fingerprint, environment, method, observed result, date, evidence location and limits. Use Not run, Passed, Failed, Blocked or N/A with a reason. An old pass requires an explicit applicability rationale; a changed relevant artifact requires a fresh check. Automated accessibility scans do not establish full conformance.

## Prepare release and continue

Maintain a release checklist in the existing plan or a linked file. Name the candidate, required checks, remaining issues and impact, preview, target environment, recovery procedure and owner. Approval is tied to that candidate; material changes require renewed review. Do not infer approval from elapsed time or a selected default.

Local edits and verified previews can iterate without asking after every step, within the user's authorization. Check whether a push or merge automatically deploys before using it. Do not publish production or merge a production-triggering branch before the user's explicit approval. Do not ask prematurely: finish preparation, show the reviewable result and evidence, and identify the exact release action first. If required checks remain blocked, report the blocker instead of presenting the release as ready.

After an approved release, check the actual public journey, routes/assets, relevant metadata, and changed integrations. Retain the prior deployable artifact and account for data migrations separately; rolling back static files does not undo database changes. Record actual release and recovery evidence.

End with what changed, what was checked, the practical limits, and the next decision or action. Update current decisions and task status once; keep the handoff concise.
