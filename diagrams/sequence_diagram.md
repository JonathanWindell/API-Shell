```Mermaid
    sequenceDiagram
    participant User
    participant Router as GeneralRouter
    participant Auth as UserManager
    participant Limiter as Limiter (Security)
    participant Redis as Redis Cache

    Note over User, Router: User calls a protected endpoint

    User->>Router: GET /protected (Headers: Bearer Token + x-api-key)
    
    %% Step 1: Authentication (Dependency Injection)
    rect rgb(240, 248, 255)
    Note over Router, Auth: Dependency: get_user_manager
    Router->>Auth: verify_token(Bearer Token)
    
    alt Invalid Token
        Auth-->>Router: Raise HTTP 401
        Router-->>User: 401 Unauthorized
    else Token Valid
        Auth-->>Router: Returns User Object
    end
    end

    %% Step 2: Rate Limiting & API Key (Dependency Injection)
    rect rgb(255, 245, 238)
    Note over Router, Redis: Dependency: check_rate_limiter
    Router->>Limiter: check_rate_limiter()
    Limiter->>Limiter: Validate x-api-key (via Identifier)
    
    alt Invalid API Key
        Limiter-->>Router: Raise HTTP 401
        Router-->>User: 401 Unauthorized
    else Key Valid
        Limiter->>Redis: Increment & Get Count
        Redis-->>Limiter: Current Count (e.g., 3)
        
        alt Over Limit (> Limit)
            Limiter-->>Router: Raise HTTP 429
            Router-->>User: 429 Too Many Requests
        else Under Limit
            Limiter-->>Router: Returns True
        end
    end
    end

    %% Step 3: Success Response
    Router-->>User: Response 200 OK (JSON)
```