def max_data(data):
    i = 1
    max_ = data[0]
    while i < len(data):
        if data[i] > max_:
            max_ = data[i]
        i += 1
    return max_


def min_data(data):
    i = 1
    min_ = data[0]
    while i < len(data):
        if data[i] < min_:
            min_ = data[i]
        i += 1
    return min_


print(f'Max is {max_data([1, 2, 3, 4])}, Min is {min_data([1, 2, 3, 4])}')
