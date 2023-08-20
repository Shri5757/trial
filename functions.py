def get_todos(filepath='todos.txt'):
    """ Reads the text file from the given path
    and returns a todo list
    """
    with open(filepath, 'r') as file_local:
        """ Writes the todo item in the txt file which is 
        at the filepath location
        """
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
