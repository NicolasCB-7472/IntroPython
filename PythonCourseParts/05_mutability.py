filenames_list = ["1.exampleA.txt", "2.exampleB.txt", "3.exampleC.txt"]

# strings are immutable, cannot be change, unlike lists
# for string filename it's used filename.replace(<<char1>>, <<char2>>, <<pos>>)

for filename in filenames_list:
    filename = filename.replace(".", "x", 1)
    # could be used file.rename(filename) method
    print(filename)

# tuples are immutable too, cannot be changed
filenames_tuples = ("1.exampleA.txt", "2.exampleB.txt", "3.exampleC.txt")