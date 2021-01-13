import sys
from collections import defaultdict


sys.stdin = open("2_inputs.txt",'r')
sys.stdout = open("outputs.txt",'w')


T = int(input())
while(T):
    N,K =list(map(int,input().strip().split()))
    collections = []
    for i in range(N):
        a,b,c =list(map(int,input().strip().split()))
        collections.append((a,b,c-1))
    collections.sort(key=lambda x: x[1])
    
    counters=defaultdict(int)
    count =0
    for item in collections:
        if not counters[item[2]]:
            counters[item[2]]=item[1]
            count+=1
        elif item[0]>=counters[item[2]]:
            counters[item[2]]=item[1]
            count+=1
       
            
    print(count)
    T-=1
