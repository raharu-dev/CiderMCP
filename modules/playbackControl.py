import requests

def register_tools(mcp, API_URL, TOKEN_HEADER):
    ## PLAYBACK CONTROL
    # Get playback mode
    @mcp.tool()
    def playback_get():
        """Get playback status is music playing or not (on, off)"""
        response = requests.get(API_URL+"is-playing", headers=TOKEN_HEADER)
        if response.status_code==200:
            if response.json().get("is_playing"):
                return {"status": "Currently playback is enabled (playing)"}
            else:
                return {"status": "Currently playback is disabled (paused)"}
        return {"error": "Couldn't get current playback status"}
    # Set playback mode
    @mcp.tool()
    def playback_set(mode: str):
        """Set the playback mode of the music player (on, off)"""
        node_mapping={
            "off": 0,
            "on": 1
        }
        # Get current shuffle mode to know if we need to toggle
        response = requests.get(API_URL + "is-playing", headers=TOKEN_HEADER)
        if response.status_code == 200:
            # XOR Current State with Desired State in order to set right mode
            if response.json().get("is_playing") ^ node_mapping.get(mode):
                response = requests.post(API_URL+"playback/playpause", headers=TOKEN_HEADER)
                if response.status_code == 200:
                    return {"status": "Succesfully changed playback mode to "+mode}
                else:
                    return {"status": "Couldn't change playback mode"}
            return {"status": "Requested playback mode is already "+mode}
        return {"error": "Couldn't get current state of playback"}

    ## Skipping tracks
    @mcp.tool()
    def playback_skip(mode:str, songs:int):
        """Skips certain amount of songs forward or backwards. (mode: next, previous) (songs: int)"""
        print(mode)
        if mode != "next" and mode != "previous":
            return {"error": "Wrong request accepted modes are either \"next\" or \"previous\""}
        for _ in range(songs):
            response = requests.post(API_URL+mode, headers=TOKEN_HEADER)
            if response.status_code!=200:
                return {"error": f"Something went wrong while trying to go {mode}."}
        return {"status": f"Succesfully went {mode} {songs}"}

    ## VOLUME CONTROL
    # Get Volume
    @mcp.tool()
    def volume_get():
        """Get the current volume level of the music player"""
        response = requests.get(API_URL + "volume", headers=TOKEN_HEADER)
        if response.status_code == 200:
            volume = response.json().get("volume")
            return {"volume": volume}
        else:
            return {"error": "Failed to get volume."}
    # Set Volume (It works but the UI doesn't update the volume slider)
    @mcp.tool()
    def volume_set(level: float):
        """Set the volume level of the music player (0.0 to 1.0)"""
        if level < 0.0 or level > 1.0:
            return {"error": "Volume level must be between 0.0 and 1.0."}
        response = requests.post(API_URL + "volume", headers=TOKEN_HEADER, json={"volume": level})
        if response.status_code == 200:
            return {"status": f"Volume set to {level}."}
        else:
            return {"error": "Failed to set volume."}

    ## REPEAT MODES
    # Get Repeat Mode
    @mcp.tool()
    def repeat_get():
        """Get the current repeat mode of the music player"""
        response = requests.get(API_URL + "repeat-mode", headers=TOKEN_HEADER)
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
    def repeat_set(mode:str):
        """Set the repeat mode of the music player (off, track, all)"""
        mode_mapping = {
            "off": 0,
            "track": 1,
            "all": 2
        }
        # First get current repeat mode to know how many times we need to cycle toggle
        response = requests.get(API_URL + "repeat-mode", headers=TOKEN_HEADER)
        if response.status_code == 200:
            current_mode = response.json().get("value")
            target_mode = mode_mapping.get(mode)
            if target_mode is None:
                return {"error": "Invalid repeat mode. Use 'off', 'track', or 'all'."}
            # Calculate how many times we need to cycle the repeat mode
            toggles_needed = (target_mode - current_mode) % 3
            for _ in range(toggles_needed):
                toggle_response = requests.post(API_URL + "toggle-repeat", headers=TOKEN_HEADER)
                if toggle_response.status_code != 200:
                    return {"error": "Failed to set repeat mode."}
            return {"status": f"Repeat mode set to {mode}."}
        else:
            return {"error": "Failed to get current repeat mode."}

    ## SHUFFLE MODES
    # Get Shuffle Mode
    @mcp.tool()
    def shuffle_get():
        """Get the current shuffle mode of the music player"""
        response = requests.get(API_URL+"shuffle-mode", headers=TOKEN_HEADER)
        if response.status_code==200:
            if response.json().get("value"):
                return {"status": "Currently shuffle is enabled"}
            else:
                return {"status": "Currently shuffle is disabled"}
        return {"error": "Couldn't get current shuffle status"}
    # Set Shuffle Mode
    @mcp.tool()
    def shuffle_set(mode: str):
        """Set the shuffle mode of the music player (on, off)"""
        node_mapping={
            "off": 0,
            "on": 1
        }
        # Get current shuffle mode to know if we need to toggle
        response = requests.get(API_URL + "shuffle-mode", headers=TOKEN_HEADER)
        if response.status_code == 200:
            # XOR Current State with Desired State in order to set right mode
            if response.json().get("value") ^ node_mapping.get(mode):
                response = requests.post(API_URL+"toggle-shuffle", headers=TOKEN_HEADER)
                if response.status_code == 200:
                    return {"status": f"Succesfully changed shuffle mode to {mode}"}
                else:
                    return {"status": "Couldn't change shuffle mode"}
            return {"status": f"Requested shuffle mode is already {mode}"}
        return {"error": "Couldn't get current state of shuffle"}

    ## AUTOPLAY MODES
    # Get Autoplay mode
    @mcp.tool()
    def autoplay_get():
        """Gets autoplay status which is used to keep playing music after queue ends. (on, off)"""
        response = requests.get(API_URL+"autoplay", headers=TOKEN_HEADER)
        if response.status_code==200:
            if response.json().get("value"):
                return {"status": "Currently autoplay is enabled"}
            else:
                return {"status": "Currently autoplay is disabled"}
        return {"error": "Couldn't get current autoplay status"}
    ## Set Autoplay mode
    @mcp.tool()
    def autoplay_set(mode:str):
        """Sets autoplay mode which is used to keep playing music after queue ends. (on, off)"""
        node_mapping={
            "off": 0,
            "on": 1
        }
        # Get current shuffle mode to know if we need to toggle
        response = requests.get(API_URL + "autoplay", headers=TOKEN_HEADER)
        if response.status_code == 200:
            # XOR Current State with Desired State in order to set right mode
            if response.json().get("value") ^ node_mapping.get(mode):
                response = requests.post(API_URL+"toggle-autoplay", headers=TOKEN_HEADER)
                if response.status_code == 200:
                    return {"status": f"Succesfully changed autoplay mode to {mode}"}
                else:
                    return {"status": "Couldn't change autoplay mode"}
            return {"status": f"Requested autoplay mode is already {mode}"}
        return {"error": "Couldn't get current state of autoplay"}