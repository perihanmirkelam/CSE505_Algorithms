#!/usr/bin/env python
# coding: utf-8

# In[32]:


import sys
  
# Calculated max sum is maximum of three cases. 
# 1. Calculate right half and left half recursively.
# 2. Plus calculate sub array(first time whole array) 
# include middle point and its both side of sum 
def calcMaxSubArraySum(arr, left, right) : 

    if (left == right) : 
        return arr[left] 
  
    mid = int((left + right) / 2)
    
    leftside = calcMaxSubArraySum(arr, left, mid)
    rightside = calcMaxSubArraySum(arr, mid+1, right)
          
    #calculate max sum of left and right side of mid
    temp_left = 0 
    left_sum = -sys.maxsize
      
    for i in range(mid, left-1, -1) : 
        temp_left = temp_left + arr[i] 
        left_sum = max(left_sum, temp_left)
      
    temp_right = 0
    right_sum = -sys.maxsize
    for i in range(mid + 1, right + 1) : 
        temp_right = temp_right + arr[i]  
        right_sum = max(right_sum, temp_right)
      
    centered = left_sum + right_sum;
  
    return max(leftside, rightside, centered)               
  
A = [5, -6, 6, 7, -6, 7, -4, 3]   
maxSum = calcMaxSubArraySum(A, 0, len(arr)-1) 
print("Max sum of subset is: ", maxSum) 

