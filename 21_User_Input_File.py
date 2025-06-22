def save_to_file():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter you gender: ")
    phone = int(input("Enter you phone number: "))

    with open("userdata.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Phone Number: {phone}\n")

save_to_file()