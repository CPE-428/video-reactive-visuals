import argparse
# import dlib

from imageMods import *
from tracker import *

parser = argparse.ArgumentParser()
parser.add_argument('--input', default='./videos/simple pink dancing.mp4')
args = parser.parse_args()

tracker = Tracker()
# cap = cv2.VideoCapture(args.input)
cap = cv2.VideoCapture(0)

ret, frame = cap.read()

rgb_out = tracker.detect_body(frame)

r = 0
prev_frame = np.zeros(frame.shape, dtype=int)

kb.addHotkeys()


#THE HEAD POSE FUNCTION ONLY WORKS ON A SINGLE IMAGE
tracker.head_pose(frame)


while cap.isOpened():



    ret, frame = cap.read()
    rgb_out = tracker.detect_body(frame)

    if not ret:
        print("Done...")
        break

    cv2.imshow('window', rgb_out)

    channel = np.dstack([rgb_out, rgb_out, rgb_out])

    if kb.color_toggle:
        channel = modifyChannel(channel, r, r * 4, r * 8)
        r += 4

    if kb.feedback_toggle:
        channel = addFeedback(channel, prev_frame)

    prev_frame = channel

    cv2.imshow('feedback', channel)
    if cv2.waitKey(1) == 27:
        break

cap.release()



