#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:58:34 2019

@author: john
"""

#bf solution O(len(n))
#optimized? ... 


#BF solution
i=00000000000000000000000000001011
#print i
i=list(str(00000000000000000000000000001011))
count=0
for item in i:
    if item=="1":
        count+=1
#print count

#optimized
n=100011
count=0
for i in range(len(str(n))):
#while i>0:
    #print i & 1
    count+= n & 1
    n=n>>1
#    print i
print count



 