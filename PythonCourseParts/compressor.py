import FreeSimpleGUI as SG
from auxfunction import make_archive

# --- Frame elements --- #

# label1 = SG.Column([[SG.Text("Select files to compress: ")]], justification="center", expand_x=True)
label1 = SG.Text("Select files to compress: ")
user_input1 = SG.Input(key="input_compress")
choose_button1 = SG.FilesBrowse("Choose your source file", key="source_file")

label2 = SG.Text("Select destination: ")
user_input2 = SG.Input(key="input_destination")
choose_button2 = SG.FolderBrowse("Choose the destination ", key="destination_folder")

compress_button = SG.Button("Compress", key="Compress")
cancel_button = SG.Button("Cancel", key="Cancel")

# --- Layout elements --- #
#mylayout = [[label1, user_input1, choose_button1], [label2, user_input2, choose_button2]]
# OR
myinput1 = [label1, user_input1, choose_button1]
myinput2 = [label2, user_input2, choose_button2]

# Fancy machinations
action_button = [compress_button, cancel_button, SG.Push()]
mylayout = [myinput1, myinput2, action_button]


# --- Window elements --- #
# resizable = True
frame = SG.Window("My File compressor", mylayout, element_justification='r')


# --- Program logic --- #
salida = False
while salida == False: 
    event, values = frame.read()
    
    match event:
        case "Compress":
            if (values["input_compress"] != "") and (values["input_destination"] != ""):
                source_path = values["source_file"].split(';')
                destination_path = values["destination_folder"]
                make_archive(source_path, destination_path)
                frame["input_compress"].update(value="")
                frame["input_destination"].update(value="")
                source_path = ""
                destination_path = ""
                # This should be executed by make_archive function
                SG.popup("Hello, your '.zip' of files is ready! Enjoy!", title="Success!", button_type=SG.POPUP_BUTTONS_OK)
            else:
                print("Nothing to compress")
        case "Cancel":
            if (values["input_compress"] != "") or (values["input_destination"] != ""):
                frame["input_compress"].update(value="")
                frame["input_destination"].update(value="")
                print("Input cleaned!")
            else:
                print("Nothing to clean")
        case SG.WIN_CLOSED:
            salida = True
        case _:
            print("Nothing")
        
            
        

frame.close()