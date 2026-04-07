"""
AeroTech Wiki Demo — Query Runner
Shows relationship-aware answers across multiple documents.

Run this AFTER ingesting all 4 documents into Claude Code.
These are the demo queries for the guild talk.
"""

DEMO_QUERIES = [
    {
        "id": "Q1",
        "title": "Service Issue Query",
        "query": "What is the current issue with aircraft XA-001 Engine #3 and what needs to be done?",
        "expected_sources": [
            "maintenance-log-xa001.md",
            "sb-2024-047.md",
            "fan-blade-assembly.md",
            "titan-900-engine.md"
        ],
        "why_interesting": "Crosses 4 documents: maintenance log → service bulletin → parts → engine specs"
    },
    {
        "id": "Q2",
        "title": "Parts Availability Query",
        "query": "Are the replacement parts available for the SB-2024-047 compliance work on XA-001?",
        "expected_sources": [
            "parts-catalogue-fan-assembly.md",
            "sb-2024-047.md",
            "maintenance-log-xa001.md"
        ],
        "why_interesting": "Crosses parts catalogue stock → bulletin requirements → maintenance log orders"
    },
    {
        "id": "Q3",
        "title": "Risk Assessment Query",
        "query": "Which aircraft are at highest risk from the fan blade erosion issue and why?",
        "expected_sources": [
            "sb-2024-047.md",
            "fan-blade-erosion.md",
            "maintenance-log-xa001.md",
            "titan-900-engine.md"
        ],
        "why_interesting": "Synthesizes risk across all documents — not possible with single-doc RAG"
    },
    {
        "id": "Q4",
        "title": "Drift Demo Query",
        "query": "What is the current stock level of fan disc AT-T900-FD-001 and is it a concern?",
        "expected_sources": [
            "parts-catalogue-fan-assembly.md"
        ],
        "why_interesting": "Run this BEFORE and AFTER updating stock levels to show TruthDrift catching the drift"
    }
]


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  AeroTech Wiki — Guild Talk Demo Queries")
    print("="*60)
    print("\nPaste each query into Claude Code at the > prompt:")
    print("Format: Query: <question>\n")

    for q in DEMO_QUERIES:
        print(f"\n{'─'*60}")
        print(f"  [{q['id']}] {q['title']}")
        print(f"{'─'*60}")
        print(f"\n  Query:\n  \"{q['query']}\"")
        print(f"\n  Expected sources crossed:")
        for s in q['expected_sources']:
            print(f"    → {s}")
        print(f"\n  Why interesting: {q['why_interesting']}")

    print("\n" + "="*60)
    print("  TruthDrift Demo:")
    print("="*60)
    print("""
  Step 1: Snapshot the parts catalogue
    python3 truthdrift.py snapshot wiki/pages/parts-catalogue-fan-assembly.md

  Step 2: Update fan disc stock in raw/AT_Parts_Catalogue_Fan_Assembly.md
    Change: 10 units globally → 6 units globally (simulate stock depletion)

  Step 3: Re-ingest
    In Claude Code: Ingest raw/AT_Parts_Catalogue_Fan_Assembly.md

  Step 4: Check drift
    python3 truthdrift.py check wiki/pages/parts-catalogue-fan-assembly.md

  Step 5: Run Q4 again
    "What is the current stock level of AT-T900-FD-001?"
    → Answer should now reflect updated stock
    → TruthDrift flags the previous answer as STALE
""")
    print("="*60)
