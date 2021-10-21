import io
from keras.backend import dtype
import numpy as np
import cv2
from keras.applications.efficientnet import EfficientNetB0, preprocess_input, decode_predictions
from time import time

class Classifier:
    def __init__(self, img_size) -> None:
        self.img_size = img_size
        self.model = EfficientNetB0(weights="imagenet")
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        
    def predict(self, img, top=3):

        img = cv2.resize(img, self.img_size)

        x = np.expand_dims(img, axis=0)
        x = preprocess_input(x)

        start_time = time()
        preds = self.model.predict(x)
        decoded = decode_predictions(preds, top=top)[0]
        print(f"Tiempo: {(time() - start_time)*1000:.1f}[ms]")
        return {label:float(conf) for _, label, conf in decoded}

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

    def predict_file(self, file, top=3):
        img_stream = io.BytesIO(file.file.read())
        img_stream.seek(0)

        img = np.asarray(bytearray(img_stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)

        return self.predict(img, top)