# Cider3MCP
This is a project to allow LLMs connect to Cider.sh music app.
## Overview
I don't really have a big experience in Python or MCP so this project is going to be a nice study.
Overall I will be guiding myself by using the repo below.
So this repo will be my personal journal of my journey with Python and MCP.
The MCP will be tested using local instance of Qwen3.5 9B in LM Studio.
## Planned MCP Tools
- Play, Pause
- Set Volume
- Shuffle, Loop, Autoplay

- Get Queue
- Move Queue Position
- Remove from Queue
- Clear Queue

- Add Song/Album (URL/HREF/ID)
- Get Lyrics
- Search (/api/v1/amapi)
## How to install
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
        "CIDER_PORT": "10767"
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