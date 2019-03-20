#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:17:53 2019

@author: john
"""

#l1="abcdbbfcba"
l1="aacdefcaa"
#l1="babad"
#l1="abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
#ugliest code ever
l1=list(l1)
print "test", l1[::-1]
l2=[]
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
print l2
print list(l1)

max=0
sub_max=0
inc=0
max_pal=[]
#bruteforce is O(n^3)
for i in range(len(l1)):
    for j in range(len(l2)):
        inc=0
        sub_max=0
        sub_max_p=0
        temp_value=[]
        print "check12", temp_value
        temp_pal=[]
        rev=l2[j:j+inc+1]
        while i+inc<len(l1) and j+inc<len(l2) and l1[i+inc]==l2[j+inc]:
            sub_max+=1
            temp_value.append(l1[i+inc])
            #rev=l2[j:j+inc+1]
            #rev=rev[::-1]
            rev=temp_value[::-1]
            print "temp_value", temp_value
            if temp_value==rev and sub_max>max:
                #print "l1, rev", l1[i:i+inc+1], rev
                print "temp_value, rev", temp_value, rev
                sub_max_p=sub_max
                print "sub_max=", sub_max
                temp_pal=rev
            inc+=1
        if len(temp_pal)>max:
            max=sub_max_p
            max_pal=temp_pal
print max_pal
print max
            
    
