#!/usr/bin/python3

import sys
factorize = __import__('factorize').factorize

print("first")
with open(sys.argv[1]) as f:
    for line in f:
        factorize(line)
