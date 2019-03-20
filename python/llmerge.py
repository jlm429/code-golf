#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:44:20 2019

@author: john
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

#1->2->4, 1->3->4
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(4)

l2=ListNode(1)
l2.next=ListNode(3)
l2.next.next=ListNode(4)

#node1=l1
#node2=l2

#set head
if l1.val < l2.val:
    head=l1
    node1=l1.next
    node2=l2
else:
    head=l2
    node1=l1
    node2=l2.next
    
node=head
while(not node1==None):
    if not node2==None and node2.val<node1.val:
        node.next=node2
        node2=node2.next
    else:
        node.next=node1
        node1=node1.next
    node=node.next

#append the rest of node2 if any
while (not node2==None):
    node.next=node2
    node2=node2.next
    node=node.next

node=head
while (not node==None):
    print node.val
    node=node.next
