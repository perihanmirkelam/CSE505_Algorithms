#!/usr/bin/env python
# coding: utf-8

# In[18]:


import array as arr

def printPath(path) :
    print("Stayed Hotels: ")
    print("->", path[0])
    for i in range(1, len(path)):
        if (path[i]!=0 and path[i] != path[i-1]):
            print("->", path[i])

def findBestRoute(A) :
    OPT = [] #optimal route to reach ith index hotel
    OPT.append(0) # starting point
    upperBound = A[len(A) -1]
    upperBound = upperBound * upperBound
    A = [0] + A
    PATH = [0] * len(A)
  
    for i in range (1, len(A)):
        tempOpt = upperBound
        #print("--------------------")
        #print("tempOpt: ", tempOpt)
        #print(" ")

        for j in range (0, i):
            #print("loop i:", i, "j:", j)
            #print(" ")
            delta = 200 - (A[i] - A[j])
            penalty = delta * delta
            #print("A[i]:", A[i], "A[j]:", A[j], "(A[i] - A[j]):",  A[i] - A[j], "delta:", delta, "penalty: ", penalty)
            #print ("OPT[j]:", OPT[j], "+ penalty:", penalty, "=", OPT[j] + penalty, "tempOpt:", tempOpt)
            #print(" ") 
            
            if(OPT[j] + penalty < tempOpt):
                tempOpt = OPT[j] + penalty
                PATH[i-1] = A[j] 
                
        OPT.append(tempOpt)
        #print("PATH:", PATH)
    print("Optimal penalties to reach each it order hotels:",OPT)
    PATH[len(A) - 1] = A[len(A) - 1]
    return PATH
        

A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]
printPath(findBestRoute(A))


# In[ ]:




