def zipper(data1, data2):
    lis = []
    for i in range(len(data1)):
        lis.append((data1[i], data2[i]))
    return lis


print(zipper([1, 2, 3, 4], [5, 6, 7, 8]))
