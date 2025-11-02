# Tournament-v5 API

## Endpoint: POST /lol/tournament/v5/codes
**Description:** Create a tournament code for the given tournament.

### Query Parameters
- **tournamentId** (required, long): The tournament ID.
- **count** (optional, int): The number of codes to create (max 1000).

### Body Parameters
- **TournamentCodeParametersV5** (required, TournamentCodeParametersV5): Metadata for the generated code.

#### TournamentCodeParametersV5

| Field | Data Type | Description |
|-------|-----------|-------------|
| allowedParticipants | Set[string] | Optional list of encrypted puuids in order to validate the players eligible to join the lobby. NOTE: We currently do not enforce participants at the team level, but rather the aggregate of teamOne and teamTwo. We may add the ability to enforce at the team level in the future. |
| enoughPlayers | boolean | Checks if allowed participants are enough to make full teams. |
| mapType | string | The map type of the game. Legal values: SUMMONERS_RIFT, HOWLING_ABYSS |
| metadata | string | Optional string that may contain any data in any format, if specified at all. Used to denote any custom information about the game. |
| pickType | string | The pick type of the game. Legal values: BLIND_PICK, DRAFT_MODE, ALL_RANDOM, TOURNAMENT_DRAFT |
| spectatorType | string | The spectator type of the game. Legal values: NONE, LOBBYONLY, ALL |
| teamSize | int | The team size of the game. Valid values are 1-5. |

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
BR, EUNE, EUW, JP, LAN, LAS, NA, OCE, PBE, RU, TR, KR, PH, SG, TH, TW, VN

---

## Endpoint: GET /lol/tournament/v5/codes/{tournamentCode}
**Description:** Returns the tournament code DTO associated with a tournament code string.

### Path Parameters
- **tournamentCode** (required, string): The tournament code string.

### Response: TournamentCodeV5DTO

#### TournamentCodeV5DTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | int | The tournament code's ID. |
| providerId | int | The provider's ID. |
| tournamentId | int | The tournament's ID. |
| code | string | The tournament code. |
| region | string | The tournament code's region. Legal values: BR, EUNE, EUW, JP, LAN, LAS, NA, OCE, PBE, RU, TR, KR, PH, SG, TH, TW, VN |
| map | string | The game map for the tournament code game |
| teamSize | int | The team size for the tournament code game. |
| spectators | string | The spectator mode for the tournament code game. |
| pickType | string | The pick mode for tournament code game. |
| lobbyName | string | The lobby name for the tournament code game. |
| password | string | The password for the tournament code game. |
| metaData | string | The metadata for tournament code. |
| participants | Set[string] | The puuids of the participants (Encrypted) |

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

---

## Endpoint: PUT /lol/tournament/v5/codes/{tournamentCode}
**Description:** Update the pick type, map, spectator type, or allowed puuids for a code.

### Path Parameters
- **tournamentCode** (required, string): The tournament code to update.

### Body Parameters
- **TournamentCodeUpdateParametersV5** (optional, TournamentCodeUpdateParametersV5): The fields to update.

#### TournamentCodeUpdateParametersV5

| Field | Data Type | Description |
|-------|-----------|-------------|
| allowedParticipants | Set[string] | Optional list of encrypted puuids in order to validate the players eligible to join the lobby. NOTE: We currently do not enforce participants at the team level, but rather the aggregate of teamOne and teamTwo. We may add the ability to enforce at the team level in the future. |
| pickType | string | The pick type. Legal values: BLIND_PICK, DRAFT_MODE, ALL_RANDOM, TOURNAMENT_DRAFT |
| mapType | string | The map type. Legal values: SUMMONERS_RIFT, HOWLING_ABYSS |
| spectatorType | string | The spectator type. Legal values: NONE, LOBBYONLY, ALL |

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

---

## Endpoint: GET /lol/tournament/v5/games/by-code/{tournamentCode}
**Description:** Get games details.

Implementation Notes: Additional endpoint to get tournament games. From this endpoint, you are able to get participants PUUID (the callback doesn't contain this info). You can also use it to check if the game was recorded and validate callbacks. If the endpoint returns the game, it means a callback was attempted. This will only work for tournament codes created after November 10, 2023.

### Path Parameters
- **tournamentCode** (required, string): The tournament code.

### Response: Set[TournamentGamesV5]

#### TournamentGamesV5

| Field | Data Type | Description |
|-------|-----------|-------------|
| startTime | long | |
| winningTeam | List[TournamentTeamV5] | |
| losingTeam | List[TournamentTeamV5] | |
| shortCode | string | Tournament Code |
| metaData | string | Metadata for the TournamentCode |
| gameId | long | |
| gameName | string | |
| gameType | string | |
| gameMap | int | Game Map ID |
| gameMode | string | |
| region | string | Region of the game |

#### TournamentTeamV5

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Player Unique UUID (Encrypted) |

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

---

## Endpoint: GET /lol/tournament/v5/lobby-events/by-code/{tournamentCode}
**Description:** Gets a list of lobby events by tournament code.

### Path Parameters
- **tournamentCode** (required, string): The short code to look up lobby events for.

### Response: LobbyEventV5DTOWrapper

#### LobbyEventV5DTOWrapper

| Field | Data Type | Description |
|-------|-----------|-------------|
| eventList | List[LobbyEventV5DTO] | |

#### LobbyEventV5DTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| timestamp | string | Timestamp from the event |
| eventType | string | The type of event that was triggered |
| puuid | string | The puuid that triggered the event (Encrypted) |

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

---

## Endpoint: POST /lol/tournament/v5/providers
**Description:** Creates a tournament provider and returns its ID.

Implementation Notes: Providers will need to call this endpoint first to register their callback URL and their API key with the tournament system before any other tournament provider endpoints will work.

### Body Parameters
- **ProviderRegistrationParametersV5** (required, ProviderRegistrationParametersV5): The provider definition.

#### ProviderRegistrationParametersV5

| Field | Data Type | Description |
|-------|-----------|-------------|
| region | string | The region in which the provider will be running tournaments. Legal values: BR, EUNE, EUW, JP, LAN, LAS, NA, OCE, PBE, RU, TR, KR, PH, SG, TH, TW, VN |
| url | string | The provider's callback URL to which tournament game results in this region should be posted. The URL must be well-formed, use the http or https protocol, and use the default port for the protocol (http URLs must use port 80, https URLs must use port 443). |

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

---

## Endpoint: POST /lol/tournament/v5/tournaments
**Description:** Creates a tournament and returns its ID.

### Body Parameters
- **TournamentRegistrationParametersV5** (required, TournamentRegistrationParametersV5): The tournament definition.

#### TournamentRegistrationParametersV5

| Field | Data Type | Description |
|-------|-----------|-------------|
| providerId | int | The provider ID to specify the regional registered provider data to associate this tournament. |
| name | string | The optional name of the tournament. |

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
