import time

import numpy as np
import keyboardChanges as kb

feedbackAmount = .2
rval = 0
gval = 0
bval = 0
colorIdx = 0
colorCooldown = time.time()
# def addFeedback(cur_frame, prev_frame):
#     black = np.zeros(cur_frame.shape, dtype=int)
#
#     return ((cur_frame + prev_frame) + black) / 1.5
def addFeedback(cur_frame, prev_frame):
    global feedbackAmount
    if not kb.toggle_headpoints:
        feedbackAmount = .2
    return (cur_frame + prev_frame) / (1 + feedbackAmount)


def modifyChannel(channel, r=255, g=255, b=255):
    channel[np.all(channel == (255, 255, 255), axis=-1)] = (r, g, b)

    return channel


def headpoint_effects(xy_angles, channel):
    global feedbackAmount
    global colorIdx
    global colorCooldown
    cool = time.time()
    x = xy_angles[0]
    y = xy_angles[1]
    cutoff = 35
    if y >= cutoff:
        if feedbackAmount > 0:
            feedbackAmount /= 2

    elif y <= -cutoff:
        if feedbackAmount < 5:
            feedbackAmount += .5

    if x >= cutoff:
        channel = channel ^ -1

    elif x <= -10 and cool - colorCooldown > 2:
        colorIdx += 1
        colorCooldown = time.time()

    channel[np.all(channel == (255, 255, 255), axis=-1)] = color_mode(colorIdx)

    return channel


def color_mode(color):
    global rval
    global gval
    global bval
    red = (0, 0, 255)
    green = (0, 255, 0)
    blue = (255, 0, 0)
    rainbow = (bval, gval, rval)
    colors = [red, green, blue, rainbow]
    rval += 1
    gval += 4
    bval += 8
    return colors[color % len(colors)]



