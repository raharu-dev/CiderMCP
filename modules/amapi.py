import requests

# Tools that use Apple Music Api through Cider, requests usually takes longer
def amapiTool(mcp, API_URL, TOKEN_HEADER, STOREFRONT):
    
    # Gets song details by it's ID
    @mcp.tool()
    def am_detailsById(sid:str):
        """
        Shows: SongID, Album ID, Song Name, Song Artists, Album Artists, Genre,
        """
        return {"status":"WIP"}
    
    # Search
    @mcp.tool()
    def am_search(query:str,type:str,results:int):
        """
        Type: Song, Album, Playlist <- if using , it can search for multiple (i.e. "songs,albums")
        Results: Number of max results that are shown (not recommended to go above 5)
        """
        return {"status":"WIP"}