```Mermaid
    sequenceDiagram
    participant User
    participant Main
    participant Identifier
    participant Limiter
    participant Storage
    participant Redis
    participant PersonData

    User->>Main: Request Data (Header)
    Main->>Identifier: Validate Key
    
    alt Invalid Key
        Identifier-->>Main: Error (401 Unauthorized)
        Main-->>User: Response 401
    else Valid Key
        Identifier-->>Main: Key OK (Return Key)
        
        Main->>Limiter: Check Rate Limit (Key)
        Limiter->>Storage: Increment Counter
        Storage->>Redis: INCR + EXPIRE
        Redis-->>Storage: New Count (t.ex. 5)
        Storage-->>Limiter: 5
        
        alt Over Limit ( > 100)
            Limiter-->>Main: Error (429 Too Many Requests)
            Main-->>User: Response 429
        else Under Limit
            Limiter-->>Main: OK (Allow)
            
            Main->>PersonData: Generate Data
            PersonData-->>Main: JSON Object
            Main-->>User: Response 200 OK (JSON)
        end
    end
```