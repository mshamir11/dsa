
from collections import defaultdict
# import sys
# sys.stdin = open("input.txt",'r')
# sys.stdout = open("output.txt",'w')

class Node:
    def __init__(self,index):
        self.rank = 0
        self.parent =None
        self.index = index
        self.max_size = 1





def find(a):

    if a.parent ==a:
        return a
    a.parent = find(a.parent)
    return a.parent

def union(root_a,root_b):
    
    
    
    if root_a ==root_b:
        return

    if root_a.rank>root_b.rank:
        root_b.parent = root_a
        root_a.max_size +=root_b.max_size
        
    elif root_a.rank<root_b.rank:
        root_a.parent = root_b
        root_b.max_size += root_a.max_size
        

    else: 
        root_b.parent = root_a
        root_a.rank +=1
        root_a.max_size +=root_b.max_size
T = int(input())
while T:
    N,M,Q = list(map(int,input().strip().split()))
    

    cell_array =[[0]*(M+1) for i in range(N+1)]
    query_list=[]
    union_array =[[0]*(M+1) for i in range(N+1)]
   

    for j in range(Q):
        query = list(map(int,input().strip().split()))

        query_list.append(query)
        if query[0]==1:
            x1,x2 =query[1],query[2]
            if cell_array[x1][x2]:
                cell_array[x1][x2][1] +=1
            else:
                cell_array[x1][x2]=defaultdict(set)
                cell_array[x1][x2][1] =1
                cell_array[x1][x2][2] =0
        
        elif query[0]==2:
            x1,x2 =query[1],query[2]
            if cell_array[x1][x2]:
                cell_array[x1][x2][2] +=1
            else:
                cell_array[x1][x2]=defaultdict(set)
                cell_array[x1][x2][2] =1
                cell_array[x1][x2][1] =0
    for i in range(1,N+1):
        for j in range(1,M+1):
            union_array[i][j] =Node((i,j))
            union_array[i][j].parent = union_array[i][j]
    
    max_size_set =0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if cell_array[i][j]:
                
                if cell_array[i][j][1] and cell_array[i][j][2]:
                    pass
                    
                elif cell_array[i][j][2]>0 and j+1<=M:
                    root_a = find(union_array[i][j])
                    root_b = find(union_array[i][j+1])
                    if root_a!=root_b:
                        
                        max_size_set=max(max_size_set,root_a.max_size+root_b.max_size)
                        union(root_a,root_b)

                elif cell_array[i][j][1]>0 and i+1<=N:
                    root_a = find(union_array[i][j])
                    root_b = find(union_array[i+1][j])
                    if root_a!=root_b:
                        max_size_set=max(max_size_set,root_a.max_size+root_b.max_size)
                        union(root_a,root_b)


                
                    
            else:
                if j+1<=M:
                    root_a = find(union_array[i][j])
                    root_b = find(union_array[i][j+1])
                    if root_a!=root_b:
            
                        max_size_set=max(max_size_set,root_a.max_size+root_b.max_size)
                        union(root_a,root_b)
                if i+1<=N:
                    root_a = find(union_array[i][j])
                    root_b = find(union_array[i+1][j])
                    if root_a!=root_b:
                    
                        max_size_set=max(max_size_set,root_a.max_size+root_b.max_size)
                        union(root_a,root_b)
                
    ans =0

    while query_list:
        query = query_list.pop()
        if query[0]==1:
            x1,x2 = query[1],query[2]
            if cell_array[x1][x2]:
                if cell_array[x1][x2][1]==1 and x2+1<=M:
                    root_a = find(union_array[x1][x2])
                    root_b = find(union_array[x1][x2+1])
                    if root_a!=root_b:
                        max_size_set=max(max_size_set,root_a.max_size+root_b.max_size)
                        union(root_a,root_b)
                cell_array[x1][x2][1]-=1

        elif query[0]==2:
            x1,x2 = query[1],query[2]
            if cell_array[x1][x2]:
                if cell_array[x1][x2][2]==1 and x1+1<=N:
                    root_a = find(union_array[x1][x2])
                    root_b = find(union_array[x1+1][x2])
                    if root_a!=root_b:
                        max_size_set=max(max_size_set,root_a.max_size+root_b.max_size)
                        union(root_a,root_b)

                cell_array[x1][x2][2]-=1

        elif query[0]==3:
            x1,x2,x3,x4 = query[1],query[2],query[3],query[4]
            root_a = find(union_array[x1][x2])
            root_b = find(union_array[x3][x4])
            if root_a==root_b:
                ans+=1
            

        elif query[0]==4:
            ans += max_size_set

    print(ans)

    T-=1