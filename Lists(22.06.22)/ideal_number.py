def ideal_number(n):
    divs = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divs.append(i)
    div_sum = sum(divs)
    if div_sum == n:
        return True
    return False


print(ideal_number(28))
