#!/usr/bin/python3
def no_c(my_string):
    strlist = list(my_string)
    for i in range(strlist.count('c')):
        strlist.remove('c')
    for i in range(strlist.count('C')):
        strlist.remove('C')
    str1 = ""
    return str1.join(strlist)
