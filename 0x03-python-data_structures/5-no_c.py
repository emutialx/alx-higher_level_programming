#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    for i in range(len(str_list)):
            if str_list[i] == 'c' or str_list[i] == 'C':
                del str_list[i]
                str_list1 = "".join(str_list)
                return str_list1
