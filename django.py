# coding: utf-8
count_world = 0
count_end = 0
line_change = ''
for line in open('text.txt'):
    count_world += line.count('Django')
    line_strip = line.strip()
    if line_strip.endswith(':'):
        count_end += 1
    line_change += line.replace('Django','{0}')
print ('количество вхождений Django: %s' % (count_world))
print ('количество вхождений \':\' : %s' % (count_end))
print (line_change.format('Django 1.6'))