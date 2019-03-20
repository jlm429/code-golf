#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:05:27 2019

@author: john
"""
#power of 3 = base is 3 (is this obvious to everyone?)
x=243
#x= y**(1./3)
#print x
#x=list(str(x))
#x=int(x.pop(0)) #fix this x>1 digit
##x=x.pop(0)
##x.pop(0)
##x=x.pop(0)
##x = ''.join(x)
##x=int(x)
#print x
#
#if x**3==y:
#    print True
#else: print False

#if int(x)==0:
#    print True
#else: print False
#print 3**4
import math
y= math.log(x,3)
z=y%1
print y
print "y%1", y % 1
if y % 1>0:
    print False
else:
    print True
#print "len=", len(y)
#BF Solution
for i in range(x):
    #print i
    if (3**i)==x:
        print True
    elif (3**i)>x:
        break

#
