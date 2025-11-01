# Orchestration — Quote Flow (Mermaid, fixed)

This version splits the diagrams into **two Mermaid blocks** (flowchart + sequence). Most renderers (Obsidian, VS Code) require one diagram per block.

## Flowchart
```mermaid
flowchart LR
    U[CSR in CRM] -->|Create Quote| O["Orchestrator (Temporal/Camunda/StepFn)"]
    O --> V["Validate (rules-svc)"]
    V --> P["Pricing (pricing-svc)"]
    P --> A{Within policy?}
    A -->|Yes| G["DocGen (docgen-svc)"]
    A -->|No| H[Human Approval Task]
    H --> G
    G --> ES{E-Sign required?}
    ES -->|Yes| S[E-Sign]
    ES -->|No| E[ERP Sync]
    S --> E
    E --> C[Update CRM]
    C --> Q[(Quote Record + PDF link)]
    O -.->|legacy needed| R[RPA Adapter/Bots]
    R --> O
    C -->|status/events| O
```

## Sequence
```mermaid
sequenceDiagram
  autonumber
  participant CRM
  participant ORCH as Orchestrator
  participant RULES as rules-svc
  participant PRICE as pricing-svc
  participant DOC as docgen-svc
  participant ESIGN as e-sign
  participant ERP as erp-sink

  CRM->>ORCH: POST /workflows/quote.start {quote_id, customer_id, items}
  ORCH->>RULES: POST /validate {customer, entitlements, credit}
  RULES-->>ORCH: 200 {ok, reasons[]}
  ORCH->>PRICE: POST /quote {items, customer, geo}
  PRICE-->>ORCH: 200 {lines[], discounts[], tax, total}
  ORCH->>CRM: PATCH quote draft + totals (idempotent)
  alt within policy
    ORCH->>DOC: POST /render {template_id, data}
    DOC-->>ORCH: 200 {url, sha256}
  else needs approval
    ORCH->>CRM: Create Human Task (approval queue)
    CRM-->>ORCH: Approved/Rejected
    ORCH->>DOC: POST /render
    DOC-->>ORCH: 200 {url, sha256}
  end
  opt e-sign enabled
    ORCH->>ESIGN: POST /envelopes {doc_url, recipients[]}
    ESIGN-->>ORCH: signed=true, envelope_id
  end
  ORCH->>ERP: POST /orders {quote_id, totals, ship_to}
  ERP-->>ORCH: 201 {order_id}
  ORCH->>CRM: PATCH quote accepted + order_id
```
