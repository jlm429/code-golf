#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:20:28 2019

@author: john
"""

def zero_out(is_row, n, m):
    if is_row:
        for i in range(len(m[0])):
            m[n][i]=0
    else:
        for i in range(len(m)):
            m[i][n]=0
            
m=[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

m=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

cols=[]
rows=[]

for i in range(len(m)):
    for j in range (len(m[0])):
        if m[i][j]==0:
            if not i in rows: 
                rows.append(i)
            if not j in cols:
                cols.append(j)

for i in range(len(cols)):
    zero_out(False, cols[i], m)

for i in range(len(rows)):
    zero_out(True, rows[i], m)

print m


