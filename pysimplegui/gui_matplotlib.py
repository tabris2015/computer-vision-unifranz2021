import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib

matplotlib.use("TkAgg")

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)

t = np.arange(0, 3, 0.01)
f_t = 2 * np.sin(2 * np.pi * t)

dibujo = fig.add_axes([0, 0, 1, 1])
dibujo.plot(t, f_t)

def dibujar(canvas, figure):
    figure_canvas = FigureCanvasTkAgg(figure, canvas)
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack(side="top", fill="both", expand=0)
    return figure_canvas

# pysimplegui

# layout
layout = [
    [sg.Text("Funcion plot test")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button("OK"), sg.Button("Coseno", key="-BUT COS-")]
]

#crear ventana
window = sg.Window(
    "test matplotlib",
    layout=layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18"
)

dibujar(window["-CANVAS-"].TKCanvas, fig)

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

    if event == "-BUT COS-":
        dibujo.plot(t, np.cos(2 * np.pi * t))
        dibujar(window["-CANVAS-"].TKCanvas, fig)



window.close()