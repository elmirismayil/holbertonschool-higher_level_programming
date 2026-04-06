#!/usr/bin/python3
def uniq_add(my_list=[]):
    u = []
    s = 0
    for i in my_list:
        if i not in u:
            s += u
            u.append(i)
    return s
