numbers = [4,8,15,23,42]
user_input = int(input("Введи число:"))
if user_input in numbers:
    print("Число є у списку!")
else:
    print("Числа немає у списку!")


count = 0
numbers = [2,7,8,11,14,20,31]
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        count = count + 1
    index = index + 1
print(count)


numbers = [5, 10, 15, 20, 25]
total = 0
index = 0
while index < len(numbers):
    total = total + numbers[index]
    index = index + 1
print(total)


numbers = [12, 5, 28, 9, 17]
largest = numbers[0]
index = 0
while index < len(numbers):
    if numbers[index] > largest:
        largest =numbers[index] 
    index = index + 1
print(largest)