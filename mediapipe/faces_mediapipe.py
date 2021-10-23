import numpy as np
import cv2
import mediapipe as mp

face_detector = mp.solutions.face_detection
face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(1)

# verificar conexion
if not cap.isOpened():
    print("No se puede abrir webcam")


with face_mesh.FaceMesh( max_num_faces=1, refine_landmarks=True) as mesh_detector:
    while True:
        # lectura de un frame
        ret, frame = cap.read()
        # operaciones con el frame
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = mesh_detector.process(frame)
        
        if not results.multi_face_landmarks:
            continue

        out = frame.copy()
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=out,
                landmark_list=face_landmarks,
                connections=face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
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
