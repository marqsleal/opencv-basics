import cv2 as cv
import numpy as np

height = 400
width = 400

# imagem = np.zeros((height, width, 3), dtype='uint8')

imagem = cv.imread('pic.jpg')

# cv.line(imagem, (0, 0), (399, 399), (0, 255, 0), 10)

# cv.rectangle(imagem, (30, 30), (300, 300), (0, 255, 0), 5)

# cv.circle(imagem, (199, 199), 100, (255, 0, 0), 5)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(imagem, 'Linux Torvald', (50, 50), font, 0.8, (0, 255, 0), 2, cv.LINE_AA)

cv.imshow('Image - Press ESC to close', imagem)

# Apertar ESC para fechar
if cv.waitKey(0) & 0xFF == 27:  # ASCII para ESC
    # Fecha todas as janelas
    cv.destroyAllWindows()