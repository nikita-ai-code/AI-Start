languages = ["Python", "C++", "JavaScript", "Java"]
print(languages)


languages = ["Python", "C++", "JavaScript", "Java"]
print(languages[0])
print(languages[2])
print(languages[3])

number = 0
languages = ["Python", "C++", "JavaScript", "Java"]
languages[1] = "C#"
languages.append("Go")
while number < len(languages):
    print(languages[number])
    number = number + 1