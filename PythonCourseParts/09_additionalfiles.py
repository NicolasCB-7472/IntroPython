date = input("Please, enter date: ")
mood = input("Rate mood from 1 to 10: ")
notes = input("Additional notes: ")

with open(f"./PythonCourseParts/journal/{date}.txt", 'w') as file:
    file.write(f"Filename: {date}.txt\n")
    file.write(f"Mood: {mood}\n")
    file.write(f"Notes: {notes}\n")