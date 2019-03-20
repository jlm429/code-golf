#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:42:16 2019

@author: john
"""
#nums1 = [1,2,2,1]
#nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

#nums1.remove(2)
#print nums1

#l = nums1
l=[]
#d={}
#preprocess nums in hash table for O(1) lookup
#count=0
#for i in range(len(nums1)):
    #if not nums1[i] in d:
#    d[nums1[i]]=i

#print d

#BF solution
for i in range(len(nums2)):
    if nums2[i] in nums1:
        l.append(nums2[i])
        nums1.remove(nums2[i])

print l