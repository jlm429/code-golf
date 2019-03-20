#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:06:54 2019

@author: john
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        self.min=10000

    def push(self, x):
        self.stack.append(x)
        if x<=self.min:
            self.min=x
            self.minStack.append(x)

    def pop(self):
        if self.stack==[]:
            return
        temp=self.stack.pop()
        if not self.minStack==[]:
            temp2=self.minStack.pop()
            if temp!=temp2:
                self.minStack.append(temp2)

    def top(self):
        temp=self.stack.pop()
        self.stack.append(temp)
        return temp

    def getMin(self):
        if self.minStack==[]:
            temp=self.stack.pop()
            self.stack.append(temp)
        else:
            temp=self.minStack.pop()
            self.minStack.append(temp)
        return temp





# Your MinStack object will be instantiated and called as such:
#obj = MinStack()
#obj.push(6)
#obj.push(5)
#print obj.stack
#print "minstack=", obj.minStack
#obj.pop()
#param_3 = obj.top()
#param_4 = obj.getMin()
        
minStack = MinStack();
minStack.push(0);
minStack.push(1);
minStack.push(0);
print minStack.minStack, minStack.stack
print minStack.getMin();   #--> Returns -3.
minStack.pop();
#print minStack.top();      #--> Returns 0.
print minStack.getMin();   #--> Returns -2.
        

