import numpy as np
from time import time
import cv2
import tensorflow as tf
import keras
from keras.applications.efficientnet import EfficientNetB7, preprocess_input, decode_predictions
from keras.preprocessing import image


class Classifier:
    def __init__(self, img_size) -> None:
        self.img_size = img_size
        self.model = EfficientNetB7(weights="imagenet")
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        
    def predict(self, img, top=3):

        img = cv2.resize(img, self.img_size)
        # dims (224, 224, 3)

        # x = image.img_to_array(img)
        # dims (1, 224, 224, 3)
        x = np.expand_dims(img, axis=0)
        x = preprocess_input(x)

        start_time = time()
        preds = self.model.predict(x)
        decoded = decode_predictions(preds, top=top)[0]
        print(f"Tiempo: {(time() - start_time)*1000:.1f}[ms]")
        return {label:conf for _, label, conf in decoded}

    def predict_and_display(self, img, top=3):
        base_img = img.copy()
        preds = self.predict(img, top)
        # dibujar predicciones sobre imagen
        x = 5
        y = 35
        for label, conf in preds.items():
            cv2.putText(base_img, f"{label}: {conf:.2f}", (x, y), self.font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            y += 45

        return base_img



cap = cv2.VideoCapture(1)

clf = Classifier(img_size=(600, 600))
# verificar conexion
if not cap.isOpened():
    print("No se puede abrir webcam")
    
while True:
    # lectura de un frame
    ret, frame = cap.read()
    # operaciones con el frame
    out = clf.predict_and_display(frame)
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