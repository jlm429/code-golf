#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 06:17:34 2019

@author: john
"""

def longestCommonPrefix(strs):
    
    if strs==[]:
        return ""
    elif len(strs)==1:
        return strs[0]
    
    s=""
    #get len of shortest string or return "" if any are empty
    min_len=len(strs[0])
    for item in strs:
        if item=="":
            return s
        elif len(item)<min_len:
            min_len=len(item)

    #build s and terminate early at first mismatch
#    for i in range(min_len):
#        if strs[0][i]==strs[1][i] and strs[0][i]==strs[2][i]:
#            s=s+strs[0][i]
#        else:
#            return s
    for i in range(min_len):
        for j in range(len(strs)-1):
            if not strs[j][i]==strs[j+1][i]:
                return s
        s=s+strs[j][i]
    
    return s

strs=["flower","flow","flight"]
s=""
#strs=["dog","racecar","car"]
print longestCommonPrefix(strs)

    