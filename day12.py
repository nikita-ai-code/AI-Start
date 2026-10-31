age = int(input("Скільки тобі років?"))
ticket = input("Чи є у тебе квиток?")
if age >=14 and ticket =="так":
    print("Ти можеш увійи!")
else:
    print("Ти не можеш увійти!")

day = int(input("Введи число: "))
if day <1 or day >7:
    print("Невірний номер дня.")
else:
    if day == 6 or day == 7:
        print("Вихідний!")
    else:
        print("Це робочий день.")