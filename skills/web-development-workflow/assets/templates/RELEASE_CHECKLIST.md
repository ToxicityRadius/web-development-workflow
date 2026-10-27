# Release checklist

Project: [Name]
Candidate revision and dirty-tree fingerprint: [Identify the actual source/build]
Preview/artifact: [Link or local path]
Target and production-triggering action: [Host/environment/command or merge]
Release owner: [Role]
Approval: Not requested

Link this file from the existing implementation plan. Keep current task progress there. For a small change, embed only the relevant records in that plan instead of creating this file.

## Checks

Choose required checks before declaring the candidate ready. Expand relevant rows, remove inapplicable details, and explain N/A. Mark an unavailable check Blocked with its concrete alternative and owner. Avoid carrying historical passes into a changed candidate without an applicability rationale.

| ID | Scenario and expected result | Required? / reason | Method or fallback / owner | Status | Evidence and candidate |
| --- | --- | --- | --- | --- | --- |
| R-BUILD | Production artifact builds using the intended runtime/configuration; relevant tests pass | [Decision] | [Existing commands] | Not run | [Record] |
| R-FLOW | Primary user journey and affected error/recovery paths work | [Decision] | [Actual browser/integration procedure] | Not run | [Record] |
| R-VISUAL | Required screens/states match DESIGN.md at wide, narrow and short sizes, with realistic content/themes | [Decision] | [Screenshots and inspection] | Not run | [Record] |
| R-ACCESS | Relevant keyboard/focus, contrast, labels, zoom/reflow, motion preference and assistive-technology behavior work | [Decision] | [Manual and automated checks; name unavailable capability fallback] | Not run | [Record] |
| R-DEVICE | Critical journey works on a real phone and supported browser engines | [Decision] | [Named phone/browser and procedure] | Not run | [Record] |
| R-PERF | Representative cold load and interaction meet documented targets without blocking essential content | [Decision] | [Device/network/CPU conditions and measurement] | Not run | [Record] |
| R-DATA | Trusted validation, owner/nonowner permissions, persistence and recovery work when applicable | [Decision] | [Real integration plus negative cases] | Not run | [Record] |
| R-CONTENT | Claims, roles, assets, links and affected canonical/social metadata are accurate | [Decision] | [Source and route review] | Not run | [Record] |
| R-USER | Representative user understands the offer/evidence and completes the primary action | [Decision] | [Observed task; no analytics assumed] | Not run | [Record] |
| R-RECOVERY | Known prior artifact/data recovery procedure and trigger are recorded | [Decision] | [Hosting procedure; migration recovery separate] | Not run | [Record] |

Each evidence record names the method, observed result, checked-at time, build/environment and limits. Statuses: Not run, Passed, Failed, Blocked, N/A with reason. A waiver is an explicit decision with impact; it does not turn a failed or unrun check into a pass.

## Review packet

- User-visible changes and preview/screenshots: [References]
- Required checks and their actual results: [References]
- Remaining issue, impact, owner and release-blocking decision: [List]
- Production action and scope: [Exact target and operation]
- Previous deployment/artifact, recovery trigger and procedure: [References]
- Candidate-bound production approval: [User instruction/date; leave Not requested until ready]

Do not publish, merge a production-triggering branch or change production settings before approval. Check automatic deployment behavior before pushing. If the candidate changes materially after approval, refresh affected checks and obtain approval for the new candidate.

## After approved publication

Record deployment identity, source/build match, public critical-journey smoke result, affected routes/assets/metadata/integrations and recovery evidence. Keep this pending until an actual release occurs. Production smoke checks happen after publication and cannot be claimed as pre-release results.
