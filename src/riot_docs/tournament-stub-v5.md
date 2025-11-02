# Tournament-Stub-v5 API

## Endpoint: POST /lol/tournament-stub/v5/codes
**Description:** Create a tournament code for the given tournament - Stub method.

### Query Parameters
- **count** (optional, int): The number of codes to create (max 1000).
- **tournamentId** (required, long): The tournament ID.

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
BR, EUNE, EUW, JP, LAN, LAS, NA, OCE, PBE, RU, TR, KR

---

## Endpoint: GET /lol/tournament-stub/v5/codes/{tournamentCode}
**Description:** Returns the tournament code DTO associated with a tournament code string - Stub method.

### Path Parameters
- **tournamentCode** (required, string): The tournament code string.

### Response: TournamentCodeV5DTO

#### TournamentCodeV5DTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| code | string | The tournament code. |
| lobbyName | string | The lobby name for the tournament code game. |
| metaData | string | The metadata for tournament code. |
| password | string | The password for the tournament code game. |
| teamSize | int | The team size for the tournament code game. |
| providerId | int | The provider's ID. |
| pickType | string | The pick mode for tournament code game. |
| tournamentId | int | The tournament's ID. |
| id | int | The tournament code's ID. |
| region | string | The tournament code's region. Legal values: BR, EUNE, EUW, JP, LAN, LAS, NA, OCE, PBE, RU, TR, KR |
| map | string | The game map for the tournament code game |
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

## Endpoint: GET /lol/tournament-stub/v5/lobby-events/by-code/{tournamentCode}
**Description:** Gets a list of lobby events by tournament code - Stub method.

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

## Endpoint: POST /lol/tournament-stub/v5/providers
**Description:** Creates a tournament provider and returns its ID - Stub method.

### Body Parameters
- **ProviderRegistrationParametersV5** (required, ProviderRegistrationParametersV5): The provider definition.

#### ProviderRegistrationParametersV5

| Field | Data Type | Description |
|-------|-----------|-------------|
| region | string | The region in which the provider will be running tournaments. Legal values: BR, EUNE, EUW, JP, LAN, LAS, NA, OCE, PBE, RU, TR, KR |
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

## Endpoint: POST /lol/tournament-stub/v5/tournaments
**Description:** Creates a tournament and returns its ID - Stub method.

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
