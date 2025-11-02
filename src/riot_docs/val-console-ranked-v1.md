# Val-Console-Ranked-v1 API

## Endpoint: GET /val/console/ranked/v1/leaderboards/by-act/{actId}
**Description:** Get leaderboard for the competitive queue.

### Path Parameters
- **actId** (required, string): Act ids can be found using the val-content API.

### Query Parameters
- **platformType** (required, string): Legal values: playstation, xbox
- **startIndex** (optional, int): Defaults to 0.
- **size** (optional, int): Defaults to 200. Valid values: 1 to 200.

### Response: LeaderboardDto

#### LeaderboardDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| actId | string | The act id for the given leaderboard. Act ids can be found using the val-content API. |
| totalPlayers | long | The total number of players in the leaderboard. |
| query | string | |
| shard | string | The shard for the given leaderboard. |
| players | List[PlayerDto] | |
| tierDetails | List[TierDto] | |

#### PlayerDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | This field may be omitted if the player has been anonymized. |
| gameName | string | This field may be omitted if the player has been anonymized. |
| tagLine | string | This field may be omitted if the player has been anonymized. |
| leaderboardRank | long | |
| rankedRating | long | |
| numberOfWins | long | |

#### TierDto

| Field | Data Type | Description |
|-------|-----------|-------------|
|  |  | |

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
AP, EU, NA
