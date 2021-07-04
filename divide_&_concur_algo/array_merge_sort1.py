#program for merge sort algorithm for array
def merge(a,l,m,r):
    n1=m-l+1
    n2=r-m
    l1=[0]*n1
    l2=[0]*n2
    for i in range(n1):
        l1[i]=a[l+i]
    for j in range(n2):
        l2[j]=a[j+m+1]
    i, j = 0, 0
    k = l
    while i<n1 and j<n2:
        if l1[i]<l2[j]:
            a[k]=l1[i]
            i=i+1
            k=k+1
        else:
            a[k]=l2[j]
            j=j+1
            k=k+1
    while i<n1:
        a[k]=l1[i]
        i=i+1
        k=k+1
    while j<n2:
        a[k]=l2[j]
        j=j+1
        k=k+1
def mergesort(a,l,r):
    if l<r:
        m=(l+r)//2
        mergesort(a,l,m)
        mergesort(a,m+1,r)
        merge(a,l,m,r)
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" %arr[i])
mergesort(arr,0,n-1)
print ("After sort the array is")
for i in range(n):
    print ("%d" %arr[i])
