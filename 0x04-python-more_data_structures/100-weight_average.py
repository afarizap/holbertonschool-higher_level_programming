#!/usr/bin/python3
def weight_average(my_list=[]):
    sum2 = 0
    quot = 0
    for i in my_list:
        mul1 = 1
        quot += i[1]
        for j in i:
            mul1 *= j
        sum2 += mul1
    if not list or quot == 0:
        return 0
    res = sum2 / quot
    return res
