#!/bin/python 
p = open('bgp.conf',"a")
k = 0
l = 2
for i in range(1,450):
    p.write("protocol bgp bgp%s_1 { \n"%i)
    p.write("      import all;  \n")
    p.write("      export all;  \n")
    p.write("      local as %s;  \n"%str(i+2000))
    p.write("      neighbor 60.%s.%s.1 as 64513;\n"%(k,l))
    p.write("}\n")
    p.write("protocol bgp bgp%s_2 { \n"%i)
    p.write("      import all;  \n")
    p.write("      export all;  \n")
    p.write("      local as %s;  \n"%str(i+2000))
    p.write("      neighbor 60.%s.%s.2 as 64513;\n"%(k,l))
    p.write("}\n")

    if l == 255 :
        k = k+1
        l = 0
    else :
        l = l + 1
p.close()
