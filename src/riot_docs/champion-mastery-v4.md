# Champion-Mastery-v4 API

## Endpoint: GET /lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}
**Description:** Get all champion mastery entries sorted by number of champion points descending.

### Path Parameters
- **encryptedPUUID** (required, string)

### Response: List[ChampionMasteryDto]

#### ChampionMasteryDto
This object contains single Champion Mastery information for player and champion combination.

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Player Universal Unique Identifier. Exact length of 78 characters. (Encrypted) |
| championPointsUntilNextLevel | long | Number of points needed to achieve next level. Zero if player reached maximum champion level for this champion. |
| chestGranted | boolean | Is chest granted for this champion or not in current season. |
| championId | long | Champion ID for this entry. |
| lastPlayTime | long | Last time this champion was played by this player - in Unix milliseconds time format. |
| championLevel | int | Champion level for specified player and champion combination. |
| championPoints | int | Total number of champion points for this player and champion combination - they are used to determine championLevel. |
| championPointsSinceLastLevel | long | Number of points earned since current level has been achieved. |
| markRequiredForNextLevel | int | |
| championSeasonMilestone | int | |
| nextSeasonMilestone | NextSeasonMilestonesDto | |
| tokensEarned | int | The token earned for this champion at the current championLevel. When the championLevel is advanced the tokensEarned resets to 0. |
| milestoneGrades | List[string] | |

#### NextSeasonMilestonesDto
This object contains required next season milestone information.

| Field | Data Type | Description |
|-------|-----------|-------------|
| requireGradeCounts | object | |
| rewardMarks | int | Reward marks. |
| bonus | boolean | Bonus. |
| rewardConfig | RewardConfigDto | Reward configuration. |

#### RewardConfigDto
This object contains required reward config information.

| Field | Data Type | Description |
|-------|-----------|-------------|
| rewardValue | string | Reward value |
| rewardType | string | Reward type |
| maximumReward | int | Maximun reward |

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

## Endpoint: GET /lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}/by-champion/{championId}
**Description:** Get a champion mastery by puuid and champion ID.

### Path Parameters
- **encryptedPUUID** (required, string)
- **championId** (required, integer): Champion ID to retrieve Champion Mastery.

### Response: ChampionMasteryDto

#### ChampionMasteryDto
This object contains single Champion Mastery information for player and champion combination.

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Player Universal Unique Identifier. Exact length of 78 characters. (Encrypted) |
| championPointsUntilNextLevel | long | Number of points needed to achieve next level. Zero if player reached maximum champion level for this champion. |
| chestGranted | boolean | Is chest granted for this champion or not in current season. |
| championId | long | Champion ID for this entry. |
| lastPlayTime | long | Last time this champion was played by this player - in Unix milliseconds time format. |
| championLevel | int | Champion level for specified player and champion combination. |
| championPoints | int | Total number of champion points for this player and champion combination - they are used to determine championLevel. |
| championPointsSinceLastLevel | long | Number of points earned since current level has been achieved. |
| markRequiredForNextLevel | int | |
| championSeasonMilestone | int | |
| nextSeasonMilestone | NextSeasonMilestonesDto | |
| tokensEarned | int | The token earned for this champion at the current championLevel. When the championLevel is advanced the tokensEarned resets to 0. |
| milestoneGrades | List[string] | |

#### NextSeasonMilestonesDto
This object contains required next season milestone information.

| Field | Data Type | Description |
|-------|-----------|-------------|
| requireGradeCounts | object | |
| rewardMarks | int | Reward marks. |
| bonus | boolean | Bonus. |
| rewardConfig | RewardConfigDto | Reward configuration. |

#### RewardConfigDto
This object contains required reward config information.

| Field | Data Type | Description |
|-------|-----------|-------------|
| rewardValue | string | Reward value |
| rewardType | string | Reward type |
| maximumReward | int | Maximun reward |

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

## Endpoint: GET /lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}/top
**Description:** Get specified number of top champion mastery entries sorted by number of champion points descending.

### Path Parameters
- **encryptedPUUID** (required, string)

### Query Parameters
- **count** (optional, int): Number of entries to retrieve, defaults to 3.

### Response: List[ChampionMasteryDto]

#### ChampionMasteryDto
This object contains single Champion Mastery information for player and champion combination.

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Player Universal Unique Identifier. Exact length of 78 characters. (Encrypted) |
| championPointsUntilNextLevel | long | Number of points needed to achieve next level. Zero if player reached maximum champion level for this champion. |
| chestGranted | boolean | Is chest granted for this champion or not in current season. |
| championId | long | Champion ID for this entry. |
| lastPlayTime | long | Last time this champion was played by this player - in Unix milliseconds time format. |
| championLevel | int | Champion level for specified player and champion combination. |
| championPoints | int | Total number of champion points for this player and champion combination - they are used to determine championLevel. |
| championPointsSinceLastLevel | long | Number of points earned since current level has been achieved. |
| markRequiredForNextLevel | int | |
| championSeasonMilestone | int | |
| nextSeasonMilestone | NextSeasonMilestonesDto | |
| tokensEarned | int | The token earned for this champion at the current championLevel. When the championLevel is advanced the tokensEarned resets to 0. |
| milestoneGrades | List[string] | |

#### NextSeasonMilestonesDto
This object contains required next season milestone information.

| Field | Data Type | Description |
|-------|-----------|-------------|
| requireGradeCounts | object | |
| rewardMarks | int | Reward marks. |
| bonus | boolean | Bonus. |
| rewardConfig | RewardConfigDto | Reward configuration. |

#### RewardConfigDto
This object contains required reward config information.

| Field | Data Type | Description |
|-------|-----------|-------------|
| rewardValue | string | Reward value |
| rewardType | string | Reward type |
| maximumReward | int | Maximun reward |

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

## Endpoint: GET /lol/champion-mastery/v4/scores/by-puuid/{encryptedPUUID}
**Description:** Get a player's total champion mastery score, which is the sum of individual champion mastery levels.

### Path Parameters
- **encryptedPUUID** (required, string)

### Response: int

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
