import numpy as np
import keyboardChanges as kb

# def addFeedback(cur_frame, prev_frame):
#     black = np.zeros(cur_frame.shape, dtype=int)
#
#     return ((cur_frame + prev_frame) + black) / 1.5
def addFeedback(cur_frame, prev_frame):
    black = np.zeros(cur_frame.shape, dtype=int)

    return ((cur_frame + prev_frame) + black) / 1.2


def modifyChannel(channel, r=255, g=255, b=255):

    channel[np.all(channel == (255, 255, 255), axis=-1)] = (r, g, b)


    return channel




