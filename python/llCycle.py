#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:10:15 2019

@author: john
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
head=ListNode(1)
head.next=head
#head.next.next=head
#head.next.next=ListNode(0)
#head.next.next.next=ListNode(4)
#head.next.next.next.next=head.next

fast=head
slow=head
while(not fast==None and not fast.next==None):
    fast=fast.next.next
    slow=slow.next
    if fast==slow:
        print True
        break

