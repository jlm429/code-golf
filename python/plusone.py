#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:59:35 2019

@author: john
"""
    
def plus_one(l):

    last=len(l)-1
    if l[last]<9:
        l[last]+=1
    else:
        #l[last]=0
        for i in range(last, -1, -1):
            if l[i]<9:
                l[i]+=1
                return l
            else:
                l[i]=0
                if i==0: 
                    l.insert(0, 1)
    return l
        
l=[9,9,9,9,9]
print plus_one(l)
