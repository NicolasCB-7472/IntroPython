
user_prompt = "Enter add, show (exit_py to quit): "
user_list = []
user_input = ""

while user_input != "exit_py" | user_input != "quit":
    user_input = input(user_prompt)
    match user_input:
        case "add":
            user_input = input("Task to add:").strip().upper()
            user_list.append(user_input)
            user_input = ""
        case "show" | "display":
            print("TASKS:")
            for task in user_list:
                # .strip method removes trailing whitespace (not jump line)
                print(task.lower().capitalize())
        case "exit_py" | "quit":
            continue
        case default:
            print("Not a valid command")

print("See you soon!")