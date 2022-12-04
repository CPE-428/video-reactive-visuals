import keyboard as kb

color_toggle = False
feedback_toggle = False


def toggleColor():
    global color_toggle
    color_toggle = not color_toggle


def toggleFeedback():
    global feedback_toggle
    feedback_toggle = not feedback_toggle


def addHotkeys():
    kb.add_hotkey('c', toggleColor)
    kb.add_hotkey('f', toggleFeedback)
