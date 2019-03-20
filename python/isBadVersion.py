#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:34:54 2019

@author: john
"""



#binary search-ish
#avg runtime/#of calls to isBadVersion is O(log(n))

class Solution: 
    
    def isBadVersion(self, x):
        self.version=[False, False, True, True, True, True, True]
        print("+1")
        return self.version[x]
    
    def findBadVersion(self, low, high):
        mid=int((low+high)/2)
        
        #midBadVersion=self.isBadVersion(mid)
        #print(low, mid, high, self.isBadVersion(mid))
        
        #works but could do less calls to isBadVersion
        #need to fix OBOB
        
        checkMid=self.isBadVersion(mid)
        
        if low==high:
            return low
        elif checkMid and self.isBadVersion(mid-1)==False:
            return mid
        elif checkMid:
            #print("go left", 0, mid)
            return self.findBadVersion(0, mid)
        else:
            #print("go right", mid, high)
            return self.findBadVersion(mid+1,high)
        
    def findBadVersionIter(self, l, r):
        
        
        while(l<=r):
            m=l+(r-l)/2
            if self.isBadVersion(m-1)==False and self.isBadVersion(m)==True:
                return m
            elif self.isBadVersion(m):
                #ignore right
                r=m-1
            else: l=m+1
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #mid=n/2
        return self.findBadVersionIter(0, 4)+1
        
        
        #midBadVersion=self.isBadVersion(mid)
        #if midBadVersion and not self.isBadVersion(mid-1):
        #    return mid
        
        #elif not midBadVersion:
        # search right
        #return ...
        
        #else:
        #search left
        #return ...
        
        #print "test"

s=Solution()
#print(s.isBadVersion(3))
print s.firstBadVersion(7)

