def f(lst):
    s = 0
    for num in lst:
        s += num
        
    return s

l = (1, 2, 3, 4)
print(f(l))