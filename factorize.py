#!/usr/bin/python3

def factorize(number):
    num = int(number)

    if num % 2 == 0:
        print("{}={}*{}" .format(num, num // 2, 2))
    else:
        i = 3
        while (num % i != 0):
            i += 2
        print("{}={}*{}" .format(num, num // i, i))
