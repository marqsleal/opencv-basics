import cv2 as cv
import sys

img_path = '/home/marqsa/Python/opencv/pic.jpg'

# Abrir Imagem

img_color = cv.imread(img_path, cv.IMREAD_COLOR)

# Escala cinza: remove parte das cores e melhora o desempenho
img_gray = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

if img_color is None:
    sys.exit('Nao foi possivel ler a imagem')

# Resize Data
escala_per = 0.6
# Lembrando: Imagens sao matrizes
altura = int(img_color.shape[0] * escala_per)
largura = int(img_color.shape[1] * escala_per)
dim = (largura, altura)

color_resize = cv.resize(img_color, dim, interpolation=cv.INTER_AREA)
gray_resize = cv.resize(img_gray, dim, interpolation=cv.INTER_AREA)

# Mostrar Imagem
cv.imshow('Imagem Cor', color_resize)
cv.imshow('Imagem PB', gray_resize)


# Apertar ESC para fechar
if cv.waitKey(0) & 0xFF == 27:  # ASCII para ESC
    # Fecha todas as janelas
    cv.destroyAllWindows()

