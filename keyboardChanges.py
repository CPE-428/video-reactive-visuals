import keyboard as kb

color_toggle = False
feedback_toggle = False
toggle_headpoints = False

def toggleColor():
    global color_toggle
    color_toggle = not color_toggle


def toggleFeedback():
    global feedback_toggle
    feedback_toggle = not feedback_toggle

def toggleHeadposeEffects():
    global toggle_headpoints
    toggle_headpoints = not toggle_headpoints

def addHotkeys():
    kb.add_hotkey('c', toggleColor)
    kb.add_hotkey('f', toggleFeedback)
    kb.add_hotkey('h', toggleHeadposeEffects)
