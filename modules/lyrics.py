import requests
# Currently planned to implement when the API gets finished. 
# (Unless I get it to work through AM API or something else)
def lyricsTool(mcp, API_URL, TOKEN_HEADER):
    # Getting whole lyrics
    @mcp.tool()
    def lyrics_all():
        return {"STATUS":"WIP"}

    # Getting a specific line
    @mcp.tool()
    def lyrics_line():
        return {"STATUS":"WIP"}   

    # Finding where is text in  (bool, line number, whole line (range))
    @mcp.tool()
    def lyrics_find():
        return {"STATUS":"WIP"}