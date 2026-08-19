import requests
import json
from dotenv import load_dotenv
import getstateinfo as gsi
from datetime import datetime
import os

load_dotenv()

token = os.environ.get("YTMD_APP_TOKEN")

headers = {"Authorization": f"{token}"}

# https://github.com/ytmdesktop/ytmdesktop/wiki/v2-%E2%80%90-Companion-Server-API-v1#post-command

def toggle_play_pause():
    try:
        requests.post("http://localhost:9863/api/v1/command", json={"command": "playPause"}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def volume_up():
    try:
        requests.post("http://localhost:9863/api/v1/command", json={"command": "volumeUp"}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def volume_down():
    try:
        requests.post("http://localhost:9863/api/v1/command", json={"command": "volumeDown"}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def set_volume(new_volume):
    try:
        if new_volume > 100:
            new_volume = 100
        elif new_volume < 0:
            new_volume = 0
        requests.post("http://localhost:9863/api/v1/command", json={"command": "setVolume", "data": new_volume}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def mute():
    try:
        requests.post("http://localhost:9863/api/v1/command", json={"command": "mute"}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def unmute():
    try:
        requests.post("http://localhost:9863/api/v1/command", json={"command": "unmute"}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def seek_to(jsonstate, seconds):
    #converts the time from MM:SS to seconds
    try:
        max_seconds = (datetime.strptime(jsonstate["duration"], "%M:%S") - datetime(1900, 1, 1)).total_seconds()

        if seconds > max_seconds:
            seconds = max_seconds - 1
        if seconds < 0:
            seconds = 0
        print(max_seconds)
        requests.post("http://localhost:9863/api/v1/command", json={"command": "seekTo", "data": seconds}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def next_song():
    try:
        requests.post("http://localhost:9863/api/v1/command", json={"command": "next"}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def previous_song():
    try:
        requests.post("http://localhost:9863/api/v1/command", json={"command": "previous"}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def set_repeat_mode(mode):
    try:
        requests.post("http://localhost:9863/api/v1/command", json={"command": "repeatMode", "data": mode}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")

def toggle_shuffle():
    try:
        requests.post("http://localhost:9863/api/v1/command", json={"command": "shuffle"}, headers=headers)
    except Exception as e:
        print(f"ERROR: {e}")