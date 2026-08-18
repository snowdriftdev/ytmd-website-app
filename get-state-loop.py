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
    print(currentState.text)
    # unminify the json and export it to the log file
    logging.debug(json.dumps(json.loads(currentState.text), indent=4))

while True:
    getState()
    time.sleep(5)
