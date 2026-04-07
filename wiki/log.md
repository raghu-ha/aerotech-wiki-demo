# AeroTech Wiki — Operation Log

---

## 2026-04-07 — Ingest: AT_Maintenance_Log_XA001.md

**Source:** raw/AT_Maintenance_Log_XA001.md (AT-MLOG-XA001-2026, April 2026)

**Pages updated:**
- wiki/pages/maintenance-log-xa001.md (stub → full: 4 engines, per-engine status, event log, parts on order, open actions)
- wiki/pages/sb-2023-031.md (subject now confirmed as IP Compressor tip rub)
- wiki/pages/ip-compressor-tip-rub.md (linked to SB-2023-031)

**Notable findings:**
- XA-001 has 4 engines; only #1 and #3 are affected by SB-2024-047
- Engine #3 blade FB-12 at 4.1mm — approaching 5mm Stage 3 threshold; PRIORITY
- Parts on order from Singapore MRO: Engine #3 ETA 2026-04-28, Engine #1 ETA 2026-05-05
- ACMS trend data on Engine #3 showed +7°C EGT rise 6 weeks before physical inspection confirmed erosion
- SB-2023-031 confirmed to address IP Compressor tip rub (from cross-reference in maintenance log)

---

## 2026-04-07 — Re-ingest: AT_Parts_Catalogue_Fan_Assembly.md (2nd)

**Change detected:**
- Fan disc (AT-T900-FD-001): Section 3 updated to **3 units globally** (was 6). Section 4 table still shows 10 — ongoing discrepancy, verify with supply chain.

**Pages updated:**
- wiki/pages/fan-disc-t900.md (stock 6 → 3)
- wiki/pages/fan-assembly-t900.md (stock 6 → 3)

---

## 2026-04-07 — Re-ingest: AT_Parts_Catalogue_Fan_Assembly.md

**Source:** raw/AT_Parts_Catalogue_Fan_Assembly.md (AT-ENG-T900-IPC-001 Rev 4.0)

**Change detected:**
- Fan disc (AT-T900-FD-001): Section 3 now states **6 units globally** (was 10). Section 4 stock table still shows 10 — internal inconsistency in source document. Wiki updated to reflect 6 as operative figure with a verification note.

**Pages updated:**
- wiki/pages/fan-disc-t900.md (stock count 10 → 6, discrepancy flagged)
- wiki/pages/fan-assembly-t900.md (stock count 10 → 6, discrepancy flagged)

---

## 2026-04-07 — Ingest: AT_Parts_Catalogue_Fan_Assembly.md

**Source:** raw/AT_Parts_Catalogue_Fan_Assembly.md (AT-ENG-T900-IPC-001 Rev 4.0, February 2026)

**Pages updated:**
- wiki/pages/fan-assembly-t900.md (added assembly PN, weight, replacement time, special tools, full parts table, supersession notice)
- wiki/pages/fan-blade-t900.md (marked SUPERSEDED; quarantine warning for AT-T900-FB-001 and AT-T900-FB-LE-001)
- wiki/pages/fan-blade-rev-b.md (added AT-T900-FB-DAMP-001, lead times, global stock levels)
- wiki/pages/fan-disc-t900.md (added 20,000-cycle life limit, critical scarcity warning, seal parts, stock levels)

**Pages created:**
- wiki/pages/fan-disc-seals.md (Part — AT-T900-FD-SEAL-001/002, 2,500-cycle life limit)

**Notable findings:**
- Fan disc (AT-T900-FD-001): only 10 units globally, 18-month production lead time — CRITICAL supply risk
- AT-T900-FB-001 and AT-T900-FB-LE-001 formally superseded — quarantine all stock
- New part identified: AT-T900-FB-DAMP-001 (fan blade damper)

---

## 2026-04-07 — Ingest: AT_Service_Bulletin_SB2024_047.md

**Source:** raw/AT_Service_Bulletin_SB2024_047.md (SB-2024-047 Rev 2.0, March 2024)

**Pages updated:**
- wiki/pages/sb-2024-047.md (ServiceBulletin — stub → full article)
- wiki/pages/fan-blade-leading-edge-erosion.md (added failure stages, rejection criteria, fleet data, XA-005)
- wiki/pages/maintenance-log-xa001.md (added per-engine SB status)
- wiki/pages/maintenance-log-xa002.md (added per-engine SB status)

**Pages created:**
- wiki/pages/fan-blade-rev-b.md (Part — AT-T900-FB-002 and associated parts)
- wiki/pages/maintenance-log-xa005.md (MaintenanceLog — SkyLine XA-005, all 4 engines affected)

**Notes:** XA-001 Engine 3 is PRIORITY — replacement required within 50 cycles.  
XA-005 is a newly identified affected aircraft (SkyLine, MSN-0063).

---

## 2026-04-07 — Ingest: AT_Engine_Titan900_Specs.md

**Source:** raw/AT_Engine_Titan900_Specs.md (AT-ENG-T900-SPEC-001 Rev 3.1, January 2026)

**Pages created:**
- wiki/pages/titan-900.md (Engine)
- wiki/pages/fan-assembly-t900.md (Assembly)
- wiki/pages/ip-compressor-t900.md (Assembly)
- wiki/pages/hp-compressor-t900.md (Assembly)
- wiki/pages/combustor-t900.md (Assembly)
- wiki/pages/hp-turbine-t900.md (Assembly)
- wiki/pages/fan-blade-t900.md (Part)
- wiki/pages/fan-disc-t900.md (Part)
- wiki/pages/fan-blade-leading-edge-erosion.md (Issue)
- wiki/pages/ip-compressor-tip-rub.md (Issue)
- wiki/pages/sb-2024-047.md (ServiceBulletin — stub, raw doc available)
- wiki/pages/sb-2023-031.md (ServiceBulletin — stub, no raw doc)
- wiki/pages/maintenance-log-xa001.md (MaintenanceLog — stub, raw doc available)
- wiki/pages/maintenance-log-xa002.md (MaintenanceLog — stub, no raw doc)

**Index:** wiki/INDEX.md created.

**Notes:** Three additional raw documents pending ingestion:
AT_Maintenance_Log_XA001.md, AT_Parts_Catalogue_Fan_Assembly.md, AT_Service_Bulletin_SB2024_047.md
