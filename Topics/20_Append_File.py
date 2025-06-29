def append_file():
    with open("output.txt", "a") as file:
        file.write("Appending a new line to the file.\n")
        file.write("This line is added after the initial content. \n")

append_file()