import cv2 as cv

VIDEO_PATH = 0  # 0 para a webcam
height = 420
width = 360

cap = cv.VideoCapture(VIDEO_PATH)

fourcc = cv.VideoWriter_fourcc(*'XVID')
saida = cv.VideoWriter('video_test.avi', fourcc, 20.0, (width, height))

while True:
    ret, video = cap.read()

    if not ret:
        print("Falha na captura de vídeo.")
        break

    video = cv.resize(video, (width, height))
    hsv = cv.cvtColor(video, cv.COLOR_BGR2HSV)
    saida.write(video)
    cv.imshow('Video', video)
    key = cv.waitKey(15) & 0xFF

    if key == ord('q'):
        break

saida.release()
cap.release()
cv.destroyAllWindows()