
file = open("example.txt", 'r')
todos = file.readlines()
file.close()

# Bugs section :
# .startswith is added
# edit is corrected (in example it was used in one line to add the todo, number type needed)
# complete is corrected (out of bounds) 

# Syntax error/ Exception error

while True:
    user_action = input("Type add, show, edit, complete, exit: ")
    user_action = user_action.strip()

    # in works in a funny way, .startswith()
    if user_action.startswith("add"):
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
    elif user_action.startswith("show"):
        new_todos = [item.strip('\n').capitalize() for item in todos]

        for index, task in enumerate(new_todos):
            row = f"{index+1}- {task.capitalize()}"
            print(row)
    elif user_action.startswith("edit"):
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

    elif user_action.startswith("complete"):
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
    elif user_action.startswith("exit"):
        print("See you soon!")
        break
    else:
        print("See you soon!")
        break
        
print("Closing program...")