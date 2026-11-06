computer = {
    "brand": "Asus",
    "model": "Tuf Gaming F16",
    "ram": 16,
    "gpu": "RTX 3050",
}
print(computer["model"])
print(computer["ram"])
print(computer["gpu"])


phone = {
    "brand": "Samsung",
    "model": "Galaxy S25",
    "memory": 128,
}
phone["memory"] = 256
phone["color"] = "Black"
phone["price"] = 25000
print(phone)


game = {
    "name": "Minecraft",
    "year": 2011,
    "price": 800,
    "genre": "Sandbox",
}
del game["price"]
game["year"] = 2009
game["developer"] = "Mojang"
print(game)


profile = {
    "username": "Nikita",
    "age": 14,
    "programming_language": "Python",
    "level": "Beginner",
}
print(profile["username"])
print(profile["programming_language"])
profile["level"] = "Intermediate"
profile["country"] = "Ukraine"
del profile["age"]
print(profile)


laptop = {
    "brand": "ASUS",
    "ram": 16,
    "gpu": "RTX 3050",
    "storage": 512
}
for key, value in laptop.items():
    print(key,"-", value)


grades = {
    "Math": 10,
    "English": 11,
    "Python": 12,
    "Physics": 9,
    "History": 8
}
for key, value in grades.items():
    print(key, "-", value)
length = len(grades)
print(length)
total = 0
for key,value in grades.items():
    total = total + value
print(total)
average = total / length
print(average)