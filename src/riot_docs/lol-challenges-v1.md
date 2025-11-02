# Lol-Challenges-v1 API

## Endpoint: GET /lol/challenges/v1/challenges/config
**Description:** List of all basic challenge configuration information (includes all translations for names and descriptions)

### Response: List[ChallengeConfigInfoDto]

#### ChallengeConfigInfoDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | long | |
| localizedNames | Map[String, Map[String, string]] | |
| state | State | |
| tracking | Tracking | |
| startTimestamp | long | |
| endTimestamp | long | |
| leaderboard | boolean | |
| thresholds | Map[String, double] | |

#### State
DISABLED - not visible and not calculated, HIDDEN - not visible, but calculated, ENABLED - visible and calculated, ARCHIVED - visible, but not calculated

#### Tracking
LIFETIME - stats are incremented without reset, SEASON - stats are accumulated by season and reset at the beginning of new season

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
BR1, EUN1, EUW1, JP1, KR, LA1, LA2, ME1, NA1, OC1, PBE1, RU, SG2, TR1, TW2, VN2

---

## Endpoint: GET /lol/challenges/v1/challenges/percentiles
**Description:** Map of level to percentile of players who have achieved it - keys: ChallengeId -> Season -> Level -> percentile of players who achieved it

### Response: Map[Long, Map[Integer, Map[Level, Double]]]

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
BR1, EUN1, EUW1, JP1, KR, LA1, LA2, ME1, NA1, OC1, PBE1, RU, SG2, TR1, TW2, VN2

---

## Endpoint: GET /lol/challenges/v1/challenges/{challengeId}/config
**Description:** Get challenge configuration (REST)

### Path Parameters
- **challengeId** (required, long)

### Response: ChallengeConfigInfoDto

#### ChallengeConfigInfoDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | long | |
| localizedNames | Map[String, Map[String, string]] | |
| state | State | |
| tracking | Tracking | |
| startTimestamp | long | |
| endTimestamp | long | |
| leaderboard | boolean | |
| thresholds | Map[String, double] | |

#### State
DISABLED - not visible and not calculated, HIDDEN - not visible, but calculated, ENABLED - visible and calculated, ARCHIVED - visible, but not calculated

#### Tracking
LIFETIME - stats are incremented without reset, SEASON - stats are accumulated by season and reset at the beginning of new season

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
BR1, EUN1, EUW1, JP1, KR, LA1, LA2, ME1, NA1, OC1, PBE1, RU, SG2, TR1, TW2, VN2

---

## Endpoint: GET /lol/challenges/v1/challenges/{challengeId}/leaderboards/by-level/{level}
**Description:** Return top players for each level. Level must be MASTER, GRANDMASTER or CHALLENGER.

### Path Parameters
- **challengeId** (required, long)
- **level** (required, string): Legal values: NONE, IRON, BRONZE, SILVER, GOLD, PLATINUM, DIAMOND, MASTER, GRANDMASTER, CHALLENGER, HIGHEST_NOT_LEADERBOARD_ONLY, HIGHEST, LOWEST

### Query Parameters
- **limit** (optional, int)

### Response: List[ApexPlayerInfoDto]

#### ApexPlayerInfoDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | |
| value | double | |
| position | int | |

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
BR1, EUN1, EUW1, JP1, KR, LA1, LA2, ME1, NA1, OC1, PBE1, RU, SG2, TR1, TW2, VN2

---

## Endpoint: GET /lol/challenges/v1/challenges/{challengeId}/percentiles
**Description:** Map of level to percentile of players who have achieved it

### Path Parameters
- **challengeId** (required, long)

### Response: Map[Level, double]

#### Level
0 NONE, 1 IRON, 2 BRONZE, 3 SILVER, 4 GOLD, 5 PLATINUM, 6 DIAMOND, 7 MASTER, 8 GRANDMASTER, 9 CHALLENGER

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
BR1, EUN1, EUW1, JP1, KR, LA1, LA2, ME1, NA1, OC1, PBE1, RU, SG2, TR1, TW2, VN2

---

## Endpoint: GET /lol/challenges/v1/player-data/{puuid}
**Description:** Returns player information with list of all progressed challenges (REST)

### Path Parameters
- **puuid** (required, string)

### Response: PlayerInfoDto

#### PlayerInfoDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| challenges | List[ChallengeInfoDto] | |
| preferences | PlayerClientPreferencesDto | |
| totalPoints | ChallengePointDto | |
| categoryPoints | Map[String, ChallengePointDto] | |

#### ChallengeInfoDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| percentile | double | |
| playersInLevel | int | |
| achievedTime | long | |
| value | double | |
| challengeId | long | |
| level | string | Legal values: NONE, IRON, BRONZE, SILVER, GOLD, PLATINUM, DIAMOND, MASTER, GRANDMASTER, CHALLENGER, HIGHEST_NOT_LEADERBOARD_ONLY, HIGHEST, LOWEST |
| position | int | |

#### PlayerClientPreferencesDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| bannerAccent | string | |
| title | string | |
| challengeIds | List[string] | |
| crestBorder | string | |
| prestigeCrestBorderLevel | int | |

#### ChallengePointDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| level | string | |
| current | long | |
| max | long | |
| precentile | long | |

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
BR1, EUN1, EUW1, JP1, KR, LA1, LA2, ME1, NA1, OC1, PBE1, RU, SG2, TR1, TW2, VN2
