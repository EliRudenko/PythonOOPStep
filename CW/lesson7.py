# УРОК 7: ІТЕРАТОРИ. ГЕНЕРАТОРИ. ЗАМИКАННЯ. ДЕКОРАТОРИ

# СЬОГОДНІ МИ ВЧИМОСЯ:
# - як Python "перебирає" об’єкти
# - як створювати свої генератори
# - як функції можуть "пам’ятати"
# - як змінювати функції без зміни коду (декоратори)


# ІТЕРАТОРИ

# УЯВИ:
# у тебе є список учнів
students = ["Олег", "Аня", "Іра"]

# ми можемо пройтись по ньому
for s in students:
    print(s)

# але що відбувається всередині?


# Python створює ІТЕРАТОР

it = iter(students)

print(next(it))
print(next(it))
print(next(it))

# якщо ще раз:
# print(next(it)) → буде помилка (StopIteration)


# ПОЯСНЕННЯ:
# iter() — створює ітератор
# next() — бере наступний елемент


# ЗАВДАННЯ:
# створи список з 3 чисел і вручну перебери через next()



# СТВОРЮЄМО СВІЙ ІТЕРАТОР

# УЯВИ:
# лічильник від 1 до 3

class Counter:
    def __init__(self, max):
        self.current = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


c = Counter(3)

for i in c:
    print(i)


# ПОЯСНЕННЯ:
# __iter__ — повертає ітератор
# __next__ — дає наступне значення


# ЗАВДАННЯ:
# зроби Counter до 5



# ГЕНЕРАТОРИ

# УЯВИ:
# ти не створюєш одразу список
# ти даєш значення ПО ОДНОМУ

def simple_gen():
    yield 1
    yield 2
    yield 3

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))


# ПОЯСНЕННЯ:
# yield — це як "пауза"
# функція запам’ятовує де була


# ЗАВДАННЯ:
# зроби генератор який повертає 10, 20, 30



# ГЕНЕРАТОР З ЦИКЛОМ

def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up(5):
    print(num)


# ЗАВДАННЯ:
# зроби генератор від 5 до 1 (назад)



# ГЕНЕРАТОР vs СПИСОК

# список:
nums = [i for i in range(5)]

# генератор:
nums_gen = (i for i in range(5))

print(nums)
print(nums_gen)


# ПОЯСНЕННЯ:
# список — всі значення одразу
# генератор — по одному


# ЗАВДАННЯ:
# створи генератор квадратів чисел



# ЗАМИКАННЯ (CLOSURE)

# УЯВИ:
# функція пам’ятає значення

def outer():
    x = 10

    def inner():
        print(x)

    return inner


f = outer()
f()


# ПОЯСНЕННЯ:
# inner пам’ятає x навіть після завершення outer


# ЗАВДАННЯ:
# зроби outer з числом 20



# ЗАМИКАННЯ З ПАРАМЕТРАМИ

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply


mul2 = make_multiplier(2)
mul3 = make_multiplier(3)

print(mul2(5))
print(mul3(5))


# ПОЯСНЕННЯ:
# ми створюємо "спеціальні функції"


# ЗАВДАННЯ:
# зроби множник на 10



# ДЕКОРАТОРИ

# УЯВИ:
# ти хочеш додати поведінку функції
# але не змінювати її код

def decorator(func):
    def wrapper():
        print("Початок")
        func()
        print("Кінець")
    return wrapper


@decorator
def hello():
    print("Привіт")

hello()


# ПОЯСНЕННЯ:
# @decorator — це як "обгорнути функцію"


# ЗАВДАННЯ:
# зроби декоратор який пише "СТАРТ" і "СТОП"



# ДЕКОРАТОР З АРГУМЕНТАМИ

def decorator(func):
    def wrapper(name):
        print("Початок")
        func(name)
        print("Кінець")
    return wrapper


@decorator
def hello(name):
    print("Привіт", name)

hello("Олег")


# ЗАВДАННЯ:
# додай ще один параметр



# ДЕКОРАТОР ДЛЯ КОНТРОЛЮ

# УЯВИ:
# перевіряємо дані

def check_positive(func):
    def wrapper(x):
        if x < 0:
            print("Помилка: число менше 0")
            return
        return func(x)
    return wrapper


@check_positive
def square(x):
    print(x * x)


square(5)
square(-3)


# ЗАВДАННЯ:
# зроби перевірку: число не більше 100



# МІНІ-ПРИКЛАД З ГЕНЕРАТОРОМ

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)


# ЗАВДАННЯ:
# зроби генератор непарних чисел



# ФІНАЛЬНИЙ МІНІ-ПРОЄКТ

# гра: даємо команди і логуємо їх

def logger(func):
    def wrapper(command):
        print("Команда:", command)
        return func(command)
    return wrapper


@logger
def process(command):
    print("Виконується:", command)


process("start")
process("run")


# ФІНАЛЬНІ ЗАВДАННЯ

# 1. зроби генератор:
# - числа кратні 3

# 2. зроби замикання:
# - додає число (add5, add10)

# 3. зроби декоратор:
# - рахує скільки разів викликали функцію

# 4. складніше:
# - декоратор перевіряє тип (тільки int)

# 5. супер:
# - зроби гру:
# вводиш команду → декоратор її логує