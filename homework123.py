# #13.1. Простые функции
# # Задание 1
# def get_square(number):
#     return number ** 2

# result = get_square(5)
# print(result)


# # # Задание 2
# def is_negative(number):
#     return number < 0
# result = is_negative(-3)
# print(result)


# # # Задание 3
# def format_name(name):
#     return name.strip().capitalize()
# print(format_name("   Kazakhstan   "))


# # # Задание 4
# def get_last_item(items):
#     if items:
#         return items[-1]
#     else:
#         return None
# print(get_last_item([1, 2, 3, 4]))


# # Задание 5
# def count_words(text):
#     return len(text)
# print(count_words("Hello, world!"))

# # 13.2. Функции со списками
# # Задание 6
# def get_even_numbers(numbers):
#     even_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#     return even_numbers
# print(get_even_numbers([1, 2, 3, 4, 5, 6]))


# # Задание 7
# def get_long_words(words):
#     long_words = []
#     for word in words:
#         if len(word) > 5:
#             long_words.append(word)
#     return long_words
# print(get_long_words(["apple", "banana", "cherry", "date"]))


# # Задание 8
# def get_average_grade(grades):
#     if grades:
#         return sum(grades) / len(grades)
#     else:
#         return None
# print(get_average_grade([85, 90, 78, 92]))


# # Задание 9
# def has_failed_grade(grades):
#     for grade in grades:
#         if grade < 50:
#             return True
#     return False
# print(has_failed_grade([85, 90, 78, 92, 45]))


# # Задание 10
'Не понял как сделать'


# # 13.3. Функции со словарями
# # Задание 11
# def create_product(title, price, category):
#     product = {
#         "title": title,
#         "price": price,
#         "category": category
#     }
#     return product
# print(create_product("Laptop", 1000, "Electronics"))

# # Задание 12
# def apply_discount(product, discount):
#     if "price" in product:
#         product["price"] -= product["price"] * (discount / 100)
#     return product
# print(apply_discount({"title": "Laptop", "price": 1000, "category": "Electronics"}, 10))


# # Задание 13
# def get_uer_info(user):
#     return f"Имя: {user['name']}, Возраст: {user['age']}"
# user = {"name": "Ayan", "age": 18}
# print(get_uer_info(user))

# # # Задание 14
# def add_skill(user, skill):
#     if "skills" not in user:
#         user["skills"] = []
#     user["skills"].append(skill)
#     return user
# print(add_skill({"name": "Ayan", "age": 18}, "Python"))

# # # Задание 15
# def is_admin(user):
#     return user.get("role") == "admin"
# user1 = {"name": "Ayan", "age": 18, "role": "admin"}
# user2 = {"name": "Ayan", "age": 18, "role": "user"}
# print(is_admin(user1))  
# print(is_admin(user2))  


# # 13.4. Большая задача - мини-анализ интернет-магазина
# # # Задание 16
# products = [
#     {"title": "Laptop", "price": 350000, "category": "Electronics", "rating": 4.8},
#     {"title": "Mouse", "price": 8000, "category": "Electronics", "rating": 4.4},
#     {"title": "Book", "price": 5000, "category": "Education", "rating": 4.9},
#     {"title": "Pen", "price": 500, "category": "Education", "rating": 4.1},
#     {"title": "Desk", "price": 45000, "category": "Furniture", "rating": 4.6}
# ]
# def get_total_price(products):
#     total_price = 0
#     for product in products:
#         total_price += product["price"]
#     return total_price

# def get_products_by_category(products, category):
#     filtered_products = []
#     for product in products:
#         if product["category"] == category:
#             filtered_products.append(product)
#     return filtered_products

# def expensive_products(products, min_price):
#     return [product for product in products if product["price"] > min_price]

# def best_product(products):
#     best = products[0]
#     for product in products:
#         if product["rating"] > best["rating"]:
#             best = product
#     return best


# # 13.5. Дополнительная задача повышенной сложности
students = [
 {
 "name": "Ayan",
 "age": 18,
 "grades": [90, 85, 100],
 "skills": {"python", "git", "html"}
 },
 {
 "name": "Dias",
 "age": 17,
 "grades": [60, 70, 65],
 "skills": {"html", "css"}
 },
 {
 "name": "Madi",
 "age": 19,
 "grades": [100, 95, 90],
 "skills": {"python", "django", "git"}
 }
]

def get_average(grades):
    return round(sum(grades) / len(grades), 2) if grades else 0


def get_best_student(students):
    return max(students, key=lambda s: get_average(s["grades"]))


def get_students_with_python(students):
    return [s for s in students if "python" in s["skills"]]


def get_adult_students(students):
    return [s for s in students if s["age"] >= 18]


def show_report(students):
    print()
    
    for s in students:
        avg = get_average(s["grades"])
        print(f"{s['name']:8} | Возраст: {s['age']} | Средний балл: {avg:5} | "
              f"Навыки: {', '.join(sorted(s['skills']))}")
    
    best = get_best_student(students)
    print("\n" + "="*55)
    print(f"Всего студентов: {len(students)}")
    print(f"Лучший студент: {best['name']} (средний балл: {get_average(best['grades'])})")
    print(f"Студентов с Python: {len(get_students_with_python(students))}")
    print(f"Совершеннолетних: {len(get_adult_students(students))}")

show_report(students)