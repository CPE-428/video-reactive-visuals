import numpy as np


def addFeedback(cur_frame, prev_frame):
    black = np.zeros(cur_frame.shape, dtype=int)

    return ((cur_frame + prev_frame) + black) / 1.5
