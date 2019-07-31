#!/usr/bin/env python
# coding: utf-8

# In[32]:


import array as arr

def search(A,lowerBound,upperBound): 
    mid = int((upperBound + lowerBound)/2) 
    print("mid: ", mid, " A[mid]: ", A[mid], " lowerBound: ", lowerBound, " upperBound: ", upperBound) 
    if lowerBound == upperBound and A[mid] != mid : 
        print("NO. There is no element on A array such that A[i] = i.")
    if A[mid] == mid:
        print("There exist an element (", mid, "th element) of array A such that A[i] = i =", mid) 
    if A[mid] > mid : 
        search(A,lowerBound,mid) 
    if A[mid] < mid :
        search(A,mid + 1,upperBound)

A = arr.array("i", [-4, -2, -1, 0, 4, 6, 7])
search(A, 0, len(A));

