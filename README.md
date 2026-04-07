# AeroTech Wiki Demo 🛩️

> Demonstrating Karpathy's LLM Wiki Pattern + TruthDrift  
> for multi-document relationship-aware queries in a manufacturing/MRO context.

---

## What This Demo Shows

1. **Multi-document relationships** — query across engine specs, service bulletins, parts catalogue, and maintenance logs simultaneously
2. **Relationship-aware answers** — not RAG fragments, but synthesized answers that traverse document connections
3. **Drift detection** — update one document, TruthDrift flags stale answers

---

## Documents in `raw/`

| File | What it contains |
|---|---|
| `AT_Engine_Titan900_Specs.md` | Engine specs, assemblies, known issues |
| `AT_Service_Bulletin_SB2024_047.md` | Mandatory fan blade replacement bulletin |
| `AT_Parts_Catalogue_Fan_Assembly.md` | Parts, stock levels, superseded parts |
| `AT_Maintenance_Log_XA001.md` | Aircraft service history, open actions |

---

## Step 1 — Set Up Wiki

```bash
cd aerotech-demo
claude
```

In Claude Code:
```
Read CLAUDE.md then ingest all files in raw/ one by one
```

Or one at a time:
```
Ingest raw/AT_Engine_Titan900_Specs.md
Ingest raw/AT_Service_Bulletin_SB2024_047.md
Ingest raw/AT_Parts_Catalogue_Fan_Assembly.md
Ingest raw/AT_Maintenance_Log_XA001.md
```

---

## Step 2 — Run Demo Queries

```
Query: What is the issue with XA-001 Engine #3 and what needs to be done?
```

Watch it traverse: maintenance log → service bulletin → parts → engine specs.

```
Query: Are replacement parts available for SB-2024-047 on XA-001?
```

Watch it cross: parts stock → bulletin requirements → maintenance orders.

```
Query: Which aircraft are at highest risk from fan blade erosion?
```

Watch it synthesize risk across ALL documents.

---

## Step 3 — TruthDrift Demo

```bash
# Snapshot current parts catalogue wiki article
python3 ../truthdrift/truthdrift.py snapshot wiki/pages/parts-catalogue-fan-assembly.md

# Simulate stock depletion — edit raw/AT_Parts_Catalogue_Fan_Assembly.md
# Change fan disc stock from 10 → 6 units globally

# Re-ingest in Claude Code
# Ingest raw/AT_Parts_Catalogue_Fan_Assembly.md

# Check drift
python3 ../truthdrift/truthdrift.py check wiki/pages/parts-catalogue-fan-assembly.md
```

**Result:** TruthDrift flags the parts article as drifted — previous stock answer is now stale.

---

## The Guild Talk Story

```
"I asked: What's wrong with Engine #3 on aircraft XA-001?

The wiki read the maintenance log.
Found the fan blade erosion issue.
Crossed to the service bulletin.
Found the replacement parts needed.
Crossed to the parts catalogue.
Found the stock levels and ETA.
Crossed back to the engine specs.
Confirmed the EGT and vibration limits.

One question. Four documents. One synthesized answer.

Then I updated the parts stock.
TruthDrift flagged the previous answer as stale.
Automatically. In seconds.

No RAG. No vector DB. No embeddings.
Just Markdown files and a schema."
```

---

## See All Demo Queries

```bash
python3 demo_queries.py
```

---

*Built by Raghavendra — Karpathy LLM Wiki Pattern + TruthDrift POC*
