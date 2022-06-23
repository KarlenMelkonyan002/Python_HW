def remove_all(data, value):
    while value in data:
        data.remove(value)
    return data


print(remove_all([1, 1, 5, 6, 8, 9], 1))
