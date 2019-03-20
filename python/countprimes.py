#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:19:56 2019

@author: john
"""

#BF solution:
#O(n) - check if num is div by any number (2-10) except itself

#seems like there is an easier/cleaner way

def isPrime1(x):
    if x==1:
        return False
    for i in range(2,10):
        #print i
        if i != x:
            temp =float(x) / i
            #print(i, "{0:.2f}".format(temp))
            #print temp % 1
            #check for fractional component
            if temp % 1==0.0: #won't always work
                return False
    return True

#slowest solution possible
def checkMod(x):
    if x==1:
        return False
    for i in range(2,10):
        if x % i==0 and i!=x:
            return False
#    for i in range(2,x):
#        if x % i==0 and i!=x:
#            return False
    
    return True

#slowest solution possible
def isPrime(x):
    if x==1:
        return False
#    for i in range(2,10):
#        if x % i==0 and i!=x:
#            return False
    for i in range(2,x):
        if x % i==0 and i!=x:
            return False
    
    return True

import fractions

def subf(x,n):
    r=(((x**2)+1) % n)
    return r

def pollard_rho(n):
    if n==2:
        return -1
    
    x=2
    y=2
    d=1
    while d==1:
        x=subf(x,n)
        y=subf(subf(y,n),n)
        d=fractions.gcd(abs(x-y), n)
    if d==n:
        return -1
    else:
        return d
#
#print pollard_rho(21)
#print "blah", fractions.gcd(21,7)
#
##import math
##z= math.log(243, 3)
##print z, int(z)
##print z % 1==0
#
#
#
#x=100
###print isPrime2(7)
###print checkDiv(9)
##
#l=[]
#for i in range(2,x):
#    #print i, pollard_rho(i)
#    if i!=1:
#        if i==2:
#            l.append(i)
#        elif i%2!=0:
#            if pollard_rho(i)==-1:
#                l.append(i)
#        
#print l
#print len(l)
#    
#  

l=[]
l2=[]
x=1000
for i in range(2,x):
#    if isPrime(i):
#        l.append(i)
    if i %100000==0:
        print i
    if pollard_rho(i)==-1 and checkMod:
        if isPrime(i):
            l2.append(i)
#    if i<10 and isPrime(i):
#        l.append(i)
#    elif isPrime(i) and pollard_rho(i)!=1:
#        l.append(i)

#print l
print len(l), len(l2)
