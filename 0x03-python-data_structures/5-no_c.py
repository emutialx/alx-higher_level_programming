#!/usr/bin/python3
def no_c(my_string):
    new_str = list(my_string)
    for x in new_str:
        if x == 'c':
            new_str.remove('c')
        if x == 'C':
            new_str.remove('C')
    my_string = "".join(new_str)
    return my_string
