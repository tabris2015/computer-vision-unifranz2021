from tkinter import Frame
from PySimpleGUI.PySimpleGUI import Window
import numpy as np
import cv2
import PySimpleGUI as sg

# layout
layout = [
    [sg.Text("opencv webcam")],
    [sg.Image(filename="", key="-GUI_IMG-")]
]

# crear ventana
window = sg.Window(
    "opencv pysimplegui", 
    layout=layout, 
    element_justification="center",
    font="Helvetica 18"
    )

# webcam
cap = cv2.VideoCapture(1)

# event loop
while True:
    event, values = window.read(timeout=20)

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    ret, frame = cap.read()
    # desplegar imagen obtenida en la GUI
    img_bytes = cv2.imencode(".png", frame)[1].tobytes()
    window["-GUI_IMG-"].update(data=img_bytes)



window.close()