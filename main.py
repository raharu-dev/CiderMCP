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


API_URL="http://localhost:"+CIDER_PORT+"/api/v1/"
TOKEN_HEADER = {
    # Key : Value
    "apptoken": CIDER_TOKEN
}

# Create MCP server
mcp = FastMCP("Cider-Music", json_response=True)

# Check Cider status and playback
@mcp.resource()
def check_status():
    """Check if Cider music player is open and its playback status"""
    response = requests.get(API_URL + "playback/is-playing", headers=TOKEN_HEADER)
    if response.status_code == 200:
        # If the request was successful, return the status and whether music is playing
        return {"status": "Cider is working.", "is_playing": response.json().get("is_playing")}
    else:
        # Error handling to know if token is wrong or if Cider is not open
        if response.json() == {"error":"UNAUTHORIZED_APP_TOKEN"}:
            return {"error": "Invalid Cider token. Please check your CIDER_TOKEN environment variable."}
        else:
            return {"error": "Cider is not open or not responding. Check if Cider have Web API enabled and if the port is correct."}

if __name__ == "__main__":
    # mcp.run(transport="streamable-http")
    mcp.run()