import sys

sys.stdin = open("input.txt",'r')
sys.stdout = open("output.txt",'w')

class Node:
    def __init__(self,index):
        self.rank = 0
        self.parent =None
        self.index = index
        self.max_index = index


T = int(input())


def find(a):

    if a.parent ==a:
        return a
    a.parent = find(a.parent)
    return a.parent

def union(root_a,root_b,input_list):
    

    if root_a.rank>root_b.rank:
        root_b.parent = root_a
        if input_list[root_a.max_index-1]<input_list[root_b.max_index-1]:
            root_a.max_index = root_b.max_index
    elif root_a.rank<root_b.rank:
        root_a.parent = root_b
        if input_list[root_a.max_index-1]>input_list[root_b.max_index-1]:
            root_b.max_index = root_a.max_index

    else: 
        root_b.parent = root_a
        if input_list[root_a.max_index-1]<input_list[root_b.max_index-1]:
            root_a.max_index = root_b.max_index
        root_a.rank +=1

while T:
    N = int(input())
    input_list = list(map(int,input().strip().split()))
    Q = int(input())

    submission_array = [0]*(N+1)
    for i in range(1,N+1):
        submission_array[i]=Node(i)
        submission_array[i].parent = submission_array[i]

    for j in range(Q):
        query = list(map(int,input().strip().split()))

        if query[0]==0:
            a,b = query[1],query[2]
            root_a = find(submission_array[a])
            root_b = find(submission_array[b])
            if input_list[a-1]!=input_list[b-1]:
                if root_a==root_b:
                    print("Invalid query!")
                    
                elif input_list[root_a.max_index-1]!=input_list[root_b.max_index-1]:
                    union(root_a,root_b,input_list)
                    
            elif a==b:
                print("Invalid query!")
        
        elif query[0]==1:
            x=query[1]
            root = find(submission_array[x])
            print(root.max_index)
    T-=1