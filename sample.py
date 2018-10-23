#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:35:24 2018

@author: dc
"""
grid = [[1,0],[0,2]]
top = 0
front = 0
for i in grid:
    top += len(i)
    front += max(i)

ziped = list(zip(*grid))
side = 0
for i in range(len(ziped)):
    side += max(ziped[i])
print (top+front+side)