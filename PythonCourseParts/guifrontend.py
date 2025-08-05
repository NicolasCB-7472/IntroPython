import FreeSimpleGUI as SG
import guibackend as BK

#SG.theme("SystemDefault")

#Add case
input_label = SG.Text("Please, enter a to-do:")
input_box = SG.InputText(tooltip="Enter todo", key="todo_add", size=[46,15])
add_button = SG.Button("Add", size=[4,1])
clean_button = SG.Button(image_filename="./PythonCourseParts/buttonimg/cleanimg.png", size=[2,1], key="Clean")

#Edit case
todos_listbox = SG.Listbox(values=BK.read_file(), key="todo_list",
                        enable_events=True, size=[49, 15])
edit_button = SG.Button("Edit", size=[4,1])

#Complete case
complete_button = SG.Button("Complete", size=[44,2])


#Cases Layout
addcase = [[input_label], [input_box, clean_button, SG.Push(), add_button]]
editcase = [[todos_listbox, SG.Push() , edit_button]]
completecase = [[complete_button]]

mylayout = [[SG.Column(addcase)],[SG.Column(editcase)], [SG.Column(completecase)]]
# Note, it can also be used to make specific elements list (button_lists, label lists etc)
 
frame = SG.Window("My To-Do app", mylayout, font=('Helvetica', 11))
#frame = SG.Window(
#    "My To-Do App", 
#    mylayout, 
#    font=('Helvetica', 11)
#)


# This while has a funny implementation, but because it is an educational project I will leave it as it is
salida=False
while salida != True:
    event, values = frame.read()
    #print(event)
    #print(values)
    match event:
        case "Add":
            todos = BK.read_file()
            new_todo = values["todo_add"]
            BK.case_add(new_todo)
            # There are better ways to do the following
            added_todos = BK.read_file()
            frame["todo_list"].update(values=added_todos)
            frame["todo_add"].update(value="")
        case "Edit":
            try:
                # Choose the todo to modify
                todo_to_edit = values["todo_list"][0]
                new_todo = values["todo_add"] + '\n'
                
                # Modifies the file of todos
                todos = BK.read_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                BK.write_file(todos)

                # Displays it on screen
                frame["todo_list"].update(values=todos)
                frame["todo_add"].update(value="")
            except IndexError:
                print("No edit selected")
        case "todo_list":
            try:
                frame["todo_add"].update(value=values["todo_list"][0])
            except:
                print("List out of bounds")
        case "Complete":
            try:
                todo_complete = values["todo_list"][0]
                todos = BK.read_file()
                todos.remove(todo_complete)
                BK.write_file(todos)
                frame['todo_list'].update(values=todos)
                frame["todo_add"].update(value="")
            except IndexError:
                print("Value out of bounds")
        case "Clean":
            frame["todo_add"].update(value="")
        case SG.WIN_CLOSED:
            salida=True


# break -/- exit()
# break only for breaking the loop, exit exits the program
print("Goodbye!")
frame.close()