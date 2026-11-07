def hello():
    print("Hello, Nikita!")
hello()


def greet(name):
    print("Welcome,", name)
greet("Nikita")
greet("Alex")
greet("Maria")


def calculate_sum(a,b):
    print("Sum =", a + b)
calculate_sum(5, 10)
calculate_sum(20,30)
calculate_sum(7, 8)


def multiply(a, b):
    return a * b

result = multiply(5, 10)
print(result)


def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
result = check_number(10)
print(result)
result = check_number(-5)
print(result)
result = check_number(0)
print(result)


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
result = add(10, 5)
print(result)
result = subtract(10, 5)
print(result)
result = multiply(10, 5)
print(result)
result = divide(10, 5)
print(result)
result = divide(10, 0)
print(result)