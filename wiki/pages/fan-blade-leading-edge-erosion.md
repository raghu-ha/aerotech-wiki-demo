---
title: Fan Blade Leading Edge Erosion
category: Issue
part_numbers: [AT-T900-FB-001, AT-T900-FB-002, AT-T900-FB-003, AT-T900-FB-004, AT-T900-FB-005, AT-T900-FB-006, AT-T900-FB-007, AT-T900-FB-008, AT-T900-FB-009, AT-T900-FB-010, AT-T900-FB-011, AT-T900-FB-012, AT-T900-FB-013, AT-T900-FB-014, AT-T900-FB-015, AT-T900-FB-016, AT-T900-FB-017, AT-T900-FB-018, AT-T900-FB-019, AT-T900-FB-020, AT-T900-FB-021, AT-T900-FB-022]
affects: [titan-900, fan-assembly-t900, maintenance-log-xa001, maintenance-log-xa002, maintenance-log-xa005]
sources: [AT-ENG-T900-SPEC-001 Rev 3.1]
last_updated: 2026-04-07
---

# Fan Blade Leading Edge Erosion

## Summary
Accelerated erosion on Titan 900 fan blade leading edges observed in high-particulate environments, resulting in reduced engine efficiency and increased fuel burn. Addressed by Service Bulletin SB-2024-047.

## Technical Details
- Affected Parts: AT-T900-FB-001 through AT-T900-FB-022
- Environment: High-particulate operations

### Failure Progression
| Stage | Cycles | Condition | Impact |
|---|---|---|---|
| Stage 1 | 0–300 | Minor pitting | No performance impact |
| Stage 2 | 300–450 | Erosion >3mm chord loss | Fuel burn +0.3–0.8%; EGT margin –5–12°C |
| Stage 3 | 450+ | Erosion >5mm | MANDATORY REPLACEMENT; fragment risk; vibration increase |

### Rejection Criteria (SB-2024-047)
- Chord loss exceeding 2mm (enhanced inspection threshold)
- Delamination at titanium-composite bond
- Any asymmetric erosion pattern

### Fleet Data (45 engines inspected)
- 22% showed >3mm erosion before 500-cycle interval
- 5% exceeded 5mm threshold before 400 cycles
- One engine: asymmetric erosion → Zone 1 vibration 4.1 IPS (limit 5.0 IPS)

## Current Status
Active issue. Mitigated via SB-2024-047. Ongoing monitoring required.

## Connections
- Related: [[fan-blade-t900]], [[fan-assembly-t900]], [[titan-900]]
- Resolves: [[sb-2024-047]]
- Affects: [[maintenance-log-xa001]], [[maintenance-log-xa002]], [[maintenance-log-xa005]]

## Open Actions
- Comply with SB-2024-047
- Inspect blades every 500 cycles; replace if >5mm chord loss

## Sources
- AT-ENG-T900-SPEC-001 Rev 3.1 (January 2026)
