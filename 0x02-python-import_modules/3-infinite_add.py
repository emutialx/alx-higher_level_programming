#!/usr/bin/python3
import sys
if __name__ == __"main"__:
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
    print("{}".format(sum))
