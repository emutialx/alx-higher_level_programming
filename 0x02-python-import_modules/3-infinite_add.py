#!/usr/bin/python3
import sys
if __name__ == __"main"__:
    sum = 0
    n = len(sys.argv)
    for i in range(1, n):
        sum += int(sys.argv[i])
    print(sum)
