import sys


sys.stdin = open("int.txt",'r')
sys.stdout = open("myout.txt",'w')

N,M = list(map(int,input().strip().split()))
requests =[]
for i in range(M):
    a,b = list(map(int,input().strip().split()))
    requests.append((a,b))

requests.sort(key=lambda x:x[1])


right_min = -1
bridges = 0
for request in requests:

    if request[0] < right_min:
        continue
    else:
        right_min = request[1]
        bridges +=1
print(bridges)
