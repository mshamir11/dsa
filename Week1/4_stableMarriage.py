import sys
from collections import deque
import time

sys.stdout = open('text.txt','w')
sys.stdin = open('int.txt','r')


def singleRemaining(men_eng):
    if -1 in men_eng:
        return True
    else:
        return False



T = int(input())
while (T):
    N = int(input())
    men_prf = []
    women_prf = []
    for i in range(N):
        incoming = deque(map(int,input().strip().split()))
        incoming.popleft()
        women_prf.append(incoming)
    for i in range(N):
        incoming = deque(map(int,input().strip().split()))
        incoming.popleft()
        
        men_prf.append(incoming)
    
    men_eng = [-1]*N
    women_eng = [-1]*N

    while (singleRemaining(men_eng)):
        for i in range(N):
            if men_eng[i]== -1:
                top = men_prf[i].popleft()

                if women_eng[top-1]==-1:
                    women_eng[top-1] =i+1
                    men_eng[i] = top
                else:
                    competition = women_eng[top-1]

                    if women_prf[top-1].index(i+1)<women_prf[top-1].index(competition):
                        women_eng[top-1]= i+1
                        men_eng[i] = top
                        men_eng[competition-1]=-1
    for i in range(N):
        print(i+1,men_eng[i])
    T -=1


# print(f"Finish time : {time.time() - start}")