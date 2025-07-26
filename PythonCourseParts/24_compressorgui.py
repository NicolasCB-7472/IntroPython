import FreeSimpleGUI as SG

# --- Frame elements --- #

# label1 = SG.Column([[SG.Text("Select files to compress: ")]], justification="center", expand_x=True)
label1 = SG.Text("Select files to compress: ")
user_input1 = SG.Input()
choose_button1 = SG.FilesBrowse("Choose your source file")

label2 = SG.Text("Select destination: ")
user_input2 = SG.Input()
choose_button2 = SG.FilesBrowse("Choose the destination ")

compress_button = SG.Button("Compress")
cancel_button = SG.Button("Cancel")

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

frame.read()
frame.close()