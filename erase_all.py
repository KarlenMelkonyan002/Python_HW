from os import remove


def remove_all(data, value):
    for item in data:
        if item == value:
            data.remove(value)
    return data


print(remove_all([1, 1, 5, 6, 8, 9], 1))
