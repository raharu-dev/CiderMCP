"""
MCP server to use Cider music player with LLMs
"""

# Imports
import os
import requests
from mcp.server.fastmcp import FastMCP

# Get env arguments
CIDER_TOKEN=os.environ.get("CIDER_TOKEN")
if not CIDER_TOKEN:
    CIDER_TOKEN=""
CIDER_PORT=os.environ.get("CIDER_PORT")
if not CIDER_PORT:
    CIDER_PORT="10767"

# Actually used variables for connection to Cider API
API_URL="http://localhost:"+CIDER_PORT+"/api/v1/"
TOKEN_HEADER = { "apptoken": CIDER_TOKEN }

# Create MCP server
mcp = FastMCP("Cider-Music", json_response=True)

# Importing Modules
from modules.playbackControl import register_tools

# Check Cider status
@mcp.tool()
def status_check():
    """Check if Cider music player is open"""
    response = requests.get(API_URL + "playback/is-playing", headers=TOKEN_HEADER)
    if response.status_code == 200:
        # If the request was successful, return the status and whether music is playing
        return {"status": "Cider is working."}
    else:
        # Error handling to know if token is wrong or if Cider is not open
        try:
            body = response.json()
        except Exception:
            body = None
        if body == {"error": "UNAUTHORIZED_APP_TOKEN"}:
            return {"error": "Invalid Cider token. Please check your CIDER_TOKEN environment variable."}
        else:
            return {"error": "Cider is not open or not responding. Check if Cider have Web API enabled and if the port is correct."}

# Register tools from modules
register_tools(mcp, API_URL+"playback/", TOKEN_HEADER)

if __name__ == "__main__":
    # mcp.run(transport="streamable-http")
    mcp.run()