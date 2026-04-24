# УРОК 4: НАСЛІДУВАННЯ КЛАСІВ. super()

# УЯВИ:
# є загальний клас "Людина"
# і є:
# - учень
# - вчитель
# вони схожі (у всіх є ім’я, вік)
# але мають свої особливості

# щоб не копіювати код — ми використовуємо НАСЛІДУВАННЯ


# СПОЧАТКУ ЗРОБИМО ЗВИЧАЙНИЙ КЛАС

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


h = Human("Олег", 15)
h.info()


# ЗАВДАННЯ:
# створи ще один об’єкт Human



# ТЕПЕР УЯВИ:
# ми хочемо зробити клас Student (учень)

# ПЛОХИЙ ВАРІАНТ (ми просто копіюємо код)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(self.name, self.age, self.grade)


# це ПОВТОР КОДУ → це погано


# ПРАВИЛЬНО: НАСЛІДУВАННЯ

class Student(Human):
    def __init__(self, name, age, grade):
        # super() бере код з класу Human
        super().__init__(name, age)
        self.grade = grade


s = Student("Аня", 14, 7)
s.info()  # працює з Human
print(s.grade)


# ПОЯСНЕННЯ:
# Student НАСЛІДУЄ Human
# тобто:
# Student отримує все з Human

# super() — це спосіб викликати батьківський код


# ПРОСТО:
# Human — це "база"
# Student — це "розширення"


# ЗАВДАННЯ:
# створи клас Teacher (вчитель), який наслідує Human
# додай поле salary



# ТЕПЕР РОЗБЕРЕМО super() ДЕТАЛЬНІШЕ

class Human:
    def __init__(self, name):
        print("Створюється людина")
        self.name = name


class Student(Human):
    def __init__(self, name):
        print("Створюється учень")
        super().__init__(name)


s = Student("Олег")


# ПОРЯДОК:
# 1. Student __init__
# 2. super() → Human __init__


# ЗАВДАННЯ:
# додай print у Human і Student щоб подивитись порядок



# ТЕПЕР ДОДАМО СВОЇ МЕТОДИ

class Student(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self):
        print(self.name, "вчиться")


s = Student("Іра", 15)
s.study()
s.info()


# ЗАВДАННЯ:
# додай метод play()



# ПЕРЕВИЗНАЧЕННЯ МЕТОДУ (override)

# іноді ми хочемо змінити поведінку

class Human:
    def info(self):
        print("Це людина")


class Student(Human):
    def info(self):
        print("Це учень")


h = Human()
s = Student()

h.info()
s.info()


# ПОЯСНЕННЯ:
# Student "переписав" метод info


# ЗАВДАННЯ:
# зроби щоб Teacher теж мав свій info()



# А ТЕПЕР ПОЄДНАЄМО super() І override

class Human:
    def info(self):
        print("Ім’я:", self.name)


class Student(Human):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        super().info()
        print("Клас:", self.grade)


s = Student("Олег", 8)
s.info()


# ПОЯСНЕННЯ:
# super().info() → викликає метод з Human
# і ми додаємо своє


# ЗАВДАННЯ:
# додай до info ще вік



# ПРИКЛАД З ЖИТТЯ: ТВАРИНИ

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Якийсь звук")


class Dog(Animal):
    def sound(self):
        print("Гав")


class Cat(Animal):
    def sound(self):
        print("Мяу")


d = Dog("Бобік")
c = Cat("Мурка")

d.sound()
c.sound()


# ПОЯСНЕННЯ:
# один клас → різна поведінка


# ЗАВДАННЯ:
# створи клас Bird (пташка), яка каже "чирік"



# ТЕПЕР МІНІ-ПРОЄКТ: THE SIMS З НАСЛІДУВАННЯМ

class Human:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.mood = 50

    def eat(self):
        self.hunger -= 10
        print(self.name, "їсть")

    def __str__(self):
        return f"{self.name} | голод: {self.hunger} | настрій: {self.mood}"


class Student(Human):
    def __init__(self, name):
        super().__init__(name)
        self.knowledge = 0

    def study(self):
        self.knowledge += 10
        self.mood -= 5
        print(self.name, "вчиться")


class Worker(Human):
    def __init__(self, name):
        super().__init__(name)
        self.money = 0

    def work(self):
        self.money += 50
        self.hunger += 10
        print(self.name, "працює")


s = Student("Аня")
w = Worker("Олег")

print(s)
s.study()
print(s)

print(w)
w.work()
print(w)


# ФІНАЛЬНІ ЗАВДАННЯ:

# 1. додай:
# - метод sleep у Human

# 2. зроби:
# - якщо hunger > 100 → "дуже голодний"

# 3. у Student:
# - якщо knowledge > 50 → "розумний"

# 4. у Worker:
# - якщо money > 200 → "багатий"

# 5. складніше:
# створи ще один клас Teenager (підліток)
# у нього є метод play() і погіршується навчання