#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:19:24 2019

@author: john
"""

import numpy as np
#too much mem - looking for non-table solution
prices=[7,1,5,3,6,4]
prices=np.array(prices)

#dp=np.full((len(prices), len(prices)), 0)

#print l
max_trade=0
for i in range(len(prices)):
    j=0
    while j<i:
        #if i==j:
        #    dp[i][j]=0
        if i>0 and j<i:
            temp=prices[i]-prices[j]
            if temp>max_trade:
                max_trade=temp
                
            #dp[i][j]=prices[i]-prices[j]
        j+=1
#################
#for i in range(len(prices)):
#    j=0
#    while j<=i:
#        if i==j:
#            dp[i][j]=0
#        elif i>0 and j<i:
#            dp[i][j]=prices[i]-prices[j]
#        j+=1
#        #    dp[i][j]=l[i]+dp[i][i-1]
#####################
        
#temp=dp.max()
#if temp<0:
#    print 0
#else: 
#    print dp.max()
        
        
print max_trade