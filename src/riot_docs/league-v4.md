# League-v4 API

## Endpoint: GET /lol/league/v4/challengerleagues/by-queue/{queue}
**Description:** Get the challenger league for given queue.

### Path Parameters
- **queue** (required, string): Legal values: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT

### Response: LeagueListDTO

#### LeagueListDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| leagueId | string | |
| entries | List[LeagueItemDTO] | |
| tier | string | |
| name | string | |
| queue | string | |

#### LeagueItemDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| freshBlood | boolean | |
| wins | int | Winning team on Summoners Rift. |
| miniSeries | MiniSeriesDTO | |
| inactive | boolean | |
| veteran | boolean | |
| hotStreak | boolean | |
| rank | string | |
| leaguePoints | int | |
| losses | int | Losing team on Summoners Rift. |
| puuid | string | Player's encrypted puuid. |

#### MiniSeriesDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| losses | int | |
| progress | string | |
| target | int | |
| wins | int | |

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

## Endpoint: GET /lol/league/v4/entries/by-puuid/{encryptedPUUID}
**Description:** Get league entries in all queues for a given puuid

### Path Parameters
- **encryptedPUUID** (required, string)

### Response: Set[LeagueEntryDTO]

#### LeagueEntryDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| leagueId | string | |
| puuid | string | Player's encrypted puuid. |
| queueType | string | |
| tier | string | |
| rank | string | The player's division within a tier. |
| leaguePoints | int | |
| wins | int | Winning team on Summoners Rift. |
| losses | int | Losing team on Summoners Rift. |
| hotStreak | boolean | |
| veteran | boolean | |
| freshBlood | boolean | |
| inactive | boolean | |
| miniSeries | MiniSeriesDTO | |

#### MiniSeriesDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| losses | int | |
| progress | string | |
| target | int | |
| wins | int | |

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

## Endpoint: GET /lol/league/v4/entries/{queue}/{tier}/{division}
**Description:** Get all the league entries.

### Path Parameters
- **queue** (required, string): Note that the queue value must be a valid ranked queue. Legal values: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT
- **tier** (required, string): Legal values: DIAMOND, EMERALD, PLATINUM, GOLD, SILVER, BRONZE, IRON
- **division** (required, string): Legal values: I, II, III, IV

### Query Parameters
- **page** (optional, int): Defaults to 1. Starts with page 1.

### Response: Set[LeagueEntryDTO]

#### LeagueEntryDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| leagueId | string | |
| puuid | string | Player's encrypted puuid. |
| queueType | string | |
| tier | string | |
| rank | string | The player's division within a tier. |
| leaguePoints | int | |
| wins | int | Winning team on Summoners Rift. |
| losses | int | Losing team on Summoners Rift. |
| hotStreak | boolean | |
| veteran | boolean | |
| freshBlood | boolean | |
| inactive | boolean | |
| miniSeries | MiniSeriesDTO | |

#### MiniSeriesDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| losses | int | |
| progress | string | |
| target | int | |
| wins | int | |

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

## Endpoint: GET /lol/league/v4/grandmasterleagues/by-queue/{queue}
**Description:** Get the grandmaster league of a specific queue.

### Path Parameters
- **queue** (required, string): Legal values: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT

### Response: LeagueListDTO

#### LeagueListDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| leagueId | string | |
| entries | List[LeagueItemDTO] | |
| tier | string | |
| name | string | |
| queue | string | |

#### LeagueItemDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| freshBlood | boolean | |
| wins | int | Winning team on Summoners Rift. |
| miniSeries | MiniSeriesDTO | |
| inactive | boolean | |
| veteran | boolean | |
| hotStreak | boolean | |
| rank | string | |
| leaguePoints | int | |
| losses | int | Losing team on Summoners Rift. |
| puuid | string | Player's encrypted puuid. |

#### MiniSeriesDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| losses | int | |
| progress | string | |
| target | int | |
| wins | int | |

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

## Endpoint: GET /lol/league/v4/leagues/{leagueId}
**Description:** Get league with given ID, including inactive entries.

**Implementation Notes:** Consistently looking up league ids that don't exist will result in a blacklist.

### Path Parameters
- **leagueId** (required, string): The UUID of the league.

### Response: LeagueListDTO

#### LeagueListDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| leagueId | string | |
| entries | List[LeagueItemDTO] | |
| tier | string | |
| name | string | |
| queue | string | |

#### LeagueItemDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| freshBlood | boolean | |
| wins | int | Winning team on Summoners Rift. |
| miniSeries | MiniSeriesDTO | |
| inactive | boolean | |
| veteran | boolean | |
| hotStreak | boolean | |
| rank | string | |
| leaguePoints | int | |
| losses | int | Losing team on Summoners Rift. |
| puuid | string | Player's encrypted puuid. |

#### MiniSeriesDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| losses | int | |
| progress | string | |
| target | int | |
| wins | int | |

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

## Endpoint: GET /lol/league/v4/masterleagues/by-queue/{queue}
**Description:** Get the master league for given queue.

### Path Parameters
- **queue** (required, string): Legal values: RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT

### Response: LeagueListDTO

#### LeagueListDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| leagueId | string | |
| entries | List[LeagueItemDTO] | |
| tier | string | |
| name | string | |
| queue | string | |

#### LeagueItemDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| freshBlood | boolean | |
| wins | int | Winning team on Summoners Rift. |
| miniSeries | MiniSeriesDTO | |
| inactive | boolean | |
| veteran | boolean | |
| hotStreak | boolean | |
| rank | string | |
| leaguePoints | int | |
| losses | int | Losing team on Summoners Rift. |
| puuid | string | Player's encrypted puuid. |

#### MiniSeriesDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| losses | int | |
| progress | string | |
| target | int | |
| wins | int | |

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
