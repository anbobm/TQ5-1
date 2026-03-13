list = []

def open_file(list):
    with open("foo.txt", "r") as file:
        for line in file:
            print(line.strip())
            list.append(line.strip())
    return list

list = open_file(list)

def search_word(list):
    for index, item in enumerate(list):
        if item == "bar":
            return f"Bar ist gefunden. Line ist: {index + 1}"

print(search_word(list))