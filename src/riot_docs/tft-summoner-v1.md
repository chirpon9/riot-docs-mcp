# Tft-Summoner-v1 API

## Endpoint: GET /tft/summoner/v1/summoners/by-puuid/{encryptedPUUID}
**Description:** Get a summoner by PUUID.

### Path Parameters
- **encryptedPUUID** (required, string): Summoner ID

### Response: SummonerDTO

#### SummonerDTO
- represents a summoner

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Encrypted PUUID. Exact length of 78 characters. |
| profileIconId | int | ID of the summoner icon associated with the summoner. |
| revisionDate | long | Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change. |
| summonerLevel | long | Summoner level associated with the summoner. |

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

## Endpoint: GET /tft/summoner/v1/summoners/me
**Description:** Get a summoner by access token.

### Header Parameters
- **Authorization** (required, string): Bearer token.

### Response: SummonerDTO

#### SummonerDTO
- represents a summoner

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Encrypted PUUID. Exact length of 78 characters. |
| profileIconId | int | ID of the summoner icon associated with the summoner. |
| revisionDate | long | Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change. |
| summonerLevel | long | Summoner level associated with the summoner. |

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
