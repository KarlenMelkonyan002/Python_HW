from math import pow

a = [5, 4, 3]
b = [2, 3, 4]
c = [10, 20, 30]
d = [2, 3, 4]


def sum_(a_, b_, c_):
    return a_ + b_ + c_


def div_(a_, b_, c_):
    return a_ / b_ / c_


def triple_data(data):
    res = [None] * len(data)
    for i in range(len(data)):
        res[i] = data[i] * 3
    return res


def map3(func, data1, data2, data3):
    if len(data1) != len(data2) or len(data2) != len(data3) or len(data1) != len(data3):
        return 'Enter equal sizes'
    res = [None] * len(data1)
    for i in range(len(data1)):
        res[i] = func(data1[i], data2[i], data3[i])
    return res


# print(map3(div_, a, b, c))

def map2(data1, data2, func=pow):
    if len(data1) != len(data2):
        return 'Enter equal sizes'
    res = [None] * len(data1)
    for i in range(len(data2)):
        res[i] = func(data1[i], data2[i])
    return res


print(map2(a, b))
