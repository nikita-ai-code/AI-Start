try:
    age = int(input("Enter your age:"))
    print("Your age is:",age)
except ValueError:
    print("Invalid input! Enter a number.")


try:
    number = float(input("Enter a first number:"))
    number2 = float(input("Enter a second number:"))
    result = number / number2
    print("Result:", result)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


try:
    number = float(input("Enter a number:"))
    print("Square number:", number ** 2)
except ValueError:
    print("Invalid input!")
finally:
    print("Program finished.")


try:
    valid_operation = True
    number = int(input("Enter a first number:"))
    number2 = int(input("Enter a second number:"))
    operation = input("Enter a operation:")
    if operation == "+":
        result = number + number2
    elif operation == "-":
        result = number - number2
    elif operation == "*":
        result = number * number2
    elif operation == "/":
        if number2 == 0:
            raise ZeroDivisionError
        result = number / number2
    else:
        print("Invalid operation!")
        valid_operation = False
    if valid_operation:
        print("Result:", result)
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Calculator finished.")