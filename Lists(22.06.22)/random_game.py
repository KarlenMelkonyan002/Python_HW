import random
res = []
for ticket in range(6):
    wining = random.randint(1, 49)
    if wining not in res:
        res.append(ticket)
print(sorted(res))
