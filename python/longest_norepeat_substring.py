#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 05:44:59 2019

@author: john
"""
#find first occurence of char c and chop string
def chopString(l, c):
    for i in range(len(l)):
        if l[0]==c:
            l.pop(0)
            return l
        else:
            l.pop(0)
    return l
            


#s="bbtablud"
#s="dvdf"
#s="pwwkew"
#s="pwwkew"
#s="ohvhjdml"
#s="abcabcbb"

#d={}
l=[]
max_len=0
temp_max=0
for i in range(len(s)):
    #print s[i], len(d), i-len(d)
    if not s[i] in l:
        l.append(s[i])
        
    #first one added is dup - remove and don't inc temp_max
    #this needs to be more general (catch if not first only)
    #elif d[s[i]]==i-len(d): 
    #    del d[s[i]]
    #    d[s[i]]=i
    
    #else chop front of string up to current letter and append
    else: 
        chopString(l, s[i])
        l.append(s[i])
    if len(l)>max_len:
        max_len=len(l)
        
print max_len, l
    