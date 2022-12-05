import numpy as np
import keyboardChanges as kb

feedbackAmount = .2
colorshift = 0


# def addFeedback(cur_frame, prev_frame):
#     black = np.zeros(cur_frame.shape, dtype=int)
#
#     return ((cur_frame + prev_frame) + black) / 1.5
def addFeedback(cur_frame, prev_frame):
    global feedbackAmount
    black = np.zeros(cur_frame.shape, dtype=int)
    if not kb.toggle_headpoints:
        feedbackAmount = .2
    return ((cur_frame + prev_frame) + black) / (1 + feedbackAmount)


def modifyChannel(channel, r=255, g=255, b=255):
    channel[np.all(channel == (255, 255, 255), axis=-1)] = (r, g, b)

    return channel


def headpoint_effects(xy_angles, channel):
    global feedbackAmount
    global colorshift
    x = xy_angles[0]
    y = xy_angles[1]

    if y >= 48:
        print('Head right')
        if feedbackAmount > 0:
            feedbackAmount /= 2

    elif y <= -48:
        print('Head left')
        if feedbackAmount < 5:
            feedbackAmount += .5

    if x >= 48:
        channel = channel ^ -1

    elif x <= -48:
        channel[:, :, :3] = 255 - channel[:, :, :3]

    return channel
