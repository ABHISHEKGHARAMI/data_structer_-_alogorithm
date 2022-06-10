# find the peak element from the array
#peak element :
#element what is greater than its neighbour
def peak(a):
    l=[]
    n=len(a)
    if a[0]>a[1]:
        l.append(a[0])
    for i in range(1,len(a)-1):
        if a[i]>a[i+1] and a[i]>a[i-1]:
            l.append(a[i])
    if a[n-1]>a[n-2]:
        l.append(a[n-1])
    for i in l:
        print(i,end=" ")
a=[80,70,90]
peak(a)
