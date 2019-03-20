#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 05:03:38 2019

@author: john
"""

#https://www.geeksforgeeks.org/given-linked-list-representation-of-complete-tree-convert-it-to-linked-representation/

# Python program to create a Complete Binary Tree from 
# its linked list representation 

# Linked List node 
class ListNode: 

		# Constructor to create a new node 
		def __init__(self, data): 
			self.data = data 
			self.next = None

# Binary Tree Node structure 


class BinaryTreeNode: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# Class to convert the linked list to Binary Tree 
class Conversion: 

	# Constructor for storing head of linked list 
	# and root for the Binary Tree 
    def __init__(self, data = None): 
		self.head = None
		self.root = None

    def push(self, new_data): 

		# Creating a new linked list node and storing data 
		new_node = ListNode(new_data) 

		# Make next of new node as head 
		new_node.next = self.head 

		# Move the head to point to new node 
		self.head = new_node 

    def convertList2Binary(self): 

		# Queue to store the parent nodes 
		q = [] 

		# Base Case 
		if self.head is None: 
			self.root = None
			return

		# 1.) The first node is always the root node, 
		# and add it to the queue 
		self.root = BinaryTreeNode(self.head.data) 
		q.append(self.root) 

		# Advance the pointer to the next node 
		self.head = self.head.next

		# Until th end of linked list is reached, do: 
		while(self.head): 

			# 2.a) Take the parent node from the q and 
			# and remove it from q 
			parent = q.pop(0) # Front of queue 

			# 2.c) Take next two nodes from the linked list. 
			# We will add them as children of the current 
			# parent node in step 2.b. 
			# Push them into the queue so that they will be 
			# parent to the future node 
			leftChild= None
			rightChild = None

			leftChild = BinaryTreeNode(self.head.data) 
			q.append(leftChild) 
			self.head = self.head.next
			if(self.head): 
				rightChild = BinaryTreeNode(self.head.data) 
				q.append(rightChild) 
				self.head = self.head.next

			#2.b) Assign the left and right children of parent 
			parent.left = leftChild 
			parent.right = rightChild 

    def inorderTraversal(self, root): 
        if(root): 
			self.inorderTraversal(root.left) 
			print root.data, 
			self.inorderTraversal(root.right) 


    #could join lists based on level (i.e. level 2 join 2 etc.)
    #seems like there is a better way
    def printTree(self,node):
        
        if node==[]:
            return
        
        else:
            #BFS
            list=[]
            temp_list=[]
            q = []
            q.append(node)
            while not q==[]:
                #print q[0].data
                #q.pop(0)
                node=q.pop(0)
                if node==-1:
                    if not temp_list==[]:
                        list.append(temp_list)
                        temp_list=[]
                else:
                    temp_list.append(node.data)
                    q.append(-1)
                    #if this was a graph, just loop all adjacent vertices
                    #btree loop not needed
                    if not node.left==None:
                        q.append(node.left)
                    if not node.right==None:
                        q.append(node.right)
        print list
        
    def printTree2(self,node, level, level_list):
        #DFS
        if node==None:
            return []
        
        else:
            level+=1
            level_list.append([])
            level_list[level].append(node.data)
            print node.data, level
            self.printTree2(node.left, level, level_list)
            self.printTree2(node.right, level, level_list)
            return level_list
                    
            
            

# Driver Program to test above function 

# Object of conversion class 
conv = Conversion() 
conv.push(36) 
conv.push(30) 
conv.push(25) 
conv.push(15) 
conv.push(12) 
conv.push(10) 

conv.convertList2Binary() 


#conv.inorderTraversal(conv.root) 

print("bfs")
conv.printTree(conv.root)
print("dfs")
level_list=[[]]
level_list= conv.printTree2(conv.root,0,level_list)
#not a very clean solution
level_list2=[]
for i in range(len(level_list)):
    if not level_list[i]==[]:
        level_list2.append(level_list[i])
print level_list2

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 


# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
