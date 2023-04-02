#!/usr/bin/python3

import sys
rsa = __import__('rsa').rsa

print("first")
with open(sys.argv[1]) as f:
    for line in f:
        rsa(line)

