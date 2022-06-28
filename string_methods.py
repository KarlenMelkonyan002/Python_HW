"""Function to replace given old string with new string in source """


def replace_str(source, old, new):
    for i in range(len(source)):
        if old == source[i:i + len(old)]:
            source = source[:i] + new + source[i + len(old):]
    return source


# print(replace_str('C++ is better than every programming language', 'C++', 'Python'))

"""This function splits string with given seperator and returns list containing split elements(needs corrections 
does not work correctly)"""


def split_str(source, sep):
    res = []
    res_str = ''
    for i in range(len(source)):
        if sep == source[i:i + len(sep)]:
            res_str += source[:i]
            res.append(res_str)
            res_str = ''
            res_str += source[i + len(sep):]
            res.append(res_str)
            res_str = ''
    return res


print(split_str('welcome the to the  jungle', 'the'))

"""This function takes list as an argument and seperator we need to join list members with seperator in empty 
string and return it """


def join_str(data, sep):
    res = ''
    for elem in data:
        res += elem + sep
    return res

# print(join_str(['Python', 'is', 'a', 'fun', 'programming', 'language'], '  '))
