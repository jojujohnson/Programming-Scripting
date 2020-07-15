#!/bin/python3
#Hacker Rank 
import re
import sys
from collections import Counter
       
if __name__ == '__main__':
    new = []
    regex1 = '^[A-Za-z0-9_]+[\._]?[A-Za-z0-9_]+[@]\w+[.]\w+$'
    regex2 = '^[A-Za-z0-9_]+[\._]?[A-Za-z0-9_]+[@]\w+[.]\w+[.]\w+$'
    regex3 = '^[A-Za-z0-9_]+[\._]?[A-Za-z0-9_]+[@]\w+[.]\w+[.]\w+[.]\w+$'
    linenum=int(sys.stdin.readline())
    for line in range(0,linenum):
        istr=(sys.stdin.readline())
        match = re.search('@', istr)
        if match:
            res = istr.split() 
            for word in res:
                #print(word)
                word = re.sub('\W$', '', word)
                if(re.search(regex1,word) or re.search(regex2,word) or re.search(regex3,word)):
                    #print(word)
                    new.append(word)
    new.sort()
    new=(Counter(new).keys())
    appstr=""
    for arr in new:
        appstr=appstr+";"+arr
    
    appstr=re.sub('^;', '', appstr)
    print (appstr) 

    
