import numpy as np
import cv2
import mediapipe as mp
import math
# from protobuf_to_dict import protobuf_to_dict

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(1)

def dist_3d(punto1, punto2):
    accum = (punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2 + (punto1[2] - punto2[2])**2
    return math.sqrt(accum) # indice a pulgar

def dist_total(lista_puntos):
    #   0   1  2    3   4
    # [p0, p1, p2, p3, p4]
    # [(p0, p1), (p1, p2), (p2, p3), (p3, p4)]
    # 
    # rango: 0, 1, 2, 3
    combos = [(lista_puntos[i], lista_puntos[i + 1]) for i in range(len(lista_puntos) - 1)]
    
    total = 0
    for p_a, p_b in combos:
        total += dist_3d(p_a, p_b)
    
    return total


def procesar_landmarks(landmarks, img_size, umbral=0.1, umbral_palma_abierta=0.6, umbral_palma_cerrada=0.4):
    # data_points = protobuf_to_dict(landmarks)
    data_points = [(dp.x, dp.y, dp.z) for dp in landmarks.landmark]

    indice_point = data_points[8]
    
    # print(f"indice: ({indice_point[0]:.2f}, {indice_point[1]:.2f})")

    pulgar_point = data_points[4]
    medio_point = data_points[12]
    
    dedos = [data_points[4], data_points[8], data_points[12], data_points[16], data_points[20]]

    resultado = "-"
    pos = (0, 0)

    if dist_3d(indice_point, pulgar_point) < umbral:
        resultado = "indice!"
        pos = (int(indice_point[0] * img_size[0]), int(indice_point[1] * img_size[1]))

    elif dist_3d(medio_point, pulgar_point) < umbral:
        resultado = "medio!"
        pos = (int(medio_point[0] * img_size[0]), int(medio_point[1] * img_size[1]))

    elif dist_total(dedos) > umbral_palma_abierta:
        resultado = "abierto!"
    elif dist_total(dedos) < umbral_palma_cerrada:
        resultado = "cerrado!"

    return resultado, pos

# verificar conexion
if not cap.isOpened():
    print("No se puede abrir webcam")


with mp_hands.Hands(model_complexity=0) as hands:
    while True:
        # lectura de un frame
        ret, frame = cap.read()
        # print(frame.shape)
        # operaciones con el frame
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = hands.process(frame)
        
        if not results.multi_hand_landmarks:
            continue

        out = frame.copy()
        for hand_landmarks in results.multi_hand_landmarks:
            evento, pos_evento = procesar_landmarks(hand_landmarks, (frame.shape[1], frame.shape[0]))
            
            if evento in ("indice!", "medio!"):
                cv2.circle(
                    out, 
                    pos_evento, 
                    25, 
                    (0, 255, 0) if evento == "indice!" else (0, 0, 255), 
                    3
                    )

            cv2.putText(out, evento, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            
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
