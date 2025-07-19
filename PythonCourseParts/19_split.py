def get_nr_items(user_input):
    curated_str = str(user_input)
    length_str = len(curated_str) - 1

    if(length_str > 1 and curated_str[0] == '"' and curated_str[length_str] == '"'):
        curated_str = curated_str[1:length_str]

    curated_list = [astr.strip() for astr in curated_str.split(',')]
    final_list = []
    for astr in curated_list:
        if(astr != ''):
            final_list.append(astr)

    return final_list

user_input = input("Names: ")
names = get_nr_items(user_input)
print(names)
