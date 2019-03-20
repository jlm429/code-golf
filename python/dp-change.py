#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 06:55:56 2019

@author: john
"""

class Solution:
    def coinChange(self, coins,  amount):
        table = []
        table.append(0)
        
        for i in range(1, amount+1):
            table.append(1000)
        
        for i in range(1, amount+1):
            for j in range(0, len(coins)):
                if coins[j] <= amount:
                    sub_res=table[i-coins[j]]
                    if sub_res !=1000 and sub_res+1< table[i]:
                        table[i]=sub_res+1
        return table[amount]

if __name__=="__main__":
    s = Solution()
    print s.coinChange([1,5,10,25], 100)
    