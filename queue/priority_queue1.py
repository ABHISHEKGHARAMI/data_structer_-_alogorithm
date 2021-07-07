#priority queue using the heap
def heapify(a,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and a[l]>a[i]:
        largest=l
    largest=i
    if r<n and a[r]>a[largest]:
        largest=r
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        heapify(a,n,largest)
#insert the data in the heap
def insert_heap(a,x):
    n=len(a)
    if n==0:
        a.append(x)
    else:
        a.append(x)
        for i in range((n//2)-1,-1,-1):
            heapify(a,n,i)
#delete the num from the heap
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(size - 1)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)

#calling the function
arr = []

insert_heap(arr, 3)
insert_heap(arr, 4)
insert_heap(arr, 9)
insert_heap(arr, 5)
insert_heap(arr, 2)
print(arr)
deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
