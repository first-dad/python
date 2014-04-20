# -*-coding: utf-8 -*-


def copyDict(old_dict):
    new_dict = {}
    for key in old_dict.keys():
        new_dict[key] = old_dict[key]
    return new_dict


def addDict(d1, d2):
    new_dict = {}
    for key in d1.keys():
        new_dict[key] = d1[key]
    for key in d2.keys():
        new_dict[key] = d2[key]
    return new_dict

if __name__ == '__main__':
    print(copyDict({1: 1, 2: 2}))
    print(addDict({1: 1, 2: 2},{2: 2, 4: 4}))