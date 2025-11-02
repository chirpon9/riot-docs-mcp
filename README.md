# riot-docs

[![smithery badge](https://smithery.ai/badge/@chirpon9/riot-docs-mcp)](https://smithery.ai/server/@chirpon9/riot-docs-mcp)

MCP server providing access to Riot Games API documentation for League of Legends, Teamfight Tactics, Valorant, Legends of Runeterra, and more.

## Features

This server provides two tools to access Riot API documentation:

### Tools

1. **`list_available_docs()`** - Lists all 33 available Riot API endpoint documentation files


2. **`get_endpoint_docs(filename: str)`** - Retrieves the full documentation for a specific endpoint
   - Example: `get_endpoint_docs("match-v5.md")`
   - Returns complete API documentation including endpoints, parameters, and response formats

## Installation


Usage with claude desktop

```json
{
  "mcpServers": {
    "riot-docs": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/riot-docs",
        "run",
        "riot_docs_server"
      ]
    }
  }
}
```

### Option 2: 


**Mac:**
```json
{
  "mcpServers": {
    "riot-docs-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "@smithery/cli@latest",
        "run",
        "@chirpon9/riot-docs-mcp",
        "--key",
        "{SMITHERY API KEY}"
      ]
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "riot-docs-mcp": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@chirpon9/riot-docs-mcp",
        "--key",
        "{smithery api key}"
      ]
    }
  }
}
```


