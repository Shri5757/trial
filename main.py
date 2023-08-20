import functions

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos('todos.txt')
        for item in todos:
            print(f'{todos.index(item) + 1}.{item.title()}', end='')

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()
            indx = int(user_action[5:])
            todo_to_be_updated = todos[indx - 1]
            todo_to_be_updated = todo_to_be_updated[:len(todo_to_be_updated) - 1]
            todos[indx - 1] = input("Enter new todo: ") + '\n'

            print(f"{todo_to_be_updated} has been updated to {todos[indx - 1]}")

            functions.write_todos(todos)
        except ValueError:
            print("Please enter a valid command.")

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()
            num = int(user_action[9:])
            todo_to_be_removed = todos[num - 1]
            todo_to_be_removed = todo_to_be_removed[:len(todo_to_be_removed) - 1]
            todos.pop(num - 1)

            print(f"{todo_to_be_removed} has been removed from todos")

            functions.write_todos(todos)
        except IndexError:
            print("Please enter a number within the range")


    elif user_action.startswith('exit'):
        break

    else:
        print("Unknown command")

print("Bye! Thank you!")
