print("Hello World")
























# ЗАДАНИЯ: БАЗОВЫЙ PYTHON
"""
Задание 1
Напиши программу, которая принимает число и выводит, больше оно 10 или нет.

Задание 2
Дан список чисел. Выведи только нечётные числа.

Задание 3
Найди сумму всех чисел в списке.

Задание 4
Выведи числа от 1 до 10 с помощью цикла.

Задание 5
Дана строка. Выведи каждую букву отдельно.

"""


""" 
# 1
n = int(input("Введи число: "))

if n > 10:
    print("Больше 10")
else:
    print("10 или меньше")



# 2
nums = [1, 2, 3, 4, 5, 6]

for n in nums:
    if n % 2 != 0:
        print(n)



# 3
nums = [1, 2, 3, 4, 5]

total = 0
for n in nums:
    total += n

print(total)



# 4
for i in range(1, 11):
    print(i)

#5
text = "hello"

for letter in text:
    print(letter)
"""







# ЗАДАНИЯ: ФУНКЦИИ
"""

Задание 1
Напиши функцию, которая принимает число и возвращает его квадрат.

Задание 2
Напиши функцию, которая принимает два числа и возвращает большее.

Задание 3
Напиши функцию, которая считает количество элементов в списке.

Задание 4
Напиши функцию, которая принимает строку и возвращает её длину.

Задание 5
Напиши функцию, которая принимает список чисел и возвращает сумму.

Задание 6 (чуть интереснее)
Напиши функцию, которая проверяет, есть ли число в списке.

"""


"""
# 1 
def square(n):
    return n * n

print(square(4))


# 2
def max_num(a, b):
    if a > b:
        return a
    return b

print(max_num(3, 7))


# 3
def count_items(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

print(count_items([1, 2, 3, 4]))


# 4

def get_length(text):
    count = 0
    for _ in text:
        count += 1
    return count

print(get_length("hello"))


# 5
def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(sum_list([1, 2, 3]))


# 6
def find_number(nums, x):
    for n in nums:
        if n == x:
            return True
    return False

print(find_number([1, 2, 3], 2))
"""










# УРОК: ООП В PYTHON (ДУЖЕ ПРОСТО)

# УЯВИ:
# КЛАС — це як шаблон (наприклад: "Учень")
# ОБ’ЄКТ — це конкретна людина (наприклад: Олег, Аня)

# Наприклад:
# клас = "Учень"
# об’єкти = Олег, Аня, Іра

"""
# створюємо найпростіший клас
class Student:
    pass

# створюємо об’єкти (екземпляри класу)
s1 = Student()
s2 = Student()

print(s1)
print(s2)
"""
# об’єкти різні, навіть якщо створені з одного класу


# ЗАВДАННЯ:
# створи клас Cat і створи 2 об’єкти



# ТЕПЕР ДОДАЄМО ДАНІ (АТРИБУТИ)

# У ЖИТТІ:
# у кожного учня є ім’я і вік
"""
class Student:
    def __init__(self, name, age):
        # self — це "цей самий учень"
        # ми записуємо дані всередину об’єкта
        self.name = name
        self.age = age

# створюємо учня
s1 = Student("Олег", 15)

print(s1.name)
print(s1.age)
"""

# ВАЖЛИВО:
# __init__ — це КОНСТРУКТОР
# він запускається САМ, коли ми створюємо об’єкт

# коли пишемо:
# s1 = Student("Олег", 15)
# Python автоматично викликає __init__


# ПРОСТІШЕ:
# __init__ — це як "створення учня і одразу заповнення анкети"


# ЩО ТАКЕ self?
# self — це сам об’єкт
"""
# якщо є 2 учні:
s1 = Student("Олег", 15)
s2 = Student("Аня", 14)
"""
# то self в кожному випадку різний


# ЗАВДАННЯ:
# створи клас Dog з name і age
# створи 2 собаки і виведи їх дані



# ТЕПЕР ДОДАЄМО ДІЇ (МЕТОДИ)

# У ЖИТТІ:
# учень може:
# вчитись, говорити, рости
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print("Мене звати", self.name)

    def grow(self):
        self.age += 1
        print(self.name, "став старше:", self.age)


s1 = Student("Олег", 15)
s1.say_name()
s1.grow()
"""

# ЗАВДАННЯ:
# додай метод say_age (виводить вік)



# ПАРАМЕТРИ ЗА ЗАМОВЧУВАННЯМ

# іноді значення можна не вводити
"""
class Student:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age

s1 = Student("Іра")
print(s1.age)  # буде 10
"""

# ЗАВДАННЯ:
# додай параметр grade = 5 за замовчуванням



# __str__ — як об’єкт виглядає при print()
"""
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Учень: " + self.name

s1 = Student("Олег")
print(s1)
"""

# ЗАВДАННЯ:
# зроби __str__ для Dog



# __len__ — що повертає len()
"""
class Student:
    def __init__(self, subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)

s1 = Student(["математика", "англ", "біологія"])
print(len(s1))
"""

# ЗАВДАННЯ:
# створи клас Group (список учнів)
# len має показувати кількість учнів



# __bool__ — як об’єкт поводиться в if
"""
class Student:
    def __init__(self, knowledge):
        self.knowledge = knowledge

    def __bool__(self):
        return self.knowledge > 0

s1 = Student(5)

if s1:
    print("Учень вчиться")
else:
    print("Учень нічого не знає")
"""

# ЗАВДАННЯ:
# зроби клас Money (гроші)
# якщо > 0 → True



# __del__ — коли об’єкт видаляється
"""
class Student:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Видалили", self.name)

s1 = Student("Олег")
del s1
"""

# ЗАВДАННЯ:
# зроби клас Car з __del__



# МІНІ-ПРОЄКТ: СИМУЛЯТОР УЧНЯ
"""
class Student:
    def __init__(self, name, age, knowledge=0):
        self.name = name
        self.age = age
        self.knowledge = knowledge

    def study(self):
        self.knowledge += 10
        print(self.name, "вчиться. Знання:", self.knowledge)

    def rest(self):
        self.knowledge -= 5
        print(self.name, "відпочиває. Знання:", self.knowledge)

    def grow(self):
        self.age += 1
        print(self.name, "став старше:", self.age)

    def __str__(self):
        return f"{self.name}, {self.age} років, знання: {self.knowledge}"

    def __len__(self):
        return self.knowledge

    def __bool__(self):
        return self.knowledge > 0


s1 = Student("Олег", 15)

print(s1)
s1.study()
s1.rest()
s1.grow()

print(len(s1))

if s1:
    print("Учень розвивається")
"""

# ФІНАЛЬНЕ ЗАВДАННЯ:

# 1. додай метод sleep (відновлює знання)
# 2. знання не можуть бути менше 0
# 3. додай настрій (mood)
# 4. якщо знання = 0 → "вигорання"
# 5. зроби красивий __str__