file = open("notes.txt", "w")
file.write("I am learning Python!")
file.close()
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()


file = open("notes.txt", "a")
file.write("\nI am learning Python every day!")
file.close()
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close


with open("notes.txt", "a") as file:
    file.write("\nI am improving my Python skills!")
with open("notes.txt","r") as file:
    content = file.read()
print(content)


try:
    with open("notes.txt", "a") as file:
        notes = input("Enter a text.")
        file.write(notes + "\n")
    with open("notes.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")


while True:
    print("1 - Add note")
    print("2 - Show notes")
    print("3 - Exit")
    choice = input("Choose an option:")
    if choice == "1":
        with open ("notes.txt", "a") as file:
            text = input("Please enter a text:")
            if text == "":
                print("Note cannot be empty!")
            file.write(text + "\n")
            else:
                print("Note saved successfully!")
    elif choice == "2":
        with open ("notes.txt", "r") as file:
            content = file.read()
            if file.read() == "":
                print("No notes yet!")
            else:    
                print(content)
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
