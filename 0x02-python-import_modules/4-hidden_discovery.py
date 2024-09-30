#!/usr/bin/python3
import dis
import sys


def main():
    if len(sys.argv) < 2:
        module_name = "hidden_4"
    else:
        module_name = sys.argv[1]

    module = __import__(module_name)

    names = dir(module)

    for name in sorted(names):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    main()
