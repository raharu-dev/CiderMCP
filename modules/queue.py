import requests

def queueTool(mcp, API_URL, TOKEN_HEADER):

    # _songId
    # albumName
    # itemName <- song name
    # year
    # genre
    # explicit
    # playlistArtistName <- album artist
    # artistsName <- song artist
    # artworkURL <- album cover
    # isCompilation <- Is it part of an album or compilation
    # playlistId

    # Get full queue but more
    # Shows: position, songid, itemName, albumName, artistsName

    # Notes on how queue work
    # The song order is right even when shuffle is enabled

    # Active playback (now playing)
    # "_state": {
    #     "current": 2
    # },
    # Already played (played)
    # "_state": {
    #     "current": 4
    # },

    @mcp.tool()
    def queue_get():
        """Get list of tracks in queue with basic info about them (mode: fluent, dev)
            Gets easy to understand and important info: position, status, songId, track name, album name, artists name
        """
        response = requests.get(API_URL + "playback/queue", headers=TOKEN_HEADER)
        if response.status_code != 200:
            return {"error": "Couldn't get queue info", "status_code": response.status_code}
        data = response.json()

        # normalize response to a list of items
        if isinstance(data, dict):
            for key in ("items", "data", "queue", "results", "tracks"):
                if key in data and isinstance(data[key], list):
                    items = data[key]
                    break
            else:
                if "assets" in data or "_songId" in data:
                    items = [data]
                else:
                    items = []
        elif isinstance(data, list):
            items = data
        else:
            items = []

        names = []
        queueposition = []

        for item in items:
            name = None
            if isinstance(item, dict):
                assets = item.get("assets")
                if isinstance(assets, list) and assets:
                    for asset in assets:
                        md = asset.get("metadata") if isinstance(asset, dict) else None
                        if isinstance(md, dict) and "itemName" in md:
                            name = md["itemName"]
                            break
                if not name:
                    attrs = item.get("attributes", {})
                    name = attrs.get("name") or item.get("itemName")
            if name:
                names.append(name)
        return {queueposition:names}

    # Get info about song in queue
    @mcp.tool()
    def queue_details(mode:str,idpos:int):
        """Check detailed informations about a track in queue by giving it's position in queue or id (mode: position, id) (idpos: int)
            - position - gets song info relative to current song (0 - current song) (-1 - previous song)
            - id - gets song info by its id
        """
        return {"error": "Not implemented"}