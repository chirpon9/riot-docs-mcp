# Lor-Inventory-v1 API

**Routing Information:** The AMERICAS routing value serves the AMERICAS shard. The EUROPE routing value serves the EUROPE shard. The SEA routing value serves the APAC shard (previously was ASIA and SEA).

---

## Endpoint: GET /lor/inventory/v1/cards/me
**Description:** Return a list of cards owned by the calling user.

### Header Parameters
- **Authorization** (required, String)

### Response: List[CardDto]

#### CardDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| code | string | |
| count | string | |

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
