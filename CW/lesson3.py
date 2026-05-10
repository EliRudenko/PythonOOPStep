# УРОК 3: РОБОТА З ДЕКІЛЬКОМА КЛАСАМИ
# МІНІ-ПРОЄКТ: RPG GAME / GAME WORLD

# СЬОГОДНІ:
# - будемо працювати з кількома класами
# - навчимось створювати зв’язки між об’єктами
# - зробимо маленький ігровий світ
# - додамо інвентар, зброю, ворогів та NPC
# - навчимось робити взаємодію персонажів


# КЛАС — це шаблон
# ОБ’ЄКТ — конкретний екземпляр


class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)


player1 = Character("Knight", 5)

player1.info()


# ЗАВДАННЯ:
# створи ще 2 персонажі
# зроби різні level


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def info(self):
        print("Зброя:", self.name)
        print("Шкода:", self.damage)


sword = Weapon("Iron Sword", 25)

sword.info()


# ЗАВДАННЯ:
# створи:
# - Bow
# - Axe
# - Magic Staff




# ВАЖЛИВО:
# тепер у нас окремий клас для зброї

# це правильна архітектура:
# Character ≠ Weapon



class Character:
    def __init__(self, name, level, weapon):
        self.name = name
        self.level = level
        self.weapon = weapon

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)
    def show_weapon(self):
        print(self.name, "використовує", self.weapon.name)


sword = Weapon("Diamond Sword", 40)

player = Character("Alex", 10, sword)

player.show_weapon()

# ОБ’ЄКТ ВСЕРЕДИНІ ОБ’ЄКТА

# player містить weapon
# weapon — теж окремий об’єкт


# ЗАВДАННЯ:
# зроби:
# - персонажа з луком
# - персонажа з магічним посохом


class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        print("Ворог:", self.name)
        print("HP:", self.health)

zombie = Enemy("Zombie", 100)

zombie.info()


# ТЕПЕР ЗРОБИМО БІЙ


class Character:
    def __init__(self, name, level, weapon):
        self.name = name
        self.level = level
        self.weapon = weapon

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)

    def show_weapon(self):
        print(self.name, "використовує", self.weapon.name)

    def attack(self, enemy):

        print(self.name, "атакує", enemy.name)

        enemy.health -= self.weapon.damage

        print(enemy.name, "отримав шкоду")
        print("HP ворога:", enemy.health)


sword = Weapon("Dragon Sword", 35)
player = Character("Knight", 12, sword)

enemy = Enemy("Skeleton", 120)

player.attack(enemy)


# ВАЖЛИВО:
# attack() отримує ОБ’ЄКТ enemy

# ми змінюємо стан іншого об’єкта


# ЗАВДАННЯ:
# зроби:
# - ще одного ворога
# - ще одну атаку


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


class Character:
    def __init__(self, name, level, weapon, armor):

        self.name = name
        self.level = level

        self.weapon = weapon
        self.armor = armor

        self.health = 100

    def show_stats(self):

        print("Ім'я:", self.name)
        print("HP:", self.health)
        print("Зброя:", self.weapon.name)
        print("Броня:", self.armor.name)


armor1 = Armor("Iron Armor", 15)

weapon1 = Weapon("Steel Sword", 30)

player = Character("Warrior", 8, weapon1, armor1)

player.show_stats()


# ЗАВДАННЯ:
# створи:
# - Golden Armor
# - Diamond Armor


# ДОДАЄМО ІНВЕНТАР


class Item:
    def __init__(self, name):
        self.name = name


class Character:
    def __init__(self, name):

        self.name = name

        self.inventory = []

    def add_item(self, item):

        self.inventory.append(item)

        print(item.name, "додано в інвентар")

    def show_inventory(self):

        print("Інвентар персонажа:")

        if len(self.inventory) == 0:
            print("Інвентар порожній")

        for item in self.inventory:
            print("-", item.name)


player = Character("Steve")

item1 = Item("Magic Crystal")
item2 = Item("Gold Key")

player.add_item(item1)
player.add_item(item2)

player.show_inventory()


# ВАЖЛИВО:
# inventory — список об’єктів


# ЗАВДАННЯ:
# додай:
# - Potion
# - Shield
# - Ring


# ТЕПЕР ДОДАМО NPC


class NPC:
    def __init__(self, name, role):

        self.name = name
        self.role = role

    def talk(self):

        print(self.name, "говорить:")
        print("Ласкаво просимо в місто!")


npc1 = NPC("Merchant", "Trader")

npc1.talk()


# NPC — це non-player character

# Так робляться:
# - торговці
# - квестові персонажі
# - охоронці


# ЗАВДАННЯ:
# створи:
# - Blacksmith
# - Wizard
# - Guard


# ТЕПЕР ДОДАМО МАГІЮ


class Spell:
    def __init__(self, name, damage, mana_cost):

        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost


