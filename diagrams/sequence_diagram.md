```Mermaid
    sequenceDiagram
    participant User
    participant Main as Main (FastAPI)
    participant Auth as Auth (JWT)
    participant Sec as Limiter & Identifier
    participant Redis

    Note over User, Main: User calls a protected endpoint

    User->>Main: GET /protected (Header: Token + x-api-key)
    
    %% Step 1: JWT Validation (Automatic via Depends)
    Main->>Auth: Validate Token (Bearer)
    
    alt Invalid Token
        Auth-->>Main: Exception
        Main-->>User: 401 Unauthorized
    else Token OK
        Auth-->>Main: User: "admin"
    end

    %% Step 2: Rate Limiting & API Key (Inside check_rate_limiter)
    Main->>Sec: check_rate_limiter()
    Sec->>Sec: Validate x-api-key (Identifier)
    
    alt Invalid Key
        Sec-->>Main: Exception
        Main-->>User: 401 Unauthorized
    else Key OK
        Sec->>Redis: Increment Count
        Redis-->>Sec: New Count (e.g. 2)
        
        alt Over Limit (> Limit)
            Sec-->>Main: Exception
            Main-->>User: 429 Too Many Requests
        else Under Limit
            Sec-->>Main: Return True (Allowed)
            
            %% Step 3: Success
            Main-->>User: Response 200 OK (UserResponse JSON)
        end
    end
```