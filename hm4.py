# #Домашнее задание 1
user = {
    "name": "Ali",
    "age": 18,
    "email": "ali@mail.com",
    "city": "Almaty",
    "skills": {"Python", "HTML", "CSS"}
}

print(f"Имя: {user['name']}, Город: {user['city']}")

user["skills"].add("JavaScript")
print("После добавления:", user["skills"])

user["skills"].remove("HTML")
print("После удаления:", user["skills"])
print("Знает Python:", "Python" in user["skills"])
print("Ключи:", list(user.keys()))
print("Значения:", list(user.values()))