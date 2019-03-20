#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 04:01:34 2019

@author: john
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
       
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)
l2=ListNode(4)
l2.next=ListNode(5)
l2.next.next=ListNode(6)        
        
s1 = ""
s2 = ""

node=l1
while (not node==None):
    s1=str(node.val)+s1
    node=node.next

node=l2
while (not node==None):
    s2=str(node.val)+s2
    node=node.next

l=list(str(int(s1)+int(s2)))   
#print l
l3=ListNode(l.pop())
node = l3
for i in range(len(l)):
    node.next=ListNode(l.pop())
    node=node.next
    
node=l3
while (not node==None):
    print node.val
    node=node.next

