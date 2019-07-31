#!/usr/bin/env python
# coding: utf-8

# In[14]:


def optOperation(n,M, NY, SF):
    FINISH_AT_NY = [0]*(n+1)
    FINISH_AT_SF = [0]*(n+1)
    LOCATION = ["NY"] * (n)
    FINISH_AT_NY[0] = 0
    FINISH_AT_SF[0] = 0
    for i in range (1, n+1):
        FINISH_AT_NY[i] = NY[i-1] + min(M + FINISH_AT_SF[i-1], FINISH_AT_NY[i-1])
        FINISH_AT_SF[i] = SF[i-1] + min(M + FINISH_AT_NY[i-1], FINISH_AT_SF[i-1])
        if(FINISH_AT_SF[i] < FINISH_AT_NY[i]):
            LOCATION[i-1] = "SF"
    #print(FINISH_AT_NY, FINISH_AT_SF)    
    print(LOCATION)
    return min(FINISH_AT_NY[n], FINISH_AT_SF[n])
        
n=4
M=10
NY = [1, 3, 20, 30]
SF = [50, 20, 2, 4]
print("Total cost:",optOperation(n,M, NY, SF))


# In[ ]:




