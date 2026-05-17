# УРОК 4: НАСЛІДУВАННЯ КЛАСІВ. super()
# ANIMAL WORLD VERSION

# СЬОГОДНІ:
# - навчимось робити ієрархію класів
# - зрозуміємо inheritance
# - розберемо super()
# - навчимось override методів
# - створимо систему тварин


# УЯВИ:

# У зоопарку є:
# - Dog
# - Cat
# - Bird

# У ВСІХ є:
# - ім'я
# - вік
# - здоров'я

# Але:
# Dog має силу
# Cat має спритність
# Bird має швидкість

# Щоб не дублювати код —
# використовують НАСЛІДУВАННЯ


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.health = 100

    def info(self):
        print("Ім'я:", self.name)
        print("Вік:", self.age)
        print("HP:", self.health)


animal = Animal("Барсик", 3)

animal.info()

# ЗАВДАННЯ:
# створи ще одну тварину


# ПРОБЛЕМА БЕЗ НАСЛІДУВАННЯ


class Dog:
    def __init__(self, name, age, strength):

        self.name = name
        self.age = age
        self.health = 100

        self.strength = strength


class Cat:
    def __init__(self, name, age, agility):

        self.name = name
        self.age = age
        self.health = 100

        self.agility = agility


# ПРОБЛЕМА:
# ми копіюємо:
# - name
# - age
# - health

# Це погана практика.


# ПРАВИЛЬНО:
# inheritance


class Animal:
    def __init__(self, name, age):

        self.name = name
        self.age = age

        self.health = 100

    def info(self):

        print("Ім'я:", self.name)
        print("Вік:", self.age)
        print("HP:", self.health)


class Dog(Animal):

    def __init__(self, name, age, strength):

        super().__init__(name, age)

        self.strength = strength

dog = Dog("Рекс", 5, 40)

dog.info()

print("Сила:", dog.strength)

# ЗАВДАННЯ:
# створи:
# - Cat
# - Bird




# ПОЯСНЕННЯ:

# Dog(Animal)

# означає:
# Dog наслідує Animal

# Dog автоматично отримує:
# - info()
# - health
# - name
# - age


# super() викликає код батьківського класу


# ПРОСТО:

# Animal = база
# Dog = розширення


# ЗАВДАННЯ:
# створи:
# - Cat
# - Bird

# через inheritance


class Animal:
    def __init__(self, name):

        print("Створюється Animal")

        self.name = name


class Cat(Animal):

    def __init__(self, name):

        print("Створюється Cat")

        super().__init__(name)


cat = Cat("Мурка")


# ПОРЯДОК:

# 1. Cat __init__
# 2. super()
# 3. Animal __init__


# ВАЖЛИВО:

# super() не копіює код

# Він ВИКЛИКАЄ код
# батьківського класу


# ЗАВДАННЯ:
# додай print у Bird


class Animal:
    def __init__(self, name, age):

        self.name = name
        self.age = age

        self.health = 100

    def info(self):
        print("Ім'я:", self.name)
        print("Вік:", self.age)
        print("HP:", self.health)

    def move(self):

        print(self.name, "рухається")


class Dog(Animal):

    def __init__(self, name, age):

        super().__init__(name, age)

        self.strength = 50

    def bark(self):

        print(self.name, "гавкає")


dog = Dog("Бобік", 4)

dog.move()

dog.bark()








# ПОЯСНЕННЯ:

# Dog має:
# - move() з Animal
# - bark() свій





# OVERRIDE МЕТОДІВ


class Animal:
    def sound(self):

        print("Тварина видає звук")


class Dog(Animal):

    def sound(self):

        print("Собака гавкає")


class Cat(Animal):

    def sound(self):

        print("Кіт нявкає")


d = Dog()
c = Cat()

d.sound()
c.sound()


# ПОЯСНЕННЯ:

# sound() один і той самий
# але поведінка різна

# Це override


# ЗАВДАННЯ:
# зроби sound() для Bird


class Animal:
    def __init__(self, name):

        self.name = name

    def info(self):

        print("Ім'я:", self.name)


class Bird(Animal):

    def __init__(self, name, speed):

        super().__init__(name)

        self.speed = speed

    def info(self):

        super().info()

        print("Швидкість:", self.speed)


bird = Bird("Кеша", 120)

bird.info()


# ПОЯСНЕННЯ:

# super().info()

# запускає:
# Animal.info()

# а потім ми додаємо своє


# ЦЕ ДУЖЕ ВАЖЛИВО:
# так будується професійний код


# ЗАВДАННЯ:
# додай:
# - age
# - hp


# PET SYSTEM


class Pet(Animal):

    def __init__(self, name, owner):

        super().__init__(name, 1)

        self.owner = owner

    def play(self):

        print(self.name, "грається")


pet = Pet("Лакі", "Олег")

pet.info()

pet.play()


# ЗАВДАННЯ:
# створи:
# - Hamster
# - Parrot
# - Rabbit


# WILD ANIMALS


class WildAnimal(Animal):

    def __init__(self, name, age, danger):

        super().__init__(name, age)

        self.danger = danger

    def attack(self):

        print(self.name, "атакує")


class Lion(WildAnimal):

    def __init__(self, name, age, danger):

        super().__init__(name, age, danger)

        self.roar_power = 100

    def roar(self):

        print(self.name, "голосно ричить")


lion = Lion("Сімба", 7, 80)

lion.info()

lion.attack()

lion.roar()


# ІЄРАРХІЯ:

# Animal
# └── WildAnimal
#     └── Lion


# ВАЖЛИВО:

# inheritance може бути багаторівневим


# ЗАВДАННЯ:
# створи:
# - Tiger
# - Wolf


# ДОДАЄМО FOOD SYSTEM


class Animal:
    def __init__(self, name):

        self.name = name

        self.food = []

    def add_food(self, item):

        self.food.append(item)

    def show_food(self):

        print("Їжа:")

        for item in self.food:
            print("-", item)


class Dog(Animal):

    def fetch_ball(self):

        print(self.name, "приніс м'яч")


dog = Dog("Рекс")

dog.add_food("М'ясо")
dog.add_food("Кістка")

dog.show_food()

dog.fetch_ball()


# ВАЖЛИВО:

# Dog отримав food
# через inheritance


# MULTIPLE ANIMALS


class Animal:
    def __init__(self, name):

        self.name = name

    def sound(self):

        print("Тварина видає звук")


class Dog(Animal):

    def sound(self):

        print(self.name, "гавкає")


class Cat(Animal):

    def sound(self):

        print(self.name, "нявкає")


class Bird(Animal):

    def sound(self):

        print(self.name, "цвірінькає")


animals = [
    Dog("Бобік"),
    Cat("Мурка"),
    Bird("Кеша")
]


for animal in animals:

    animal.sound()


# ПОЯСНЕННЯ:

# Один код
# різна поведінка

# Це POLYMORPHISM


# MINI ANIMAL PROJECT


class Animal:
    def __init__(self, name, age):

        self.name = name
        self.age = age

        self.health = 100
        self.energy = 100

    def info(self):

        print(
            self.name,
            "| AGE:", self.age,
            "| HP:", self.health,
            "| ENERGY:", self.energy
        )

    def action(self):

        print(self.name, "щось робить")


class Dog(Animal):

    def __init__(self, name, age):

        super().__init__(name, age)

        self.strength = 50

    def action(self):

        print(self.name, "біжить за м'ячем")

    def guard_house(self):

        print(self.name, "охороняє будинок")


class Cat(Animal):

    def __init__(self, name, age):

        super().__init__(name, age)

        self.agility = 120

    def action(self):

        print(self.name, "лазить по меблях")

    def sleep(self):

        print(self.name, "спить")


class Bird(Animal):

    def __init__(self, name, age):

        super().__init__(name, age)

        self.fly_energy = 30

    def action(self):

        if self.fly_energy > 0:

            self.fly_energy -= 1

            print(self.name, "летить")

            print("Енергія польоту:", self.fly_energy)

        else:
            print("Птах втомився")

    def sing(self):

        print(self.name, "співає")


dog = Dog("Рекс", 5)

cat = Cat("Мурка", 3)

bird = Bird("Кеша", 2)

dog.info()
dog.action()
dog.guard_house()

print()

cat.info()
cat.action()
cat.sleep()

print()

bird.info()
bird.action()
bird.sing()


# ФІНАЛЬНІ ЗАВДАННЯ


# 1.
# Додай Fish class

# 2.
# Зроби:
# - swim()
# - jump()

# 3.
# Створи FarmAnimal class:
# - Cow
# - Sheep
# - Chicken

# 4.
# Додай happiness system

# 5.
# Якщо happiness > 100:
# тварина щаслива

# 6.
# Додай:
# - улюблену їжу
# - вагу
# - колір

# 7.
# Зроби:
# - race між тваринами
# - battle між дикими тваринами

# 8.
# Додай:
# - energy regeneration
# - hunger system

# 9.
# Створи Zoo class

# 10.
# Зроби:
# цикл догляду через while


# inheritance —
# одна з головних частин ООП.