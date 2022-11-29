#!/usr/bin/python3
def_removechar_at(str, n):
    if n >= 0:
        str = str[:n] + str[n + 1:]
    return str
