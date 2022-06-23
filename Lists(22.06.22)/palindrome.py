sentence = input()


def palindrome_check(line_):
    str_ = line_.replace(',', '')
    str_list = list(str_.split())
    for i in range(len(str_list)):
        if str_list[i] == str_list[len(str_list) - i - 1]:
            i += 1
        return True
    return False


print(palindrome_check(sentence))
