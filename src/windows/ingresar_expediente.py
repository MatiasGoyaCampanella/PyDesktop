import PySimpleGUI as sg
from src.consts.font import font_name, font_size


sg.theme('DarkGreen3')

def build():

    categorias = [ "Segurizado", "No Segurizado"]
    
    layout = [
        [sg.Text('Ingresar Edificio',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Text('ID', size=(15,1)), sg.Spin(list(range(99999)), size=(10, 1), key="-ID-")],
        [sg.Text('Edificio', size=(15,1)), sg.Input(size=(30,1),key='-EDIFICIO-')],
        [sg.Text('Contacto', size=(15,1)), sg.Input(size=(30,1),key='-CONTACTO-')],
        [sg.Text('Estado', size=(15,1)), sg.Input(size=(30,1),key='-ESTADO-')],
        [sg.Text('Categoría', size=(15,1)), sg.Combo(categorias,default_value=categorias[0],size=(24,1),key="-CATEGORIA-",readonly=True)],
        [sg.Button('Guardar', size=(10, 1),key="-GUARDAR-", bind_return_key=True)]
    ]

    window = sg.Window('Ingresar Edificio', layout, font=(font_name,font_size), modal=True)
    return window