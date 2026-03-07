# Cider3MCP
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
- Get Lyrics
- Search (/api/v1/amapi)
## How to install
`CIDER_HOST` and `CIDER_PORT` are optional it should work without providing them, however if you port changes or if you want to control it from another PC it might be useful.
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
        "CIDER_HOST": "localhost",
        "CIDER_PORT": "10767",
        "CIDER_TOKEN": "CIDER-API-TOKEN"
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