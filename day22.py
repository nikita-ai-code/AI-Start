def introduce(name, age=18):
    print("Hello", name, "you are", age, "years old")
introduce("Nikita")
print(introduce)
introduce("Alex", 20)


def create_profile(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
create_profile(age=14, name="Nikita", city="Kyiv")


city = "Kyiv"
def show_city():
    country = "Ukraine"
    print("City:",city,"Country:",country)
show_city()
print(city)


def calculate_price(price, discount=0):
    new_price = price * discount / 100
    final_price = price - new_price
    return final_price
print(calculate_price(1000))
print(calculate_price(1000,20))
print(calculate_price(price=2000, discount=10))


grades = {
    "Math": 10,
    "English": 11,
    "Python": 12,
    "Physics": 4,
    "History": 9
}
def calculate_average(grades):
    total = 0
    for grade in grades.values():
        print(grade)
        total = total + grade
    average = total / len(grades)
    return average
average = calculate_average(grades)
print("Average grade:", average)
def get_performance(average):
    if average >= 10:
        return "Excellent"
    elif average >=7:
        return "Good"
    elif average >= 4:
        return "Average"
    else:
        return "Needs improvement"
performance = get_performance(average)
print("Performance:", performance)
def show_report(name, grades, average):
    print("Student:", name)
    for subject,grade in grades.items():
        print(subject, ":", grade)
    print("Average grade:", average)
    print("Performance:", get_performance(average))
show_report("Nikita", grades, average)