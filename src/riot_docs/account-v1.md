# Account-v1 API

**Routing Information:** There are three routing values for account-v1: americas, asia, and europe. You can query for any account in any region. We recommend using the nearest cluster.　

---

## Endpoint: GET /riot/account/v1/accounts/by-puuid/{puuid}
**Description:** Get account by puuid

### Path Parameters
- **puuid** (required, string)

### Response: AccountDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Encrypted PUUID. Exact length of 78 characters. |
| gameName | string | This field may be excluded from the response if the account doesn't have a gameName. |
| tagLine | string | This field may be excluded from the response if the account doesn't have a tagLine. |

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
AMERICAS, ASIA, EUROPE

---

## Endpoint: GET /riot/account/v1/accounts/by-puuid/{puuid} (ESPORTS)
**Description:** Get account by puuid - ESPORTS

### Path Parameters
- **puuid** (required, string)

### Response: AccountDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Encrypted PUUID. Exact length of 78 characters. |
| gameName | string | This field may be excluded from the response if the account doesn't have a gameName. |
| tagLine | string | This field may be excluded from the response if the account doesn't have a tagLine. |

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
AMERICAS, ASIA, EUROPE

---

## Endpoint: GET /riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}
**Description:** Get account by riot id

### Path Parameters
- **gameName** (required, string): When querying for a player by their riot id, the gameName and tagLine query params are required.
- **tagLine** (required, string): When querying for a player by their riot id, the gameName and tagLine query params are required.

### Response: AccountDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Encrypted PUUID. Exact length of 78 characters. |
| gameName | string | This field may be excluded from the response if the account doesn't have a gameName. |
| tagLine | string | This field may be excluded from the response if the account doesn't have a tagLine. |

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
AMERICAS, ASIA, EUROPE

---

## Endpoint: GET /riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine} (ESPORTS)
**Description:** Get account by riot id - ESPORTS

### Path Parameters
- **gameName** (required, string): When querying for a player by their riot id, the gameName and tagLine query params are required.
- **tagLine** (required, string): When querying for a player by their riot id, the gameName and tagLine query params are required.

### Response: AccountDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Encrypted PUUID. Exact length of 78 characters. |
| gameName | string | This field may be excluded from the response if the account doesn't have a gameName. |
| tagLine | string | This field may be excluded from the response if the account doesn't have a tagLine. |

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
AMERICAS, ASIA, EUROPE

---

## Endpoint: GET /riot/account/v1/accounts/me
**Description:** Get account by access token

### Header Parameters
- **Authorization** (required, string)

### Response: AccountDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Encrypted PUUID. Exact length of 78 characters. |
| gameName | string | This field may be excluded from the response if the account doesn't have a gameName. |
| tagLine | string | This field may be excluded from the response if the account doesn't have a tagLine. |

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
AMERICAS, ASIA, EUROPE

---

## Endpoint: GET /riot/account/v1/accounts/me (ESPORTS)
**Description:** Get account by access token - ESPORTS

### Header Parameters
- **Authorization** (required, string)

### Response: AccountDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Encrypted PUUID. Exact length of 78 characters. |
| gameName | string | This field may be excluded from the response if the account doesn't have a gameName. |
| tagLine | string | This field may be excluded from the response if the account doesn't have a tagLine. |

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
AMERICAS, ASIA, EUROPE

---

## Endpoint: GET /riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}
**Description:** Get active shard for a player

### Path Parameters
- **game** (required, string): Valid values: `val`, `lor`
- **puuid** (required, string)

### Response: ActiveShardDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Player Universal Unique Identifier. Exact length of 78 characters. (Encrypted) |
| game | string | Game identifier |
| activeShard | string | Active shard for the player |
| region | string | Region identifier |

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
AMERICAS, ASIA, EUROPE

---

## Endpoint: GET /riot/account/v1/region/by-game/{game}/by-puuid/{puuid}
**Description:** Get active region (lol and tft)

### Path Parameters
- **game** (required, string): Valid values: `lol`, `tft`
- **puuid** (required, string)

### Response: AccountRegionDTO
Account region

| Field | Data Type | Description |
|-------|-----------|-------------|
| puuid | string | Player Universal Unique Identifier. Exact length of 78 characters. (Encrypted) |
| game | string | Game to lookup active region |
| region | string | Player active region |

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
AMERICAS, ASIA, EUROPE
