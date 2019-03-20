#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:11:13 2019

@author: john
"""

l="ccd"
l=list(l)
list.reverse(l)
l2=[]
#print l


#d={}
#preprocess nums in hash table for O(1) lookup
#for i in range(len(l)):
#    if not l[i] in d:
#        d[l[i]]=i

#print d
for i in range(len(l)):
    temp=l.pop()
    #l.pop(0)
    if not temp in l and not temp in l2:
        print i
    else:
        l2.append(temp)

#return -1