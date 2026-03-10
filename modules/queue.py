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
        # return {
        # "position":pos,
        # "status":songstatus, <- Unplayed, Played, Playing
        # "songID": songID, <- ID or unknown
        # "Track Name": trackname,
        # "Artists Name": artists}
        return {"status":"WIP"}

    # Get info about song in queue, if song is in QUEUE it is better to search for details here since it's already loaded (might do autodetect for it later)
    @mcp.tool()
    def queue_details(mode:str,idpos:int):
        """Check detailed informations about a track in queue by giving it's position in queue or id (mode: position, id) (idpos: int)
            - position - gets song info relative to current song (0 - current song) (-1 - previous song)
            - id - gets song info by its id
        """
        return {"status": "WIP"}