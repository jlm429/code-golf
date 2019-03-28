#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 20:54:48 2019

@author: john
"""

class Solution:
    
    def kLargestElt(self, nums, k):
        #nums=sorted(nums)
        nums=self.mergeSort(nums, 0, len(nums))
        return nums[len(nums)-k]
        
    def mergeSort(self, nums, low, high):
        
        if len(nums[low:high])>1:
            mid=(low+high)//2
            self.mergeSort(nums, low, mid)
            self.mergeSort(nums, mid, high)
            
            #merge
            left=nums[low:mid]
            right=nums[mid:high]
            i=low
            while (len(left)>0 and len(right)>0):
                if left[0]<right[0]:
                    nums[i]=left.pop(0)
                else:
                    nums[i]=right.pop(0)
                i+=1
            
            while len(left)>0:
                nums[i]=left.pop(0)
                i+=1
            
            while len(right)>0:
                nums[i]=right.pop(0)
                i+=1
     
        return nums
    
        
            

s=Solution()
#nums=[1,3,4,5,6,1,2,3,4, 3]

nums = [3,2,3,1,2,4,5,5,6]
#print s.mergeSort(nums,0,len(nums))

#nums2=[1,2,3,4,5,1,2,3,4]
#print s.merge(nums2, 0, 5, 9)

print s.kLargestElt(nums, 4)