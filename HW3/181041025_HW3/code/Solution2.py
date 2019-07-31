#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = 19 #Number of chips
m = 3  #Number of maximum taken chips
isFirstPlayer = True


def startGame(n, m, isFirstPlayer):
    print("n ", n, ", m", m)
    if isFirstPlayer :
        player = 'First'
    else:
        player = 'Second'
        
    if not n % (m+1) == 0:
        ask = str(player) + ' player. How many chips will you get: '
        var = int(input(ask))
        if var > 3 or var < 1 :
            error = "You can get at least 1 and at most "+ str(m) + " chips."
            print(error)
            var = int(input(ask))
        startGame(n-var, m, not isFirstPlayer) 
    return player
    
print(startGame(n, m, isFirstPlayer), "player wins!")

