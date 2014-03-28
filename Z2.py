a = ('a',1,17,-9)
b = ('b',7,38,16)
c = ('c',12,7,8)
d = [a,b,c]
y =0
z =0
for f in d:
    print (f[0],':',f[1],f[2],f[3])
    if f[2] > y:
        y = f[2]
        z = f
print ('Highest :' , y , 'in cortege' , z [0].upper(), z)