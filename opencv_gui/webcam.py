import numpy as np
import cv2

def procesar_frame(img):
    # detectar y mostrar el color verde
    # convertir a el espacio de color HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    canal_color = img_hsv[:, :, 0]
    
    verde_bajo = np.array([95 // 2, 10, 100], dtype=np.uint8)
    verde_alto = np.array([125 // 2, 60, 200], dtype=np.uint8)

    # ret, mask_bajo = cv2.threshold(canal_color, verde_bajo, 255, cv2.THRESH_BINARY)
    # ret, mask_alto = cv2.threshold(canal_color, verde_alto, 255, cv2.THRESH_BINARY_INV)
    # mask = cv2.bitwise_and(mask_bajo, mask_alto)
    mask2 = cv2.inRange(img_hsv, verde_bajo, verde_alto)
    return mask2



cap = cv2.VideoCapture(1)

# verificar conexion
if not cap.isOpened():
    print("No se puede abrir webcam")
    
while True:
    # lectura de un frame
    ret, frame = cap.read()
    # operaciones con el frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out = procesar_frame(frame)
    # mostrar imagenes en una ventana
    cv2.imshow("input", frame)
    cv2.imshow("gray", out)

    # detectar una tecla
    c = cv2.waitKey(1)
    # si la tecla es 'esc'
    if c == 27: 
        # salir del bucle
        break

# liberar recursos
cap.release()
cv2.destroyAllWindows()