#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for y in range(x):
        try:
            print(f"my_list[i]", end="")
            count += 1
        except Exception as e:
            break
    print()
    return(count)
