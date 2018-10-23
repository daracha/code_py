#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:32:28 2018

@author: dc
"""

a = [4,1,1,0,1,0]
b =[]
for i in a:
    if i%2 == 0:
        b.insert(0,i)
    else:
        b.append(i)
#print(b)
n = int(len(b)/2)
c = [None]*len(b)
#print (b[::2])
c[::2] = b[:n]
c[1::2] = b[n:]
print(c)