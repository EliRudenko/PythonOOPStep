# УРОК 5: ІНТРОСПЕКЦІЯ МОДУЛІВ І КЛАСІВ
# SUPER RPG VERSION


# СЬОГОДНІ:
# - навчимось дивитись всередину об'єктів
# - зрозуміємо introspection
# - навчимось:
#   - перевіряти поля
#   - перевіряти методи
#   - викликати методи через текст
#   - створювати smart systems
# - зробимо mini RPG engine


# ЩО ТАКЕ ІНТРОСПЕКЦІЯ?

# УЯВИ:
# у грі є герой

# і ми можемо спитати:
# - який у тебе hp?
# - які є здібності?
# - які є методи?
# - що ти вмієш робити?
# - ти Mage чи Warrior?

# Python теж це вміє.


class Hero:

    def __init__(self, name):

        self.name = name

        self.hp = 100
        self.mana = 50
        self.level = 1

    def attack(self):

        print(self.name, "атакує")

    def heal(self):

        print(self.name, "лікується")


hero = Hero("Arthur")


# dir() показує ВСЕ,
# що є всередині об'єкта

print(dir(hero))


# ПОЯСНЕННЯ:

# dir() повертає:
# - поля
# - методи
# - системні функції Python

# тобто:
# Python може "подивитись"
# всередину об'єкта


# ЗАВДАННЯ:
# створи:
# - Mage
# - Archer
# і виклич:
# dir() для них




# type() показує
# до якого класу належить об'єкт

print(type(hero))


# ПОЯСНЕННЯ:

# Hero — це клас
# hero — це об'єкт

# type() допомагає
# зрозуміти:
# що це за об'єкт


# У СПРАВЖНІХ ІГРАХ:
# type() використовують:
# - у battle systems
# - у AI systems
# - у перевірках ворогів


# ЗАВДАННЯ:
# створи:
# - Boss
# - Monster
# перевір:
# type() для них




# isinstance() перевіряє:
# чи належить об'єкт класу

if isinstance(hero, Hero):

    print("це Hero")


# ПОЯСНЕННЯ:

# isinstance() повертає:
# True або False

# це дуже важливо
# для великих систем


class Warrior(Hero):

    def sword_attack(self):

        print(self.name, "б'є мечем")


w = Warrior("Leon")


print(isinstance(w, Warrior))
print(isinstance(w, Hero))


# ПОЯСНЕННЯ:

# Warrior наслідує Hero

# тому Warrior —
# це теж Hero


# inheritance
# працює разом
# з isinstance()


# ЗАВДАННЯ:
# створи:
# - Mage(Hero)
# - Archer(Hero)

# перевір:
# isinstance() для них




# getattr() отримує поле
# або метод через текст

hp = getattr(hero, "hp")

print(hp)


mana = getattr(hero, "mana")

print(mana)


# ПОЯСНЕННЯ:

# getattr() дозволяє:
# отримувати дані
# через назву у вигляді тексту


# це дуже важливо
# для:
# - game engines
# - command systems
# - admin panels


# якщо поля нема —
# буде помилка

# але можна дати:
# default value

gold = getattr(hero, "gold", 0)

print(gold)


# тут:
# якщо gold нема —
# Python поверне 0


# ЗАВДАННЯ:
# через getattr()
# отримай:
# - level
# - hp
# - energy




class Mage:

    def __init__(self):

        self.mana = 100

    def fireball(self):

        print("FIREBALL")

    def teleport(self):

        print("TELEPORT")


mage = Mage()


# getattr() може отримувати
# навіть методи

spell = getattr(mage, "fireball")

spell()


# ПОЯСНЕННЯ:

# method = getattr(...)

# тепер method —
# це змінна,
# яка містить функцію


# тобто:
# функції можна
# зберігати у змінні


# ЗАВДАННЯ:
# виклич через getattr():
# - teleport()




# setattr() змінює поля

print(hero.level)

setattr(hero, "level", 10)

print(hero.level)


# ПОЯСНЕННЯ:

# setattr() працює
# як:

# hero.level = 10

# але через текст


# це дуже корисно
# для:
# - save systems
# - upgrades
# - admin commands


# setattr() може
# створювати нові поля

setattr(hero, "gold", 500)

print(hero.gold)


setattr(hero, "weapon", "Epic Sword")

print(hero.weapon)


# ПОЯСНЕННЯ:

# якщо поля не було —
# Python створить його


# ЗАВДАННЯ:
# додай через setattr():
# - armor
# - pet
# - stamina




# inventory system

setattr(hero, "inventory", [])

hero.inventory.append("Potion")
hero.inventory.append("Bow")

print(hero.inventory)


# ПОЯСНЕННЯ:

# setattr() може створювати:
# - числа
# - рядки
# - списки
# - будь-які об'єкти


# ЗАВДАННЯ:
# додай:
# - sword
# - shield
# - food




