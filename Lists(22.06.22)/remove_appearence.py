def remove_duplicates():
    _strings = input('Enter string: ').split(",")
    res = []
    for item in _strings:
        if item not in res:
            res.append(item)
    return res


print(remove_duplicates())
