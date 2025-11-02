# Lor-Status-v1 API

**Routing Information:** The AMERICAS routing value serves the AMERICAS shard. The EUROPE routing value serves the EUROPE shard. The SEA routing value serves the APAC shard (previously was ASIA and SEA).

---

## Endpoint: GET /lor/status/v1/platform-data
**Description:** Get Legends of Runeterra status for the given platform.

### Response: PlatformDataDto

#### PlatformDataDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | string | |
| name | string | |
| locales | List[string] | |
| maintenances | List[StatusDto] | |
| incidents | List[StatusDto] | |

#### StatusDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | int | |
| maintenance_status | string | Legal values: scheduled, in_progress, complete |
| incident_severity | string | Legal values: info, warning, critical |
| titles | List[ContentDto] | |
| updates | List[UpdateDto] | |
| created_at | string | |
| archive_at | string | |
| updated_at | string | |
| platforms | List[string] | Legal values: windows, macos, android, ios, ps4, xbone, switch |

#### ContentDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| locale | string | |
| content | string | |

#### UpdateDto

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | int | |
| author | string | |
| publish | boolean | |
| publish_locations | List[string] | Legal values: riotclient, riotstatus, game |
| translations | List[ContentDto] | |
| created_at | string | |
| updated_at | string | |

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
AMERICAS, EUROPE, SEA
