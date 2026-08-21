from flask import Flask, Response, render_template, request
import time
import json
import socketio
import os
import threading
import ytmdcommands as cmd

from dotenv import load_dotenv
load_dotenv()

sio = socketio.Client()

@sio.on("state-update", namespace="/api/v1/realtime")
def on_state_update(data):
    global latest_state
    latest_state = data

def start_socketio():
    sio.connect(
    "http://127.0.0.1:9863",
        transports=["websocket"],
        auth={"token": os.environ.get("YTMD_APP_TOKEN")},
        namespaces=["/api/v1/realtime"]
    )

    sio.wait()

sio_thread = threading.Thread(target=start_socketio, daemon=True)
sio_thread.start()
app = Flask(__name__)

def event_stream():
    while True:
        payload = json.dumps(latest_state)
        yield f"data: {payload}\n\n"
        time.sleep(2)

@app.route("/events")
def events():
    return Response(event_stream(), mimetype = "text/event-stream")

@app.route("/music")
def music_page():
    return render_template("music.html")

@app.route("/command", methods=["POST"])
def command():
    body = request.get_json()
    command_name = body.get("command")
    commands = {
        "toggle_play_pause": cmd.toggle_play_pause,
        "next_song": cmd.next_song,
        "previous_song": cmd.previous_song,
    }

    if command_name in commands:
        commands[command_name]()
        return "", 204
    return "", 400

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)