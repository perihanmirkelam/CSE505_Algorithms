#!/usr/bin/env python
# coding: utf-8

# In[96]:


def dict(word) :
    if word in dictionary :
        return True
    return False

        
def reconstructDocument(doc) :
    VALID = [False] * (len(doc) + 1)
    newDoc = ""    
    startIndex = -1
    for i in range(1,len(doc)):
        if(dict(doc[:i])):
            startIndex = i
            VALID[i] = True
            print("First valid word:", doc[:i])
            newDoc += doc[:i] + " "
            break
    if(startIndex != -1):        
        for i in range(startIndex, len(doc)+1):
            for j in range (0, i-1):
                word = doc[j:i]
                #print("\n loop i:", i, "j:", j, "\n word:", word, "= doc[", j, ":", i-1 ,"] dict(word):", dict(word), "and valid[j]:" , valid[j])
                if(VALID[j] and dict(word)):
                    print("Found a valid word:", word)
                    VALID[i]=True
                    newDoc += (word) + " "
    
        print("The last indices of valid words in document: ", VALID)
        print("\nReconstructed document: ", newDoc)
    else :
        print("The document has not a valid word.")

dictionary = ["it","was","the","best","of","times", "some", "thing", "else"]
s = "itwasthebestoftimes"
reconstructDocument(s)


# In[ ]:




