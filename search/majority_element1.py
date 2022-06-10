#majority element in the array
#majority element is the element appears n/2times in the array
from itertools import count


def majority(a):
    maxcount=0
    index=-1
    n=len(a)
    for i in range(n):
        count=0
        for j in range(n):
            if a[i]==a[j]:
                count+=1
        if maxcount<count:
            maxcount=count
            index=i
    if maxcount>n//2:
        return a[index]
    else:
        return -1
a=[3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majority(a))
