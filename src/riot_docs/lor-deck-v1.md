# Lor-Deck-v1 API

**Routing Information:** The AMERICAS routing value serves the AMERICAS shard. The EUROPE routing value serves the EUROPE shard. The SEA routing value serves the APAC shard (previously was ASIA and SEA).

---

## Endpoint: GET /lor/deck/v1/decks/me
**Description:** Get a list of the calling user's decks.

### Header Parameters
- **Authorization** (required, String)

### Response: List[DeckDto]

#### DeckDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | string | |
| name | string | |
| code | string | |

### Response Errors
| HTTP Status Code | Reason |
|------------------|--------|
| 400 | Bad request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Data not found |
| 405 | Method not allowed |
| 415 | Unsupported media type |
| 429 | Rate limit exceeded |
| 500 | Internal server error |
| 502 | Bad gateway |
| 503 | Service unavailable |
| 504 | Gateway timeout |

### Supported Regions
AMERICAS, EUROPE, SEA

---

## Endpoint: POST /lor/deck/v1/decks/me
**Description:** Create a new deck for the calling user.

### Header Parameters
- **Authorization** (required, String)

### Body Parameters
- **deck** (required, NewDeckDto)

#### NewDeckDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| name | string | |
| code | string | |

**Example:**
```json
{
  "code": "",
  "name": ""
}
```

### Response: String

### Response Errors
| HTTP Status Code | Reason |
|------------------|--------|
| 400 | Bad request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Data not found |
| 405 | Method not allowed |
| 415 | Unsupported media type |
| 429 | Rate limit exceeded |
| 500 | Internal server error |
| 502 | Bad gateway |
| 503 | Service unavailable |
| 504 | Gateway timeout |

### Supported Regions
AMERICAS, EUROPE, SEA
