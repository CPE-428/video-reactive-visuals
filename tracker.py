import cv2
import numpy as np


def detect_body(frame):
    # Convert BGR to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 1)

    # Apply Canny edge detection
    edges = cv2.Canny(image=blur, threshold1=40, threshold2=50)
    return edges


