#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:11:23 2019

@author: john
"""
d={}
nums=[2,2,1,1,1,2,2]
maj_elt = len(nums)//2
#print "maj_elt=", maj_elt

for i in range(len(nums)):
    if not nums[i] in d:
        d[nums[i]]=1
    else:
        d[nums[i]]+=1
        if d[nums[i]] > maj_elt:
            print "majority elt", nums[i]

print d
    