import PySimpleGUI as gui

txt1 = gui.Text("Enter feet")
feet_ip = gui.InputText(tooltip='Enter feet')
txt2 = gui.Text("Enter Inches")
inches = gui.InputText()
button = gui.Button('Convert')

window = gui.Window("Converter", layout = [[txt1,feet_ip],[txt2,inches]])
window.read()

