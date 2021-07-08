#random quick sort for random pivot
import random
def quick_sort(arr,a,b):
    if a<b:
        q=partition(arr,a,b)
        quick_sort(arr,a,q-1)
        quick_sort(arr,q+1,b)
#partition
def partition(arr,a,b):
    pivot=random.randint(a,b)
    for i in range(a,b):
        if arr[i]<arr[b]:
            arr[i],arr[pivot]=arr[pivot],arr[i]
            pivot+=1
    arr[pivot],arr[b]=arr[b],arr[pivot]
    return pivot

array = [10, 7, 8, 9, 1, 5]
quick_sort(array,0,len(array)-1)
print(array)
