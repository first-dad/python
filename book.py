# -*- coding: utf-8 -*-


# Инструкции циклов вместо рекурсии. стр.540


'''
L = [1,2,3,4,5]
sum = 0
while L:
    sum += L[0]
    L = L[1:]
print (sum)
'''

'''
L = [1,2,3,4,5]
sum = 0
for x in L: sum += x
print (sum)
'''


'''
def sumtree(L):
    tot = 0
    for x in L:            # Обход элементов одного уровня
        if not isinstance(x,list):
            tot += x       # Числа суммируются непосредственно
        else:
            tot += sumtree(x)     # Списки обрабатываются рекурсивными вызовами
    return tot
L = [1,[2,[3,4],5],6,[7,8]]
print (sumtree(L))
'''


