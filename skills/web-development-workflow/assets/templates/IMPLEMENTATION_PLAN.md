# Implementation and verification

Project: [Name]
Owner: [Name or role]
Document review: Draft
Last substantive review: [Date, or not reviewed]
Current scope: [Next feature or release]

Essential = answer briefly for the next feature. Optional = keep only when relevant.
Placeholders are questions to resolve, not confirmed facts. See README.md for decision ownership.

## 1. Objective and dependencies - Essential
Milestone/user-visible result: [Outcome]
Requirements/acceptance: [PRD.md references]
Exclusions: [PRD.md references]

| Dependency | Required for | Owner | Resolution criterion/source |
|---|---|---|---|
| [Dependency] | [Task] | [Role] | [Criterion/reference] |

Do not block unrelated work because of unresolved future decisions.

## 2. Task definition - Essential
T-[number]: [Title]
Goal: [Small end-to-end user-visible capability]
Requirement/acceptance: [References]
Relevant document sections: [References]
Allowed scope: [Areas that may change]
Out of scope: [Exclusions]
Dependencies: [References]
Required checks/evidence: [V-references and requirements]

For an exploration task, replace implementation scope with a question,
bounded experiment and decision criterion. Use the same task-status table below.
Do not repeat current status or next action in task definitions or handoffs.

## 3. Verification records - Essential
V-[number]: [Check title]
Requirement/acceptance: [R- or AC-reference]
Scenario: [Start and action]
Expected result: [Observable outcome linked to authoritative criteria]
Revision/build tested: Not run
Environment: Not run
Relevant conditions: [Device/browser/viewport, content, network/workload or test data]
Method/command: [Procedure or suite]
Observed result: Not run
Check status: Not run
Evidence location: None
Checked at: Not run
Limitations: [Coverage or unresolved uncertainty]

Check statuses: Not run, Passed, Failed, Blocked.
Visual evidence names screen/state/viewport/environment/build.
Automated evidence names the command/suite, conditions, revision and result.
Earlier evidence does not automatically verify changed behavior. Identify affected checks
and rerun as appropriate. If evidence carries forward, state why it still applies.

Select relevant success, recovery, permission, integrity, accessibility,
responsive, integration and regression checks. Never claim unobserved results.

## 4. Release and recovery - Essential
Release candidate and environment: [Revision/build and target]
Acceptance contract: [PRD.md reference]
Required checks: [V-references derived from that contract]
Deployment and post-release smoke checks: [Procedure and expected results]
Recovery trigger/procedure/checks: [Details appropriate to the hosting setup]
Release owner: [Role]

| Remaining issue | Impact | Blocks release? | Action or explicit decision |
|---|---|---|---|
| [Issue] | [Effect] | [Yes/no with reason] | [Decision] |

An exception does not turn a failed check into a pass.

## 5. Authoritative task status - Essential
This is the only location for current task status, blocker and next action.

| Task ID | Status | Blocker | Next action | Verification links |
|---|---|---|---|---|
| T-[number] | Pending | [None or issue] | [Action] | [V-references] |

Task statuses: Pending, Active, Blocked, Implemented, Verified.
Implemented means the change exists. Verified means applicable required checks passed
and evidence is recorded. Revisit progress when a later change invalidates verification.

## 6. Agent handoff - Essential
Task: [T-reference and task-definition section]
Current status/blocker/next action: See section 5; do not duplicate.
Read: [Relevant authoritative document sections]
Constraints/allowed scope: [References]
Acceptance/checks: [References]
Known limitations: [References]

Instruction: Inspect the existing implementation and referenced decisions. Implement only
the task. Resolve consequential missing/conflicting decisions in their owning document
before dependent changes; continue unaffected work. Verify specified scenarios and report
changes, actual results, evidence and remaining issues.

## Ready and update
- Explore when a question and bounded activity are clear.
- Build when necessary behavior, data, permissions and technical choices are resolved.
- Mark Verified only after applicable required checks pass with evidence.
- Update when scope, dependencies, progress, blockers, evidence or release conditions change.

Worked example: [the connected walkthrough](WORKED_EXAMPLE.md) traces R-001 through all six documents.
