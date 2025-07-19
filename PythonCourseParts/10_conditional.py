
file = open("example.txt", 'r')
todos = file.readlines()
file.close()

while True:
    user_action = input("Type add, show, edit, complete, exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        # list slicing
        todo = user_action[4:] + '\n'

        file = open("example.txt" , 'r')
        todos = file.readlines()
        todos.append(todo)

        file = open("example.txt", 'w') 
        file.writelines(todos)
        file.close()

        file = open("example.conf", 'w')
        file.writelines(todos + ["funny string"])
        file.close()
    elif "show" in user_action:
        new_todos = [item.strip('\n').capitalize() for item in todos]

        for index, task in enumerate(new_todos):
            row = f"{index+1}- {task.capitalize()}"
            print(row)
    elif "edit" in user_action:
        number = input("Enter the number to edit task: ")
        number = int(number) - 1

        with open("example.txt", 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter edited new todo: ")
        todos[number]= new_todo + '\n'

        with open("example.txt", 'w') as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = input("Enter the number of complete task: ")
        number = int(number) - 1
        
        with open("example.txt", 'r') as file:
            todos = file.readlines()
        message = todos[number].strip('\n')
        todos.pop(number)

        with open("example.txt", 'w') as file:
            file.writelines(todos)

        print(f"Todo eliminado {message}")

    elif "exit" in user_action:
        print("See you soon!")
        break
    else:
        print("See you soon!")
        break
        
print("Closing program...")