def even_odd():
    num = int(input("Enter number: "))
    if num == 0:
        return "Not even, not odd"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# print(even_odd())


def cons_vowel():
    char = input("Enter character: ")
    if char.lower() in "aeiouy":
        return "Vowel"
    else:
        return "Consonant"


# print(cons_vowel())


def fib(n):
    a = 0
    b = 1

    if n < 0:
        return False

    elif n == 0:
        return a

    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
    return b


# num = int(input("Enter number: "))
# print(fib(num))
def digit_sum():
    num = int(input("Enter number: "))
    sum_ = 0
    while num > 0:
        digit = num % 10
        sum_ += digit
        num = num // 10
    return sum_


# print(digit_sum())

for i in range(2):
    print("******")
    for j in range(3):
        if i == 1:
            break
        print("*    *")
