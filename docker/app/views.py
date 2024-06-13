from flask import Flask
from app import app, g
import json
import imutils
import base64

@app.route("/")
def index():
    if g.vid.isOpened():
        ret, frame = g.vid.read()
        if ret:
            frame = imutils.resize(frame, width=400)
            image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
            g.last_frame = image_bytes
        else:
            image_bytes = g.last_frame
    else:
        image_bytes = last_frame
    image_base64 = base64.b64encode(image_bytes)
    return json.dumps(image_base64.decode("utf-8"))
