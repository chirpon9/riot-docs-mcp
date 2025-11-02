# Spectator-Tft-v5 API

## Endpoint: GET /lol/spectator/tft/v5/active-games/by-puuid/{encryptedPUUID}
**Description:** Get current game information for the given puuid.

### Path Parameters
- **encryptedPUUID** (required, string): The puuid of the summoner.

### Response: CurrentGameInfo

#### CurrentGameInfo

| Field | Data Type | Description |
|-------|-----------|-------------|
| gameId | long | The ID of the game |
| gameType | string | The game type |
| gameStartTime | long | The game start time represented in epoch milliseconds |
| mapId | long | The ID of the map |
| gameLength | long | The amount of time in seconds that has passed since the game started |
| platformId | string | The ID of the platform on which the game is being played |
| gameMode | string | The game mode |
| bannedChampions | List[BannedChampion] | Banned champion information |
| gameQueueConfigId | long | The queue type (queue types are documented on the Game Constants page) |
| observers | Observer | The observer information |
| participants | List[CurrentGameParticipant] | The participant information |

#### BannedChampion

| Field | Data Type | Description |
|-------|-----------|-------------|
| pickTurn | int | The turn during which the champion was banned |
| championId | long | The ID of the banned champion |
| teamId | long | The ID of the team that banned the champion |

#### Observer

| Field | Data Type | Description |
|-------|-----------|-------------|
| encryptionKey | string | Key used to decrypt the spectator grid game data for playback |

#### CurrentGameParticipant

| Field | Data Type | Description |
|-------|-----------|-------------|
| championId | long | The ID of the champion played by this participant |
| perks | Perks | Perks/Runes Reforged Information |
| profileIconId | long | The ID of the profile icon used by this participant |
| teamId | long | The team ID of this participant, indicating the participant's team |
| puuid | string | The encrypted puuid of this participant. null when the player is anonym. |
| spell1Id | long | The ID of the first summoner spell used by this participant |
| spell2Id | long | The ID of the second summoner spell used by this participant |
| gameCustomizationObjects | List[GameCustomizationObject] | List of Game Customizations |

#### Perks

| Field | Data Type | Description |
|-------|-----------|-------------|
| perkIds | List[long] | IDs of the perks/runes assigned. |
| perkStyle | long | Primary runes path |
| perkSubStyle | long | Secondary runes path |

#### GameCustomizationObject

| Field | Data Type | Description |
|-------|-----------|-------------|
| category | string | Category identifier for Game Customization |
| content | string | Game Customization content |

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
