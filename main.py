todos = []

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(f'{todos.index(item)+1}.{item.title()}')
        case 'edit':
            indx = int(input("Enter the item number to edit: "))
            todos[indx-1] = input("Enter new todo: ")
        case 'complete':
            num = int(input("Enter th number to mark complete: "))
            todos.pop(num-1)
        case 'exit':
            break
        case whatever:
            print("Unknown command")

print("Bye! Thank you!")

