"""
👋 Welcome to your Smithery project!
To run your server, use "uv run dev"
To test interactively, use "uv run playground"

You might find this resources useful:

🧑‍💻 MCP's Python SDK (helps you define your server)
https://github.com/modelcontextprotocol/python-sdk
"""

from mcp.server.fastmcp import Context, FastMCP
from pydantic import BaseModel, Field
from pathlib import Path

from smithery.decorators import smithery

# For servers with configuration:
@smithery.server()

def create_server():
    """Create and configure the MCP server."""

    # Create your FastMCP server as usual
    server = FastMCP("riot-docs")
    
    DOCS_DIR = Path(__file__).parent.parent / "riot_docs"

    @server.tool()
    def list_available_docs() -> str:
        """List all available Riot API endpoint documentation files"""
        all_files = [
            # League of Legends
            "champion-mastery-v4.md",
            "champion-v3.md",
            "clash-v1.md",
            "league-exp-v4.md",
            "league-v4.md",
            "lol-challenges-v1.md",
            "lol-rso-match-v1.md",
            "lol-status-v4.md",
            "match-v5.md",
            "spectator-v5.md",
            "summoner-v4.md",
            "tournament-v5.md",
            "tournament-stub-v5.md",
            # TFT
            "tft-league-v1.md",
            "tft-match-v1.md",
            "tft-status-v1.md",
            "tft-summoner-v1.md",
            "spectator-tft-v5.md",
            # Valorant
            "val-console-match-v1.md",
            "val-console-ranked-v1.md",
            "val-content-v1.md",
            "val-match-v1.md",
            "val-ranked-v1.md",
            "val-status-v1.md",
            # Legends of Runeterra
            "lor-deck-v1.md",
            "lor-inventory-v1.md",
            "lor-match-v1.md",
            "lor-ranked-v1.md",
            "lor-status-v1.md",
            # Other
            "riftbound-content-v1.md",
            "account-v1.md"
        ]
        
        result = "Available Riot API Documentation Files:\n\n"
        for filename in all_files:
            result += f"- {filename}\n"
        result += "\nUse get_endpoint_docs(filename) to retrieve the full documentation for any endpoint."
        return result
    
    @server.tool()
    def get_endpoint_docs(filename: str) -> str:
        """
        Get the full documentation for a specific Riot API endpoint.
        
        Args:
            filename: The name of the documentation file (e.g., 'match-v5.md', 'summoner-v4.md')
        """
        filepath = DOCS_DIR / filename
        
        if not filepath.exists():
            return f"Error: Documentation file '{filename}' not found. Use list_available_docs() to see all available files."
        
        try:
            content = filepath.read_text()
            return f"# {filename}\n\n{content}"
        except Exception as e:
            return f"Error reading file '{filename}': {str(e)}"

    @server.resource("riot://api-overview")
    def api_overview() -> str:
        """
        Overview of all available Riot Games API endpoints organized by game.
        This resource provides a quick reference to all 31 available API documentation files.
        """
        return """# Riot Games API Documentation Overview

This MCP server provides access to comprehensive documentation for Riot Games APIs across multiple titles.

## Available APIs by Game

### League of Legends (13 endpoints)
- **account-v1.md** - Account management and cross-game identification
- **champion-mastery-v4.md** - Champion mastery points and progression
- **champion-v3.md** - Champion rotation information
- **clash-v1.md** - Clash tournament data
- **league-exp-v4.md** - Experimental league endpoints
- **league-v4.md** - Ranked league and tier information
- **lol-challenges-v1.md** - Challenge progression and rewards
- **lol-rso-match-v1.md** - RSO match data
- **lol-status-v4.md** - Server status and incidents
- **match-v5.md** - Match history and detailed match data
- **spectator-v5.md** - Live game spectator data
- **summoner-v4.md** - Summoner profiles and basic info
- **tournament-v5.md** - Tournament codes and management
- **tournament-stub-v5.md** - Tournament testing stub

### Teamfight Tactics (4 endpoints)
- **tft-league-v1.md** - TFT ranked league data
- **tft-match-v1.md** - TFT match history
- **tft-status-v1.md** - TFT server status
- **tft-summoner-v1.md** - TFT summoner profiles
- **spectator-tft-v5.md** - TFT live game data

### Valorant (6 endpoints)
- **val-console-match-v1.md** - Console match data
- **val-console-ranked-v1.md** - Console ranked data
- **val-content-v1.md** - Game content and localization
- **val-match-v1.md** - Match history and details
- **val-ranked-v1.md** - Competitive ranked data
- **val-status-v1.md** - Server status

### Legends of Runeterra (5 endpoints)
- **lor-deck-v1.md** - Deck codes and management
- **lor-inventory-v1.md** - Player card inventory
- **lor-match-v1.md** - Match history
- **lor-ranked-v1.md** - Ranked leaderboards
- **lor-status-v1.md** - Server status

### Other (1 endpoint)
- **riftbound-content-v1.md** - Riftbound game content

## Usage
Use `get_endpoint_docs(filename)` to retrieve the full documentation for any endpoint listed above.
Use `list_available_docs()` to get a simple list of all available files.
"""

    @server.prompt()
    def explain_endpoint(endpoint_name: str) -> list:
        """
        Generate a prompt to get a clear explanation of a specific Riot API endpoint.
        This is useful when you need to understand what an endpoint does and how to use it.
        
        Args:
            endpoint_name: The name of the endpoint (e.g., 'match-v5', 'summoner-v4')
        """
        return [
            {
                "role": "user",
                "content": f"Please explain the {endpoint_name} Riot API endpoint. Include:\n"
                          f"1. What data it provides\n"
                          f"2. Common use cases\n"
                          f"3. Key request parameters\n"
                          f"4. Important response fields\n"
                          f"5. Any rate limits or special considerations"
            }
        ]

    return server
