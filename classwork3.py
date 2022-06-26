import random
from calendar import monthrange


def rev():
    num = input()
    return num[::-1]


# print(rev())

def get_num():
    nums = list(map(int, input().split()))
    tup = tuple(nums)
    str_tup = ''.join(map(str, tup))
    return str_tup


# print(get_num())

def sum_of_min_max(data):
    return min(data) + max(data)


# print(sum_of_min_max([1, 2, 3, 5, 100]))

def even_index(data):
    indexes = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            indexes.append(i)
    return indexes


# print(even_index([1, 2, 3, 4, 5, 6]))

def new_rev():
    word = input()
    words = []
    index = len(word)
    while index > 0:
        index -= 1
        words.append(word[index])
    print(''.join(words))


# new_rev()

def smallest_prime(n):
    while True:
        flag = True
        n += 1
        for j in range(2, int(n / 2) + 1):
            if n % j == 0:
                flag = False
        if flag:
            return n


# print(smallest_prime(15))


def median(nums):
    num_sorted = nums.sort()
    if len(nums) % 2 != 0:
        i = int((len(nums) + 1) / 2 - 1)
        return nums[i]
    else:
        i1 = int(len(nums) / 2 - 1)
        i2 = int(len(nums) / 2)
        return (nums[i1] + nums[i2]) / 2


# print(median([2, 4, 6, 8]))


def days_in_month(year, month):
    return monthrange(year, month)[1]


# print(days_in_month(2024, 2))


def random_passwd(n):
    passwd = ''
    for i in range(n):
        rand_num = random.randint(33, 126)
        passwd += chr(rand_num)
    return passwd


print(random_passwd(3))


def same_parity(n, *args):
    res = []
    for elem in args:
        if elem % n == 0:
            res.append(elem)
    return res


print(same_parity(6, 6, 12, 36, 4, 5, 6, 7, 666, 9))
