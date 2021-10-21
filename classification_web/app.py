import io
import uvicorn
import numpy as np
from fastapi import FastAPI, UploadFile, File, HTTPException
from classifier import Classifier

clf = Classifier((224, 224))
app = FastAPI(title="Image classification service")


@app.get("/")
def index():
    return "La API funciona!"


@app.post("/predict")
def predict(n_top: int = 3, file: UploadFile = File(...)):
    # validar imagen de entrada
    is_valid = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")

    if not is_valid:
        raise HTTPException(status_code=415, detail="Tipo de archivo no soportado")

    preds = clf.predict_file(file, n_top)

    return preds


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)