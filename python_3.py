def sep_by_plus():
    inp = input("Enter numbers seperated by spaces: ")
    sep = inp.replace(" ", "+")
    print(sep)


def validate_number(phone_num):
    num_lst = phone_num.split("-")
    for i in range(len(num_lst)):
        num_lst[i] = num_lst[i].replace(" ", "")
        if not num_lst[i].isnumeric():
            return "Invalid"
    if len(num_lst[0]) == 1 and len(num_lst[1]) == 3 and len(num_lst[2]) == 3 and len(num_lst[3]) == 4:
        return "Valid"
    elif len(num_lst[0]) == 3 and len(num_lst[1]) == 3 and len(num_lst[2]) == 4:
        return "Valid"
    else:
        return "Invalid"


# num = input("Enter phone number in the form abc-def-hijk or 1-abc-def-hijk to validate: ")
# print(validate_number(num))
palindromic = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
# print(palindromic)
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
res = [list(range(L[i] + 1, L[i + 1])) for i in range(len(L) - 1)]
lengths = [len(res[i]) for i in range(len(res))]
print(lengths)
print(max(lengths))
print(res)





def products_dict():
    di = {}
    products = int(input("Enter number of products: "))
    for i in range(products):
        prod_name = input("Enter product name: ")
        prod_price = int(input("Enter product price: "))
        di[prod_name] = prod_price
    while True:
        entered_name = input("Enter product name to see price: ")
        if entered_name in di:
            print(f"The price is {di[entered_name]}")
        else:
            print("Not in dictionary")


def data_analyze():
    di = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
          {'name': 'Princess', 'phone': '555-3141', 'email': ''},
          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]
    for i in range(len(di)):
        dic = di[i]
        for key, val in dic.items():
            if key == 'phone' and val[-1] == "8":
                print(dic)
            if key == 'email' and val == '':
                print(dic)


def matrix_dict():
    matrix = [1, 2, 3, 3, 1,
              2, 4, 6, 8, 7,
              8, 8, 9, 7, 1,
              2, 4, 6, 9, 11,
              5, 7, 9, 11, 2]
    di = {}
    for i in matrix:
        key = i
        val = matrix.count(i)
        di.update({key: val})
    print(di)
