def pop(data, index):
    if index == -1:
        res = data[len(data) - 1]
        del data[len(data) - 1]
        return res
    elif 0 <= index < len(data):
        res = data[index]
        del data[index]
    else:
        raise IndexError('Index out of range')
    return res


print(pop([1, 2, 3, 4], 1))
