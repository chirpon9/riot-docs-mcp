# Lol-Rso-Match-v1 API

## Endpoint: GET /lol/rso-match/v1/matches/ids
**Description:** Get a list of match ids by player access token - Includes custom matches

### Header Parameters
- **Authorization** (required, string)

### Query Parameters
- **count** (optional, int): Defaults to 20. Valid values: 0 to 100. Number of match ids to return.
- **start** (optional, int): Defaults to 0. Start index.
- **type** (optional, string): Filter the list of match ids by the type of match. This filter is mutually inclusive of the queue filter meaning any match ids returned must match both the queue and type filters. Legal values: ranked, normal, tourney, tutorial
- **queue** (optional, int): Filter the list of match ids by a specific queue id. This filter is mutually inclusive of the type filter meaning any match ids returned must match both the queue and type filters.
- **endTime** (optional, long): Epoch timestamp in seconds.
- **startTime** (optional, long): Epoch timestamp in seconds. The matchlist started storing timestamps on June 16th, 2021. Any matches played before June 16th, 2021 won't be included in the results if the startTime filter is set.

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
AMERICAS, ASIA, EUROPE, SEA

---

## Endpoint: GET /lol/rso-match/v1/matches/{matchId}
**Description:** Get a match by match id

### Header Parameters
- **Authorization** (required, string)

### Path Parameters
- **matchId** (required, string)

### Response: MatchDto

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
AMERICAS, ASIA, EUROPE, SEA

---

## Endpoint: GET /lol/rso-match/v1/matches/{matchId}/timeline
**Description:** Get a match timeline by match id

### Header Parameters
- **Authorization** (required, string)

### Path Parameters
- **matchId** (required, String)

### Response: TimelineDto

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
AMERICAS, ASIA, EUROPE, SEA
