
file = open("example.txt", 'r')
todos = file.readlines()
file.close()

while True:
    user_action = input("Type add, show, edit, complete, exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + '\n'
            
            # to read the contents of the file, can be absolute or relative path
            # r"<<text>>" clarifies that is a raw string"
            file = open("example.txt" , 'r')
            todos = file.readlines()
            todos.append(todo)

            # in order to store the todo list
            file = open("example.txt", 'w') 
            file.writelines(todos) #rewrites the file
            #file.write(todos) #file.read (reads everything as a string) 
            file.close()

            #work with .conf
            file = open("example.conf", 'w')
            file.writelines(todos + ["funny string"])
            file.close()
        case "show":
            for index, task in enumerate(todos):
                #print(index, '.', task)
                #reserved word f<<string>> to access variables
                row = f"{index+1}- {task.capitalize()}"
                print(row)
        case "edit":
            #input always produce string type
            number = input("Enter the number to edit task: ")
            number = int(number) - 1
            new_todo = input("Enter edited new todo: ")
            todos[number]= new_todo
        case "complete":
            number = input("Enter the number of complete task: ")
            number = int(number) - 1
            todos.pop(number)
        case "exit" | _:
            print("See you soon!")
            break
        
print("Closing program...")