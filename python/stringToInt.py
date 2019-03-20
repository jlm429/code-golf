#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:50:41 2019

@author: john
"""


s="   3.14159"
s=list(s)

#trim whitespace
while (s[0]==' '):
    s.pop(0)
    
#check sign
neg=False
if s[0]=='-':
    neg=True
    s.pop(0)

#check if first non-whitespace is digit
if not s[0].isdigit():
    print "return False"

#get int
s2=[]
for i in range(len(s)):
    if not s[i].isdigit():
        break
    else:
        s2.append(s[i])

#to string
s=""
for i in range(len(s2)):
    s=s+s2[i]

#check for overflow
#INT_MAX (231 − 1) or INT_MIN (−231) 
i=int(s)
if neg:
    if i> (2**31):
        print "overflow"
    i=i*-1

elif i> (2**31)-1:
    print "overflow"

print i
    

    