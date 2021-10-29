from tkinter import Frame
from PySimpleGUI.PySimpleGUI import Window
from matplotlib.pyplot import show
import numpy as np
import cv2
import tensorflow_hub as hub
from cvlib.object_detection import draw_bbox

import PySimpleGUI as sg


LABELS = [
"person",
"bicycle",
"car",
"motorcycle",
"airplane",
"bus",
"train",
"truck",
"boat",
"traffic light",
"fire hydrant",
"street sign",
"stop sign",
"parking meter",
"bench",
"bird",
"cat",
"dog",
"horse",
"sheep",
"cow",
"elephant",
"bear",
"zebra",
"giraffe",
"hat",
"backpack",
"umbrella",
"shoe",
"eye glasses",
"handbag",
"tie",
"suitcase",
"frisbee",
"skis",
"snowboard",
"sports ball",
"kite",
"baseball bat",
"baseball glove",
"skateboard",
"surfboard",
"tennis racket",
"bottle",
"plate",
"wine glass",
"cup",
"fork",
"knife",
"spoon",
"bowl",
"banana",
"apple",
"sandwich",
"orange",
"broccoli",
"carrot",
"hot dog",
"pizza",
"donut",
"cake",
"chair",
"couch",
"potted plant",
"bed",
"mirror",
"dining table",
"window",
"desk",
"toilet",
"door",
"tv",
"laptop",
"mouse",
"remote",
"keyboard",
"cell phone",
"microwave",
"oven",
"toaster",
"sink",
"refrigerator",
"blender",
"book",
"clock",
"vase",
"scissors",
"teddy bear",
"hair drier",
"toothbrush",
"hair brush"
]

# funciones
def draw_objects(img, boxes, scores, classes, min_score=0.5, show_scores=False):
    img2 = img.copy()
    
    for bbox, class_id, score in zip(boxes, classes, scores):
        # print(bbox,class_id, score)

        x0 = int(bbox[1])
        y0 = int(bbox[0])
        x1 = int(bbox[3])
        y1 = int(bbox[2])
        # print(x0, y0, x1, y1)
        if score > min_score:
            cv2.rectangle(
                img2, 
                (x0, y0), 
                (x1, y1), 
                (0, 255, 0), 
                3
            )
            label = LABELS[int(class_id.numpy().item()) - 1]
            cv2.putText(img2, label, (x0, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            if show_scores:
                cv2.putText(img2, f"{score.numpy().item():.2f}", (x0, y1+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    return img2

# layout
layout = [
    [sg.Text("opencv webcam")],
    [sg.Image(filename="", key="-GUI_IMG-")],
    [sg.Slider((0, 100), 50, 1, orientation="h", size=(40, 15), key="-GUI_THRES_SLIDER-"), sg.Checkbox("Scores: ", key="-GUI_SHOW_SCORES-")]
]

# crear ventana
window = sg.Window(
    "opencv pysimplegui", 
    layout=layout, 
    element_justification="center",
    font="Helvetica 18",
    resizable=True
    )

# webcam
cap = cv2.VideoCapture(1)

# instanciar el modelo
detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")

# event loop
while True:
    event, values = window.read(timeout=20)

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if values["-GUI_SHOW_SCORES-"]:
        show_scores = values["-GUI_SHOW_SCORES-"]
    else:
        show_scores = False

    print(show_scores)
    
    if values["-GUI_THRES_SLIDER-"]:
        min_score = values["-GUI_THRES_SLIDER-"] / 100.0
        # print(f"min score: {min_score}")

    ret, frame = cap.read()
    frame = np.expand_dims(frame, axis=0).astype(np.uint8)
    # print(frame.shape)
    # procesamiento del frame
    boxes, scores, classes, num_detections = detector(frame)

    out = draw_objects(frame[0], boxes[0], scores[0], classes[0], min_score=min_score, show_scores=show_scores)
    # print(out.shape)
    # draw_bbox(frame, bbox, label, conf)

    # desplegar imagen obtenida en la GUI
    img_bytes = cv2.imencode(".png", out)[1].tobytes()
    window["-GUI_IMG-"].update(data=img_bytes)



window.close()