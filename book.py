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


# Косвенный вызов функции

'''
def echo(message):
    print (message)
'''


'''
schedule = [(echo,'Spam!'),(echo,'Ham!')]
for (func,arg) in schedule:
    func (arg)
'''


'''
def make(label):
    def echo(message):
        print (label +':'+ message)
    return echo
F = make('Spam!')
F('Ham!')
'''

if __name__ == '__main__':
'''
    from tkinter import Button, mainloop
    L = input('Write a few digits after the comma:').split(',')
    n=1
    while n < len(L):
        for i in range(len(L)-n):
            if L[i] > L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
        n += 1
    L = list(map(float,L))
    x = Button(
        text = 'Press me, if you will want to see result',
        command = (lambda : print(L)))
    x.pack()
    mainloop()
'''
