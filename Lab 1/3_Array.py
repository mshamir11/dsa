import sys
from collections import Counter
import heapq

sys.stdin = open("3_inputs.txt",'r')
sys.stdout = open("outputs.txt",'w')



T = int(input())
while T:
    N = int(input())
    array1 = list(map(int,input().strip().split()))
    
    array = Counter(array1)
    freq =[]
    for (key,value) in array.items():
        freq.append(-value)

    heapq.heapify(freq)
    count=0
    while len(freq)>1:
        a= heapq.heappop(freq)
        b = heapq.heappop(freq)
        if -a-1>0:
            heapq.heappush(freq,a+1)
        if -b-1>0:
            heapq.heappush(freq,b+1)
        count +=1
    while freq:
        a=freq.pop()
        count+= abs(a)
    print(count)
    T -=1