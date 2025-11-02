# Tft-League-v1 API

## Endpoint: GET /tft/league/v1/by-puuid/{puuid}
**Description:** Get league entries in all queues for a given puuid

### Path Parameters
- **puuid** (required, string)

### Response: Set[LeagueEntryDTO]

#### LeagueEntryDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Player Universal Unique Identifier. Exact length of 78 characters. (Encrypted) |
| leagueId | string | Not included for the RANKED_TFT_TURBO queueType. |
| queueType | string | |
| ratedTier | string | Only included for the RANKED_TFT_TURBO queueType. Legal values: ORANGE, PURPLE, BLUE, GREEN, GRAY |
| ratedRating | int | Only included for the RANKED_TFT_TURBO queueType. |
| tier | string | Not included for the RANKED_TFT_TURBO queueType. |
| rank | string | The player's division within a tier. Not included for the RANKED_TFT_TURBO queueType. |
| leaguePoints | int | Not included for the RANKED_TFT_TURBO queueType. |
| wins | int | First placement. |
| losses | int | Second through eighth placement. |
| hotStreak | boolean | Not included for the RANKED_TFT_TURBO queueType. |
| veteran | boolean | Not included for the RANKED_TFT_TURBO queueType. |
| freshBlood | boolean | Not included for the RANKED_TFT_TURBO queueType. |
| inactive | boolean | Not included for the RANKED_TFT_TURBO queueType. |
| miniSeries | MiniSeriesDTO | Not included for the RANKED_TFT_TURBO queueType. |

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

## Endpoint: GET /tft/league/v1/challenger
**Description:** Get the challenger league.

### Query Parameters
- **queue** (optional, string): Defaults to RANKED_TFT. Legal values: RANKED_TFT, RANKED_TFT_DOUBLE_UP

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
| wins | int | First placement. |
| miniSeries | MiniSeriesDTO | |
| inactive | boolean | |
| veteran | boolean | |
| hotStreak | boolean | |
| rank | string | |
| leaguePoints | int | |
| losses | int | Second through eighth placement. |
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

## Endpoint: GET /tft/league/v1/entries/{tier}/{division}
**Description:** Get all the league entries.

### Path Parameters
- **tier** (required, string): Legal values: DIAMOND, EMERALD, PLATINUM, GOLD, SILVER, BRONZE, IRON
- **division** (required, string): Legal values: I, II, III, IV

### Query Parameters
- **queue** (optional, string): Defaults to RANKED_TFT. Legal values: RANKED_TFT, RANKED_TFT_DOUBLE_UP
- **page** (optional, int): Defaults to 1. Starts with page 1.

### Response: Set[LeagueEntryDTO]

#### LeagueEntryDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Player Universal Unique Identifier. Exact length of 78 characters. (Encrypted) |
| leagueId | string | Not included for the RANKED_TFT_TURBO queueType. |
| queueType | string | |
| ratedTier | string | Only included for the RANKED_TFT_TURBO queueType. Legal values: ORANGE, PURPLE, BLUE, GREEN, GRAY |
| ratedRating | int | Only included for the RANKED_TFT_TURBO queueType. |
| tier | string | Not included for the RANKED_TFT_TURBO queueType. |
| rank | string | The player's division within a tier. Not included for the RANKED_TFT_TURBO queueType. |
| leaguePoints | int | Not included for the RANKED_TFT_TURBO queueType. |
| wins | int | First placement. |
| losses | int | Second through eighth placement. |
| hotStreak | boolean | Not included for the RANKED_TFT_TURBO queueType. |
| veteran | boolean | Not included for the RANKED_TFT_TURBO queueType. |
| freshBlood | boolean | Not included for the RANKED_TFT_TURBO queueType. |
| inactive | boolean | Not included for the RANKED_TFT_TURBO queueType. |
| miniSeries | MiniSeriesDTO | Not included for the RANKED_TFT_TURBO queueType. |

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

## Endpoint: GET /tft/league/v1/grandmaster
**Description:** Get the grandmaster league.

### Query Parameters
- **queue** (optional, string): Defaults to RANKED_TFT. Legal values: RANKED_TFT, RANKED_TFT_DOUBLE_UP

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
| wins | int | First placement. |
| miniSeries | MiniSeriesDTO | |
| inactive | boolean | |
| veteran | boolean | |
| hotStreak | boolean | |
| rank | string | |
| leaguePoints | int | |
| losses | int | Second through eighth placement. |
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

## Endpoint: GET /tft/league/v1/leagues/{leagueId}
**Description:** Get league with given ID, including inactive entries.

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
| wins | int | First placement. |
| miniSeries | MiniSeriesDTO | |
| inactive | boolean | |
| veteran | boolean | |
| hotStreak | boolean | |
| rank | string | |
| leaguePoints | int | |
| losses | int | Second through eighth placement. |
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

## Endpoint: GET /tft/league/v1/master
**Description:** Get the master league.

### Query Parameters
- **queue** (optional, string): Defaults to RANKED_TFT. Legal values: RANKED_TFT, RANKED_TFT_DOUBLE_UP

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
| wins | int | First placement. |
| miniSeries | MiniSeriesDTO | |
| inactive | boolean | |
| veteran | boolean | |
| hotStreak | boolean | |
| rank | string | |
| leaguePoints | int | |
| losses | int | Second through eighth placement. |
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

## Endpoint: GET /tft/league/v1/rated-ladders/{queue}/top
**Description:** Get the top rated ladder for given queue

### Path Parameters
- **queue** (required, string): Legal values: RANKED_TFT_TURBO

### Response: List[TopRatedLadderEntryDto]

#### TopRatedLadderEntryDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Player's encrypted puuid. |
| ratedTier | string | Legal values: ORANGE, PURPLE, BLUE, GREEN, GRAY |
| ratedRating | int | |
| wins | int | First placement. |
| previousUpdateLadderPosition | int | |

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
