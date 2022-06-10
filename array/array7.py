#return the number of majority element
# majority element is the element appears the n/2 times in the array
def majority(arr):
    n=len(arr)
    count=0
    max1=0
    for i in range(n):
        j=i+1
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if count>n//2:
            max1=max(count,max1)
        else:
            max1=0
    return i
a=[3,7,4,7,7,5]
k=majority(a)
if k>0:
    print("element is :",k)
else:
    print("No majority element")