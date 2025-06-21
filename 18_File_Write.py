def write_to_file():
    with open("output.txt", "w") as file:
        file.write("Hello, World..!!\n")
        file.write("This is a test file.\n")

write_to_file()