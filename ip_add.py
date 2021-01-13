#!/bin/python 
p = open('ip_add.conf',"a")
k = 0
l = 2
for i in range(2,450):
    p.write("ip addr add 60.%s.%s.100/32 dev eth1.%s \n"%(k,l,i))
    if l == 255 :
        k = k+1
        l = 0
    else :
        l = l + 1
p.close()
