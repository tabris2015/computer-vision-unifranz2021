import numpy as np
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(1)

# verificar conexion
if not cap.isOpened():
    print("No se puede abrir webcam")


with mp_hands.Hands(model_complexity=0) as hands:
    while True:
        # lectura de un frame
        ret, frame = cap.read()
        # operaciones con el frame
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = hands.process(frame)
        
        if not results.multi_hand_landmarks:
            continue

        out = frame.copy()
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                out,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
        # mostrar imagenes en una ventana
        cv2.imshow("out", out)

        # detectar una tecla
        c = cv2.waitKey(1)
        # si la tecla es 'esc'
        if c == 27: 
            # salir del bucle
            break

# liberar recursos
cap.release()
cv2.destroyAllWindows()
