# given two array sorted an combine the two array in soretd order
# after that find the median
def merge_sort(a,b):
    m=len(a)
    n=len(b)
    i,j=0,0
    k=0
    c=[]
    while i<m and j<n:
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
            k+=1
        else:
            c.append(b[j])
            j+=1
            k+=1
    while i<m:
        c.append(a[i])
        i+=1
        k+=1
    while j<n:
        c.append(b[j])
        j+=1
        k+=1
    return c
def find_median(a,b):
    c=merge_sort(a,b)
    n=len(c)
    if n%2==0:
        print("The median of the arrays are :",c[((n-1)//2)]," and ",c[((n+1)//2)])
    else:
        print("The median of the arrays is :",c[n//2])
a=[10,20,30,40,50]
b=[5,15,25,35,45]
find_median(a,b)