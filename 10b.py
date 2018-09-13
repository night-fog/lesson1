import sys


def is_str(value):
    try:
        if str(value):
            return True
    except ValueError:
        return False



def string_compare(str1: str, str2: str):
    if not is_str(str1) or not is_str(str2):
        return 0
    elif str1 == str2:
        return 1
    else:
        len_str1 = len(str1)
        len_str2 = len(str2)
        if len_str1 > len_str2:
            return 2
        if (len_str1 != len_str2) and ('learn' == str2):
            return 3
        else:
            return -1

str1, str2 = input('Enter two strings: ').split()
print(string_compare(str1, str2))
