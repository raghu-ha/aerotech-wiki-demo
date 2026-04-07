---
title: Maintenance Log — Aircraft XA-001
category: MaintenanceLog
part_numbers: [AT-T900-FB-002, AT-T900-FB-LE-002]
affects: [titan-900, fan-blade-leading-edge-erosion, sb-2024-047]
sources: [AT-MLOG-XA001-2026]
last_updated: 2026-04-07
---

# Maintenance Log — Aircraft XA-001

## Summary
AeroMax A80, registration XA-001, operated by GlobalAir (MSN-0047). Fitted with 4x Titan 900 engines. Engines #1 and #3 are under active SB-2024-047 action for fan blade erosion. Engine #3 is PRIORITY — blade replacement parts due 2026-04-28. Engines #2 and #4 are normal.

## Aircraft Details
| Field | Detail |
|---|---|
| Aircraft Type | AeroMax A80 |
| MSN | MSN-0047 |
| Operator | GlobalAir |
| Total Flight Hours | 18,432 |
| Total Flight Cycles | 4,218 |
| Last Heavy Check | C-Check, October 2025 |
| Next Scheduled Check | A-Check, June 2026 |

## Engine Status
| Engine | Serial | Cycles Since Install | Status |
|---|---|---|---|
| #1 | AT-E-10047 | 1,847 | ⚠️ SB-2024-047 pending — replacement due ~100 cycles |
| #2 | AT-E-10089 | 2,103 | ✅ Normal |
| #3 | AT-E-10102 | 1,921 | 🔴 SB-2024-047 PRIORITY — replacement due within 50 cycles |
| #4 | AT-E-10034 | 987 | ✅ Normal |

## Maintenance Event Log

### 2026-04-05 — Engine #3 Borescope Inspection
- Technician: J. Martinez (AT-TECH-0892)
- Fan blade leading edge erosion confirmed on blades FB-07, FB-12, FB-15:
  - FB-07: 3.8mm chord loss (Stage 2)
  - FB-12: 4.1mm chord loss (Stage 2 — approaching Stage 3 limit of 5mm)
  - FB-15: 3.2mm chord loss (Stage 2)
- **Action:** Full fan blade replacement per SB-2024-047 within 50 cycles
- Parts ordered: 22x AT-T900-FB-002, 22x AT-T900-FB-LE-002 (Singapore MRO, ETA 2026-04-28)

### 2026-04-03 — Engine #1 Scheduled Inspection
- Technician: S. Patel (AT-TECH-1204)
- Fan blade erosion Stage 2 confirmed. Average chord loss 3.1mm
- EGT margin: 48°C (minimum 45°C — acceptable)
- Zone 1 vibration: 2.8 IPS (limit 3.5 IPS — acceptable)
- **Action:** SB-2024-047 compliance within 100 cycles
- Parts ordered (Singapore MRO, ETA 2026-05-05)

### 2026-03-18 — Engine #2 Oil System Check
- Technician: R. Kumar (AT-TECH-0654)
- Oil consumption: 0.18 L/hr (limit 0.3 L/hr — normal)
- Oil pressure: 68 psi (range 55–85 psi — normal)
- Status: ✅ Normal

### 2026-03-10 — Engine #4 Routine A-Check
- All parameters within limits
- Fan blade inspection: no erosion detected at 987 cycles
- Status: ✅ Normal

### 2026-02-22 — Engine #3 ACMS Data Review
- EGT trending upward: +7°C over 90-day baseline
- Consistent with Stage 2 fan blade erosion
- Borescope subsequently scheduled and completed 2026-04-05
- Note: ACMS trend data identified the issue 6 weeks before physical inspection

### 2025-10-14 — All Engines C-Check
- Full heavy maintenance completed
- Engine #1: Fan blades within limits (412 cycles at that time)
- Engine #3: Minor Stage 1 erosion noted — monitoring commenced
- All engines returned to service

## Parts on Order
| Part Number | Description | Qty | For Engine | ETA | MRO |
|---|---|---|---|---|---|
| AT-T900-FB-002 | Fan blade Rev B | 22 | #3 | 2026-04-28 | Singapore |
| AT-T900-FB-LE-002 | Leading edge strip Rev B | 22 | #3 | 2026-04-28 | Singapore |
| AT-T900-FB-002 | Fan blade Rev B | 22 | #1 | 2026-05-05 | Singapore |
| AT-T900-FB-LE-002 | Leading edge strip Rev B | 22 | #1 | 2026-05-05 | Singapore |

## Open Actions
| Item | Engine | Action | Due By | Status |
|---|---|---|---|---|
| SB-2024-047 | #3 | Fan blade replacement (PRIORITY) | 50 cycles | 🔴 OPEN |
| SB-2024-047 | #1 | Fan blade replacement | 100 cycles | 🟡 OPEN |
| ACMS Baseline Reset | #3 | After blade replacement | Post-replacement | 🔴 OPEN |
| Zone 1 Vibration Check | #3 | After blade replacement | Post-replacement | 🔴 OPEN |

## Connections
- Related: [[titan-900]], [[fan-blade-leading-edge-erosion]], [[fan-blade-rev-b]], [[sb-2024-047]], [[sb-2023-031]]
- Parts involved: [[fan-blade-t900]], [[fan-blade-rev-b]]
- Related aircraft: [[maintenance-log-xa002]]

## Sources
- AT-MLOG-XA001-2026 (April 2026)
- SB-2024-047 Rev 2.0 (March 2024)
