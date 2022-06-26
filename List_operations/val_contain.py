def contain(data, val):
    for i in range(len(data)):
        if data[i] == val:
            return True
        return False


print(contain([1, 2, 3, 4], 1))
