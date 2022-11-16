import cv2
import numpy as np
import argparse
from tracker import *

parser = argparse.ArgumentParser()
parser.add_argument('--input', default='simple pink dancing.mp4')
args = parser.parse_args()

tracker = Tracker()
cap = cv2.VideoCapture(args.input)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Done...")
        break

    frame_out = tracker.detect_body(frame)

    cv2.imshow('window', frame_out)
    if cv2.waitKey(1) == 27:
        break

cap.release()
