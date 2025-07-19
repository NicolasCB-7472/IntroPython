try:
    width = input("Enter your rectangle width: ")
    length = input("Enter your rectangle length: ")

    # New functionality
    if width == length:
        exit("This is a rectangle operation, not a square operation.")

    area = width * length
    print("The area is: " + str(area))
except ValueError:
    print("Please enter a valid number for width and length.")
