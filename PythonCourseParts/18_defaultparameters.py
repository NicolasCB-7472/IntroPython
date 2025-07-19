# To import elements from other files
# from split import get_nr_items
# import split #global functions are executed, not functions that are defined but not call
# call usecase: split.get_nr_items()
# allow functions to work outside a file: if __name__ == "__filename__"


# Functions part
# Reads the contents of example (as in video)
def read_file():
    """ This is a function that reads a file, a file is read """
    file = open("example.txt", 'r')
    todos = file.readlines()
    file.close()
    return todos

# Use case of adding todo
def case_add(user_action: str):
    """ Takes user input parameter and executes add case"""
    todo = user_action[4:] + '\n'

    file = open("example.txt" , 'r')
    todos = file.readlines()
    todos.append(todo)

    file = open("example.txt", 'w') 
    file.writelines(todos)
    file.close()

# Use case for showing todos
def case_show(user_action: str, todos: list):
    """ Takes user input parameter, todo list and executes show case"""
    new_todos = [item.strip('\n').capitalize() for item in todos]

    for index, task in enumerate(new_todos):
        row = f"{index+1}- {task.capitalize()}"
        print(row)


# Use case for editing a todo
def case_edit(user_action: str):
    """ Attempts to take user input parameter and executes edit case if possible"""
    try:
        number = input("Enter the number to edit task: ")
        number = int(number) - 1

        with open("example.txt", 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter edited new todo: ")
        todos[number]= new_todo + '\n'

        with open("example.txt", 'w') as file:
            file.writelines(todos)
    except (ValueError, IndexError):
        print("Command invalid")

# Use case for completing a todo
def case_complete(user_action: str):
    """ Attempts to take user input parameter and executes complete case if possible"""
    try:
        number = input("Enter the number of complete task: ")
        number = int(number) - 1
        
        with open("example.txt", 'r') as file:
            todos = file.readlines()
        message = todos[number].strip('\n')
        todos.pop(number)

        with open("example.txt", 'w') as file:
            file.writelines(todos)

        print(f"Todo eliminado {message}")
    except IndexError:
        print("Number invalid")

# Program halted, there are better ways to do this
def halt_program(condicion_ejecucion: bool):
    """ Halt! """
    print("See you soon!")
    condicion_ejecucion = False
    return condicion_ejecucion


#Main part
condicion_ejecucion = True
while condicion_ejecucion:
    user_action = input("Type add, show, edit, complete, exit: ")
    user_action = user_action.strip()

    todos = read_file()

    if user_action.startswith("add"):
        case_add(user_action)

    elif user_action.startswith("show"):
        case_show(user_action, todos)

    elif user_action.startswith("edit"):
        case_edit(user_action)

    elif user_action.startswith("complete"):
        case_complete(user_action)

    elif user_action.startswith("exit"):
        condicion_ejecucion = halt_program(condicion_ejecucion)
    else:
        condicion_ejecucion = halt_program(condicion_ejecucion)
        
print("Closing program...")


# Note:
# Functions can have a default parameters meaning assignment when declared
# When called can be modified with a new parameter
# There is also explicit parameter calls

# Important note
# If something doesn't make sense, bare in mind this code was meant to be
# the first educational project in learning python from the course
# and is respecting its original structure