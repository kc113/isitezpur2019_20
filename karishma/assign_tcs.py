def iteratelist(l):
    """
    (list) -> list
    returns the position and value of elements in the list.
    """
    #create empty list
    res_l = list()
    #iterate through the list
    for i in range(len(l)):
        #append the position and the item
        res_l.append([i, l[i]])
    #return the list
    return(res_l)
    

def rotatestr(s):
    """
    (str) -> str
    returns the rotation of the string.
    """
    #create empty string
    rotstr = ""
    #split the string by space
    str_words = s.split()
    #add the words to the string
    for i in range(1, len(str_words)):
        rotstr = rotstr + str_words[i] + " "
    #add the last word
    rotstr += str_words[0]
    #return the result
    return(rotstr)

def isprime(n):
    """
    (num) -> bool
    checks if a given number is prime or not
    """
    #if n is 2, return true
    if n == 2:
        return(True)
    #if n is less than 2, return false
    elif n < 2:
        return(False)
    #else, check for a factor of the number
    else:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                break
        else:
            return(True)
    return(False)
        

def fibo(n):
    """
    (num) -> list
    returns the first n numbers of fibonacci series
    """
    #create list with n elements
    l = [0] * n
    #assign the first two elements
    l[0] = 0
    l[1] = 1
    #assign the next n-2 two elements
    for i in range(2, n):
        l[i] = l[i-1] + l[i-2]
    #return the list
    return(l)

def findprime(n):
    """
    (num) -> list
    returns teh list of prime numbers within n
    """
    return([(num + 1) for num in range(n) if isprime(num + 1)])
    
        
        

def sumsquare(n):
    """
    (num) -> num
    returns the sum of first n natural numbers
    """
    #set s to 0
    s = 0
    #iterate through the numbers
    for i in range(1, n+1):
        #update the sum
        s += (i * i)
    #return the result
    return(s)

def calcarea(r):
    """
    (num) -> num
    returns the area of the circle
    """
    import math
    return(math.pi * r * r)

def palinstr(s):
    if s == s[::-1]:
        return(True)
    else:
        return(False)
        
def swapnum(l):
    """
    (list) -> list
    swaps the two elements in a list
    """
    #swap the elements
    l[0], l[1] = l[1], l[0]
    #return the list
    return(l)

    
def copylist(l):
    return(l[:])

def revlist(l):
    """
    (list) -> list
    returns the reverse of the list
    """
    return(l[::-1])
    
def revstr(s):
    """
    (str) -> str
    returns the reverse of the string.
    """
    #create empty string
    revstr = ""
    #split the string by space
    str_words = s.split()
    #add the words to the string
    for i in range(len(str_words)-1, 0, -1):
        revstr = revstr + str_words[i] + " "
    #add the last word
    revstr += str_words[-1]
    #return the result
    return(revstr)

def unilist(l):
    """
    (list) -> list
    returns the unique element of the list
    """
    return(list(set(l)))

            
def finddigit(s):
    """
    (str) -> dict
    returns the digits in the string and its position
    """
    #create empty dictionary
    d = dict()
    #for every character in string
    for i in range(len(s)):
        #if it is a digit
        if s[i].isdigit():
            #add it to the dictionary
            d[i] = s[i]
    #return the dictionary
    return(d)

#wap to find common element between two lists
l1 = [1,2,3,4,5,1,2,3]
l2 = [4,5,1,2,3,4,1,32,4]
#function to find common element between two lists
def common(l1, l2):
    #list compression
    l = [item for item in l1 if item in l2]
    #return l
    return(list(set(l)))

#funtion to find number of times a word appears in a file
def findword(filename, word):
    """
    (str, str) -> num
    returns the number of times a word appears in a file
    """
    #open the file
    fp = open(filename)
    #read the file
    data = fp.read().split()
    #count the number of words
    s = len([item for item in data if item == word])
    #close the file
    fp.close()
    #return the count
    return(s)



    






                

