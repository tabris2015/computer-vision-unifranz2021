import PySimpleGUI as sg

# layout: el conjunto de elementos presentes en una ventana
layout = [
    [sg.Text("hola amigos")], 
    [sg.Button("OK")]
    ]

# crear ventana
window = sg.Window("Hola", layout)

# event loop
while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()