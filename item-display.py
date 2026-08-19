import getstateinfo as gsi
from flask import Flask, Response
import os
import json
import time
from dotenv import load_dotenv
load_dotenv()


def get_current_song():
    currentSongData = gsi.parseStateForActiveSong(gsi.getState())
    return currentSongData


def event_stream():
    last_value = None
    while True:
        value = get_current_song()
        if value != last_value:
            yield (f"data: {json.dumps(value)}\n\n")
            last_value = value

def stream():
    return Response(event_stream(), mimetype="text/event-stream")

#TODO: make the website interface (claude --resume)