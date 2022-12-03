#!/usr/bin/python3
from add_0 import add


if __name__ == "__main__":
    """Print some of 1 and 2"""
    a = 1
    b = 2
#   c = add(a, b)
    print("{} + {} = {}".format(a, b, add(a, b)))
