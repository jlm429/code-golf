#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 05:44:16 2019

@author: john
"""

s="pi"
s2="mississippi"

s=list(s)
s2=list(s2)

for i in range(len(s2)-len(s)+1):
    print s2[i:i+len(s)]
    if s2[i:i+len(s)]==s:
        print True