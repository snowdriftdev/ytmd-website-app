import requests
import os
import time
import logging
import json

logging.basicConfig(level=logging.DEBUG, filename='logs/state-loop.log')

token = os.environ.get("YTMD_APP_TOKEN")
if token is None:
    print("Error: YTMD_APP_TOKEN environment variable is not set or could not be found. Try re-loading your terminal or IDE.")
    exit()

# adds the auth header
headers = {"Authorization": f"{token}"}

def getState():
    currentState = requests.get("http://localhost:9863/api/v1/state", headers=headers)
    #print(currentState.text)
    # unminify the json and export it to the log file
    #logging.debug(json.dumps(json.loads(currentState.text), indent=4))
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


while True:
    # converts the result to a formatted json dump and prints it
    print(json.dumps(parseStateForActiveSong(getState()), indent=4))
    time.sleep(5)
