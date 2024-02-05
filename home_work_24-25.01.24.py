'''
ДЗ - 1
Папка - type_data
Файл - diff-actions-for-home-work
'''


'''
ДЗ - 1: Работа с целыми числами (int)

Определите переменную num1 со значением 15 и переменную num2 со значением 7.
Выполните сложение, вычитание, умножение и деление переменных num1 и num2.
Выведите результат каждой операции на экран.
'''

# num1 = 15
# num2 = 7
#
# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# divide = num1 / num2
# print(f'Sum addition: {addition}\nSum subtraction: {subtraction}\nSum multiplication: {multiplication}\nSum '
#       f'dividing: {divide}')

'''
ДЗ - 2:

Определите переменную name со значением "Name" и переменную surname со значением "Surname".
Объедините строки в одну, разделив их пробелом.
Выведите результат на экран.
'''

# name = "Name"
# surname = " Surname"
# full_name = name + surname
# print(full_name)


'''
ДЗ - 3:

Определите словарь person с ключами "name", "age" и "city", и значениями "your_nick", 27  и "Kiev" соответственно.
Выведите на экран все ключи словаря.
Выведите на экран все значения словаря.
'''

# person = dict(
#     name = 'hooch',
#     age = 29,
#     city = "Kiev"
# )
# keys = person.keys()
# value = person.values()
# print(keys)
# print(value)


'''
ДЗ - 4:

Определите переменную age со значением 22.
Используя условный оператор (if-elif-else), выведите сообщение:
"Вы совершеннолетний" если возраст больше или равен 18.
"Вы несовершеннолетний" в противном случае.
'''

# age = 22
#
# if age >= 18:
#     print("Вы совершеннолетний")
# else:
#     print("Вы несовершеннолетний")


'''
ДЗ - 5:

Создайте список numbers от 1 до 5.
Используя цикл for, выведите каждый элемент списка, умноженный на 2.
'''

# lst = [1, 2, 3, 4, 5]
#
# for i in lst:
#     squ = i * 2
#     print(squ)


'''
ДЗ - 6:

Определите переменную user_number со значением, введенным пользователем с клавиатуры (используйте функцию input).
Проверьте, является ли введенное число четным. Выведите соответствующее сообщение.
'''

# user_number = int(input('Введите число: '))
#
# if user_number % 2 == 0:
#     print('Введенное число является четным')
# else:
#     print('Введенное число не является четным')


'''
ДЗ - 7:

Создайте функцию calculate_square, которая принимает на вход сторону квадрата и возвращает его площадь.
Вызовите функцию для квадрата со стороной 4 и выведите результат.
'''

# def calculate_square(len_side):
#     sum = len_side ** 2
#     return sum
#
# len_side = 4
# result = calculate_square(len_side)
# print(f"Площадь квадрата со стороной {len_side} равна {result}.")


'''
ДЗ - 8:

Создайте список numbers от 1 до 5.
Создайте функцию square_numbers, которая принимает список чисел и возвращает список их квадратов.
Вызовите функцию для списка numbers и выведите результат.

'''

# numbers = [1, 2, 3, 4, 5]
# square_list = []
#
# def square_numbers():
#     for number in numbers:
#         squ_number = number ** 2
#         square_list.append(squ_number)
#     print(square_list)
# square_numbers()



'''
ДЗ - 9:

Создайте функцию reverse_string, которая принимает строку и возвращает ее в обратном порядке используйте срез.
Вызовите функцию для строки "Python" и выведите результат.
'''

# s = "Python"
# def reverse_string(string):
#     reverse = string[::-1]
#     return reverse
# result = reverse_string(s)
# print(result)


'''
ДЗ - 10:

Создайте список чисел от 1 до 10 используя range.
Используя цикл for и оператор if, выведите только те числа из списка, которые делятся на 2 без остатка.
'''
# numbers = list(range(1, 11))
#
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