class Mage:
    def __init__(self, name):

        self.name = name
        self.mana = 100

    def cast_spell(self, spell, enemy):

        if self.mana >= spell.mana_cost:

            self.mana -= spell.mana_cost

            enemy.health -= spell.damage

            print(self.name, "використав", spell.name)

            print("Mana:", self.mana)

            print(enemy.name, "отримав шкоду")
            print("HP:", enemy.health)

        else:
            print("Недостатньо мани")


fireball = Spell("Fireball", 40, 30)

enemy = Enemy("Orc", 150)

mage = Mage("Dark Wizard")

mage.cast_spell(fireball, enemy)


# ВАЖЛИВО:
# тут вже справжня взаємодія кількох класів:
# Mage
# Spell
# Enemy


# ЗАВДАННЯ:
# створи:
# - Ice Blast
# - Thunder Strike


# ДОДАЄМО РІВЕНЬ ТА ДОСВІД


class Character:
    def __init__(self, name):

        self.name = name

        self.level = 1
        self.exp = 0

    def gain_exp(self, amount):

        self.exp += amount

        print(self.name, "отримав", amount, "EXP")

        if self.exp >= 100:

            self.level += 1
            self.exp = 0

            print("LEVEL UP!")
            print("Новий рівень:", self.level)


player = Character("Hero")

player.gain_exp(50)

player.gain_exp(60)


# ЗАВДАННЯ:
# зроби:
# - якщо level up:
# health збільшується


# ТЕПЕР ЗРОБИМО КОМАНДУ / PARTY


class Party:
    def __init__(self):

        self.members = []

    def add_member(self, character):

        self.members.append(character)

    def show_members(self):

        print("Команда:")

        for member in self.members:
            print("-", member.name)


p1 = Character("Knight")
p2 = Character("Mage")
p3 = Character("Archer")

party = Party()

party.add_member(p1)
party.add_member(p2)
party.add_member(p3)

party.show_members()


# ВАЖЛИВО:
# тепер один об’єкт Party
# містить багато Character


# ФІНАЛЬНИЙ ВЕЛИКИЙ ПРОЄКТ


class Weapon:
    def __init__(self, name, damage):

        self.name = name
        self.damage = damage


class Armor:
    def __init__(self, name, defense):

        self.name = name
        self.defense = defense


class Enemy:
    def __init__(self, name, health, damage):

        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, player):

        real_damage = self.damage - player.armor.defense

        if real_damage < 0:
            real_damage = 0

        player.health -= real_damage

        print(self.name, "атакує", player.name)

        print(player.name, "отримав", real_damage, "шкоди")

        print("HP гравця:", player.health)


class Character:
    def __init__(self, name, weapon, armor):

        self.name = name

        self.weapon = weapon
        self.armor = armor

        self.health = 100
        self.level = 1
        self.exp = 0

        self.inventory = []

    def attack(self, enemy):

        enemy.health -= self.weapon.damage

        print(self.name, "атакує", enemy.name)

        print(enemy.name, "HP:", enemy.health)

        if enemy.health <= 0:

            print(enemy.name, "переможений")

            self.gain_exp(50)

    def gain_exp(self, amount):

        self.exp += amount

        print(self.name, "отримав EXP:", amount)

        if self.exp >= 100:

            self.level += 1
            self.exp = 0

            self.health += 20

            print("LEVEL UP!")
            print("Рівень:", self.level)

    def add_item(self, item):

        self.inventory.append(item)

    def show_inventory(self):

        print("Інвентар:")

        for item in self.inventory:
            print("-", item.name)

    def __str__(self):

        return (
            f"{self.name} | "
            f"HP: {self.health} | "
            f"LEVEL: {self.level} | "
            f"EXP: {self.exp}"
        )


weapon1 = Weapon("Crystal Sword", 35)

armor1 = Armor("Knight Armor", 12)

player = Character("Arthur", weapon1, armor1)

enemy = Enemy("Dark Orc", 120, 25)

print(player)

player.attack(enemy)

enemy.attack(player)

player.attack(enemy)
player.attack(enemy)
player.attack(enemy)

print(player)


# ФІНАЛЬНІ ЗАВДАННЯ


# 1.
# Додай Mana System

# 2.
# Зроби:
# - healing spell
# - shield spell

# 3.
# Додай Boss class

# 4.
# Зроби:
# - critical damage
# - dodge chance

# 5.
# Додай:
# - rarity предметів
# - epic / legendary

# 6.
# Зроби Shop System:
# - buy weapon
# - sell item

# 7.
# Додай карту:
# - Forest
# - Dungeon
# - Castle

# 8.
# Створи Quest System

# 9.
# Зроби battle loop через while

# 10.
# Спробуй зробити:
# turn-based combat system


# ТЕ, ЩО ТИ ЗАРАЗ РОБИШ —
# це вже справжня структура ігор.

# Саме так створюються:
# - RPG
# - survival games
# - MMORPG
# - Minecraft plugins
# - Discord RPG bots
# - game servers

# Головна ідея ООП:
# розділяти логіку на окремі класи,
# які взаємодіють між собою.