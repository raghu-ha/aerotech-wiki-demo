# Query: What is the issue with aircraft XA-001 Engine #3 and what needs to be done?

**Date:** 2026-04-07  
**Articles consulted:** maintenance-log-xa001, fan-blade-leading-edge-erosion, sb-2024-047, fan-blade-rev-b

---

## The Issue

XA-001 Engine #3 (serial AT-E-10102, 1,921 cycles since install) has **fan blade leading edge erosion** — accelerated material loss on the carbon fibre composite blades in high-particulate operating environments. This is a known fleet-wide Titan 900 issue addressed by mandatory Service Bulletin SB-2024-047.

Borescope inspection on **2026-04-05** (technician J. Martinez, AT-TECH-0892) confirmed Stage 2 erosion on three blades:

| Blade | Chord Loss | Stage | Note |
|---|---|---|---|
| FB-07 | 3.8mm | Stage 2 | Exceeds 3mm threshold |
| FB-12 | 4.1mm | Stage 2 | Approaching Stage 3 limit (5mm) — most critical |
| FB-15 | 3.2mm | Stage 2 | Exceeds 3mm threshold |

Stage 2 erosion impacts: fuel burn increase of 0.3–0.8% and EGT margin reduction of 5–12°C. ACMS data had already flagged a +7°C EGT trend on 2026-02-22 — six weeks before the borescope confirmed the finding.

## Why It Is Urgent

SB-2024-047 classifies this as **MANDATORY** and sets a **50-cycle deadline** for Engine #3 specifically (vs 300 cycles for general compliance). Blade FB-12 at 4.1mm is only 0.9mm from the Stage 3 threshold of 5mm, at which point:
- Replacement becomes immediately mandatory
- Risk of blade fragment separation
- Zone 1 vibration increase (limit 5.0 IPS)

## What Needs to Be Done

### 1. Fan Blade Replacement — within 50 cycles (PRIORITY)
Replace all 22 fan blades with Rev B specification per SB-2024-047.

**Parts ordered** (Singapore MRO, ETA **2026-04-28**):
- 22x AT-T900-FB-002 (Fan blade Rev B)
- 22x AT-T900-FB-LE-002 (Leading edge strip Rev B)

Note: AT-T900-FB-SEAL-001 (root seal) and AT-T900-FD-BOLT-001 (retention bolts) are also required per SB-2024-047 parts list — confirm these are included in the work order. Labour estimate: 46 man-hours.

### 2. Post-Replacement Checks (all mandatory per SB-2024-047)
- Ground engine run per AT-AMM-T900-71-00-01
- Zone 1 vibration check — must read **below 3.5 IPS**
- EGT margin at takeoff — must be **≥ 45°C**
- ACMS baseline reset

### 3. Do Not Exceed 50 Cycles Before Replacement
Engine #3 must not accumulate more than 50 additional cycles in its current condition. If parts are delayed beyond that window, the engine should be taken out of service.

## What Happens After

Once Rev B blades are installed and post-replacement checks pass, the inspection interval extends from 500 to 750 cycles. The ACMS baseline reset will re-establish the EGT trend reference against the new blade condition.

---

*Sources: maintenance-log-xa001 · fan-blade-leading-edge-erosion · sb-2024-047 · fan-blade-rev-b*
