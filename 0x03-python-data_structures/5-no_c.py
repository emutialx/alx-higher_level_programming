#!/usr/bin/python3
def no_c(my_string):
    new_str = list(my_string)
    for x in new_str:
        if x == 'c':
            new_str.remove('c')
        if x == 'C':
            new_str.remove('C')
    my_string = "".join(l)
    return my_string
