#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:43:38 2019

@author: john
"""


def groupAnagrams2(strs):
    

    #create hash of sorted values
    d={}
    for item in strs:
        d[str(sorted(item))]=[]
    
    #check each sorted elt and append to dict if match
    for item in strs:
        if str(sorted(item)) in d:
            d[str(sorted(item))].append(item)
    return d.values()
    

                        
                     
         
strs=["eat", "tea", "tan", "ate", "nat", "bat"]

print groupAnagrams2(strs)
                