# Lor-Match-v1 API

**Routing Information:** The AMERICAS routing value serves the AMERICAS shard. The EUROPE routing value serves the EUROPE shard. The SEA routing value serves the APAC shard (previously was ASIA and SEA).

---

## Endpoint: GET /lor/match/v1/matches/by-puuid/{puuid}/ids
**Description:** Get a list of match ids by PUUID

### Path Parameters
- **puuid** (optional, String)

### Response: List[string]

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
AMERICAS, APAC, EUROPE, SEA

---

## Endpoint: GET /lor/match/v1/matches/{matchId}
**Description:** Get match by id

### Path Parameters
- **matchId** (required, String)

### Response: MatchDto

#### MatchDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| metadata | MetadataDto | Match metadata. |
| info | InfoDto | Match info. |

#### MetadataDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| data_version | string | Match data version. |
| match_id | string | Match id. |
| participants | List[string] | A list of participant PUUIDs. |

#### InfoDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| game_mode | string | Legal values: Constructed, Expeditions, Tutorial |
| game_type | string | Legal values: Ranked, Normal, AI, Tutorial, VanillaTrial, Singleton, StandardGauntlet |
| game_start_time_utc | string | |
| game_version | string | |
| game_format | string | Legal values: standard, eternal |
| players | List[PlayerDto] | |
| total_turn_count | int | Total turns taken by both players. |

#### PlayerDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | |
| deck_id | string | |
| deck_code | string | Code for the deck played. Refer to LOR documentation for details on deck codes. |
| factions | List[string] | |
| game_outcome | string | |
| order_of_play | int | The order in which the players took turns. |

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
AMERICAS, APAC, EUROPE, SEA
