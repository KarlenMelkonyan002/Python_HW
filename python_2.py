import random


def kilo_pound():
    kilograms = int(input("Enter kilograms: "))
    pounds = 2.2 * kilograms
    return pounds


def generate_ints():
    lst = []
    for i in range(51):
        x = random.randint(3, 6)
        lst.append(x)
    return lst


def expr():
    x = int(input("X: "))
    y = int(input("Y: "))
    return abs(x - y) / (x + y)


def leap_year():
    year = int(input("Enter year: "))
    leap_years = []
    for i in range(1600, year + 1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            leap_years.append(i)
    return leap_years


def perfect_num(num):
    sum_ = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            sum_ += i
    if num == sum_:
        return True
    return False


def perfect_nums_from_range(range_):
    lst = []
    num = 1
    while num < range_:
        if perfect_num(num):
            lst.append(num)
        num += 1
    return lst


print(perfect_nums_from_range(10000))
