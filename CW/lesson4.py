# УРОК 4: НАСЛІДУВАННЯ КЛАСІВ. super()
# GAME RPG VERSION

# СЬОГОДНІ:
# - навчимось робити ієрархію класів
# - зрозуміємо inheritance
# - розберемо super()
# - зробимо професійну структуру персонажів
# - навчимось override методів
# - створимо RPG систему класів


# УЯВИ:

# У грі є:
# - Warrior
# - Mage
# - Archer

# У ВСІХ є:
# - ім'я
# - hp
# - level

# Але:
# Warrior має силу
# Mage має ману
# Archer має точність

# Щоб не дублювати код —
# використовують НАСЛІДУВАННЯ


class Character:
    def __init__(self, name, level):

        self.name = name
        self.level = level

        self.health = 100

    def info(self):

        print("Ім'я:", self.name)
        print("Рівень:", self.level)
        print("HP:", self.health)


player = Character("Hero", 1)

player.info()


# ЗАВДАННЯ:
# створи ще одного персонажа


# ПРОБЛЕМА БЕЗ НАСЛІДУВАННЯ


class Warrior:
    def __init__(self, name, level, strength):

        self.name = name
        self.level = level
        self.health = 100

        self.strength = strength


class Mage:
    def __init__(self, name, level, mana):

        self.name = name
        self.level = level
        self.health = 100

        self.mana = mana


# ПРОБЛЕМА:
# ми копіюємо:
# - name
# - level
# - health

# Це погана практика.


# ПРАВИЛЬНО:
# inheritance


class Character:
    def __init__(self, name, level):

        self.name = name
        self.level = level

        self.health = 100

    def info(self):

        print("Ім'я:", self.name)
        print("Рівень:", self.level)
        print("HP:", self.health)


class Warrior(Character):

    def __init__(self, name, level, strength):

        super().__init__(name, level)

        self.strength = strength


warrior = Warrior("Knight", 5, 40)

warrior.info()

print("Сила:", warrior.strength)


# ПОЯСНЕННЯ:

# Warrior(Character)

# означає:
# Warrior наслідує Character

# Warrior автоматично отримує:
# - info()
# - health
# - name
# - level


# super() викликає код батьківського класу


# ПРОСТО:

# Character = база
# Warrior = розширення


# ЗАВДАННЯ:
# створи:
# - Mage
# - Archer

# через inheritance


class Character:
    def __init__(self, name):

        print("Створюється Character")

        self.name = name


class Mage(Character):

    def __init__(self, name):

        print("Створюється Mage")

        super().__init__(name)


mage = Mage("Dark Wizard")


# ПОРЯДОК:

# 1. Mage __init__
# 2. super()
# 3. Character __init__


# ВАЖЛИВО:

# super() не копіює код

# Він ВИКЛИКАЄ код
# батьківського класу


# ЗАВДАННЯ:
# додай print у Archer


class Character:
    def __init__(self, name, level):

        self.name = name
        self.level = level

        self.health = 100

    def attack(self):

        print(self.name, "атакує")


class Warrior(Character):

    def __init__(self, name, level):

        super().__init__(name, level)

        self.strength = 50

    def heavy_attack(self):

        print(self.name, "використовує HEAVY ATTACK")


player = Warrior("Arthur", 10)

player.attack()

player.heavy_attack()


# ПОЯСНЕННЯ:

# Warrior має:
# - attack() з Character
# - heavy_attack() свій


# ЗАВДАННЯ:
# додай:
# - fireball() для Mage
# - sniper_shot() для Archer


# OVERRIDE МЕТОДІВ


class Character:
    def attack(self):

        print("Базова атака")


class Warrior(Character):

    def attack(self):

        print("Warrior б'є мечем")


class Mage(Character):

    def attack(self):

        print("Mage кидає магію")


w = Warrior()
m = Mage()

w.attack()
m.attack()


# ПОЯСНЕННЯ:

# attack() один і той самий
# але поведінка різна

# Це override


# В ІГРАХ:
# майже всі системи
# працюють через override


# ЗАВДАННЯ:
# зроби attack() для Archer


class Character:
    def __init__(self, name):

        self.name = name

    def info(self):

        print("Ім'я:", self.name)


class Mage(Character):

    def __init__(self, name, mana):

        super().__init__(name)

        self.mana = mana

    def info(self):

        super().info()

        print("Mana:", self.mana)


mage = Mage("Wizard", 120)

mage.info()


# ПОЯСНЕННЯ:

# super().info()

# запускає:
# Character.info()

# а потім ми додаємо своє


# ЦЕ ДУЖЕ ВАЖЛИВО:
# так будується професійний код


# ЗАВДАННЯ:
# додай:
# - level
# - hp


# NPC SYSTEM


class NPC(Character):

    def __init__(self, name, role):

        super().__init__(name, 1)

        self.role = role

    def talk(self):

        print(self.name, "говорить:")
        print("Ласкаво просимо в місто")


