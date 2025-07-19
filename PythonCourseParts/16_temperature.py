def get_average():
    with open("./PythonCourseParts/temperature.txt", 'r') as file:
        temperatures = file.readlines()
    data = temperatures[1:] # Fancy way of removing header
    values = [float(i) for i in data]
    average_local = sum(values) / len(values)
    return average_local

average = get_average()
print(average)