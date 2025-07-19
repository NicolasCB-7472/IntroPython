contents = ["My header " "text", 
            "My body text", 
            "My footer text"]
#strings "<<text>>" "<<text2>>" is treated as one string, backlash for IDE line break
filenames =["header.txt", "body.txt", "footer.txt"]

#zip contents concatenates two lists
#be wary of name sequence!
for filename, content in zip(filenames, contents):
    file = open(f"./PythonCourseParts/folder_07/{filename}", 'w')
    file.write(content)

file.close()


# Exercises #


# """Exercise 1"""
# file = open("essay.txt", 'r')
# essaycontent = file.readlines()

# for index, content in enumerate(essaycontent):
#     essaycontent[index] = content.title()
#     print(essaycontent[index])


# file.close()


# """Exercise 2"""
# file = open("essay.txt", 'r')
# essay_content = file.readlines()

# char_count = 0
# for content in essay_content:
#     char_count = char_count + len(content)

# print(f"The file contains {char_count} characters.")
# file.close()

# """Exercise 3"""
# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
# filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

# for country, filename in zip(countries, filenames):
#     file = open(f"{filename}", 'w')
#     file.writelines(f"{country}")
#     file.close()

# """Exercise 4"""
# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

# for country in countries:
#     file = open(f"{country}.txt", 'w')
#     file.writelines(f"{country}")
#     file.close()