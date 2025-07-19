user_prompt = "Enter a todo:"
var = 1
mylist = []

while var > 0:
    todo = input(user_prompt)
    # For list .append method # For string .capitalize method
    #mylist.append(todo.capitalize())
    mylist.append(todo.title())
    var-=1
    print("Next: ")
    print(mylist)

# in python console >>> dir(primitive) / >>> help(element.methodname) (implicit print)
# import builtins adds several functions