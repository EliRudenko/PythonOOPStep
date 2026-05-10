print("Hello World")


n = int(input("Введи число: "))

if n > 10:
    print("Больше 10")
else:
    print("10 или меньше")





nums = [1, 2, 3, 4, 5, 6]
sum_nums = 0

for i in nums:
    sum_nums += i
    print(sum_nums)
    if i % 2 != 0:
        print(n)


# ЗАДАНИЯ: БАЗОВЫЙ PYTHON
"""
Задание 1
Напиши программу, которая принимает число и выводит, больше оно 10 или нет.
n = int(input("Введи число: "))

*
запросить 2 числа, проверить какое из них больше и вывести больее

Задание 2
Дан список чисел. Выведи только нечётные числа.

Задание 3
Найди сумму всех чисел в списке. 

* В ФУНКЦИИ !!!







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



# УРОК: ООП В PYTHON (ПОЛНЫЙ ФАЙЛ)


# 1. САМЫЙ ПРОСТОЙ КЛАСС

class Student:
    pass


s1 = Student()
s2 = Student()
s3 = Student()

print("Объекты:")
print(s1)
print(s2)
print(s3)


# ЗАДАНИЯ:
# 1. Создай класс Cat
# 2. Создай 3 объекта
# 3. Выведи их
# 4. Проверь type(cat1)



# 2. АТРИБУТЫ (ДАННЫЕ)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Олег", 14)
s2 = Student("Аня", 15)

print("\nАтрибуты:")
print(s1.name, s1.age)
print(s2.name, s2.age)


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


c1 = Car("BMW",200)
c2 = Car("Tesla", 250)

print(c1.brand, c1.speed)
print(c2.brand, c2.speed)


# ЗАДАНИЯ:
# 1. Создай Dog:
#    name, age, breed
# 2. Создай 2 собаки
# 3. Выведи:
#    Собака: Бобик, 3 года, порода: хаски
#
#
#
#
# 4. Добавь weight



# 3. МЕТОДЫ (ДЕЙСТВИЯ)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print("Меня зовут", self.name)

    def say_age(self):
        print("Мне", self.age)

    def grow(self):
        self.age += 1
        print(self.name, "теперь", self.age)


s1 = Student("Олег", 15)

print("\nМетоды:")
s1.say_name()
s1.say_age()
s1.grow()


class Dog:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def bark(self):
        print(self.name, "ГАВ ГАВ!")

    def eat(self):
        print(self.name, "ест")
        self.energy += 3
        print("energy: " , self.energy)


dog = Dog("Рекс" , 10)
dog.bark()
dog.eat()


# ЗАДАНИЯ:
# 1. Добавь методы:
#    eat() , sleep()
# 2. Сделай вывод:
#    name ест, name спит
# 3. Добавь energy
# 4. +3 energy в eat()





# 4. ПАРАМЕТРЫ ПО УМОЛЧАНИЮ

class Student:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age


s1 = Student("Ира")
s2 = Student("Олег", 15)

print("\nПо умолчанию:")
print(s1.age)
print(s2.age)


class Game:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level


g1 = Game("Minecraft")
g2 = Game("CS", 5)

print(g1.level)
print(g2.level)


# ЗАДАНИЯ:
# 1. В Dog добавь:
#    age=1
#    energy=100
# 2. Ограничь energy до 100



# 5. __str__

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Учень: {self.name}"


s1 = Student("Олег")

print("\n__str__:")
print(s1)


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def __str__(self):
        return f"{self.brand} едет {self.speed} км/ч"


c1 = Car("BMW", 200)
print(c1)


# ЗАДАНИЯ:
# 1. Сделай __str__ для Dog:
#    Рекс | 3 года | энергия: 80
# 2. Добавь эмодзи



# 6. __len__

class Student:
    def __init__(self, subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)


s1 = Student(["мат", "англ", "био"])

print("\n__len__:")
print(len(s1))


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


# ЗАДАНИЯ:
# 1. Создай Group
# 2. len = количество учеников
# 3. Добавь add_student()



# 7. __bool__

class Student:
    def __init__(self, knowledge):
        self.knowledge = knowledge

    def __bool__(self):
        return self.knowledge > 0


s1 = Student(0)

print("\n__bool__:")
if s1:
    print("Учится")
else:
    print("Ничего не знает")


class Battery:
    def __init__(self, power):
        self.power = power

    def __bool__(self):
        return self.power > 20


# ЗАДАНИЯ:
# 1. Сделай Money
# 2. >0 = True
# 3. <0 = долг



# 8. __del__

class Student:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Удалили", self.name)


s1 = Student("Олег")
del s1


# ЗАДАНИЯ:
# 1. Сделай Car
# 2. При удалении:
#    Машина BMW удалена



# МИНИ-ПРОЕКТ

class Student:
    def __init__(self, name, age, knowledge=0, mood="норм"):
        self.name = name
        self.age = age
        self.knowledge = knowledge
        self.mood = mood

    def study(self):
        self.knowledge += 10
        if self.knowledge > 100:
            self.knowledge = 100
        self.mood = "мотивирован"
        print(self.name, "учится:", self.knowledge)

    def rest(self):
        self.knowledge -= 5
        if self.knowledge < 0:
            self.knowledge = 0
        self.mood = "ленится"
        print(self.name, "отдыхает:", self.knowledge)

    def sleep(self):
        self.knowledge += 5
        if self.knowledge > 100:
            self.knowledge = 100
        self.mood = "восстановился"
        print(self.name, "спит:", self.knowledge)

    def grow(self):
        self.age += 1

    def __str__(self):
        status = "выгорание" if self.knowledge == 0 else "ок"
        return f"{self.name} | {self.age} лет | знания: {self.knowledge} | настроение: {self.mood} | статус: {status}"

    def __len__(self):
        return self.knowledge

    def __bool__(self):
        return self.knowledge > 0


print("\nМИНИ-ПРОЕКТ:")
s1 = Student("Олег", 15)

print(s1)

s1.study()
s1.rest()
s1.sleep()

print(s1)

if s1:
    print("Учится 😄")
else:
    print("Выгорание 💀")


# ФИНАЛЬНЫЕ ЗАДАНИЯ

# 1. Добавь метод work() (дает деньги)
# 2. Сделай максимум знаний = 100
# 3. Сделай минимум = 0

# 4. Создай GameCharacter:
#    name, hp, attack
#    методы: attack_enemy(), heal()

# 5. Сделай бой между 2 персонажами

# 6. SUPER HARD:
#    Создай BankAccount:
#    balance
#    deposit()
#    withdraw()
#    нельзя уйти в минус





































# створюємо найпростіший клас
"""
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
s1 = Student("Олег",14)

print(s1.name)
print(s1.age)
"""
# ЗАВДАННЯ:
# створи клас Dog з name і age
# створи 2 собаки і виведи їх дані







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

s1 = Student( ["математика", "англ", "біологія"] )
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