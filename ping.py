#!/bin/python 
p = open('aap.conf',"a")
k = 0
l = 2
for i in range(2,450):
    p.write("ping 60.%s.%s.100 -c 10 -i 0.02 \n"%(k,l))
    if l == 255 :
        k = k+1
        l = 0
    else :
        l = l + 1
p.close()
