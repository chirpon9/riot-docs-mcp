# Clash-v1 API

## Endpoint: GET /lol/clash/v1/players/by-puuid/{puuid}
**Description:** Get players by puuid

**Implementation Notes:** This endpoint returns a list of active Clash players for a given PUUID. If a summoner registers for multiple tournaments at the same time (e.g., Saturday and Sunday) then both registrations would appear in this list.

### Path Parameters
- **puuid** (required, string)

### Response: List[PlayerDto]

#### PlayerDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | |
| teamId | string | |
| position | string | Legal values: UNSELECTED, FILL, TOP, JUNGLE, MIDDLE, BOTTOM, UTILITY |
| role | string | Legal values: CAPTAIN, MEMBER |

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

---

## Endpoint: GET /lol/clash/v1/teams/{teamId}
**Description:** Get team by ID.

### Path Parameters
- **teamId** (required, string)

### Response: TeamDto

#### TeamDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | string | |
| tournamentId | int | |
| name | string | |
| iconId | int | |
| tier | int | |
| captain | string | Summoner ID of the team captain. |
| abbreviation | string | |
| players | List[PlayerDto] | Team members. |

#### PlayerDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | |
| position | string | Legal values: UNSELECTED, FILL, TOP, JUNGLE, MIDDLE, BOTTOM, UTILITY |
| role | string | Legal values: CAPTAIN, MEMBER |

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

---

## Endpoint: GET /lol/clash/v1/tournaments
**Description:** Get all active or upcoming tournaments.

Returns a list of active and upcoming tournaments.

### Response: List[TournamentDto]

#### TournamentDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | int | |
| themeId | int | |
| nameKey | string | |
| nameKeySecondary | string | |
| schedule | List[TournamentPhaseDto] | Tournament phase. |

#### TournamentPhaseDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | int | |
| registrationTime | long | |
| startTime | long | |
| cancelled | boolean | |

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

---

## Endpoint: GET /lol/clash/v1/tournaments/by-team/{teamId}
**Description:** Get tournament by team ID.

### Path Parameters
- **teamId** (required, string)

### Response: TournamentDto

#### TournamentDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | int | |
| themeId | int | |
| nameKey | string | |
| nameKeySecondary | string | |
| schedule | List[TournamentPhaseDto] | Tournament phase. |

#### TournamentPhaseDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | int | |
| registrationTime | long | |
| startTime | long | |
| cancelled | boolean | |

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

---

## Endpoint: GET /lol/clash/v1/tournaments/{tournamentId}
**Description:** Get tournament by ID.

### Path Parameters
- **tournamentId** (required, int)

### Response: TournamentDto

#### TournamentDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | int | |
| themeId | int | |
| nameKey | string | |
| nameKeySecondary | string | |
| schedule | List[TournamentPhaseDto] | Tournament phase. |

#### TournamentPhaseDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | int | |
| registrationTime | long | |
| startTime | long | |
| cancelled | boolean | |

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
