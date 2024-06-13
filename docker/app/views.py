from flask import Flask
from app import app
import json
import imutils
import base64
import cv2

@app.route("/")
def index():
    if app.config['camera'].isOpened():
        ret, frame = app.config['camera'].read()
        if ret:
            frame = imutils.resize(frame, width=400)
            image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
            app.config['last_frame'] = image_bytes
        else:
            image_bytes = app.config['last_frame']
    else:
        image_bytes = last_frame
    image_base64 = base64.b64encode(image_bytes)
    return json.dumps(image_base64.decode("utf-8"))
