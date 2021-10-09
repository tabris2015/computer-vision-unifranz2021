import numpy as np
import cv2

cap = cv2.VideoCapture(1)

# verificar conexion
if not cap.isOpened():
    print("No se puede abrir webcam")
    
while True:
    # lectura de un frame
    ret, frame = cap.read()
    # operaciones con el frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # mostrar imagenes en una ventana
    cv2.imshow("input", frame)
    cv2.imshow("gray", gray)

    # detectar una tecla
    c = cv2.waitKey(1)
    # si la tecla es 'esc'
    if c == 27: 
        # salir del bucle
        break

# liberar recursos
cap.release()
cv2.destroyAllWindows()