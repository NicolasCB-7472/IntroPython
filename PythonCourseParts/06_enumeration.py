waiting_list = ["james forest", "diana smith", "alicia cortez", "bob builder the"]
#waiting_list.sort(reverse=True)
waiting_list.sort(reverse=False)

for index, item in enumerate(waiting_list):
    print(f"{index+1}.{item.title()}")