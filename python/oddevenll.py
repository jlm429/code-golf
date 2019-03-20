#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:34:27 2019

@author: john
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(6)

#node=head
#while (not node==None):
#    print node.val
#    node=node.next
    

head_odd=head
head_even=head.next
node1=head_odd
node2=head_even
while (not node1.next==None and not node1.next.next==None):
    node1.next=node1.next.next
    node2.next=node2.next.next
    node1=node1.next
    node2=node2.next
    

node1.next=head_even
#node.next=head_even

#return head_odd

node=head_odd
while (not node==None):
    print node.val
    node=node.next

    

