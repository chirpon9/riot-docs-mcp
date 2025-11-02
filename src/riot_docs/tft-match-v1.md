# Tft-Match-v1 API

**Routing Information:** The AMERICAS routing value serves NA, BR, LAN and LAS. The ASIA routing value serves KR and JP. The EUROPE routing value serves EUNE, EUW, TR, ME1, and RU. The SEA routing value serves OCE, SG2, TW2 and VN2.

---

## Endpoint: GET /tft/match/v1/matches/by-puuid/{puuid}/ids
**Description:** Get a list of match ids by PUUID

### Path Parameters
- **puuid** (optional, String)

### Query Parameters
- **start** (optional, int): Defaults to 0. Start index.
- **endTime** (optional, long): Epoch timestamp in seconds.
- **startTime** (optional, long): Epoch timestamp in seconds. The matchlist started storing timestamps on June 16th, 2021. Any matches played before June 16th, 2021 won't be included in the results if the startTime filter is set.
- **count** (optional, int): Defaults to 20. Number of match ids to return.

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
AMERICAS, ASIA, ESPORTS, ESPORTSEU, EUROPE, SEA

---

## Endpoint: GET /tft/match/v1/matches/{matchId}
**Description:** Get a match by match id

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
| endOfGameResult | string | Refer to indicate if the game ended in termination. |
| gameCreation | long | Unix timestamp for when the game is created on the game server (i.e., the loading screen). |
| gameId | long | |
| game_datetime | long | Unix timestamp. |
| game_length | float | Game length in seconds. |
| game_version | string | Game client version. |
| game_variation | string | Deprecated. Game variation key. Game variations documented in TFT static data. |
| mapId | int | Refer to the Game Constants documentation. |
| participants | List[ParticipantDto] | |
| queue_id | int | Please refer to the League of Legends documentation. |
| queueId | int | Deprecated. Use queue_id instead. |
| tft_game_type | string | Teamfight Tactics game type. |
| tft_set_core_name | string | Teamfight Tactics game set. |
| tft_set_number | int | Teamfight Tactics set number. |

#### ParticipantDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| companion | CompanionDto | Participant's companion. |
| gold_left | int | Gold left after participant was eliminated. |
| last_round | int | The round the participant was eliminated in. Note: If the player was eliminated in stage 2-1 their last_round would be 5. |
| level | int | Participant Little Legend level. Note: This is not the number of active units. |
| placement | int | Participant placement upon elimination. |
| players_eliminated | int | Number of players the participant eliminated. |
| puuid | string | |
| riotIdGameName | string | |
| riotIdTagline | string | |
| time_eliminated | float | The number of seconds before the participant was eliminated. |
| total_damage_to_players | int | Damage the participant dealt to other players. |
| traits | List[TraitDto] | A complete list of traits for the participant's active units. |
| units | List[UnitDto] | A list of active units for the participant. |
| win | boolean | |

#### CompanionDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| content_ID | string | |
| item_ID | int | |
| skin_ID | int | |
| species | string | |

#### TraitDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| name | string | Trait name. |
| num_units | int | Number of units with this trait. |
| style | int | Current style for this trait. (0 = No style, 1 = Bronze, 2 = Silver, 3 = Gold, 4 = Chromatic) |
| tier_current | int | Current active tier for the trait. |
| tier_total | int | Total tiers for the trait. |

#### UnitDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| items | List[int] | A list of the unit's items. Please refer to the Teamfight Tactics documentation for item ids. |
| character_id | string | This field was introduced in patch 9.22 with data_version 2. |
| itemNames | List[string] | |
| chosen | string | If a unit is chosen as part of the Fates set mechanic, the chosen trait will be indicated by this field. Otherwise this field is excluded from the response. |
| name | string | Unit name. This field is often left blank. |
| rarity | int | Unit rarity. This doesn't equate to the unit cost. |
| tier | int | Unit tier. |

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
AMERICAS, ASIA, ESPORTS, ESPORTSEU, EUROPE, SEA
