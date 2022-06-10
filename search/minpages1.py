# find the min pages to allocate resource
#a=[10,20,30,40,50]
#k=2
#output=60
import math


def sum(a,l,r):
    s=0
    for i in range(l,r):
        s+=a[i]
    return s

#recursive function
def find_min(a,n,k):
    if k==1:
        return sum(a,0,n-1)
    if n==1:
        return a[0]
    res=math.inf
    for i in range(1,n-1):
        res=min(res,max(find_min(a,i,k-1),sum(a,i,n-1)))
    return res
a=[10,20,30,40]
k=2
print("the minimum number of pages divided is :",find_min(a,len(a),k))