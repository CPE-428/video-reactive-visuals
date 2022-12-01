import cv2
import numpy as np
import argparse
from tracker import *
from imageMods import *

parser = argparse.ArgumentParser()
parser.add_argument('--input', default='./videos/simple pink dancing.mp4')
args = parser.parse_args()

tracker = Tracker()
# cap = cv2.VideoCapture(args.input)
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
rgb_out = tracker.detect_body(frame)

while cap.isOpened():
    prev_frame = rgb_out[:]
    ret, frame = cap.read()

    if not ret:
        print("Done...")
        break

    # Body Outline
    rgb_out = tracker.detect_body(frame)
    cv2.imshow('window', rgb_out)

    # Body After-Effect
    rgb_out = addFeedback(rgb_out, prev_frame)
    prev_frame = rgb_out
    cv2.imshow('feedback', rgb_out)

    # Eye Detection
    # Problem: video contains silhouette of the performer, so face features aren't detected
    # Possible Solutions:
    #   detect circles (eyes) from the image produced from the edge detection feature
    #   brighten the darker areas of the frame to detect face features

    tracker.detect_face(frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
