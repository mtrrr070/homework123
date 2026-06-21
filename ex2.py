#Задание 1
# user = int(input("Введите число: "))
# if user > 0:
#     print("Положительное")
# elif user < 0:
#     print("Отрицательное")
# elif user == 0:
#     print("Ноль")
# else:
#     print("Введите другое число")


#Задание 2
# number = int(input("Введите число: "))

# if number % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")


#Задание 3
# age = int(input("Введите ваш возраст: "))
# if age <= 7:
#     print("Ребенок")
# elif age >= 7 and age <= 17:
#     print("Школьник")
# elif age >= 18 or age <= 59:
#     print("Взрослый")
# elif age > 60:
#     print("Пенсионер")
# else:
#     print("Введите другое число")


#Задание 4
# score = int(input("Введите балл: "))

# if score < 0 or score > 100:
#     print("Некорректный балл")
# elif score >= 90:
#     print("Отлично")
# elif score >= 75:
#     print("Хорошо")
# elif score >= 50:
#     print("Сдал")
# else:
#     print("Не сдал")


# #Задание 5
# password = input("Введите пароль: ")
# if not password == "admin":
#     print("Ошибка")
# else:
#     print("Верно")


# #Задание 6
# user_age = int(input("Введите возраст: "))
# adult = input("Есть ли сопровождающий: Да/Нет?")
# if user_age >= 16 or adult == "Да":
#     print("Можно на фильм")
# else:
#     print("Нельзя")


# #Задание 7
# user_age = int(input("Введите ваш возраст: "))
# status = input("Студент ли вы? (Да/Нет): ")
# if user_age < 18 or status == "Да":
#     print("Скидка 30%")
# else:
#     print("Скидки нет")


# #Задание 8
# temperture = int(input("Введите температуру: "))
# wind = input("Сильный ли ветер?: (Да/Нет)")
# if temperture < 0 or wind == "Да":
#     print("Нужна теплая одежда")
# elif temperture <= 15:
#     print("Куртка")
# else:
#     print("Легкая одежда")


# #Задание 9
# login = input("Введите логин: ")
# password = input("Введите пароль: ")

# if login == "admin" and password == "12345":
#     print("Вход выполнен")
# elif login == "admin":
#     print("Неверный пароль")
# else:
#     print("Пользователь не найден")


# #Задание 10
# age = int(input("Введите возраст: "))
# balance = int(input("Введите баланс: "))
# blocked = input("Карта заблокирована? (да/нет): ")
# if age < 18:
#     print("Операция доступна только с 18 лет")
# else:
#     if balance < 1000:
#         print("Недостаточно средств")
#     else:
#         if blocked == "да":
#             print("Карта заблокирована")
#         else:
#             print("Операция разрешена")


# #Задание 11
# attendance = int(input("Посещаемость: "))
# homework = int(input("Балл за домашки: "))
# project = input("Проект сдан? (да/нет): ")
# debt = input("Есть долги? (да/нет): ")
# if attendance >= 80 and homework >= 60 and project == "да" and debt == "нет":
#     print("Допуск к экзамену разрешён")
# else:
#     print("Допуск закрыт. Причины:")
#     if attendance < 80:
#         print(f"Низкая посещаемость: {attendance}")
#     if homework < 60:
#         print(f"Низкий балл за домашки: {homework}")
#     if project == "нет":
#         print("Проект не сдан")
#     if debt == "да":
#         print("Есть долги")
