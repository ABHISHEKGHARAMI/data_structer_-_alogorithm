'''this is the search technique for long array integer'''





def binary_search(a,l,r,k):
    if r>=l:

        mid= (l+r)//2
        if a[mid]==k:
            return mid
        if a[mid]<k:
            return binary_search(a,mid+1,r,k)
        return binary_search(a,l,mid-1,k)

    return -1

def findPos(a,k):
    l,r,val=0,1,a[0]
    while val<=k:
        l=r
        r=2*r
        val=a[r]
    return binary_search(a,l,r,k)
        
a=[0.042, 0.083, 0.123, 0.162, 0.2, 0.236, 0.273, 0.303, 0.337, 0.37, 0.403, 0.425, 0.448, 0.477, 0.504, 0.528, 0.553,
     0.577, 0.599, 0.621, 0.645, 0.667, 0.689, 0.711, 0.733, 0.753, 0.774, 0.796, 0.818, 0.838, 0.859, 0.878, 0.898,
     0.914, 0.933, 0.945, 0.96, 0.977, 0.993, 1]
print(binary_search(a,0,len(a),0.945))