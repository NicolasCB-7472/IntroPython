import FreeSimpleGUI as SG

# filename should be feetconverter not convertor
feet_label = SG.Text("Enter feet: ")
feet_input = SG.Input(key="feet_input")

inches_label = SG.Text("Enter inches:")
inches_input = SG.Input(key="inches_input")

convert_button = SG.Button("Convert")

feet_layout = [feet_label, SG.Push(), feet_input]
inches_layout = [inches_label, SG.Push(), inches_input]
button_layout = [convert_button, SG.Push()]

layout = [[feet_layout], [inches_layout], [button_layout]]

frame = SG.Window("Converter", layout)

salida = False
while salida == False:
    event, values = frame.read()

    match event:
        case "Convert":
            total = 0
            feet = 0
            inches = 0
            valid = True
            try:
                if(values["feet_input"] != ""):
                    feet = float(values["feet_input"]) * 0.3048 
            
                if(values["inches_input"] != ""):
                    inches = (float(values["inches_input"]) / 12) * 0.3048
            
            except ValueError:
                SG.popup("The conversion failed, try with integers and rational numbers", title="Failure!", button_type=SG.POPUP_BUTTONS_OK)
                valid = False
                print("Catastrophic failure in the program")
                frame["feet_input"].update(value="")
                frame["inches_input"].update(value="")

            if(valid):
                total = feet + inches
                SG.popup(f"Your feets and inches are: {total}ms", title="Success!", button_type=SG.POPUP_BUTTONS_OK)
                print("Succesful conversion")
        case SG.WINDOW_CLOSED:
            salida=True
            print("Window closure")
        case _:
            print("No event")

frame.close()