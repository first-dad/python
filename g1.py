import os
mo = {'name':'suzen','age':41,'parent':None}
son = {'name':'alex','age':8,'parent':mo}
mo ['child'] = son

for a in mo:
    print (a, 'value :',mo[a])