'''
ДЗ - 2
Папка - create_func
Файл -  func-home-work
'''

'''
Создайте функцию greet, которая принимает один аргумент name.
Функция должна вернуть строку приветствия: "Hello, [name]!
'''

# def greet(name):
#     return f'Hello, {name}!'
#
# result = greet('hooch')
# print(result)

'''
Создайте функцию is_positive, которая принимает один аргумент number.
Функция должна вернуть True, если число положительное, и False в противном случае.
'''

# def is_positive(number):
#     return number > 0
#
# result = is_positive(1)
# print(result)

'''
 Напишите функцию,c использованием input, которая распечатает текст "hello world!"
 если при ее вызове вы передаете в качестве аргументов пустую строку, но если было передано имя, то выводить "hello имя!"
'''

# def greeting():
#     text = input("Введите имя: ")
#     if text == "":
#         print("hello world!")
#     else:
#         print(f'hello {text}!')
#     return text
#
# greeting()

'''
Сделал два варианта так как не до конца понял как именно надо написать
'''
# def greeting(text):
#     if text == "":
#         print("hello world!")
#     else:
#         print(f'hello {text}!')
#     return text
# greeting("")



'''
ДЗ - 3
Папка - solid-oop
Файл -  solid-oop-home-work
'''

'''
Домашнее задание по ООП: "Person"
Создайте класс "Person" с атрибутами "имя", "возраст" и "пол". Добавьте метод для вывода информации о человеке.

# Example:
person = Person("nick_name", age, "gender")
person.print_info()
'''
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def print_info(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")
#
# nick = Person("hooch", 25, "Мужской")
# nick.print_info()



'''Задание 2: Инкапсуляция для "Employee")
2. Создайте класс "Employee" с атрибутом "зарплата", инкапсулируйте его. Добавьте методы для ставки и получения зарплаты с учетом премии.
# Cоздаем класс Employee и наследуемся от Person :
'''
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# class Employee(Person):
#     def __init__(self, name, age, gender, salary):
#         super().__init__(name, age, gender)
#         self._salary = salary
#
#     def set_salary(self, new_salary):
#         self._salary = new_salary
#
#     def get_salary(self):
#         return self._salary
#
# employee = Employee("hooch", 20, "M", 2000)
# employee.set_salary(3500)
# print(f"Зарплата работника {employee.name}: {employee.get_salary()}")



'''Задание 3: Полиморфизм для "Student"
3. Давайте создадим два класса, например, "Student" и "Employee", оба из которых имеют метод "study".
Затем напишем функцию "study", которая будет принимать объект любого из этих классов и вызывать метод "study".
'''

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self):
#         print(f"{self.name} is studying.")
#
# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self):
#         print(f"{self.name} is learning for professional development.")
#
#
# def study_student(student):
#     student.study()
#
# def study_employee(employee):
#     employee.study()
#
#
# student = Student("John")
# employee = Employee("Ted")
#
# study_student(student)
# study_employee(employee)




'''4. Принцип единственной ответственности (Single Responsibility Principle, SRP):
Описание: Каждый класс должен иметь только одну причину для изменения.
Пример нарушения:
'''
'''Задание: Разделите класс на два класса: один для работы с базой данных, другой для отправки электронной почты.'''

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
# class Database:
#     def save_to_database(self, user_data):
#         print(f"Данный пользователь: Имя: {user_data.username}, Почта: {user_data.email} успешно сохранен!")
#     # Логика сохранения пользователя в базе данных
#
# class EmailSender:
#     def send_email(self, user_email, message):
#         print(f"Письмо отправлено на почту: {user_email.email}, содержание: {message}")
#     # Логика отправки электронной почты
#
#
# user = User("Pit", "pit@gmail.com")
#
# database_saver = Database()
# database_saver.save_to_database(user)
#
# email_sender = EmailSender()
# email_sender.send_email(user, "Письмо успешно доставлено!")
