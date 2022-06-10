'''find the consequtive one'''
'''def cons_one(arr):
    res=0
    n=len(arr)
    for i in range(n):
        count=0
        j=i
        for j in range(n):
            if arr[j]==1:
                count+=1
            else:
                break
        res=max(count,res)
        '''
from subprocess import list2cmdline


def cons_ones(a):
    n=len(a)
    res=0
    for i in range(n):
        if a[i]==0:
            count=0
        else:
            count+=1
            res=max(res,count)
    return res
a=[0,1,1,1,0,1,1]
print("The maximum number of 1 s present is :",cons_ones(a))

# different subarray in the array
def subarray(a):
    lists=[[]]
    sum=0
    max=0
    n=len(a)
    for i in range(n+1):
        for j in range(i):
            lists.append(a[j:i])
    for i in range(len(lists)):
        sum=sum(lists[i])
        max=max(sum,max)

a1=[1,2,3,4]
subarray(a1)