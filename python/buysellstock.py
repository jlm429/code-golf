#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 03:51:56 2019

@author: john
"""
class Solution(object): 
    def __init__(self, p):
        self.p=p
        self.profit=0
        self.buy_day=None
    
    
    def sell_stock(self, sell_day):
        if self.buy_day==None:
            return 0
        else:
            profit=self.p[sell_day]-self.p[self.buy_day]
            self.buy_day=None
            return profit
        
    def buy_stock(self, buy_day):
        if not self.buy_day==None:
            return
        else:
            self.buy_day=buy_day
            
    def sim(self):
        for i in range(len(p)-1):
            if self.p[i+1]>self.p[i]:
                self.buy_stock(i)
                print("buy_stock, value, profit", self.buy_day, p[i], self.profit)
            elif self.p[i+1]<self.p[i]:
                self.profit+=self.sell_stock(i)
                print("sell_stock, value, profit", self.buy_day, p[i], self.profit)
            
            if len(self.p)-1==i+1: #last day / sell
                self.profit+=self.sell_stock(i+1)
                print("last day, sell", p[i+1])
                
        return self.profit

p=[7,6,4,3,1]
s=Solution(p)
print("profit=", s.sim())


                

            
    