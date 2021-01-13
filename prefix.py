#!/bin/python 
p = open('prefix_add_91.conf',"a")
k = 0
l = 2
for i in range(2,100):
    p.write("        route 91.%s.%s.0/24 reject; \n"%(k,l))
    if l == 255 :
        k = k+1
        l = 0
    else :
        l = l + 1
p.close()
