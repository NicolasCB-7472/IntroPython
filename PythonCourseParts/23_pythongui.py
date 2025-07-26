import FreeSimpleGUI as SG

label = SG.Text("Hello World")
input_box = SG.InputText(tooltip="Hi World")
add_button = SG.Button("Hi")

# [] represents a list of rows in SG layout, layout requires a list of something
# widget type, specific Window type object inside layout list
frame = SG.Window("My To-Do App", layout=[[label, input_box], [add_button]]) 
# Display frame
frame.read()
frame.close()