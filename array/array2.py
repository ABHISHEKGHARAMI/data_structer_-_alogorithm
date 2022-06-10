'''
program to move all the non zero element at rear end of the end of an array
'''
def swap(a,b):
    temp=a
    a=b
    b=temp
def move_nonzero(arr):
    count=0
    for  i in range(len(arr)):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count<len(arr):
        arr[count]=0
        count+=1
    print(arr)
    
def move_zero(arr):
    for i in range(len(arr)-1):
        if arr[i]==0:
            j=i+1
            for j in range(len(arr)-1):
                if arr[j]!=0:
                    swap(arr[i],arr[j])
    print(arr)

# left rotate array by one
def left_rotate(arr):
    n=len(arr)
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    print(arr)

#letf rotate by various time
def left_rotate_v(arr,k):
    for i in range(k):
        left_rotate(arr)


#program to find the leader
''' leader is which that does not have any bigger element after that
and the right most element by default is the leader'''

def print_leader(arr):
    n=len(arr)
    curr_leader=arr[n-1]
    l1=[]
    l1.append(curr_leader)
    for i in range(n-2,0,-1):
        if curr_leader<arr[i]:
            curr_leader=arr[i]
            l1.append(curr_leader)
    for x in l1:
        print(x,end=" ")

'''
................................
/// program to find the greatest difference between the array element......
................................
'''
def find_max(arr):
    n=len(arr)
    max_diff=arr[0]
    for i in range(n):
        j=i+1
        for j in range(n):
            if abs(arr[j]-arr[i])>max_diff:
                max_diff=abs(arr[j]-arr[i])
    return max_diff




'''program to find the frequencies in the array element'''
def find_frequency(arr):
    freq={}
    for item in arr:
        if  item in  freq:
            freq[item]+=1
        else:
            freq[item]=1
    print("The frequency check in the list:")
    for i, j in freq.items():
        print(i,j,end=" ")
        print("\n")

        





arr=[2,3,10,6,4,8,1,2,3,3,3,10,6,4,-1]
#move_nonzero(arr)
#move_zero(arr)
#left_rotate(arr)
#k=int(input("thenumber of rotation :"))
#left_rotate_v(arr,k)
#print_leader(arr)
#print("the maximum difference in the list is  :",find_max(arr))
find_frequency(arr)