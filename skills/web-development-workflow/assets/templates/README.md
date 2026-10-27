# Web project operating guide

Default approach: prioritize reliable, polished work and prepare a reviewable candidate before asking the user to approve production publication. Follow the project scope and explicit user choices.

Use the six-document planning toolkit as a reference. It supplies connected decisions, not six forms to complete before every edit. For an existing project, retain its document names and fill only missing decisions. For a small fix, keep the task and checks in the conversation or existing issue.

## Start a project or a substantial feature

1. Inspect existing instructions, working behavior, stack, Git state and hosting. Define the audience, user task, desired result and exclusions. Ask only decision-changing questions.
2. Locate the authoritative product, technical, flow, design, data and work-status records. Copy relevant templates from this folder only where useful. Name one DESIGN.md and one task-status table. Mark irrelevant backend sections N/A with a short data-handling statement.
3. Resolve uncertain design direction with a bounded visual exploration. Preserve an approved direction for refinements. Use one primary design workflow; add specialists only for a specific need.
4. Build a small complete journey, including applicable failure/recovery states. Inspect the actual UI; keep truthful content, keyboard/touch access and motion alternatives.
5. Run the existing focused checks and production build. Review affected screens/states on desktop and phone. Select release checks from real risks, and give capability gaps a runnable fallback and owner.
6. Record evidence against the candidate revision/fingerprint. Update the owning decisions and one task table. A handoff links these records rather than repeating status.
7. Prepare a preview, release/recovery procedure and remaining-issue list. Ask for production approval only after the candidate is concrete and required checks pass. A push or merge that triggers production counts as publishing.
8. After approval, publish the reviewed candidate, check its real public journey, and record deployment identity and recovery evidence.

## One home for each decision

| File | Owns |
| --- | --- |
| [PRD.md](PRD.md) | Audience, behavior, scope and acceptance |
| [TECHNICAL_REQUIREMENTS.md](TECHNICAL_REQUIREMENTS.md) | Stack, contracts, runtime, hosting and constraints |
| [APP_FLOW.md](APP_FLOW.md) | Routes, state transitions, interaction order and recovery |
| [DESIGN.md](DESIGN.md) | Visual foundations, references, density and motion intent |
| [BACKEND_SCHEMA.md](BACKEND_SCHEMA.md) | Actual data handling, ownership, integrity and permissions |
| [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) | Current task table and links to verification/release evidence |
| [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) | Optional detailed release check record, linked from the plan |

The six starter templates and [worked example](WORKED_EXAMPLE.md) retain the 18 October 2026 toolkit's essential/optional distinctions. These templates contain questions and hypothetical examples, not established project facts or executed checks. Replace or remove example links when adapting.

## Use the bundled planning PDF

The skill bundles the [16-page planning PDF](../../references/planning-guide.pdf) and its [searchable page-by-page version](../../references/planning-guide.md). Its instructions select relevant pages during product/technical planning, flow design, interface design, data handling, implementation and verification. It reads orientation pages for a substantial new project and reuses material already read during the task. Existing project decisions and explicit user instructions remain authoritative. The external one-page portfolio PDF is excluded from the workflow and portable package.

## A useful request

> Use $web-development-workflow. Continue the next task from this project's implementation plan. Inspect the repository first, ask only consequential missing questions, preserve the approved design, verify the complete user journey, and prepare the result for my production publishing approval.

## Maintain the system

When a decision changes, edit its owner and update pointers/prompts that depend on it in the same task. Move long historical snapshots out of active instructions. Keep evidence dated, distinguish historical results from fresh checks, and retain limitations. This workflow is instruction guidance, not an external deployment lock.
