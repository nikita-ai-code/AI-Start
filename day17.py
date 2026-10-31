languages = ["Python", "C++", "JavaScript", "Java", "Go"]
for language in languages:
    print(language)


numbers = [3, 8, 12, 5, 17, 20, 7, 14]
for number in numbers:
    if number % 2 == 0:
        print(number)


numbers = [5, 10, 15, 20, 25]
total = 0
for number in numbers:
    total = total + number
print(total)


numbers = [12, 5, 28, 9, 17]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)