### MODULE GLOB ###
# import glob

# Retrieves all file names a folder
# myfiles glob.glob("./*.txt")

#import csv
# file -> weather.csv
# header element 1, header element n
# "element A1", "element An"
# "element B1", "element Bn"

### MODULE CSV ###
#with open("weather.csv", 'r') as file:
#   data = list(csv.reader(file))

#city = input("Enter a city: ")
# print(data)
# for row in data[1:]:
#     if row[0] == city:
#         print(row[1])

### MODULE SHUTIL (shell utility)  ###
#import shutil
#shutil.make_archive("<<output file>>", "zip", <<filedirectory>>)

### MODULE WEBBROWSER ###
#import webbrowser
#user_term = input("Enter a search term: ")
#user_term can be changed to .replace(" ", "+")
#webbrowser.open("https://google.com")
#webbrowser.open("https://google.com/search?q=python+website")
#webbrowser.open("https://google.com/search?q=" + user_term)