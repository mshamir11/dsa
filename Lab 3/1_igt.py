import sys

sys.stdin = open("input.txt",'r')
sys.stdout = open("output.txt",'w')

class Node:
    def __init__(self,index,data):
        self.data = data
        self.index = index
        self.next =None


T = int(input())
while T:
    N = int(input())
    input_list = list(map(int,input().strip().split()))
    Q = int(input())

    submission_array = [0]*(N+1)
    for i in range(1,N+1):
        submission_array[i]=Node(i,input_list[i-1])
    for j in range(Q):
        query = list(map(int,input().strip().split()))
        
        if query[0]==0:
            a,b = query[1],query[2]
            temp1 = submission_array[a]
            temp2 = submission_array[b]
            
            if temp1.index == temp2.index:
                print("Invalid query!")
            
            elif temp1.data <temp2.data:
                temp2.next = temp1
                submission_array[a] = temp2
                temp = temp2.next
                while temp:
                    submission_array[temp.index]=temp2
                    temp = temp.next
                    
                
            elif temp1.data>temp2.data:
                temp1.next = temp2
                submission_array[b] = temp1
                temp = temp1.next
                while temp:
                    submission_array[temp.index]=temp1
                    temp = temp.next

      

        elif query[0]==1:
            x = query[1]
            print(submission_array[x].index)
    T-=1