# УРОК 8: ЛОГУВАННЯ. НАЛАШТУВАННЯ ЛОГУВАННЯ. ТЕСТИ

# УЯВИ:
# ти робиш гру або програму
# і хочеш знати:
# - що відбувається всередині
# - де помилка
# - хто що зробив

# для цього є ЛОГУВАННЯ (logging)


# ПРОСТИЙ PRINT

print("Програма стартувала")

# але print — це просто текст
# його складно контролювати


# ЛОГУВАННЯ

import logging

logging.warning("Це попередження")


# ПОЯСНЕННЯ:
# logging — це як "розумний print"


# ЗАВДАННЯ:
# виклич logging.error()



# РІВНІ ЛОГУВАННЯ

logging.debug("debug — для розробника")
logging.info("info — звичайна інформація")
logging.warning("warning — щось не так")
logging.error("error — помилка")
logging.critical("critical — дуже серйозно")


# УЯВИ:
# debug → дрібні деталі
# info → що відбувається
# warning → щось підозріле
# error → помилка
# critical → все дуже погано


# ЗАВДАННЯ:
# напиши по одному повідомленню кожного рівня



# НАЛАШТУВАННЯ (basicConfig)

logging.basicConfig(level=logging.DEBUG)

logging.debug("Тепер debug видно")


# ПОЯСНЕННЯ:
# ми включили більше повідомлень


# ЗАВДАННЯ:
# постав level=logging.INFO



# ФОРМАТ ЛОГУ

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logging.info("Програма працює")


# ПОЯСНЕННЯ:
# format — як виглядає повідомлення


# ЗАВДАННЯ:
# додай %(asctime)s (час)



# ЛОГ У ФАЙЛ

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logging.info("Запис у файл")


# ПОЯСНЕННЯ:
# тепер лог зберігається у файл


# ЗАВДАННЯ:
# додай ще одне повідомлення



# ПРИКЛАД З ЖИТТЯ

class Bank:
    def __init__(self):
        self.money = 100

    def take(self, amount):
        if amount > self.money:
            logging.error("Недостатньо грошей")
        else:
            self.money -= amount
            logging.info("Зняли гроші")


bank = Bank()
bank.take(50)
bank.take(200)


# ЗАВДАННЯ:
# додай logging.warning якщо грошей мало (<20)



# ТЕСТИ

# УЯВИ:
# ти хочеш перевірити:
# чи працює код правильно

def add(a, b):
    return a + b


# простий тест
assert add(2, 3) == 5


# ПОЯСНЕННЯ:
# assert перевіряє
# якщо неправильно → помилка


# ЗАВДАННЯ:
# перевір add(10, 5)



# ЩЕ ТЕСТИ

def multiply(a, b):
    return a * b

assert multiply(2, 3) == 6
assert multiply(0, 5) == 0


# ЗАВДАННЯ:
# додай тест для 10 * 10



# ТЕСТ З ПОМИЛКОЮ

def divide(a, b):
    return a / b

# assert divide(10, 0)  # тут буде помилка


# ЗАВДАННЯ:
# додай try/except до divide



# ПРОСТИЙ "ТЕСТЕР"

def test_add():
    if add(2, 2) == 4:
        print("OK")
    else:
        print("FAIL")

test_add()


# ЗАВДАННЯ:
# зроби test_multiply()



# МІНІ-ПРОЄКТ

class Player:
    def __init__(self):
        self.energy = 50

    def work(self):
        self.energy -= 10
        logging.info("Player працює")

    def sleep(self):
        self.energy += 20
        logging.info("Player спить")


player = Player()

player.work()
player.sleep()


# ДОДАЄМО ТЕСТИ

assert player.energy >= 0


# ФІНАЛЬНІ ЗАВДАННЯ

# 1. додай:
# - logging.warning якщо energy < 10

# 2. зроби:
# - logging.error якщо energy < 0

# 3. напиши тести:
# - після work енергія менша
# - після sleep більша

# 4. складніше:
# - лог у файл + перевір

# 5. супер:
# - зроби 3 тести для Player