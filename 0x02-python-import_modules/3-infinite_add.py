#!/usr/bin/python3
import sys
argv = sys.argv
result = 0
if len(argv) == 1:
    print("{}".format(result))
else:
    for i in range(1, len(argv)):
        result += int(argv[i])
    print("{}".format(result))
