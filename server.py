from flask import Flask, Response
import time
import json
import socketio
import os
import threading

from dotenv import load_dotenv
load_dotenv()

sio = socketio.Client()

@sio.on("state-update")
def on_state_update(data):
    print(data)


@sio.on("connect")
def on_connect():
    print("connected to YTMD")

@sio.on("connect_error")
def on_connect_error(data):
    print(f"connection failed: {data}")

@sio.on("disconnect")
def on_disconnect():
    print("disconnected")

def start_socketio():
    sio.connect(
    "http://127.0.0.1:9863",
        transports=["websocket"],
        auth={"token": os.environ.get("YTMD_APP_TOKEN")},
    )

    sio.wait()

sio_thread = threading.Thread(target=start_socketio, daemon=True)
sio_thread.start()
app = Flask(__name__)

def event_stream():
    while True:
        payload = json.dumps({"title": "Test Song", "artist": "Test Artist"})
        yield f"data: {payload}\n\n"
        time.sleep(2)

@app.route("/events")
def events():
    return Response(event_stream(), mimetype = "text/event-stream")

@app.route("/")
def index():
    return "<h1>hello</h1>"

if __name__ == "__main__":
    app.run(debug=True)