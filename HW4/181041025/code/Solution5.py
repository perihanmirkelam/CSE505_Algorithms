#!/usr/bin/env python
# coding: utf-8

# In[22]:


def isSatisfied(elements, equals, inequals):
    print(elements, equals, inequals)
    newList = [-1] * len(elements)
    for eq in equals:
        print(eq)
        temp = 1
        if (eq[0] != -1 and eq[1] != -1):
            newList[eq[0]] = temp
            newList[eq[1]] = temp
            print("1",newList)
            temp+=1
        elif (eq[0] != -1):
            newList[eq[1]] = eq[0]
            print("2",newList)
        elif (eq[1] != -1):
            newList[eq[0]] = eq[1]
            print("3",newList)
        else:
            return False
    for ineq in inequals:
        if(newList[ineq[0]] == newList[ineq[1]]):
            return False
    
 
print(isSatisfied([2,4,5,7,10], [[0,1],[2,3]], [[0,4],[2,3]]))


# In[ ]:




