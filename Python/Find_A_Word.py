#!/bin/python3
#Hacker Rank
import re
import sys

def fizzBuzz(string,findstr):
    findstr=findstr.strip()
 
    new_string = re.sub('\W', " ", string) 
    pattern = ' '
    result = re.split(pattern, new_string) 
    arrlen = len(result)

    cnt=0    
    for i in range(0,arrlen):
        matchfound = re.match('^'+findstr+'$', result[i])

        if matchfound:
            #print (result[i])
            cnt=cnt+1     
    
    if (cnt > 0):
        f=findstr,cnt
        total.append(f)         
           
if __name__ == '__main__':
    new = []
    tew = []
    total=[]
    a1=int(sys.stdin.readline())
    for n1 in range(0,a1):
        n=(sys.stdin.readline())
        new.append(n)

    b1=int(sys.stdin.readline())
    for t1 in range(0,b1):
        t=(sys.stdin.readline())
        tew.append(t)

    #print(new)  
    #print(tew)  
    for n1 in range(0,a1):
        for t1 in range(0,b1):
            fizzBuzz(new[n1],tew[t1])
    
    #print(total)
    
    arrlen = len(total)
    for t1 in range(0,b1):
        Newtot=0
        checkname=tew[t1].strip()
        for n1 in range(0,arrlen): 
            t2=total[n1][0].strip()        
            if(checkname==t2):
                Newtot=Newtot+total[n1][1]
        print (Newtot)                          
