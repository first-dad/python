def mt (**params):
    fgcolor = params.pop('fgcolor',"black")
    if params:
        raise TypeError ("nety %" % list (params))
    print (fgcolor)
print (mt(fgcolor = 'white'))