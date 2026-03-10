# CiderMCP
Connect Cider with LLMs
## Overview
MCP server that allows [Cider](https://cider.sh/) (Apple Music client) to be controlled by LLM clients (i.e. Claude Code, LM Studio).
This might increase accessibility of Cider client through LLM interactions or just be a fun way to control your music.
## Features (MCP Tools)
- Get Cider API status
### Playback Controls
- Get/Set Playback Mode (Playing/Paused)
- Skip songs (forward/backwards certain amount of songs)
- Get/Set Volume (0.0 - 1.0)
- Get/Set Repeat Mode (OFF/TRACK/ALL)
- Get/Set Shuffle Mode (ON/OFF)
- Get/Set Autoplay Mode (ON/OFF)
## Planned MCP Tools
### Queue Management
- Get Queue
- Move position in Queue
- Remove from Queue
- Clear Queue
### Other features
- Add Song/Album (URL/HREF/ID)
- Get Lyrics *[Currently not implementing due to API not being finished]*
- Search (/api/v1/amapi)
## How to install
- `CIDER_TOKEN` - Websocket API token, without the token it most probably won't work even if requirement is disabled
- `CIDER_HOST` - `default: localhost` **OPTIONAL** Sets websocket address, might be useful when trying to control from different device
- `CIDER_PORT`- `default: 10767` **OPTIONAL** Sets websocket port, usage similar as above
- `AM_STOREFRONT` - `default: ca` **OPTIONAL** Sets storefront used by amapi module for requests outside Cider (i.e. "ca", "pl", "de")
Github version:
```json
{
  "mcpServers": {
    "cider-music": {
      "command": "uv",
      "args": [
        "--directory",
        "/Path/To/Cider3MCP",
        "run",
        "main.py"
      ],
      "env": {
        "CIDER_TOKEN": "CIDER-API-TOKEN",
        "CIDER_HOST": "localhost",
        "CIDER_PORT": "10767",
        "AM_STOREFRONT": "Country Code"
      }
    }
  }
}
```
## Sources
MCP Python SDK:
 https://github.com/modelcontextprotocol/python-sdk

Cider API:
 https://cider.sh/docs/client/rpc

This helped me how to add to mcp.json locally:
 https://github.com/reading-plus-ai/mcp-server-deep-research