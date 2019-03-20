#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:25:44 2019

@author: john
"""

x = -431
print x
s = str(x)
l = list(s)
neg=False
if l[0]=='-':
    neg=True
    l.pop(0)

l2 = []

for i in range(len(l)):
    l2.append(l.pop())

s2=""
for i in range(len(l2)):
    s2 = s2+l2[i]

if neg:
    if int(s2)>2**31:
        print 0
    s2='-'+s2

elif int(s2)>(2**31)-1:
    print 0

print int(s2)

