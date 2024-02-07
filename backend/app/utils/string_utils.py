# -*- coding: utf-8 -*-


# 双引号转单引号
def convert_double_to_single_quotes(s):
    lst = eval(s)
    return ",".join(f"'{i}'" for i in lst)


# 双引号转无引号
def convert_double_to_no_quotes(s):
    lst = eval(s)
    return ",".join(i for i in lst)


# 双引号转无引号(前拼and后拼=)
def convert_double_to_no_quotes_with_and_equal(s):
    lst = eval(s)
    return " ".join("and " + i + " = " for i in lst)


# 去除首尾空格
def trim(s):
    startIndex = -1
    endSpaceNum = 0
    for i in range(len(s)):
        if s[i] == " ":
            startIndex = i
            continue
        else:
            break
    for x in s[::-1]:
        if x == " ":
            endSpaceNum += 1
            continue
        else:
            break
    if startIndex + 1 >= len(s):
        return ""
    return s[startIndex + 1 : len(s) - endSpaceNum]


# 去除全部空格
def remove_spaces_and_newlines(s):
    return s.replace(" ", "").replace("\n", "")
