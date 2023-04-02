#!/usr/bin/python3

check_prime = __import__('check_prime').check_prime

def rsa(number):
    num = int(number)
    if num % 2 == 0:
        if check_prime(num // 2) is True:
            print("{}={}*{}" .format(num, num // 2, 2))
    else:
        i = 3
        while i <= num // 2:
            if num % i == 0:
                if check_prime(num // i) is True:
                    print("{}={}*{}" .format(num, num // i, i))
                    return
            else:
                i += 2
