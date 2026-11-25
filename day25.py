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
            else:
                file.write(text + "\n")
                print("Note saved successfully!")
    elif choice == "2":
        try:
            with open ("notes.txt", "r") as file:
                content = file.read()
                if content == "":
                    print("No notes yet!")
                else:    
                    print(content)
        except FileNotFoundError:
            print("No notes yet!")
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
