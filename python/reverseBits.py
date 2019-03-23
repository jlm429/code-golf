#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:49:49 2019

@author: john
"""

def reverseBits(self, n):
    n2=0
    for i in range(31, -1, -1):
        n2 = n2 | (n&1) << i
        n=n>>1
    return n2