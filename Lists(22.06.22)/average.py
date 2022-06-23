nums = list(map(int, input().split()))


def average(num_list):
    greater = []
    smaller = []
    aver = sum(num_list) / len(num_list)
    for elem in num_list:
        if elem < aver:
            smaller.append(elem)
        elif elem > aver:
            greater.append(elem)
    return greater, smaller, aver


print(average(nums))
