import cv2
cap = cv2.VideoCapture(0)
def fra():
    _, frame = cap.read()
    return frame
