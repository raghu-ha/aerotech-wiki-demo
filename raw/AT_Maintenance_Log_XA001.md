# AeroTech Industries — Maintenance Log

**Aircraft Registration:** XA-001  
**Operator:** GlobalAir  
**Engine Configuration:** 4x Titan 900  
**Document ID:** AT-MLOG-XA001-2026  
**Last Updated:** April 2026

---

## 1. Aircraft Summary

| Field | Detail |
|---|---|
| Aircraft Type | AeroMax A80 |
| MSN | MSN-0047 |
| Total Flight Hours | 18,432 |
| Total Flight Cycles | 4,218 |
| Last Heavy Check | C-Check, October 2025 |
| Next Scheduled Check | A-Check, June 2026 |

---

## 2. Engine Status Summary

| Engine | Position | Serial | Cycles Since Install | Status |
|---|---|---|---|---|
| Titan 900 | #1 | AT-E-10047 | 1,847 | ⚠️ SB-2024-047 pending |
| Titan 900 | #2 | AT-E-10089 | 2,103 | ✅ Normal |
| Titan 900 | #3 | AT-E-10102 | 1,921 | ⚠️ SB-2024-047 PRIORITY |
| Titan 900 | #4 | AT-E-10034 | 987 | ✅ Normal |

---

## 3. Maintenance Event Log

### April 2026

**2026-04-05 | Engine #3 | Borescope Inspection**
- Technician: J. Martinez (Lic: AT-TECH-0892)
- Finding: Fan blade leading edge erosion confirmed on blades FB-07, FB-12, FB-15
- Measurement: FB-07 chord loss 3.8mm, FB-12 chord loss 4.1mm, FB-15 chord loss 3.2mm
- All exceed Stage 2 threshold (3mm). FB-12 approaching Stage 3 (5mm limit)
- **Action Required:** Fan blade replacement per SB-2024-047 within 50 cycles
- **Parts Ordered:** 22x AT-T900-FB-002, 22x AT-T900-FB-LE-002
- **Parts ETA:** 3 weeks (Singapore MRO)
- Next inspection: Before next revenue flight if cycles exceed 412 total

**2026-04-03 | Engine #1 | Scheduled Inspection**
- Technician: S. Patel (Lic: AT-TECH-1204)
- Finding: Fan blade erosion Stage 2 confirmed. Average chord loss 3.1mm
- EGT margin: 48°C (above 45°C minimum — acceptable)
- Zone 1 vibration: 2.8 IPS (below 3.5 IPS limit — acceptable)
- **Action Required:** SB-2024-047 compliance within 100 cycles
- Parts order placed. ETA 4 weeks.

### March 2026

**2026-03-18 | Engine #2 | Oil System Check**
- Technician: R. Kumar (Lic: AT-TECH-0654)
- Oil consumption: 0.18 litres/hour (within 0.3 limit)
- Oil pressure: 68 psi (within 55–85 range)
- No anomalies detected
- **Status: ✅ Normal**

**2026-03-10 | Engine #4 | Routine A-Check Items**
- All parameters within limits
- Fan blade inspection: No erosion detected (987 cycles — well within 500 cycle interval)
- **Status: ✅ Normal**

### February 2026

**2026-02-22 | Engine #3 | ACMS Data Review**
- EGT trending upward: +7°C over 90-day baseline
- Consistent with Stage 2 fan blade erosion
- Borescope scheduled (completed 2026-04-05)
- **Flag:** Trending data suggested issue 6 weeks before physical inspection

### October 2025

**2025-10-14 | All Engines | C-Check**
- Full heavy maintenance check completed
- Engine #1: Fan blades inspected — all within limits (412 cycles at that time)
- Engine #3: Fan blades inspected — minor Stage 1 erosion noted, monitoring commenced
- All engines returned to service

---

## 4. Open Action Items

| Item | Engine | Action | Due By | Status |
|---|---|---|---|---|
| SB-2024-047 | #3 | Fan blade replacement (PRIORITY) | 50 cycles | 🔴 OPEN |
| SB-2024-047 | #1 | Fan blade replacement | 100 cycles | 🟡 OPEN |
| ACMS Baseline Reset | #3 | After blade replacement | Post-replacement | 🔴 OPEN |
| Zone 1 Vibration Check | #3 | After blade replacement | Post-replacement | 🔴 OPEN |

---

## 5. Parts on Order

| Part Number | Description | Qty | For Engine | ETA | MRO |
|---|---|---|---|---|---|
| AT-T900-FB-002 | Fan blade Rev B | 22 | #3 | 2026-04-28 | Singapore |
| AT-T900-FB-LE-002 | Leading edge strip Rev B | 22 | #3 | 2026-04-28 | Singapore |
| AT-T900-FB-002 | Fan blade Rev B | 22 | #1 | 2026-05-05 | Singapore |
| AT-T900-FB-LE-002 | Leading edge strip Rev B | 22 | #1 | 2026-05-05 | Singapore |

---

## 6. Cross References

- Engine Specs: AT-ENG-T900-SPEC-001
- Service Bulletin: SB-2024-047 (fan blade erosion)
- Service Bulletin: SB-2023-031 (compressor tip rub)
- Parts Catalogue: AT-ENG-T900-IPC-001
- Related Aircraft: XA-002 (same issue, Engine #2)
