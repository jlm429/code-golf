#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:47:07 2019

@author: john
"""

import numpy as np
#too slow - looking for O(n) solution
nums=[1, -3, 4, -2, 9]
nums=np.array(nums)

#dp=np.full((len(l), len(l)), None)

#print l


#################
#for i in range(len(l)):
#    j=0
#    while j<=i:
#        if i==j:
#            dp[i][j]=l[i] 
#        elif i>0 and j<i:
#            dp[i][j]=l[i]+dp[i-1][j]
#        j+=1
#        #    dp[i][j]=l[i]+dp[i][i-1]
#####################

import sys
max_value=-sys.maxint
consec_value=0
for item in nums:
    if consec_value+item>=item:
        consec_value=item+consec_value
    else:
        consec_value=item
    max_value=max(consec_value, max_value)
      
print max_value
#print dp
#dp[3][4]=5
#print int(dp.max())
            