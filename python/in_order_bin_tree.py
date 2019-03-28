#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 05:12:06 2019

@author: john
"""

class TreeNode: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
        
class Solution:
    
    def inorderTraversal(self, root):
        self.inorder_list=[]
        self.inorder(root)
        return self.inorder_list
    
        
    def inorder(self, node):
        if not node.left == None:
            self.inorder(node.left)
        self.inorder_list.append(node.data)
        if not node.right == None:
            self.inorder(node.right)
    
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
    
s = Solution()
print s.inorderTraversal(root)
    
    