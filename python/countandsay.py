#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 04:26:00 2019

@author: john
"""

def countSay(l):
    #l=[1]
    l2=[]
    count=1
    for i in range(len(l)-1):
        if not l[i+1]==l[i]:
            l2.append(count)
            l2.append(l[i])
            count=1
        else:
            count+=1
    #add the last elt
    if l[len(l)-2]==l[len(l)-1]:
        l2.append(count)
        l2.append(l[len(l)-1])
    else:
        l2.append(1)
        l2.append(l[len(l)-1])
    return l2

def genCountSay(n):
    
    if n==1:
        return [1]
    
    else:
        l=genCountSay(n-1)
        return countSay(l)
    
l= genCountSay(6)
print l
s=""
for i in range(len(l)):
    s=s+str(l[i])
print s

    