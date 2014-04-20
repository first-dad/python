# -*- coding: utf-8 -*-


def adder1(*args):
    x = args[0]
    for arg in args[1:]:
        x += arg
    print(x)


def adder2(**args):
    args = list(args.keys())
    x = args[0]
    for arg in args[1:]:
        x += arg
    print(x)


def adder3(**args):
    args = list(args.values())
    x = args[0]
    for arg in args[1:]:
        x += arg
    print(x)


def adder4(**args):
    print(adder1(*args.values()))
if __name__ == '__main__':
    adder1(5, 5), adder1('df', 'dfsa', 'fs')
    adder2(a=5,b=2), adder2(a='df', b='dfsa', c='fs')
    adder3(a=5,b=2), adder3(a='df', b='dfsa', c='fs')
    adder4(a=5,b=2), adder4(a='df', b='dfsa', c='fs')