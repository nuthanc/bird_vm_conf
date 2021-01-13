#!/bin/python 
p = open('bfd.conf',"a")
k = 0
l = 2
p.write("protocol bfd bfd_1 {\n")
p.write("    interface \"eth1\" {\n")
p.write("      min rx interval 300ms;\n")
p.write("      min tx interval 400ms;\n")
p.write("      multiplier 3;  \n")
p.write("    };\n")
for i in range(2,450):
    p.write("    neighbor 60.%s.%s.1;\n"%(k,l))
    if l == 255 :
        k = k+1
        l = 0
    else :
        l = l + 1
p.write("}\n")
p.close()
