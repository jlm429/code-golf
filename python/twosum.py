#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:39:11 2019

@author: john
"""
#import numpy as np
#l=[1,9,2,3,5,2,2]
#l=np.array(l)
#d={}
#target=11
#for i in range(len(l)):
#    if not l[i] in d:
#        d[l[i]] = i
#print d
#
#for i in range(len(l)):
#    if target-l[i] in d:
#        print("twosum found", i, d[target-l[i]])
#        break
    
    
    
    
#import numpy as np
l=[3,2,4]
#l=np.array(l)
d={}
target=6
for i in range(len(l)):
    if not l[i] in d:
        d[l[i]] = i
print d

#print 2 in d

for i in range(len(l)):
    print target-l[i]
    
    if target-l[i] in d:
        if not i==d[target-l[i]]:
            print("twosum found", i, d[target-l[i]])
            break
    