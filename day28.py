numbers = [12,5,8,20,3,15]
for number in numbers:
    print(number)
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(len(numbers))
numbers.append(25)
print(numbers)


grades = {
    "Math": 12,
    "English": 10,
    "Python": 11,
    "History": 8,
    "Physics": 9
}
average = 0
for subject, grade in grades.items():
    print(subject,grade)
    average = average + grade
print(average / len(grades))
print(max(grades.values()))
print(min(grades.values()))
grades["Biology"] = 10
print(grades)


students = {
    "Alex": [10,11,12],
    "Maria": [9,10,11],
    "Ivan": [7,8,9]
}
for name, grades_list in students.items():
    print(name, grades_list)
    average_everyone = sum(grades_list) / len(grades_list)
    print(name, "Your average:", average_everyone)
average_maria = sum(students["Maria"]) / len(students["Maria"])
print("Maria your average:", average_maria)


students = {
    "Alex": [10,11,12],
    "Maria": [9,10,11],
    "Ivan": [7, 8, 9]
}
best_student = ""
best_average = 0
total_grades = 0
count_grades = 0
for name, grades_list in students.items():
    print(name, grades_list)
    average_everyone = sum(grades_list) / len(grades_list)
    print(name, "Your average:", average_everyone)
    if average_everyone > best_average:
        best_average = average_everyone
        best_student = name
    total_grades = total_grades + sum(grades_list)
    count_grades = count_grades + len(grades_list)
print("Overall average:", total_grades / count_grades)
print("Best student:", best_student)
print("Best average:", best_average)
students["Nikita"] = [12,11,12]
print(students)