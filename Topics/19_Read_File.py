def read_file():
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)

read_file()