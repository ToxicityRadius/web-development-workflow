# Skill selection research

Reviewed 27 October 2026 before implementing the routing update. Scope: a small redistributable core for a web-development coordinator, plus optional specialist routes. This is a targeted source, compatibility and license review, not a ranking of every available skill or a comparative model benchmark.

## Evidence and selection method

Pinned six upstream repositories and retrieved 28 source files without running their installers or launchers. Read the selected core guidance and licenses, inspected optional entrypoints and dependencies, and compared them with the existing workflow. Selection considered task fit, scope, supporting resources, portability, runtime/tool requirements, conflict behavior, redistribution terms and maintainability. Popularity was not a selection criterion.

Official [skill authoring guidance](https://developers.openai.com/plugins/build/skills) supports concise instructions with supporting references, scoped triggers and representative behavior checks. [Local discovery guidance](https://learn.chatgpt.com/docs/build-skills) notes that same-name skills can both appear; bundled adapters therefore use distinct names.

## Decisions

| Source | Evidence and constraints | Decision |
| --- | --- | --- |
| [Anthropic Frontend Design](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design) | Apache-2.0 license supplied in that skill's LICENSE.txt; instruction-only and framework-neutral. Some opening statements assume a client history; aesthetic cautions are not universal requirements. | Bundle unchanged source and license behind `workflow-interface-design`. The adapter grounds the actual brief, removes inferred client history from the operative contract, and preserves approved design/content. No Claude account or runtime is required. |
| [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines/tree/434b7f91364665f2f733b310ec54809bf8f37937) | Explicit MIT license and a self-contained command.md. Rules mix functional checks, style preferences and context-dependent heuristics. | Bundle the unchanged licensed guidelines behind `workflow-interface-review`, with applicability corrections and source date. Do not copy the separate agent-skills web-review wrapper, whose retrieved file has no license declaration. |
| [Emil Kowalski Mobile Native](https://github.com/emilkowalski/skills/tree/2d228630ba1446365f614a108cb8252f1feda202/skills/mobile-native) | Repository MIT license; instruction-only platform fixes. Examples include broad root overscroll/tap settings; initial greeting is an invocation convention. Actual hardware testing remains necessary for hardware-specific conclusions. | Bundle unchanged source and license behind `workflow-mobile-web`. Apply symptom-relevant changes, preserve zoom/content selection/native navigation, and separate emulation from actual-phone evidence. |
| [Impeccable](https://github.com/pbakaus/impeccable/tree/414603bf14c7a344edb466bb1f85690c77ce8b7d) | Apache-2.0; version 4.8.0 in package.json. Instructions invoke a launcher, supporting references and a native engine that can download on first use. Existing local skill reports 4.4.0; that installation was not upgraded. | Optional primary design workflow when explicitly selected or usable in the project. Do not vendor an incomplete launcher-only installation or auto-download its engine. Use its documented context fallback when appropriate. |
| [Vercel React Best Practices](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices) | The skill explicitly declares MIT; it references individual rules and a compiled AGENTS.md. React/Next.js APIs and optimizations are stack/version-dependent. | Optional for actual React/Next.js work. Check installed supporting files and current framework contracts; do not load it for a vanilla site or add its suggested libraries without a task-specific reason. |
| [OpenAI Playwright](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/playwright) | Per-skill license and notice supplied. CLI wrapper requires npx and uses a shell script; browsers and package caches are separate prerequisites. Interactive variant depends on a supported persistent JavaScript/browser environment. | Optional browser automation through the existing usable client or project setup. Disk presence, npx and a skill name do not prove a working browser. Do not install packages or browsers automatically. |
| Emil motion skills | Reviewed animate and related entrypoints at the same pinned repository. These introduce stronger motion-specific decisions and sometimes refer to other specialist skills. | Optional per concrete animation task; prefer existing tokens and tools. Keep cinematic Taste opt-in, outside the default core. |

## Applicability corrections

- Explicit user instructions, actual acceptance criteria, approved project design and accessibility requirements govern adaptation. Third-party source documents are preserved for provenance; the adapter defines how they apply.
- Native controls already supply keyboard behavior. Add keyboard handling to custom controls when needed rather than duplicating native behavior.
- Preserve meaningful autocomplete tokens for personal-information fields. Do not blanket-disable autofill to satisfy a generic rule. [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete) and [WCAG input-purpose guidance](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html) support this distinction.
- Root overscroll suppression changes scroll chaining and native navigation. Apply it only when the interaction needs it, and test affected devices. [MDN overscroll reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior).
- Capitalization, typography preferences, a fixed list-size threshold for virtualization and example CSS are heuristics. Match the project and measure before adding complexity.
- Browser tools, provider authentication, real devices and skill activation are distinct capabilities. Missing capability means a documented fallback or an honest Blocked/Not run result, not an installation or a claimed pass.

## Why routing is selective

[WebDev-Skills-Bench](https://arxiv.org/abs/2608.23067) tested 31 skills across 50 projects and four models. Its reported average outcomes worsened under some skill-injection conditions, with substantial token overhead and model-dependent rankings. [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) also reports limited average gains and regressions from context/version mismatch. These preprints inform the decision to load relevant guidance only; their results do not predict this plugin's performance or prove that a named skill is universally better.

The update should check availability, choose one primary design workflow, load a specialist only for a concrete need, and retain a small-task bypass. Package/fixture tests can verify declared routes, resources, discovery states and failure handling. Future agent-level evaluations are still needed to establish actual instruction-following and website-quality gains.

## Reproducibility and local constraints

Bundled upstream files retain exact source bytes and their original licenses. The third-party lock record stores repository, commit, path and SHA-256 for each. Authored adapters and workflow code retain the project's MIT license; bundled Anthropic material remains Apache-2.0, and the Vercel/Emil material remains MIT.

No new standalone specialists are installed in the existing local setup. The local coordinator should use its current catalogue, report missing names and preserve working skills. Public plugin users receive the three bundled adapters; advanced skills and runtime tools remain optional.