# hasattr() перевіряє:
# чи існує поле

print(hasattr(hero, "hp"))
print(hasattr(hero, "pet"))


# ПОЯСНЕННЯ:

# hasattr() повертає:
# True або False


# це допомагає:
# уникати помилок


# наприклад:
# перевіримо
# чи є зброя

if hasattr(hero, "weapon"):

    print("У героя є зброя")


# ЗАВДАННЯ:
# перевір:
# чи є:
# - mana
# - dragon
# - inventory




class Assassin:

    def stealth(self):

        print("STEALTH MODE")


a = Assassin()


# hasattr() працює
# навіть для методів

if hasattr(a, "stealth"):

    a.stealth()


# ПОЯСНЕННЯ:

# hasattr()
# часто використовують
# разом з getattr()


# ЗАВДАННЯ:
# створи:
# - invisible()
# - critical_hit()

# перевір hasattr()




# delattr() видаляє поля

print(hasattr(hero, "weapon"))

delattr(hero, "weapon")

print(hasattr(hero, "weapon"))


# ПОЯСНЕННЯ:

# delattr()
# повністю видаляє поле


# у реальних іграх:
# це може бути:
# - remove buff
# - remove item
# - remove effect


setattr(hero, "rage_mode", True)

print(hero.rage_mode)

delattr(hero, "rage_mode")

print(hasattr(hero, "rage_mode"))


# ЗАВДАННЯ:
# створи:
# - poison_effect
# потім видали його




# __dict__
# показує всі поля об'єкта

print(hero.__dict__)


# ПОЯСНЕННЯ:

# __dict__ —
# це словник
# усіх полів


# Python зберігає
# дані об'єкта
# саме так


class Character:

    def __init__(self, name):

        self.name = name

        self.hp = 100
        self.damage = 20
        self.level = 5
        self.gold = 300


player = Character("Knight")


print(player.__dict__)


# змінюємо stats

player.hp += 50
player.damage += 10

print(player.__dict__)


# ПОЯСНЕННЯ:

# __dict__ оновлюється
# автоматично


# ЗАВДАННЯ:
# додай:
# - mana
# - stamina
# - arrows

# подивись __dict__()




# dir() працює
# навіть для класів

print(dir(Character))


# ПОЯСНЕННЯ:

# клас теж має:
# - методи
# - системні функції
# - службові атрибути


class Boss:

    def attack(self):

        print("Boss attack")

    def ultimate(self):

        print("ULTIMATE")

    def rage(self):

        print("RAGE MODE")


print(dir(Boss))


# ЗАВДАННЯ:
# створи:
# - Dragon
# - DemonBoss

# виклич dir()




# introspection модулів

import random

print(dir(random))


# ПОЯСНЕННЯ:

# random —
# це модуль

# dir(random)
# показує:
# які функції є у модулі


damage = random.randint(10, 50)

print("Damage:", damage)


loot = random.choice([
    "Sword",
    "Potion",
    "Epic Armor",
    "Bow"
])

print("Loot:", loot)


# ЗАВДАННЯ:
# зроби:
# random monster
# через random.choice()




import math

print(dir(math))


print(math.sqrt(81))

print(math.ceil(4.2))

print(math.floor(9.8))


# ПОЯСНЕННЯ:

# math —
# модуль для математики


# ЗАВДАННЯ:
# використай:
# - sqrt
# - ceil
# - floor




# getattr() для команд


class Warrior:

    def attack(self):

        print("Sword attack")

    def shield(self):

        print("Shield block")

    def rage(self):

        print("RAGE")


w = Warrior()


command = "shield"


method = getattr(w, command)

method()


# ПОЯСНЕННЯ:

# ми отримали метод
# через текст


# command ->
# перетворився
# у справжню функцію


# це основа:
# - game commands
# - console systems
# - bots


# ЗАВДАННЯ:
# виклич:
# - rage()
# через getattr()




# safe command system

command = "ultimate"


method = getattr(w, command, None)

if method:

    method()

else:

    print("Команда не знайдена")


# ПОЯСНЕННЯ:

# якщо метод не існує —
# getattr() поверне None


# це дозволяє
# уникати помилок


# ЗАВДАННЯ:
# зроби:
# - heal
# - fly
# - teleport

# перевір:
# які існують




# MINI COMMAND ENGINE


class Hero:

    def __init__(self, name):

        self.name = name

        self.hp = 100
        self.energy = 100

    def attack(self):

        self.energy -= 10

        print(self.name, "атакує")

    def sleep(self):

        self.energy += 30

        print(self.name, "спить")

    def eat(self):

        self.hp += 20

        print(self.name, "їсть")

    def info(self):

        print(
            self.name,
            "| HP:", self.hp,
            "| ENERGY:", self.energy
        )


hero = Hero("Arthur")


commands = [
    "info",
    "attack",
    "sleep",
    "eat",
    "info"
]


