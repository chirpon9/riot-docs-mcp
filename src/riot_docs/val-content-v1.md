# Val-Content-v1 API

## Endpoint: GET /val/content/v1/contents
**Description:** Get content optionally filtered by locale.

### Query Parameters
- **locale** (optional, String)

### Response: ContentDto

#### ContentDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| version | string | |
| characters | List[ContentItemDto] | |
| maps | List[ContentItemDto] | |
| chromas | List[ContentItemDto] | |
| skins | List[ContentItemDto] | |
| skinLevels | List[ContentItemDto] | |
| equips | List[ContentItemDto] | |
| gameModes | List[ContentItemDto] | |
| sprays | List[ContentItemDto] | |
| sprayLevels | List[ContentItemDto] | |
| charms | List[ContentItemDto] | |
| charmLevels | List[ContentItemDto] | |
| playerCards | List[ContentItemDto] | |
| playerTitles | List[ContentItemDto] | |
| acts | List[ActDto] | |

#### ContentItemDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| name | string | |
| localizedNames | LocalizedNamesDto | This field is excluded from the response when a locale is set |
| id | string | |
| assetName | string | |
| assetPath | string | This field is only included for maps and game modes. These values are used in the match response. |

#### LocalizedNamesDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| ar-AE | string | |
| de-DE | string | |
| en-GB | string | |
| en-US | string | |
| es-ES | string | |
| es-MX | string | |
| fr-FR | string | |
| id-ID | string | |
| it-IT | string | |
| ja-JP | string | |
| ko-KR | string | |
| pl-PL | string | |
| pt-BR | string | |
| ru-RU | string | |
| th-TH | string | |
| tr-TR | string | |
| vi-VN | string | |
| zh-CN | string | |
| zh-TW | string | |

#### ActDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| name | string | |
| localizedNames | LocalizedNamesDto | This field is excluded from the response when a locale is set |
| id | string | |
| isActive | boolean | |

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
AP, BR, ESPORTS, EU, KR, LATAM, NA
