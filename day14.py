n = int(input("Введи число:"))
number = 1
while number <= n:
    if number % 2 == 0:
        print(number, "Число парне")
    else:
        print(number, "Число непарне")
    number = number + 1

n = int(input("Введи число:"))
number = 1
while number <= n:
    if number % 2 == 0:
        print(number)
    number = number + 1

n = int(input("Введи число:"))
total = 0
number = 1
while number <= n:
    total = total + number
    number = number + 1
print(total)

import random
secret_number = random.randint(1, 10)
guess = int(input("Введи число від 1 до 10:"))
while guess != secret_number:
    print("Неправильно!")
    guess = int(input("Спробуй ще раз:"))
print("Ти вгадав!")