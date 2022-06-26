lst1 = [5, 8, 1, 2, 3, 4]
lst2 = [54, 85]


def sublist(larger, smaller):
    if len(smaller) == 0:
        return True
    for i in range(len(larger)):
        if larger[i] == smaller[0]:
            n = 1
            while n < len(smaller) and (larger[i + n] == smaller[n]):
                n += 1
            if n == len(smaller):
                return True
            return False


print(sublist(lst1, lst2))
