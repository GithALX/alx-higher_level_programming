#!/usr/bin/python3
import calculator_1
import sys
argv = sys.argv
if __name__ == "__main__":
    if len(argv) == 4:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
            sys.exit(0)
        elif argv[2] == '-':
            print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
            sys.exit(0)
        elif argv[2] == '*':
            print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
            sys.exit(0)
        elif argv[2] == '/':
            print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
