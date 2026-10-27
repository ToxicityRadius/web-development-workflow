# Technical requirements

Project: [Name]
Owner: [Name or role]
Document review: Draft
Last substantive review: [Date, or not reviewed]
Current scope: [Next feature or release]

Essential = answer briefly for the next feature. Optional = keep only when relevant.
Placeholders are questions to resolve, not confirmed facts. See README.md for decision ownership.

## 1. Existing environment and constraints - Essential
Inspect first; do not assume replacements are needed.

| Area | Current fact | Evidence | Necessary action |
|---|---|---|---|
| Repository/tools | [Fact] | [Reference] | [Action] |
| Hosting/integrations | [Fact] | [Reference] | [Action] |
| Working behavior | [Preserve what?] | [Reference] | [Action] |

Supported environments: [Browsers/devices]
Confirmed deployment, cost or compatibility constraints: [Facts]
Unknown constraint and resolution trigger: [Question]

## 2. Components and trust boundaries - Essential
Architecture: [Major components and responsibilities]
Connections/data movement: [Description or simple diagram]
Identity, validation and authorization enforcement: [Trusted locations or not applicable]

Do not add an application server or database solely to fill the template.
Data definitions and permissions: [BACKEND_SCHEMA.md references]

## 3. Necessary choices and quality requirements - Essential
| Choice | Reason | Alternative/trade-off | Revisit trigger |
|---|---|---|---|
| [Choice] | [Reason] | [Limitation] | [Trigger] |

| Scenario | Observable metric/result | Justified target | Representative conditions | Check |
|---|---|---|---|---|
| [Operation/page] | [Result] | [Target] | [Content/device/network/workload] | [Method] |

Resolve only what the next feature needs. Do not invent performance numbers.

## 4. Interfaces - Optional
Interface: [Name and purpose]
Inputs/outputs: [Authoritative contracts]
Authentication: [Method]
Relevant limits/timeout/retry or duplicate handling: [Behavior]
Failure and recovery: [Behavior; link APP_FLOW.md]
Success event: [What actually establishes completion?]
Provider contract/version checked: [Reference]

Check the current provider contract before dependent work. Provider acceptance may differ from the final outcome.

## 5. Development, protection and operations - Essential
- Setup/commands: [Instructions or reference]
- Configuration: [Variable names and purposes; never secret values]
- Untrusted-input/output handling: [Relevant responsibilities]
- Preview/deployment and diagnostics: [Approach]
- Operational owner: [Role]
- Release execution: [IMPLEMENTATION_PLAN.md reference]

## 6. Significant decision or migration - Optional
ADR-[number]: [Title]
Owner: [Role]
Status: Proposed
Accepted date: [If accepted]
Context: [Problem/constraints]
Decision: [Choice]
Alternatives/consequences: [Benefits, costs, risks]
Supersedes: [ID or none]
Superseded by: [ID or none]
Revisit trigger: [Condition]

Statuses: Proposed, Accepted, Rejected, Superseded. Preserve accepted rationale;
a new accepted record supersedes an old one. Routine implementation choices need no ADR.

If existing behavior/data is affected: [Compatibility, migration and recovery constraints].
Data migration details belong in BACKEND_SCHEMA.md; execution order belongs in IMPLEMENTATION_PLAN.md.

## Ready and update
- Ready to explore: question, bounded experiment and decision criterion are clear.
- Ready to build: necessary boundaries, contracts and consequential choices are settled.
- Update when architecture, tools, interfaces, constraints or responsibilities change.

Worked example: [the connected walkthrough](WORKED_EXAMPLE.md) traces R-001 through all six documents.
