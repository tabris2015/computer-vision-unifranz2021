import os.path
import PySimpleGUI as sg

# layout
file_list_column = [
    [
        sg.Text("Directorio"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(values=[], enable_events=True, size=(40, 40), key="-FILE LIST-")
    ]
]

image_viewer_column = [
    [sg.Text("Escoja una imagen de la lista: ")],
    [sg.Text(size=(60, 2), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")]
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column)
    ]
]

# crear ventana
window = sg.Window("Image Viewer", layout)

# event loop
while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # ingreso directorio, se llena una lista de archivos disponibles
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
            print(file_list)
        except:
            print("directorio invalido")
            file_list = []
        # limpiar lista de archivos disponibles
        fnames = [
            f for f in file_list
            if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".png", ".gif"))
        ]

        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            print("archivo invalido")


window.close()