#WRITE YOUR CODE IN THIS FILE
#define function 
def countA(w):
    total = 0
    for i in range(0,len(w)):
        if w[i] == "a":
            total = total + 1
    return total       
countA("cat")
#You can put if statements inside of for loops.  
#w[0] returns the first letter of a word.

#1 function X 
#1 for loop  
#1 if statement