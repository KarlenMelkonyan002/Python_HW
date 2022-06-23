def reverse_data(data):
    i = len(data)
    rev = []
    while i > 0:
        rev.append(data[i - 1])
        i -= 1
    return rev


print(reverse_data([1, 2, 3, 4]))
