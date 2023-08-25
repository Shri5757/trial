import functions
import PySimpleGUI


label = PySimpleGUI.Text('Type in a To-Do')
input_box = PySimpleGUI.InputText(tooltip="Enter a To-Do", key='todo')
add_button = PySimpleGUI.Button("ADD")
list_of_todos = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                                    enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("EDIT")
# input_box2 = PySimpleGUI.InputText(tooltip="Enter the serial number and new todo to be edited", key='edit')

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[label],
                                    [input_box, add_button],
                                    [list_of_todos, edit_button]
                                    ],
                            font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'ADD':
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'EDIT':
            todos = functions.get_todos()
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()

