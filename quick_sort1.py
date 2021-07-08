#quicksort for sorting
def quick_sort(a,p,r):
    if  p<r:
        q=partition(a,p,r)
        quick_sort(a,p,q-1)
        quick_sort(a,q+1,r)
#partition function
def partition(a,p,r):
    pivot=a[r]
    i=p-1
    for j in range(p,r):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]

    a[i+1],a[r]=a[r],a[i+1]
    return i+1
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr,0,n-1)
for i in arr:
    print(i,end=" ")