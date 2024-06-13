from flask import Flask
from flask_cors import CORS
import logging
import sys
import cv2

app = Flask(__name__)

CORS(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

app.config['camera'] = cv2.VideoCapture(0)
app.config['last_frame'] = None

from app import views