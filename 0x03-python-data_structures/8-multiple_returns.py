#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = tuple(sentence)
    len_tuple = len(my_tuple)
    first_char = my_tuple[0]
    return len_tuple, first_char
