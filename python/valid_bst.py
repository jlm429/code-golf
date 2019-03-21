#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:57:40 2019

@author: john
"""

class TreeNode: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.val = data 
		self.left = None
		self.right = None
    
class Solution:
    
        def checkValidBST(self, node, Min, Max):
            
            #base case node=none
            if node==None:
                return True
            if not Min==None and node.val <= Min:
                return False
            if not Max==None and node.val >= Max:
                return False
            if (not self.checkValidBST(node.left, Min, node.val)) or (not self.checkValidBST(node.right, node.val, Max)):
                return False
            return True
            

root = TreeNode(2)
root.left = TreeNode(1)
#root.right = TreeNode(6)
s = Solution()
print s.checkValidBST(root, None, None)