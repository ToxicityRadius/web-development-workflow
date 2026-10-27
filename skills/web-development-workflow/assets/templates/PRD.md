# Product requirements

Project: [Name]
Owner: [Name or role]
Document review: Draft
Last substantive review: [Date, or not reviewed]
Current scope: [Next feature or release]

Essential = answer briefly for the next feature. Optional = keep only when relevant.
Placeholders are questions to resolve, not confirmed facts. See README.md for decision ownership.

## 1. Product and audience - Essential
Product: [What are we building?]
Primary user: [Who needs it?]
Problem: [What difficulty exists today?]
Smallest useful release: [Boundary]

| Claim or assumption | Evidence/source | Observed, reported, or assumed | Next action |
|---|---|---|---|
| [Claim] | [Reference] | [Status] | [Action] |

Do not turn an assumption into a confirmed user need.

## 2. Outcomes and scope - Essential
Desired user/business outcome: [Improvement]
Measurement and review point: [How and when; leave unknowns explicit]

- Essential for this release: [Capabilities and reasons]
- Later, not promised now: [Possibilities]
- Explicitly excluded: [Exclusions]
- Confirmed constraints/dependencies: [Facts and sources]

Product success and release acceptance are separate. A working site does not by itself prove business impact.

## 3. Requirements and acceptance - Essential
| Requirement ID | User need | Observable behavior | Priority | Acceptance condition | Flow |
|---|---|---|---|---|---|
| R-[number] | [Need] | [Behavior] | [Priority] | [Condition/reference] | F-[number] |

Acceptance format: Given [start], when [action], then [observable result].
Use AC-[number] only when separate conditions need separate links.
Verification methods and results belong in IMPLEMENTATION_PLAN.md.

## 4. Business rules - Optional
| Rule | Meaning | Example/exception | Requirement |
|---|---|---|---|
| [Rule] | [Eligibility, limit, calculation, or ownership meaning] | [Example] | [Reference] |

This document owns business meaning. APP_FLOW.md owns validation timing/recovery;
BACKEND_SCHEMA.md owns persistent constraints and permissions. Link rather than redefine.

## 5. Open product questions - Essential
| Question | Owner | Next action/trigger | Dependent work |
|---|---|---|---|
| [Question] | [Role] | [Action] | [Task or requirement] |

## 6. Release acceptance - Essential
| Required release condition | Acceptance reference | Verification check |
|---|---|---|
| [Named condition] | [R- or AC-reference] | [V-reference] |

Required checks must pass against the intended release revision. Keep execution results
and exceptions in IMPLEMENTATION_PLAN.md. Do not weaken criteria to fit the implementation.

## Ready and update
- Ready to explore: a meaningful uncertainty and bounded investigation are defined.
- Ready to build this feature: purpose, priority, behavior, acceptance and dependent decisions are clear.
- Update when audience, scope, priorities, business rules or acceptance change.

Worked example: [the connected walkthrough](WORKED_EXAMPLE.md) traces R-001 through all six documents.
