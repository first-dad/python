# -*- coding: utf-8 -*-
import math


def num(val):
    new = []
    for x in val:
        new.append(math.sqrt(x))
    return new

if __name__ == '__main__':
    val = [2, 4, 9, 16, 25]
    print(num(val))
    print(list(map(math.sqrt, val)))
    print([math.sqrt(a) for a in val])
    print([pow(a, .5) for a in val])
    print([a ** .5 for a in val])