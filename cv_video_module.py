import cv2 as cv

VIDEO_PATH = 'video.mp4'
height = 420
width = 360

cap = cv.VideoCapture(VIDEO_PATH)

while True:
    ret,video = cap.read()

    video1 = cv.resize(video, (width,height), fx=0, fy=0, interpolation=cv.INTER_AREA)

    cv.imshow('Video', video1)

    key = cv.waitKey(15) & 0xFF

    if key == ord('q'):
        break

cv.destroyAllWindows()
cap.release()