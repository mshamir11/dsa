import sys
import itertools
sys.stdin = open("inputs.txt",'r')
sys.stdout = open("outputs.txt",'w')


T =int(input())
while (T):
    G,C,K = list(map(int,input().strip().split()))
    collection = []
    total_toff =0
    for i in range(C):
        S,E = list(map(int,input().strip().split()))
        collection.append((S,E))
        total_toff += (E-S+1)
    collection.sort(key=lambda x: x[1])

    right_min = -1
    if K==0:
        flag=0
        for item in collection:
            if item[0]<=right_min:
                flag=1
                break
            else:
                right_min = item[1]
        if flag:
            print("Bad")
        else:
            print("Good")
    if K==1:
        temp_count=0
        count =0
       
        

        for i in range(len(collection)):
            
            item = collection[i]
            if i==0:
                consecutive_zeros = item[0]-1
                prev = item
                right_min = item[1]
                left_min =item[0]

            elif item[0]<=right_min:
                temp_count+=1
                count = max(temp_count,count)
                first_endtime=right_min
                firt_starttime = left_min
                first_length = right_min-left_min+1
                second_length = item[1]-item[0]+1
                if i==1:
                    balance = item[0]-1
                    consecutive_zeros_left = max(consecutive_zeros,balance)
                else:
                    balance = item[0]-prev[1]
                    consecutive_zeros_left = max(consecutive_zeros,balance)
                if i<len(collection)-1:
                    balance = collection[i+1][0]-prev[1]
                    consecutive_zeros_right = max(0,balance)
                   
                else:
                    balance = G-max(item[0],prev[1])
                    consecutive_zeros_right = max(0,balance)
                    
               
                prev = item
            else:
                right_min = item[1]
                left_min =item[0]
                temp_count=0
                consecutive_zeros = max(consecutive_zeros,item[0]-prev[1])
                prev = item

        consecutive_zeros = max(consecutive_zeros,G-prev[1])


        
        
       
        
            
        if count>1:
            print("Bad")
        elif count==0:
            print("Good")
        else:
            if second_length<first_length:
                if second_length<=consecutive_zeros_right or second_length<=consecutive_zeros:
                    print("Good")
                else:
                    print("Bad")
            elif first_length<second_length:
                if first_length<=consecutive_zeros_left or first_length<=consecutive_zeros:
                    print("Good")
                else:
                    print("Bad")
            else:
                if second_length<=consecutive_zeros_right or first_length<=consecutive_zeros_left:
                    print("Good")
                else:
                    print("Bad")


    T -=1