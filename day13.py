number = 1
while number <= 5:
    print(number)
    number = number + 1

number = 5
while number >= 1:
    print(number)
    number = number -1

password = int(input("Введи пароль: "))
while password != 1234:
    password = int(input("Неправильно! Спробуй ще раз: "))
print("Доступ дозволено!")

n = int(input("Введи число:"))
number = 1
while number <= n:
    print(number)
    number = number + 1