for command in commands:

    print()
    print("КОМАНДА:", command)

    method = getattr(hero, command, None)

    if method:

        method()

    else:

        print("Unknown command")


# ПОЯСНЕННЯ:

# один цикл
# може запускати
# різні команди


# це вже:
# mini game engine


# ЗАВДАННЯ:
# додай:
# - train()
# - heal()
# - battle()




# PLAYER INPUT SYSTEM


class Mage:

    def __init__(self):

        self.mana = 100

    def fireball(self):

        self.mana -= 20

        print("FIREBALL")

        print("Mana:", self.mana)

    def teleport(self):

        self.mana -= 30

        print("TELEPORT")

        print("Mana:", self.mana)

    def regen(self):

        self.mana += 40

        print("MANA REGEN")

        print("Mana:", self.mana)


mage = Mage()


command = input("Введи spell: ")


method = getattr(mage, command, None)

if method:

    method()

else:

    print("Невідоме заклинання")


# ПОЯСНЕННЯ:

# тепер гравець
# сам вводить команди


# це вже схоже
# на справжню консольну гру


# ЗАВДАННЯ:
# додай:
# - iceball()
# - shield()
# - lightning()




# AUTO BATTLE SYSTEM


class Warrior:

    def attack(self):

        print("Sword attack")

    def heavy_attack(self):

        print("HEAVY ATTACK")

    def block(self):

        print("BLOCK")


warrior = Warrior()


battle_commands = [
    "attack",
    "attack",
    "heavy_attack",
    "block",
    "attack"
]


for command in battle_commands:

    method = getattr(warrior, command)

    method()


# ПОЯСНЕННЯ:

# battle_commands —
# це ніби battle script


# гра автоматично
# запускає команди


# ЗАВДАННЯ:
# додай:
# - dodge()
# - kick()
# - rage()




# AI ENEMY SYSTEM


class Monster:

    def bite(self):

        print("Monster bites")

    def roar(self):

        print("Monster roars")

    def poison(self):

        print("Monster uses poison")


monster = Monster()


enemy_ai = random.choice([
    "bite",
    "roar",
    "poison"
])


print("AI chose:", enemy_ai)


method = getattr(monster, enemy_ai)

method()


# ПОЯСНЕННЯ:

# AI випадково
# вибирає команду


# так працює
# проста логіка ворогів


# ЗАВДАННЯ:
# додай:
# - fire_attack()
# - stun()
# - jump_attack()




# SUPER ADVANCED RPG SYSTEM


class RPGHero:

    def __init__(self, name):

        self.name = name

        self.hp = 100
        self.energy = 100
        self.gold = 0
        self.level = 1

    def info(self):

        print(
            self.name,
            "| HP:", self.hp,
            "| ENERGY:", self.energy,
            "| GOLD:", self.gold,
            "| LEVEL:", self.level
        )

    def mine_gold(self):

        self.gold += 100

        print(self.name, "добуває золото")

    def train(self):

        self.level += 1

        print(self.name, "тренується")

    def sleep(self):

        self.energy += 30

        print(self.name, "відпочиває")

    def battle(self):

        self.energy -= 20

        print(self.name, "б'ється")


hero = RPGHero("Knight")


while True:

    print()
    print("КОМАНДИ:")
    print("- info")
    print("- mine_gold")
    print("- train")
    print("- sleep")
    print("- battle")
    print("- exit")

    command = input(">>> ")

    if command == "exit":

        print("Гра завершена")

        break

    method = getattr(hero, command, None)

    if method:

        method()

    else:

        print("Unknown command")


# ПОЯСНЕННЯ:

# це вже:
# mini console RPG


# getattr()
# дозволяє:
# запускати методи
# через текст


# саме так працюють:
# - game consoles
# - admin systems
# - Discord bots
# - command engines


# ФІНАЛЬНІ ЗАВДАННЯ


# 1.
# Створи:
# - Mage
# - Archer
# - Assassin

# 2.
# Додай:
# - invisibility
# - critical_hit
# - dodge

# 3.
# Зроби:
# battle commands

# 4.
# Додай:
# - inventory system
# - equipment system

# 5.
# Створи:
# monster AI

# 6.
# Зроби:
# випадкові скіли через random.choice()

# 7.
# Додай:
# - Boss class
# - ultimate attacks

# 8.
# Зроби:
# level up system

# 9.
# Додай:
# command history

# 10.
# СУПЕР ЗАВДАННЯ:
# створи:
# mini console RPG engine
# через:
# - getattr()
# - hasattr()
# - setattr()
# - introspection


# ТЕ, ЩО ТИ ЗАРАЗ ВЧИШ —
# це вже:
# - game architecture
# - command systems
# - AI systems
# - console engines
# - admin panels
# - Discord bot logic
# - Minecraft plugin systems

# introspection —
# одна з найсильніших
# можливостей Python