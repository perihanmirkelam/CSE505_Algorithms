#!/usr/bin/env python
# coding: utf-8

# In[29]:


def mergeSort(jobs):
    if len(jobs)>1:
        mid = len(jobs)//2
        lefthalf = jobs[:mid]
        righthalf = jobs[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][weight]/lefthalf[i][time] > righthalf[j][weight]/righthalf[j][time]: #sort by weight/time
                jobs[k]=lefthalf[i]
                i=i+1
            else:
                jobs[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            jobs[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            jobs[k]=righthalf[j]
            j=j+1
            k=k+1
            
def findOptimalCompletionTime(jobs):
    mergeSort(jobs)
    print("Scheduled jobs list: ", jobs)
    completionTime = 0
    for i in range(0,len(jobs)):
        tempTime=0
        for j in range(0,i+1):
            tempTime += jobs[j][time]
        completionTime += tempTime * jobs[i][weight]
        print("Job ", i+1 , ":", jobs[i] ,"has completed at time:", tempTime)
    print("Minimized weighted sum of completion time: ",completionTime)

     
time=0
weight=1
jobs =  [[3,5], [1,2], [4,5], [2,8]] # jobs[i] =  [time_i, weight_i]

print("Let's schedule these jobs: ", jobs)
findOptimalCompletionTime(jobs)


# In[ ]:





# In[ ]:




