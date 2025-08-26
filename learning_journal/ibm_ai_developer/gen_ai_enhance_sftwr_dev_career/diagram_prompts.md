# Diagram Prompts for your Node/Express Register API (avm_ops)

## 1) Mermaid — Sequence (POST /register)
```mermaid
sequenceDiagram
participant U as Client
participant API as Express /register
participant R as Redis (rate/locks)
participant DB as Postgres (users)
U->>API: POST /register {email, password, ...}
API->>R: incr ip:count (60s window)
R-->>API: count
alt >5/min
  API-->>U: 429 RATE_LIMITED
else proceed
  API->>R: get lock(email/ip)
  alt locked
    API-->>U: 403 REG_LOCKED
  else validate fields
    alt invalid
      API->>R: add failure(email/ip)
      API-->>U: 400 REG_INVALID (field)
    else check uniqueness
      API->>DB: SELECT by email/username
      alt exists
        API-->>U: 409 REG_CONFLICT
      else create
        API->>DB: INSERT user
        API->>R: reset failures
        API-->>U: 201 REG_CREATED
      end
    end
  end
end
```

**Prompt template:**  
“Create a Mermaid *sequenceDiagram* for a Node/Express `/register` endpoint with Redis rate limits and lockouts and Postgres for users. Include 429, 403, 400, 409, 201 branches.”

## 2) Mermaid — System Overview (Flowchart)
```mermaid
flowchart LR
  U[User] -->|HTTPS| API[Registration API (Node/Express)]
  API -->|Read/Write| DB[(Postgres: users)]
  API -->|Counters/locks| REDIS[(Redis)]
  subgraph Security
    RL[Rate limit 5/min/IP]
    LK[Lock after 5 fails/15m]
  end
  API -.enforces .-> RL
  API -.enforces .-> LK
```

**Prompt template:**  
“Create a Mermaid flowchart showing user → Node/Express API → Postgres and Redis; annotate rate limit and lockout policies.”

## 3) PlantUML — Sequence
```plantuml
@startuml
actor User as U
participant "Express /register" as API
database Postgres as DB
collections Redis as R

U -> API : POST /register {email, password,...}
API -> R : INCR ip:count (60s)
R --> API : count
alt > 5/min
  API --> U : 429 RATE_LIMITED
else not locked
  API -> R : GET lock(email/ip)
  alt locked
    API --> U : 403 REG_LOCKED
  else validate
    alt invalid
      API -> R : LPUSH failures key
      API --> U : 400 REG_INVALID
    else unique?
      API -> DB : SELECT email/username
      alt exists
        API --> U : 409 REG_CONFLICT
      else ok
        API -> DB : INSERT user
        API -> R : DEL failures key
        API --> U : 201 REG_CREATED
      end
    end
  end
end
@enduml
```

**Prompt template:**  
“Generate a PlantUML sequence diagram for `/register` with Redis (rate+lock) and Postgres. Show all response codes.”

## 4) C4-style Text Prompt (for LLM)
“Produce a C4 *Container* diagram description for ‘AVM Ops’. Containers: Web Client, Registration API (Node/Express), Redis (rate + locks), Postgres (users). Add relations: HTTPS, CRUD users, counters/locks. Output Mermaid or PlantUML.”
