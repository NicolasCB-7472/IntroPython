import FreeSimpleGUI as SG

feet_label = SG.Text("Enter feet: ")
feet_input = SG.Input()

inches_label = SG.Text("Enter inches:")
inches_input = SG.Input()

convert_button = SG.Button("Convert")

feet_layout = [feet_label, SG.Push(), feet_input]
inches_layout = [inches_label, SG.Push(), inches_input]
button_layout = [convert_button, SG.Push()]

layout = [[feet_layout], [inches_layout], [button_layout]]

frame = SG.Window("Converter", layout)

frame.read()
frame.close()