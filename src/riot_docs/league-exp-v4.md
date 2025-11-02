# League-Exp-v4 API

## Endpoint: GET /lol/league-exp/v4/entries/{queue}/{tier}/{division}
**Description:** Get all the league entries.

### Path Parameters
- **queue** (required, string): Note that the queue value must be a valid ranked queue. Legal values: RANKED_SOLO_5x5, RANKED_TFT, RANKED_FLEX_SR, RANKED_FLEX_TT
- **tier** (required, string): Legal values: CHALLENGER, GRANDMASTER, MASTER, DIAMOND, EMERALD, PLATINUM, GOLD, SILVER, BRONZE, IRON
- **division** (required, string): Legal values: I, II, III, IV

### Query Parameters
- **page** (optional, int): Defaults to 1. Starts with page 1.

### Response: Set[LeagueEntryDTO]

#### LeagueEntryDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| leagueId | string | |
| summonerId | string | Player's summonerId (Encrypted) |
| puuid | string | Player's encrypted puuid. |
| queueType | string | |
| tier | string | |
| rank | string | The player's division within a tier. |
| leaguePoints | int | |
| wins | int | Winning team on Summoners Rift. First placement in Teamfight Tactics. |
| losses | int | Losing team on Summoners Rift. Second through eighth placement in Teamfight Tactics. |
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
