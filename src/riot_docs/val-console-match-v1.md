# Val-Console-Match-v1 API

## Endpoint: GET /val/match/console/v1/matches/{matchId}
**Description:** Get match by id.

### Path Parameters
- **matchId** (required, string)

### Response: MatchDto

#### MatchDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| matchInfo | MatchInfoDto | |
| players | List[PlayerDto] | |
| coaches | List[CoachDto] | |
| teams | List[TeamDto] | |
| roundResults | List[RoundResultDto] | |

#### MatchInfoDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| matchId | string | |
| mapId | string | |
| gameLengthMillis | int | |
| gameStartMillis | long | |
| provisioningFlowId | string | |
| isCompleted | boolean | |
| customGameName | string | |
| queueId | string | |
| gameMode | string | |
| isRanked | boolean | |
| seasonId | string | |

#### PlayerDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | |
| gameName | string | |
| tagLine | string | |
| teamId | string | |
| partyId | string | |
| characterId | string | |
| stats | PlayerStatsDto | |
| competitiveTier | int | |
| playerCard | string | |
| playerTitle | string | |

#### PlayerStatsDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| score | int | |
| roundsPlayed | int | |
| kills | int | |
| deaths | int | |
| assists | int | |
| playtimeMillis | int | |
| abilityCasts | AbilityCastsDto | |

#### AbilityCastsDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| grenadeCasts | int | |
| ability1Casts | int | |
| ability2Casts | int | |
| ultimateCasts | int | |

#### CoachDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | |
| teamId | string | |

#### TeamDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| teamId | string | This is an arbitrary string. Red and Blue in bomb modes. The puuid of the player in deathmatch. |
| won | boolean | |
| roundsPlayed | int | |
| roundsWon | int | |
| numPoints | int | Team points scored. Number of kills in deathmatch. |

#### RoundResultDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| roundNum | int | |
| roundResult | string | |
| roundCeremony | string | |
| winningTeam | string | |
| bombPlanter | string | PUUID of player |
| bombDefuser | string | PUUID of player |
| plantRoundTime | int | |
| plantPlayerLocations | List[PlayerLocationsDto] | |
| plantLocation | LocationDto | |
| plantSite | string | |
| defuseRoundTime | int | |
| defusePlayerLocations | List[PlayerLocationsDto] | |
| defuseLocation | LocationDto | |
| playerStats | List[PlayerRoundStatsDto] | |
| roundResultCode | string | |

#### PlayerLocationsDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | |
| viewRadians | float | |
| location | LocationDto | |

#### LocationDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| x | int | |
| y | int | |

#### PlayerRoundStatsDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | |
| kills | List[KillDto] | |
| damage | List[DamageDto] | |
| score | int | |
| economy | EconomyDto | |
| ability | AbilityDto | |

#### KillDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| timeSinceGameStartMillis | int | |
| timeSinceRoundStartMillis | int | |
| killer | string | PUUID |
| victim | string | PUUID |
| victimLocation | LocationDto | |
| assistants | List[string] | List of PUUIDs |
| playerLocations | List[PlayerLocationsDto] | |
| finishingDamage | FinishingDamageDto | |

#### FinishingDamageDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| damageType | string | |
| damageItem | string | |
| isSecondaryFireMode | boolean | |

#### DamageDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| receiver | string | PUUID |
| damage | int | |
| legshots | int | |
| bodyshots | int | |
| headshots | int | |

#### EconomyDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| loadoutValue | int | |
| weapon | string | |
| armor | string | |
| remaining | int | |
| spent | int | |

#### AbilityDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| grenadeEffects | string | |
| ability1Effects | string | |
| ability2Effects | string | |
| ultimateEffects | string | |

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

## Endpoint: GET /val/match/console/v1/matchlists/by-puuid/{puuid}
**Description:** Get matchlist for games played by puuid and platform type.

### Path Parameters
- **puuid** (required, string)

### Query Parameters
- **platformType** (required, string): Legal values: playstation, xbox

### Response: MatchlistDto

#### MatchlistDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | |
| history | List[MatchlistEntryDto] | |

#### MatchlistEntryDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| matchId | string | |
| gameStartTimeMillis | long | |
| queueId | string | |

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

## Endpoint: GET /val/match/console/v1/recent-matches/by-queue/{queue}
**Description:** Get recent matches.

Implementation Notes: Returns a list of match ids that have completed in the last 10 minutes for live regions and 12 hours for the esports routing value. NA/LATAM/BR share a match history deployment. As such, recent matches will return a combined list of matches from those three regions. Requests are load balanced so you may see some inconsistencies as matches are added/removed from the list.

### Path Parameters
- **queue** (required, string): Legal values: console_unrated, console_swiftplay, console_hurm, console_deathmatch, console_competitive

### Response: RecentMatchesDto

#### RecentMatchesDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| currentTime | long | |
| matchIds | List[string] | A list of recent match ids. |

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
AP, BR, EU, LATAM, NA
