# -*- coding: utf-8 -*-

import sys

from lutz import mytimer

reps = 10000
reps_list = range(reps)

from math import sqrt


def for_loop():
    res = []
    for x in reps_list:
        res = sqrt(x)
    return res


def list_comp():
    res = []
    for x in reps_list:
        res = x ** .5
    return res


def map_call():
    res = []
    for x in reps_list:
        res = pow(x, .5)
    return res


if __name__ == '__main__':
    print(sys.version)
    for tester in (mytimer.timer, mytimer.best):
        print('<%s>' % tester.__name__)
        for test in (for_loop, list_comp, map_call):
            elapsed, ret = tester(test)
            print('-' * 35)
            print('{0}-9s: {1}.5f => {2}'.format (test.__name__, elapsed, ret))