# -*- coding: utf-8 -*-


def num(y):
    if y <= 1:
        print(y, 'not prime')
    else:
        x = y // 2
        while x > 1:
            if y % x == 0:
                print(y, 'has factor', x)
                break
            x -= 1
        else:
            print(y, 'is prime')

if __name__ == '__main__':
    num(2687)
    num(1)
    num(21)
    num(-684)
    num(0)
    num(2455505)
    num(254)
    num(22.55)