#!/usr/bin/python3
import sys
n = len(sys.argv) - 1
if n != 0:
    print("{} {}:".format(n, "arguments"))
    for i in range(1, n+1):
        print("{}: {}".format(i, sys.argv[i]))
elif n == 0:
    print("{} {}".format(0,"arguments"))
