# AeroTech Knowledge Wiki — Schema

Domain: Aircraft Engine Maintenance · Parts · Service Bulletins · Maintenance Logs

---

## Directory Layout

```
aerotech-wiki/
├── CLAUDE.md       ← Schema (you are here)
├── raw/            ← Source documents (append-only)
├── wiki/
│   ├── INDEX.md    ← Master catalog
│   ├── log.md      ← Operation log
│   └── pages/      ← One article per concept
└── outputs/        ← Query answers
```

---

## Domain Taxonomy

| Category | Examples |
|---|---|
| Engine | Titan 900 specs, assemblies, limits |
| Assembly | Fan assembly, compressor, turbine |
| Part | Fan blade, disc, seal, bearing |
| ServiceBulletin | SB-2024-047, SB-2023-031 |
| MaintenanceLog | Aircraft XA-001, XA-002 |
| Issue | Erosion, tip rub, vibration |

---

## Ingest Workflow

When a new file arrives in raw/:
1. Read INDEX.md
2. Read the source document fully
3. Identify all concepts — engines, parts, issues, bulletins, aircraft
4. Create or update wiki/pages/<slug>.md per concept
5. Cross-link related articles using [[slug]] backlinks
6. Update INDEX.md
7. Append to log.md

**Critical rule:** Always link parts → their engine, issues → their service bulletin, maintenance logs → both parts and bulletins. Relationships are as important as the articles themselves.

---

## Query Workflow

When asked a question:
1. Read INDEX.md
2. Find ALL relevant articles (not just the most obvious one)
3. Traverse backlinks to find connected articles
4. Synthesize answer citing which articles contributed
5. Save answer to outputs/YYYY-MM-DD-<slug>.md

**Example:** "What is the issue with Engine #3 on XA-001?"
→ Read: maintenance-log-xa001.md → fan-blade-erosion.md → sb-2024-047.md → fan-blade-rev-b.md
→ Synthesize across ALL four articles

---

## Article Template

```markdown
---
title: <Name>
category: <Engine|Assembly|Part|ServiceBulletin|MaintenanceLog|Issue>
part_numbers: []
affects: []
sources: []
last_updated: YYYY-MM-DD
---

# <Name>

## Summary
<!-- One paragraph -->

## Technical Details

## Current Status

## Connections
- Related: [[slug]], [[slug]]
- Affects: [[aircraft-slug]]
- Resolves: [[issue-slug]]
- Parts involved: [[part-slug]]

## Open Actions

## Sources
```
