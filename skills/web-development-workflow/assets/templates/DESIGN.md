# Design brief

Project: [Name]
Owner: [Name or role]
Document review: Draft
Last substantive review: [Date, or not reviewed]
Current scope: [Next feature or release]

Essential = answer briefly for the next feature. Optional = keep only when relevant.
Placeholders are questions to resolve, not confirmed facts. See README.md for decision ownership.

## 1. Intent and references - Essential
Audience/task: [Who and what]
Desired impression: [Description]
Primary visual priority: [What should users notice first?]
Principles: [A few rules tied to the task]

| Reference | Mode | Qualities/aspects to use | Limits |
|---|---|---|---|
| [URL/asset] | [Exact reference, qualities to adapt, inspiration only] | [Qualities] | [What is not prescribed] |

| Consequential decision | Classification | Specification/constraints | Reason |
|---|---|---|---|
| [Decision] | [Required, Adaptable, Exploratory] | [Definition] | [Reason] |

Required means implement the decision. Adaptable means vary within constraints.
Exploratory means validate before adoption. Do not classify every tiny visual choice.
Clarify consequential discretion before an implementation depends on exact interpretation.

## 2. Visual foundations - Essential
| Role/token | Value | Purpose/constraint |
|---|---|---|
| [Color role] | [Value] | [Purpose] |
| [Type role] | [Font, size/scale, weight, line height] | [Purpose] |
| [Spacing/width] | [Value/scale] | [Purpose] |

Relevant borders, radii, elevation and icon treatment: [Rules]
Do not invent arbitrary values merely to fill this table.

## 3. Layout, components and content - Essential
| Context/screen | Layout/reading order | Navigation presentation | Overflow/reflow |
|---|---|---|---|
| [Context] | [Rules] | [Pattern] | [Behavior] |

| Component | Purpose/variants | Applicable states | Labels/help | Responsive/accessibility presentation |
|---|---|---|---|---|
| [Component] | [Purpose] | [States] | [Rules] | [Rules] |

APP_FLOW.md owns when states occur. This document owns their presentation.
Voice/errors: [Style]
Assets and alternatives: [Images, icons, text alternatives and ownership]

## 4. Motion - Optional
Interaction: [Name]
Purpose/trigger: [Useful reason and APP_FLOW.md reference]
Presentation: [Behavior]
Reduced-motion alternative: [Alternative]

Essential information must not depend on animation.

## 5. Accessibility and review - Essential
Target: [Project target; starting default WCAG 2.2 AA]
Relevant requirements: [Structure, focus/keyboard, contrast, labels/errors,
text alternatives, reflow/zoom and motion alternatives as applicable]

| Screen/state | Viewport/conditions | Review focus | Verification check |
|---|---|---|---|
| [Screen/state] | [Conditions] | [Concern] | [V-reference] |

Identify applicable criteria and manual/automated checks. A filled template or automated scan
alone does not establish conformance. Evidence records belong in IMPLEMENTATION_PLAN.md.

## Ready and update
- Ready to explore: prototype/review activity and decision criterion are clear.
- Ready to build: hierarchy, key states, responsive behavior and discretion are defined.
- Update when visual rules, presentation, references or content conventions change.

Worked example: [the connected walkthrough](WORKED_EXAMPLE.md) traces R-001 through all six documents.
