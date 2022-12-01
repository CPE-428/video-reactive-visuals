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
    rgb_out = tracker.detect_body(frame)

    if not ret:
        print("Done...")
        break

    cv2.imshow('window', rgb_out)

    rgb_out = addFeedback(rgb_out, prev_frame)

    prev_frame = rgb_out

    cv2.imshow('feedback', rgb_out)
    if cv2.waitKey(1) == 27:
        break

cap.release()
