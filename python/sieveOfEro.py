#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:39:14 2019

@author: john
"""
#import numpy as np

n=100

a=[]
a.append(False)
a.append(False)
for i in range(2, n):
    a.append(True)

for i in range(2, int(n*(1./2))):
    if a[i]==True:
        for j in range(i**2, n, i):
            a[j]=False
            
l=[]
for i in range(len(a)):
    if a[i]:
        print i
        l.append(0)

print len(l)
    
    