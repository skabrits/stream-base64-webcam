from flask import Flask, g
from flask_cors import CORS
import logging
import sys

app = Flask(__name__)

CORS(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

g.last_frame = None
g.vid = cv2.VideoCapture(0)

from app import views