#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:50:16 2019

@author: john
"""

class TreeNode: 

	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
        


class Solution:
    #not a very clean solution
    def levelOrder(self, root):
        level_list=self.getLevelList(root, 0, [[]])
        level_list2=[]
        for i in range(len(level_list)):
            if not level_list[i]==[]:
                level_list2.append(level_list[i])
        return level_list2
        
        
    def getLevelList(self,node, level, level_list):
        #there is a better solution than using this POS 
        if node==None:
            return None
        
        else:
            level+=1
            level_list.append([])
            level_list[level].append(node.data)
            #print node.data, level
            self.getLevelList(node.left, level, level_list)
            self.getLevelList(node.right, level, level_list)
            return level_list
    
    def printLevelDFS(self,node, level):
        if node==None:
            return None
        
        else:
            level+=1
            print node.data, level
            self.printLevelDFS(node.left, level)
            self.printLevelDFS(node.right, level)
            #return level_list
    
    def DFS(self, node, x):
        if node==None:
            return False
        elif node.data==x:
            return True
        elif self.DFS(node.left, x) or self.DFS(node.right, x):
                return True
        else: 
            return False
        
    def BFS(self,node, x):
        
        if node==[]:
            return
        
        else:
            #BFS
            q = []
            q.append(node)
            while not q==[]:
                node=q.pop(0)
                if node.data==x:
                    return True
                if not node.left==None:
                    q.append(node.left)
                if not node.right==None:
                    q.append(node.right)
        return False
    
    def checkSym(self, l):
        for level in l:
            if len(level)>1:
                for i in range(len(level)/2):
                    if not level[i]==level[len(level)-i-1]:
                        return False
        return True
    
    def checkSym2(self, node1, node2):
        if node1==None and not node2==None:
            return False
        elif node2==None and not node1==None:
            return False
        elif node1==None and node2==None:
            return True
        elif not node1.data==node2.data:
            return False
        elif self.checkSym2(node1.left, node2.right)==False or self.checkSym2(node1.right, node2.left)==False:
            return False
        else: 
            return True

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
#root.left.right=TreeNode(4)
root.right.left=TreeNode(3)
#root.right.right=TreeNode(2)

solution = Solution()
#print solution.printLevelDFS(root,0)
l=solution.levelOrder(root)
print solution.checkSym2(root.left, root.right)
#for each level make sure is the same forward/backward
