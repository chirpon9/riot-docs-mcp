# Champion-v3 API

## Endpoint: GET /lol/platform/v3/champion-rotations
**Description:** Returns champion rotations, including free-to-play and low-level free-to-play rotations (REST)

### Response: ChampionInfo

| Field | Data Type | Description |
|-------|-----------|-------------|
| maxNewPlayerLevel | int | |
| freeChampionIdsForNewPlayers | List[int] | |
| freeChampionIds | List[int] | |

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
BR1, EUN1, EUW1, JP1, KR, LA1, LA2, ME1, NA1, OC1, RU, SG2, TR1, TW2, VN2
