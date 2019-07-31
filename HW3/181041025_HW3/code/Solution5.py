#!/usr/bin/env python
# coding: utf-8

# In[17]:


text = 'Tobeornottobe'
A = 'to'
B = 'be'
C = 'or'
D = 'not'
pattern = [A, B, C, D, A, B]

def match(text, pattern):
    textLength = len(text)
    patternCharLength = 0
    
    for pat in pattern:
        patternCharLength += len(pat)
    
    #text length and total length of pattern items must match
    if len(pattern) == 1 or patternCharLength == textLength:
        startIndex = 0
        endIndex = 0
        if len(pattern) > 1:
            #this part works when the function is called for the first time
            #the recursive call for each pattern element
            for i in range(len(pattern)):
                partOfPattern = [pattern[i]]
                endIndex = startIndex + len(pattern[i])
                if not match(text[startIndex: endIndex], partOfPattern):
                    print("Not match text part: ", text[startIndex:endIndex], " partOfPattern: ", partOfPattern)
                    return False
                startIndex = endIndex
                
        #this part works for each element of pattern list after the function called for the first time
        #complexity is m_i
        if len(pattern) == 1:
            patternItem = pattern[0]
            for i in range(len(patternItem)):
                if not patternItem[i].lower() == text[i].lower():
                    return False
           # print(patternItem, " matches to ", text)
        return True
    else:
        print("Not valid sizes. Pattern sizes are greater than text size!")
        return False

print(text, " matches to ", pattern, ": ", match(text, pattern))

