def get_max():
    grades = [9.6, 9.2, 9.7]
    
    grade_MM = {"Max":int, "Min":int}
    grade_MM["Max"] = max(grades)
    grade_MM["Min"] = min(grades)
    
    grade_str = f"Max: {grade_MM['Max']}, " + f"Min: {grade_MM['Min']}"
    return grade_str
    
my_string = get_max()
print(my_string)

def format_filename():
    filename = "report.txt"
    filename = filename[:len(filename) - 4].capitalize()
    return filename

altered_string = format_filename()
print(altered_string)

def square_number():
    number = 5
    result = number**2
    
    return result
    
mysquare = square_number()
print(mysquare)