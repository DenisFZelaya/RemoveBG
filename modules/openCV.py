# mimodulo.py
import numpy as np
import cv2 as cv
import io
import base64
from PIL import Image

def BinaryImg(input_image_path):
    print("invoke BinaryImg")
    
    # Leer la imagen usando OpenCV
    img = cv.imread(input_image_path)
    if img is None:
        raise FileNotFoundError(f"No se pudo encontrar la imagen en la ruta: {input_image_path}")

    # Convertir la imagen a escala de grises
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Binarizar la imagen usando el método de Otsu
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Guardar la imagen binarizada temporalmente
    binarized_image_path = 'imagen_binarizada.jpg'
    cv.imwrite(binarized_image_path, thresh)

    # Abrir la imagen binarizada usando PIL
    input_image = Image.open(binarized_image_path)

    # Convertir la imagen a base64
    buffered = io.BytesIO()
    input_image.save(buffered, format="PNG")
    encoded_img = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return encoded_img


def saludar(nombre):
    return f"Hola, {nombre}!"

def despedirse(nombre):
    return f"Adiós, {nombre}!"



