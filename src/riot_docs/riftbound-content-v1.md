# Riftbound-Content-v1 API

## Endpoint: GET /riftbound/content/v1/contents
**Description:** Get riftbound content

### Query Parameters
- **locale** (optional, string): Defaults to en. Optional. Specifies the language and regional settings for the response. Use a locale code. During beta only en available.

### Response: RiftboundContentDTO

#### RiftboundContentDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| game | string | Game Name |
| version | string | Content version |
| lastUpdated | string | ISO Timestamp of content last update |
| sets | List[SetDTO] | |

#### SetDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | string | Set ID |
| name | string | Set Name |
| cards | List[CardDTO] | |

#### CardDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | string | Card ID |
| collectorNumber | long | |
| set | string | |
| name | string | Card Name |
| description | string | |
| type | string | Card Type |
| rarity | string | |
| faction | string | |
| stats | CardStatsDTO | |
| keywords | List[string] | |
| art | CardArtDTO | |
| flavorText | string | |
| tags | List[string] | |

#### CardStatsDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| energy | long | |
| might | long | |
| cost | long | |
| power | long | |

#### CardArtDTO

| Field | Data Type | Description |
|-------|-----------|-------------|
| thumbnailURL | string | |
| fullURL | string | |
| artist | string | |

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
