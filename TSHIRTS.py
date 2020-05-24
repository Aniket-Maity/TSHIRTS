# -*- coding: utf-8 -*-
"""
Created on Sun May 24 08:35:01 2020

@author: Aniket Maity
"""

import itertools 
def main():
    T = int(input())
    output = []
    while(T>0):
        T-=1
        N = int(input())
        shirtArrAll = []
        count=0
        for i in range(N):
            a=list(map(int,input().split()))
            shirtArrAll.append(a)
        res = list(itertools.product(*shirtArrAll))
        
        for items in res:
            if(len(set(list(items))) == N):
                count+=1
        output.append(count)
    for item in output:
        print(item+"\n")
                

if __name__== '__main__':
    
    try:
        main()
    except:
        pass

#res = list(itertools.product(*all_list))

