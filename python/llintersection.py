#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:54:54 2019

@author: john
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

#class Solution(object):
    #def __init_(self):

l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l2=ListNode(4)
l2.next=l1.next
l2.next.next=l1.next.next 

 
d={}

#hash first list
node=l1
while (not node==None):
    d[node] = node.val
    node=node.next

#check for intersection
node=l2
while (not node==None):
    if node in d:
        #return node
        print node.val
    node=node.next

#return no_intersection


    
    
        