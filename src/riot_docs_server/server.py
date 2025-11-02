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

    return server
