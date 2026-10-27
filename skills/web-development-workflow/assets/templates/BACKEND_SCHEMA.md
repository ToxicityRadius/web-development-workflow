# Data and access

Project: [Name]
Owner: [Name or role]
Document review: Draft
Last substantive review: [Date, or not reviewed]
Current scope: [Next feature or release]

Essential = answer briefly for the next feature. Optional = keep only when relevant.
Placeholders are questions to resolve, not confirmed facts. See README.md for decision ownership.

## 1. Applicability and inventory - Essential
Application type: [Description]
Storage/providers: [Locations, none, or undecided]
User data persisted: [Yes, no, or undecided]

| Data category | Purpose | Location/provider | Owner/authority | Retention/sensitivity |
|---|---|---|---|---|
| [Category] | [Purpose] | [Location] | [Owner/source] | [Rules] |

Include relevant forms, analytics, browser storage, files and external recipients.
No application database does not mean no data handling.
For a static site, retain this section and the lifecycle statement; omit irrelevant database sections.

## 2. Entities, fields and integrity - Optional
| Entity | Meaning | Relationships/cardinality | Lifecycle dependency |
|---|---|---|---|
| [Entity] | [Meaning] | [Relationships] | [Dependency] |

| Field | Meaning/type | Required/default | Trusted source | Constraint/sensitivity |
|---|---|---|---|---|
| [Field] | [Meaning/type] | [Rule] | [Who supplies/derives] | [Rule] |

Integrity: [Relevant uniqueness, references, valid states, duplicates,
failed-write guarantees and parent/owner-removal consequences]
Business-rule references: [PRD.md]
Validation timing/recovery: [APP_FLOW.md]

## 3. Permissions - Optional
| Actor | Resource | In-scope operation | Ownership/context condition | Enforcement point | Check |
|---|---|---|---|---|---|
| [Actor] | [Resource] | [Operation] | [Condition] | [Trusted point] | [V-reference] |

Deny operations unless explicitly permitted. UI visibility is not authorization.
Client-supplied ownership does not establish trusted identity.
Define positive and negative checks; do not add operations outside product scope.

## 4. Queries and recovery - Optional
Important access patterns: [Filters, actual/expected volume, pagination and index rationale]
Migration: [Changes and affected existing data]
Backup/restore: [Approach and restoration checks]
Irreversible changes: [Limitations]

Technical compatibility: TECHNICAL_REQUIREMENTS.md
Release sequencing/execution: IMPLEMENTATION_PLAN.md

## 5. Lifecycle - Essential
- Collection and purpose: [Statement]
- Storage and external recipients: [Statement]
- Retention: [Rule or decision owner/trigger]
- Deletion/export responsibilities: [Applicable mechanism]
- Owner/parent removal: [Applicable consequences]
- Diagnostic data/sensitivity: [Applicable scope]

A lifecycle responsibility does not automatically authorize a new product feature.
Resolve consequential privacy/data-loss uncertainty before dependent production use.

## Ready and update
- Ready to explore: data uncertainty, experiment and decision criterion are clear.
- Ready to build: needed meaning, ownership, constraints, permissions and lifecycle are known.
- Results/evidence belong in IMPLEMENTATION_PLAN.md.
- Update when data, access, queries, retention or external handling change.

Worked example: [the connected walkthrough](WORKED_EXAMPLE.md) traces R-001 through all six documents.
