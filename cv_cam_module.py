import cv2 as cv

VIDEO_PATH = 0 # 0 for WebCam
height = 420
width = 360

cap = cv.VideoCapture(VIDEO_PATH) 

fourcc = cv.VideoWriter_fourcc(* 'XVID')
saida = cv.VideoWriter('video_test.mp4', fourcc, 20.0, (width,height))

while True:
    ret,video = cap.read()

    hsv = cv.cvtColor(video, cv.COLOR_BAYER_BG2HSV)

    saida.write(hsv)

    cv.imshow('Video', video)

    key = cv.waitKey(15) & 0xFF

    if key == ord('q'):
        break

saida.release()
cap.release()
cv.destroyAllWindows()
