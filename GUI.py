import functions
import PySimpleGUI
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

PySimpleGUI.theme("Black")
clock = PySimpleGUI.Text("", key="clock")
label = PySimpleGUI.Text('Type in a To-Do')
input_box = PySimpleGUI.InputText(tooltip="Enter a To-Do", key='todo')
add_button = PySimpleGUI.Button("ADD")
list_of_todos = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                                    enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("EDIT")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")
# input_box2 = PySimpleGUI.InputText(tooltip="Enter the serial number and new todo to be edited", key='edit')

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[clock],
                                    [label],
                                    [input_box, add_button],
                                    [list_of_todos, edit_button, complete_button],
                                    [exit_button]
                                    ],
                            font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=300)
    window['clock'].update(value=time.strftime("%b %d. %Y, %H:%M:%S"))
    match event:
        case 'ADD':
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'EDIT':
            try:
                todo_list = functions.get_todos()
                print(todo_list)
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                index = todo_list.index(todo_to_edit)
                todo_list[index] = new_todo + '\n'
                print(new_todo)
                functions.write_todos(todo_list)
                window['todos'].update(values=todo_list)
            except IndexError:
                PySimpleGUI.popup("Please Select Item first", font=("Helvetica", 20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            try:
                todo_list = functions.get_todos()
                todo_list.remove(values['todo'])
                functions.write_todos(todo_list)
                window['todos'].update(values=todo_list)
            except ValueError:
                PySimpleGUI.popup("Please Select Item first", font=("Helvetica", 20))

        case 'Exit':
            break

        case PySimpleGUI.WIN_CLOSED:
            break

window.close()

