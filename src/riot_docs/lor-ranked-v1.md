# Lor-Ranked-v1 API

**Routing Information:** The AMERICAS routing value serves the AMERICAS shard. The EUROPE routing value serves the EUROPE shard. The SEA routing value serves the APAC shard (previously was ASIA and SEA).

---

## Endpoint: GET /lor/ranked/v1/leaderboards
**Description:** Get the players in Master tier.

**Implementation Notes:** The leaderboard is updated once an hour.

### Response: LeaderboardDto

#### LeaderboardDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| players | List[PlayerDto] | A list of players in Master tier. |

#### PlayerDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| name | string | |
| rank | int | |
| lp | int | League points. |

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
