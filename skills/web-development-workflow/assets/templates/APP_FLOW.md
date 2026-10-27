# App flow

Project: [Name]
Owner: [Name or role]
Document review: Draft
Last substantive review: [Date, or not reviewed]
Current scope: [Next feature or release]

Essential = answer briefly for the next feature. Optional = keep only when relevant.
Placeholders are questions to resolve, not confirmed facts. See README.md for decision ownership.

## 1. Task and destination map - Essential
| Actor | Goal | Requirement | Entry point |
|---|---|---|---|
| [Role] | [Task] | [R-reference] | [Start] |

| Destination | Kind | Purpose | Access/entry |
|---|---|---|---|
| [Route or destination] | [Page, external link, download, action] | [Purpose] | [Rule] |

Navigation map: [Simple connections between destinations]
A sitemap alone does not specify dynamic behavior.

## 2. Main flow - Essential
F-[number]: [Name]
Actor/goal: [Who and what]
Preconditions: [Identity/data/start state]
Trigger: [Action/event]

| Step | Action/event | System response | Resulting state |
|---|---|---|---|
| 1 | [Action] | [Response] | [State] |

Successful end state: [Observable result]
Requirement/acceptance: [PRD.md references]
Data rules: [BACKEND_SCHEMA.md references]
Verification: [IMPLEMENTATION_PLAN.md references]

## 3. Alternative paths and states - Essential
| Condition | User-visible response | Recovery | Rule/acceptance reference |
|---|---|---|---|
| [Relevant failure or alternative] | [Response] | [Action] | [Reference] |

Include only applicable invalid-input, missing-content, denied-access, expired-session,
service-failure and interrupted/ambiguous-outcome cases.

| Screen | Applicable states | Available actions | Exit condition |
|---|---|---|---|
| [Screen] | [Initial, loading, empty, populated, success, error] | [Actions] | [Condition] |

## 4. Forms - Optional
Form: [Name]
Business/field rules: [PRD.md references]
Persistent constraints: [BACKEND_SCHEMA.md references]
Interface: [TECHNICAL_REQUIREMENTS.md reference]

- Validation timing and feedback: [Behavior]
- Pending state: [Available actions]
- Input preservation and retry: [Behavior]
- Duplicate submission, cancellation, ambiguous outcome: [Relevant behavior]
- Confirmation trigger: [Trusted event establishing success]

Reference field meaning/requiredness; do not redefine it independently here.

## 5. Navigation behavior - Essential
- Narrow/wide-screen navigation: [Behavior]
- Keyboard and focus transitions: [Behavior]
- Back, direct link and refresh: [Behavior]
- Unsaved changes/authentication return: [If applicable]

DESIGN.md defines how these states and controls look.

## Ready and update
- Ready to explore: the journey uncertainty and validation activity are defined.
- Ready to build: entry, steps, responses, completion and relevant recovery are clear.
- Update when destinations, transitions, states, validation timing or recovery change.

Worked example: [the connected walkthrough](WORKED_EXAMPLE.md) traces R-001 through all six documents.
