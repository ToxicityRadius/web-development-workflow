# One feature through all six documents

Hypothetical example only. This is not a specification for the user's actual portfolio.
No code was built and none of the following product checks have been run.

Assumptions: a personal project portfolio publishes a project list and case studies as
static content. No accounts, forms, analytics or persistent browser storage are used.
The routes and content names below are illustrative choices for this example.

## 1. PRD.md: define what must work
R-001: A visitor can open a listed project's case study and return to the list.
- AC-001: Selecting the illustrative "Sensor Demo" project displays that case study's
  matching title, description and image.
- AC-002: Entering `/projects/sensor-demo/` directly and refreshing displays the same content.
- AC-003: Selecting "All projects" returns to `/projects/` with the project list visible.

First-release scope: this journey and relevant responsive/keyboard behavior.
Exclude accounts, forms and stored visitor records. The three acceptance conditions are
release-blocking for this feature. They do not establish business impact.

## 2. TECHNICAL_REQUIREMENTS.md: resolve only needed choices
Use the project's existing suitable static publishing setup; do not select a new framework
for this example. The host must serve the case-study route directly and after refresh.
If that capability is unknown, test it on the intended preview host before dependent work.
Published project content is the source of the displayed text and imagery.
There is no authenticated application service or application database in this example.

## 3. APP_FLOW.md: describe F-001
Start: `/projects/` with the illustrative project listed.
1. Visitor selects "Sensor Demo".
2. System navigates to `/projects/sensor-demo/` and shows the matching content.
3. Visitor selects "All projects".
4. System returns to `/projects/` and displays the list.
Alternate entry: open the case-study URL directly, then refresh it.
Acceptance: AC-001 through AC-003. Result checks: V-001 through V-003.

## 4. DESIGN.md: identify binding and adaptable choices
Required: the project title, description and image identify the same selected project;
the "All projects" link is visible and keyboard-operable with visible focus.
Adaptable: exact layout may vary while maintaining readable order and usable controls.
No colors, fonts or animation are prescribed by this example.

For this example only, also review at a 375 CSS-pixel viewport and at 1440 CSS pixels,
and navigate the journey with the keyboard. These are illustrative review conditions,
not universal breakpoints and not a complete accessibility conformance evaluation.

## 5. BACKEND_SCHEMA.md: describe actual data handling
Inventory: public project title, description and image, stored as published site content.
Authoritative source: the project's content files and assets.
Visitor data collection: none under the stated assumptions.
Database/entities/permission matrix: not applicable to an application database.
Lifecycle: the site owner maintains the public content; reassess handling if forms,
analytics, accounts or other data collection are introduced.

## 6. IMPLEMENTATION_PLAN.md: define T-001 and check it
T-001: Implement the complete F-001 journey using the established project setup.
Allowed scope: required content, listing link, case-study route and return link.
Do not add accounts, forms, a database or an unrelated redesign.
Acceptance: AC-001 through AC-003.

### Authoritative task status for this hypothetical example
| Task ID | Status | Blocker | Next action | Verification links |
|---|---|---|---|---|
| T-001 | Pending | Existing setup not inspected | Inspect routes/content and fill technical unknowns | V-001, V-002, V-003, V-009 |

### Named checks (all unexecuted)
| Check | Reference | Scenario | Expected result | Check status |
|---|---|---|---|---|
| V-001 | AC-001 | Select Sensor Demo from `/projects/` | Matching title, description and image display | Not run |
| V-002 | AC-002 | Open direct case-study URL, then refresh | Same case-study content displays after both actions | Not run |
| V-003 | AC-003 | Select All projects from case study | `/projects/` displays the project list | Not run |
| V-009 | Example design requirement | Review narrow/wide layouts and use keyboard | No clipped required content; controls operable; visible focus | Not run |

For each execution record: exact revision/build, environment, relevant browser/device/
viewport/content conditions, method, observed result, evidence location, check time and
limitations. Keep these as Not run/None until actual observations exist.

Release only when the named required checks pass against the candidate build, or record
an explicit issue-impact/release decision. An exception is not a passing test. If later
changes affect the behavior, rerun the affected checks or justify evidence carry-forward.

## Change one thing without rewriting everything
If a contact form becomes part of a future release, define it as a new requirement.
Revisit the technical integration, form/recovery flow, relevant design states and data
inventory/lifecycle. Add its task/checks to the existing plan. Do not assume the previous
"no visitor data collection" statement still holds, or change the accepted R-001 behavior
without a stated reason. This is a change-impact illustration, not authorization to add a form.
