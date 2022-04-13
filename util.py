import numpy as np
import cv2 as cv

# https://stackoverflow.com/questions/19068085/shift-image-content-with-opencv
def shiftX(image, shift):
    for i in range(image.shape[1] -1, image.shape[1] - shift, -1):
        image = np.roll(image, -1, axis=1)
        image[:, -1] = 0
    
    return image

def shiftY(image, shift):
    for i in range(image.shape[0] -1, image.shape[0] - shift, -1):
        image = np.roll(image, -1, axis=0)
        image[-1, :] = 0
    
    return image

def is_moving(current_frame, previous_frame):
    frame_diff = cv.absdiff(current_frame, previous_frame)

    diff_gray = cv.cvtColor(frame_diff, cv.COLOR_BGR2GRAY)

    diff_blur = cv.GaussianBlur(diff_gray, (5,5), 0)

    _, thresh = cv.threshold(diff_blur, 20, 255, cv.THRESH_BINARY)

    thresh = cv.dilate(thresh, None, iterations=2)

    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    total = 0
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        total += cv.contourArea(contour)

    if total > (current_frame.shape[0] * current_frame.shape[1] * 0.5):
        return True

    return False