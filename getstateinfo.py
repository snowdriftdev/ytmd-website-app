import requests
import os
import time
import logging
import json
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.DEBUG, filename='logs/state-loop.log')

token = os.environ.get("YTMD_APP_TOKEN")
if token is None:
    print("Error: YTMD_APP_TOKEN environment variable is not set or could not be found. Try re-loading your terminal or IDE.")
    exit()

# adds the auth header
headers = {"Authorization": f"{token}"}

# this should be called in most things that require the current state
# TODO: implement a caching system with datetime (like a 5s cache with automated timing offset calculation)
def getState():
    currentState = requests.get("http://localhost:9863/api/v1/state", headers=headers)
    #print(currentState.text)
    # unminify the json and export it to the log file
    # logging.debug(json.dumps(json.loads(currentState.text), indent=4))
    return(currentState.text)

def parseStateForActiveSong(state):
    jsonState = json.loads(state)
    for item in jsonState["player"]["queue"]["items"]:
        if item["selected"]:
            logging.debug(json.dumps(item, indent=4))
            # returns just the currently playing song from the queue
            return(item)
    print("ERROR: No current song found.")
    return("")

def parseStateForTrackStatus(state):
    jsonState = json.loads(state)
    # -1 Unknown, 0 Paused, 1 Playing, 2 Buffering | Returns the current track status
    return jsonState["player"]["trackState"]

def parseStateForTrack(state):
    jsonState = json.loads(state)
    # returns how long in seconds the player is through the video/song
    return jsonState["player"]["videoProgress"]

# while True:
#     # converts the result to a formatted json dump and prints it
#     print(json.dumps(parseStateForActiveSong(getState()), indent=4))
#     time.sleep(5)
