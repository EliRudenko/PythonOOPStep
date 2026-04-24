# УРОК 3: РОБОТА З ДЕКІЛЬКОМА КЛАСАМИ
# МІНІ-ПРОЄКТ: "THE SIMS" (СПРОЩЕНА ВЕРСІЯ)

# СЬОГОДНІ:
# - будемо працювати з кількома класами
# - навчимось як об’єкти "взаємодіють"
# - зробимо маленький симулятор життя


# ЧАСТИНА 1. ПОВТОРЕННЯ (ДУЖЕ КОРОТКО)

# КЛАС — це шаблон
# ОБ’ЄКТ — це конкретна штука

class Human:
    def __init__(self, name):
        self.name = name

h1 = Human("Олег")

print(h1.name)


# ЗАВДАННЯ:
# створи ще один об’єкт Human



# ЧАСТИНА 2. ЧОМУ ПОТРІБНО КІЛЬКА КЛАСІВ

# У ЖИТТІ:
# є люди
# є будинки
# є їжа

# це РІЗНІ сутності → значить РІЗНІ класи


# створимо клас Людина
class Human:
    def __init__(self, name):
        self.name = name


# створимо клас Будинок
class House:
    def __init__(self, color):
        self.color = color


# створюємо об’єкти
h = Human("Аня")
house = House("червоний")

print(h.name)
print(house.color)


# ВАЖЛИВО:
# ми розділяємо логіку:
# людина ≠ будинок


# ЗАВДАННЯ:
# створи клас Food (їжа) з атрибутом name
# створи 2 об’єкти




# ЧАСТИНА 3. ОБ’ЄКТИ ВСЕРЕДИНІ ОБ’ЄКТІВ

# У ЖИТТІ:
# людина живе В будинку

# значить:
# один об’єкт може містити інший

class House:
    def __init__(self, color):
        self.color = color


class Human:
    def __init__(self, name, house):
        self.name = name
        self.house = house  # тут зберігається ОБ’ЄКТ


house1 = House("синій")
human1 = Human("Олег", house1)

print(human1.house.color)


# ПРОСТО:
# human1 має house1
# і ми можемо дістатись до кольору


# ЗАВДАННЯ:
# зроби так:
# Human має улюблену їжу (Food)
# і виведи її назву




# ЧАСТИНА 4. ВЗАЄМОДІЯ ОБ’ЄКТІВ

# У ЖИТТІ:
# людина їсть їжу

class Food:
    def __init__(self, name):
        self.name = name


class Human:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name, "їсть", food.name)


food1 = Food("яблуко")
human1 = Human("Аня")

human1.eat(food1)


# ВАЖЛИВО:
# ми передаємо ОБ’ЄКТ у метод


# ЗАВДАННЯ:
# зроби метод play(), який приймає іграшку (Toy)



# ЧАСТИНА 5. ДОДАЄМО СТАН (ГОЛОД, НАСТРІЙ)

# У ЖИТТІ:
# у людини є стан:
# - голод
# - настрій

class Human:
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # 0 = ситий, 100 = дуже голодний

    def eat(self, food):
        self.hunger -= 20
        print(self.name, "з’їв", food.name)
        print("Голод:", self.hunger)


food1 = Food("піца")
h = Human("Олег")

h.eat(food1)


# ЗАВДАННЯ:
# зроби щоб голод не був менше 0




# ЧАСТИНА 6. ЩЕ ОДИН КЛАС: РОБОТА

# У ЖИТТІ:
# людина може працювати і заробляти гроші

class Job:
    def __init__(self, salary):
        self.salary = salary


class Human:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.money = 0

    def work(self):
        self.money += self.job.salary
        print(self.name, "заробив", self.money)


job1 = Job(100)
h = Human("Іра", job1)

h.work()


# ЗАВДАННЯ:
# зроби зарплату 200 і перевір



# ЧАСТИНА 7. ДЕКІЛЬКА ОБ’ЄКТІВ В ОДНОМУ

# У ЖИТТІ:
# в будинку може бути кілька людей

class House:
    def __init__(self):
        self.people = []  # список

    def add_person(self, human):
        self.people.append(human)


house = House()

h1 = Human("Олег", job1)
h2 = Human("Аня", job1)

house.add_person(h1)
house.add_person(h2)

print(len(house.people))


# ЗАВДАННЯ:
# виведи імена всіх людей у будинку



# ЧАСТИНА 8. МІНІ-ПРОЄКТ: THE SIMS

class Food:
    def __init__(self, name, value):
        self.name = name
        self.value = value  # скільки зменшує голод


class Job:
    def __init__(self, salary):
        self.salary = salary


class Human:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.hunger = 50
        self.money = 0
        self.mood = 50

    def eat(self, food):
        self.hunger -= food.value
        if self.hunger < 0:
            self.hunger = 0

        print(self.name, "їсть", food.name)
        print("Голод:", self.hunger)

    def work(self):
        self.money += self.job.salary
        self.hunger += 10
        print(self.name, "працює")
        print("Гроші:", self.money)

    def relax(self):
        self.mood += 10
        print(self.name, "відпочиває")
        print("Настрій:", self.mood)

    def __str__(self):
        return f"{self.name} | Голод: {self.hunger} | Гроші: {self.money} | Настрій: {self.mood}"


# створюємо світ
food = Food("бургер", 30)
job = Job(100)
human = Human("Олег", job)

print(human)

human.work()
human.eat(food)
human.relax()

print(human)



# ФІНАЛЬНЕ ЗАВДАННЯ (ДЛЯ УРОКУ)


# 1. додай:
# - sleep() (зменшує голод і покращує настрій)

# 2. зроби:
# - якщо голод > 100 → "персонаж дуже голодний"

# 3. додай:
# - новий клас Shop (магазин)
# - метод buy_food()

# 4. зроби:
# - перевірку: якщо грошей нема → не можна купити

# 5. ускладнення:
# - кілька людей в одному будинку