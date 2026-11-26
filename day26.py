try:
    number = int(input("Введіть число:"))
    print(number)
except ValueError:
    print("Invalid number!")


try:
    number = int(input("Введіть перше число:"))
    number2 = int(input("Введіть друге число:"))
    print(number / number2)
except ZeroDivisionError:
    print("Cannot divide by zero!")


try:
    with open("test.txt", "r") as file:
        content = file.read()
        if content == "":
            print("File is empty!")
        else:
            print(content)
except FileNotFoundError:
    print("File not found!")


try:
    number = float(input("Введіть число:"))
    print(number * number)
except ValueError:
    print("Invalid number!")
finally:
    print("Program finished!")


try:
    number = float(input("Введіть перше число:"))
    number2 = float(input("Введіть друге число:"))
    print("Sum:", number + number2)
    print("Difference:", number - number2)
    print("Multiplication:", number * number2)
    print("Division:", number / number2)
except ValueError:
    print("Invalid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Program finished!")