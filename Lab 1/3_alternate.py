import sys
from collections import deque

sys.stdin = open("3_inputs.txt",'r')
sys.stdout = open("outputs.txt",'w')



T = int(input())
while T:
    N = int(input())
    array1 = list(map(int,input().strip().split()))
    array1.sort()
    array = deque(array1.copy())
    count =0
    while array:
        if array[0]!=array[-1]:
            array.popleft()
            array.pop()
            count+=1
        else:
            array.pop()
            count+=1
    print (count)
    T -=1