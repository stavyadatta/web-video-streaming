from motion_detection.singlemotiondetection import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import imutils
import time
import cv2

outputFrame = None
lock = threading.Lock()

app = Flask(__name__)
