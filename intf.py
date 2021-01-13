#!/bin/python 
p = open('intf.conf',"a")
k = 0
l = 250
for i in range(250,450):
    p.write("auto eth1.%s\n"%(i))
    p.write("iface eth1.%s inet static\n"%(i))
    p.write("address 60.%s.%s.4/24\n"%(k,l))
    p.write("\n")
    if l == 255 :
        k = k+1
        l = 0
    else :
        l = l + 1
p.close()
