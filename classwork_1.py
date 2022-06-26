import math
import time

# 1
print('Melkonyan Karlen,Sargsyan str. 207/133')
# 2
name = input('Enter your name:')
print(f'Hello {name}')
# 3
height = float(input('Enter height: '))
weight = float(input('Enter weight: '))
square = height * weight
print(f'Square of room is {square} m^2 ')
# 4
height = float(input('Enter height: '))
weight = float(input('Enter weight: '))
square = (height * weight) / 43560
print(f'The square of place is {square}')
# 5
small = int(input('Enter small bottles count: '))
big = int(input('Enter big bottles count: '))
res = (0.10 * small) + (0.25 * big)
print(f'Total cost of bottles is: ${res}')
# 6
bill = float(input('Enter your bill: '))
res = float((bill - bill * 0.2) * 0.18)
tax = float(bill * 0.2)
print(f'Your tax is {tax:.2f}$ , and your tip is {res:.2f}$')
# 7
num = int(input('Enter number: '))
i = 1
sum_ = 0
while i <= num:
    sum_ += i
    i += 1
print(sum_)
# 8
n = int(input('Enter souvenir count: '))
m = int(input('Enter trifle count: '))
souvenir = 75
trifle = 112
res = n * souvenir + m * trifle
print(f'Total weight is {res} gram')
# 9
money = float(input("Enter your cash: "))
first = money * 0.04 + money
second = first * 0.04 + first
third = second * 0.04 + second
print(f'First year:{first}\nSecond year:{second}\nThird year:{third}')
# 10
a = int(input('Enter a:'))
b = int(input('Enter b:'))
print(f'Sum:{a + b}\nDiff:{a - b}\nDiv:{a / b}\nFloorDiv:{a // b}\nModulos:{a % b}\nLog:{math.log(a, 10)}')
# 11
mpg = int(input('Enter MPG:'))
liter = 3.785411784
meter = 1609.344
kpg = liter / meter * 1000
res = 100 / mpg * kpg
print(res)
# 12
fut = int(input('Enter futs: '))
duim = int(input('Enter duim: '))

height1 = fut * 12 * 2.54
height2 = duim * 2.54
print(f'Converted from fut {height1} cm\nConverted from duim {height2} cm')
# 13
fut_dist = int(input('Enter distance: '))
duim_dist = fut_dist * 12
yard_dist = fut_dist * 0.333333
mile_dist = fut_dist * 0.000189394
print(f'Duim:{duim_dist}\nYard:{yard_dist}\nMile:{mile_dist}')
# 14
r = float(input('Enter radius: '))
print(f'Area is:{math.pi * (r ** 2)}\n Volume is:{(4 * math.pi * (r ** 3)) / 3}')
# 15
r = float(input('Enter radius: '))
h = float(input('Enter height: '))
print(f'V is:{(math.pi * (r ** 2)) * h}')
# 16
from math import sqrt

d = int(input())
a = int(input())
g = 9.8
v = 0
res = sqrt(v ** 2 + 2 * a * d * g)
print(res)
# 17
b = float(input('Enter b: '))
h = float(input('Enter h: '))
area = (b * h) / 2
print(f'Area is:{area}')
# 18
s1 = float(input('Enter s1: '))
s2 = float(input('Enter s2: '))
s3 = float(input('Enter s3: '))
p = s1 + s2 + s3
area = math.sqrt(p * (p - s1) * (p - s2) * (p - s3))
print(f'Area is:{area}')
# 19
days = int(input('Enter days: '))
hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))
seconds = int(input('Enter seconds: '))
day_seconds = days * 86400
hours_seconds = hours * 3600
minutes_seconds = minutes * 60
total = day_seconds + hours_seconds + minutes_seconds + seconds
print(f'Sec in day:{day_seconds}\nSec in hour:{hours_seconds}\nSec in minutes:{minutes_seconds}\nTotal seconds:{total}')
# 20
t = time.asctime()
print(t)
# 21
month = input('Enter month starting with capital letter: ')
if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    print('31 days')
elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print('30 days')
else:
    print('28 or 29 days')
# 22
letter = input('Enter one letter, not capital: ')
vowels = 'aeiou'
if letter in vowels:
    print('Vowel')
elif letter == 'y':
    print('Vowel or consonant')
else:
    print('Consonant')
# 23
day = int(input('Enter day: '))
month = input('Enter month: ')
if month == 'January' or month == 'December' or month == 'February':
    print('Winter')
elif month == 'June' or month == 'July' or month == 'August':
    print('Summer')
elif month == 'March' or month == 'April' or month == 'May':
    print('Spring')
else:
    print('Fall')
# 24
nums = list(map(int, input().split()))
aver = sum(nums) / len(nums)
print(aver)
# 25
celsius = float(input('Temperature value in degree Celsius: '))
fahrenheit = float(input('Temperature value in degree Fahrenheit: '))
fahrenheit_val = (celsius * 1.8) + 32
celsius_val = (fahrenheit - 32) / 1.8
print(f'Cel to Far: {fahrenheit_val}\nFar to Cel {celsius_val}')
# 26
number = int(input('Enter number: '))
while 1 <= number < 101:
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
        number += 1
    elif number % 3 == 0:
        print('Fizz')
        number += 1
    elif number % 5 == 0:
        print('Buzz')
        number += 1
    else:
        print(number)
        number += 1

