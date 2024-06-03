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
        raise FileNotFoundError(
            f"No se pudo encontrar la imagen en la ruta: {input_image_path}")

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


def PerpectiveTransformation(input_image_path):
    print("invoke PerpectiveTransformation")

    # Leer la imagen usando OpenCV
    img = cv.imread(input_image_path)
    if img is None:
        raise FileNotFoundError(
            f"No se pudo encontrar la imagen en la ruta: {input_image_path}")
        
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    
    M = cv.getPerspectiveTransform(pts1,pts2)
    
    dst = cv.warpPerspective(img,M,(300,300))
    
    # Guardar la imagen binarizada temporalmente
    perspective_transformation = 'perspective_transformation.jpg'
    cv.imwrite(perspective_transformation, dst)

    # Abrir la imagen binarizada usando PIL
    input_image = Image.open(perspective_transformation)

    # Convertir la imagen a base64
    buffered = io.BytesIO()
    input_image.save(buffered, format="PNG")
    encoded_img = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return encoded_img

def Canny(input_image_path):
    print("invoke Laplacian")

    # Leer la imagen usando OpenCV
    img = cv.imread(input_image_path)
    if img is None:
        raise FileNotFoundError(
            f"No se pudo encontrar la imagen en la ruta: {input_image_path}")
        
    laplacian = cv.Canny(img,100,200)
    sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
    sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
    
    # Guardar la imagen binarizada temporalmente
    response = 'canny.jpg'
    cv.imwrite(response, laplacian)

    # Abrir la imagen binarizada usando PIL
    input_image = Image.open(response)

    # Convertir la imagen a base64
    buffered = io.BytesIO()
    input_image.save(buffered, format="PNG")
    encoded_img = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return encoded_img

def Laplacian(input_image_path):
    print("invoke Laplacian")

    # Leer la imagen usando OpenCV
    img = cv.imread(input_image_path)
    if img is None:
        raise FileNotFoundError(
            f"No se pudo encontrar la imagen en la ruta: {input_image_path}")
        
    laplacian = cv.Laplacian(img,cv.CV_64F)
    sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
    sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
    
    # Guardar la imagen binarizada temporalmente
    response = 'laplacian.jpg'
    cv.imwrite(response, laplacian)

    # Abrir la imagen binarizada usando PIL
    input_image = Image.open(response)

    # Convertir la imagen a base64
    buffered = io.BytesIO()
    input_image.save(buffered, format="PNG")
    encoded_img = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return encoded_img
