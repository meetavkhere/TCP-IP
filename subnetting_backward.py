# PROGRAM FOR SUBNETTING BACKWARD APPROACH

import os
import numpy
import sys
import math

host_add = raw_input("Enter the HOST/Network address in dotted Decimal : ")
# calculating netmast 
parts = host_add.split(".")
if len(parts)!=4:
    print("Invalid IP Address!!")
    sys.exit()
for y in parts:
    y=int(y)
    if(y>255)or(y<0):
        print("Invalid IP Address!!")
        sys.exit()

part = list()
for i in range(0,len(parts)):
    part.append(int(parts[i]))
if part[0]<128:
    itsclass= 'A'
    part[1]=255
    part[2]=255
    part[3]=255
    netmask = 8
elif part[0]<192:
    itsclass = 'B'
    part[2]=255
    part[3]=255
    netmask = 16
elif part[0]<223:
    itsclass = 'C'
    part[3]=255
    netmask = 24
    
submask = int(input("\nEnter Netmask for sub.supernet "))
subnets = pow(2,submask-netmask)
print("\nPrinting addresses for each subnet :\n")
add_per_subnet = pow(2,32-submask)

for i in range(0,subnets):
    print("\n"+str(part[0])+'.'+str(part[1])+'.'+str(part[2])+'.'+str(part[3]-(add_per_subnet-1)))
    
    print("TO")
    print(str(part[0])+'.'+str(part[1])+'.'+str(part[2])+'.'+str(part[3]))
    part[3]= part[3]-add_per_subnet
    if part[3]==0:
        part[2]=part[2]-1
        part[3]=255
    
        
print("\n\nSubnets = "+str(subnets))
    


