import functions
import PySimpleGUI

label = PySimpleGUI.Text('Type in a To-Do')
input_box = PySimpleGUI.InputText(tooltip="Enter a To-Do")
add_button = PySimpleGUI.Button("ADD")
window = PySimpleGUI.Window('My To-Do App',layout=[[label],[input_box, add_button]])
window.read()