npc = NPC("Merchant", "Trader")

npc.info()

npc.talk()


# ЗАВДАННЯ:
# створи:
# - Blacksmith
# - Guard
# - Healer


# MONSTER SYSTEM


class Monster(Character):

    def __init__(self, name, level, damage):

        super().__init__(name, level)

        self.damage = damage

    def attack(self):

        print(self.name, "атакує монстрами")


class Boss(Monster):

    def __init__(self, name, level, damage):

        super().__init__(name, level, damage)

        self.rage = 100

    def ultimate(self):

        print(self.name, "використовує ULTIMATE")


boss = Boss("Dragon Lord", 50, 80)

boss.info()

boss.attack()

boss.ultimate()


# ІЄРАРХІЯ:

# Character
# └── Monster
#     └── Boss


# ВАЖЛИВО:

# inheritance може бути багаторівневим


# ЗАВДАННЯ:
# створи:
# - MiniBoss
# - DemonBoss


# ДОДАЄМО INVENTORY SYSTEM


class Character:
    def __init__(self, name):

        self.name = name

        self.inventory = []

    def add_item(self, item):

        self.inventory.append(item)

    def show_inventory(self):

        print("Інвентар:")

        for item in self.inventory:
            print("-", item)


class Warrior(Character):

    def equip_sword(self):

        print(self.name, "екіпірував меч")


player = Warrior("Knight")

player.add_item("Health Potion")
player.add_item("Epic Sword")

player.show_inventory()

player.equip_sword()


# ВАЖЛИВО:

# Warrior отримав inventory
# через inheritance


# MULTIPLE CHARACTERS


class Character:
    def __init__(self, name):

        self.name = name

        self.health = 100

    def attack(self):

        print("Базова атака")


class Warrior(Character):

    def attack(self):

        print(self.name, "б'є мечем")


class Mage(Character):

    def attack(self):

        print(self.name, "кидає Fireball")


class Archer(Character):

    def attack(self):

        print(self.name, "стріляє з лука")


characters = [
    Warrior("Knight"),
    Mage("Wizard"),
    Archer("Sniper")
]


for character in characters:

    character.attack()


# ПОЯСНЕННЯ:

# Один код
# різна поведінка

# Це POLYMORPHISM


# MINI RPG PROJECT


class Character:
    def __init__(self, name, level):

        self.name = name
        self.level = level

        self.health = 100
        self.energy = 100

    def info(self):

        print(
            self.name,
            "| LEVEL:", self.level,
            "| HP:", self.health,
            "| ENERGY:", self.energy
        )

    def attack(self):

        print(self.name, "атакує")


class Warrior(Character):

    def __init__(self, name, level):

        super().__init__(name, level)

        self.strength = 50

    def attack(self):

        damage = self.strength

        print(self.name, "атакує мечем")
        print("Damage:", damage)

    def shield_block(self):

        print(self.name, "використовує SHIELD BLOCK")


class Mage(Character):

    def __init__(self, name, level):

        super().__init__(name, level)

        self.mana = 120

    def attack(self):

        if self.mana >= 20:

            self.mana -= 20

            print(self.name, "використовує FIREBALL")
            print("Mana:", self.mana)

        else:
            print("Недостатньо мани")

    def teleport(self):

        print(self.name, "телепортується")


class Archer(Character):

    def __init__(self, name, level):

        super().__init__(name, level)

        self.arrows = 30

    def attack(self):

        if self.arrows > 0:

            self.arrows -= 1

            print(self.name, "стріляє")

            print("Стріл залишилось:", self.arrows)

        else:
            print("Немає стріл")

    def dodge(self):

        print(self.name, "ухиляється")


warrior = Warrior("Arthur", 10)

mage = Mage("Merlin", 12)

archer = Archer("Robin", 9)

warrior.info()
warrior.attack()
warrior.shield_block()

print()

mage.info()
mage.attack()
mage.teleport()

print()

archer.info()
archer.attack()
archer.dodge()


# ФІНАЛЬНІ ЗАВДАННЯ


# 1.
# Додай Assassin class

# 2.
# Зроби:
# - critical hit
# - stealth mode

# 3.
# Створи Pet class:
# - Wolf
# - Dragon
# - Phoenix

# 4.
# Додай EXP system

# 5.
# Якщо EXP > 100:
# level up

# 6.
# Додай:
# - rarity предметів
# - common
# - rare
# - epic
# - legendary

# 7.
# Зроби:
# - PvP battle
# - Monster battle

# 8.
# Додай:
# - stamina
# - mana regeneration

# 9.
# Створи Guild class

# 10.
# Зроби:
# battle loop через while


# ТЕ, ЩО ТИ ЗАРАЗ ВЧИШ —
# це вже справжня архітектура ігор.

# Саме так створюються:
# - RPG engines
# - MMORPG systems
# - battle simulators
# - Minecraft servers
# - Unity gameplay systems
# - Discord RPG bots

# inheritance —
# одна з головних частин ООП.