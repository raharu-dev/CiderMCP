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

# Actually used varaibles for connection to Cider API
API_URL="http://localhost:"+CIDER_PORT+"/api/v1/"
TOKEN_HEADER = {
    # Key : Value
    "apptoken": CIDER_TOKEN
}

# Create MCP server
mcp = FastMCP("Cider-Music", json_response=True)

# Check Cider status and playback status
@mcp.tool()
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

#
# GENERAL PLAYBACK CONTROLS
#

# Toggle playback
@mcp.tool()
def toggle_playback():
    """Toggle the playback status of the music player"""
    response = requests.post(API_URL + "playback/playpause", headers=TOKEN_HEADER)
    if response.status_code == 200:
        response = requests.get(API_URL + "playback/is-playing", headers=TOKEN_HEADER)
        if response.status_code == 200:
            is_playing = response.json().get("is_playing")
            if is_playing:
                return {"status": "Playback started."}
            else:
                return {"status": "Playback paused."}
        else:
            return {"error": "Playback status is unknown."}
            
    else:
        return {"error": "Failed to toggle playback."}

# Get Volume
@mcp.tool()
def get_volume():
    """Get the current volume level of the music player"""
    response = requests.get(API_URL + "playback/volume", headers=TOKEN_HEADER)
    if response.status_code == 200:
        volume = response.json().get("volume")
        return {"volume": volume}
    else:
        return {"error": "Failed to get volume."}
# Set Volume (It works but the UI doesn't update the volume slider)
@mcp.tool()
def set_volume(level: float):
    """Set the volume level of the music player (0.0 to 1.0)"""
    if level < 0.0 or level > 1.0:
        return {"error": "Volume level must be between 0.0 and 1.0."}
    
    response = requests.post(API_URL + "playback/volume", headers=TOKEN_HEADER, json={"volume": level})
    if response.status_code == 200:
        return {"status": f"Volume set to {level}."}
    else:
        return {"error": "Failed to set volume."}


# Get Repeat Mode
@mcp.tool()
def get_repeat():
    """Get the current repeat mode of the music player"""
    response = requests.get(API_URL + "playback/repeat-mode", headers=TOKEN_HEADER)
    if response.status_code == 200:
        repeat_mode = response.json().get("value")
        if repeat_mode == 0:
            return {"repeat_mode": "off"}
        elif repeat_mode == 1:
            return {"repeat_mode": "track"}
        elif repeat_mode == 2:
            return {"repeat_mode": "all"}
    else:
        return {"error": "Failed to get current repeat mode."}
# Set Repeat Mode
@mcp.tool()
def set_repeat(mode: str):
    """Set the repeat mode of the music player (off, track, all)"""
    mode_mapping = {
        "off": 0,
        "track": 1,
        "all": 2
    }
    # First get current repeat mode to know how many times we need to cycle toggle
    response = requests.get(API_URL + "playback/repeat-mode", headers=TOKEN_HEADER)
    if response.status_code == 200:
        current_mode = response.json().get("value")
        target_mode = mode_mapping.get(mode)
        if target_mode is None:
            return {"error": "Invalid repeat mode. Use 'off', 'track', or 'all'."}
        # Calculate how many times we need to cycle the repeat mode
        toggles_needed = (target_mode - current_mode) % 3
        for _ in range(toggles_needed):
            toggle_response = requests.post(API_URL + "playback/toggle-repeat", headers=TOKEN_HEADER)
            if toggle_response.status_code != 200:
                return {"error": "Failed to set repeat mode."}
        return {"status": f"Repeat mode set to {mode}."}
    else:
        return {"error": "Failed to get current repeat mode."}

# Get Shuffle Mode
@mcp.tool()
def get_shuffle():
    """Get the current shuffle mode of the music player"""
    response = requests.get(API_URL + "playback/shuffle-mode", headers=TOKEN_HEADER)
    if response.status_code == 200:
        shuffle_mode = response.json().get("shuffle")
        return {"shuffle": shuffle_mode}
    else:
        return {"error": "Failed to get current shuffle mode."}
# Set Shuffle Mode
# SET xor CURRENT = Right State
@mcp.tool()
def set_shuffle(mode: str):
    """Set the shuffle mode of the music player (on, off)"""
    # Get current shuffle mode to know if we need to toggle
    response = requests.get(API_URL + "playback/shuffle-mode", headers=TOKEN_HEADER)
    if response.status_code == 200:
        if response.json().get("value") ^ enabled:
            response = requests.post(API_URL+"playback/toggle-shuffle", headers=TOKEN_HEADER)
            if response.status_code != 200:
                return {"error": "Failed to set shuffle mode."}
    return {"status": "Succesfully changed shuffle mode to {enabled}"}
        
            


if __name__ == "__main__":
    # mcp.run(transport="streamable-http")
    mcp.run()