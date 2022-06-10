'''tapping water problem'''
def tap_water(arr):
    res=0
    n=len(arr)
    for i in range(1,n-1):
        lmax=arr[i]
        for j in range(i):
            lmax=max(lmax,arr[j])

        j=i+1
        rmax=arr[i]
        for j in range(n):
            rmax=max(arr[j],rmax)
        res=res+min(lmax,rmax)-arr[i]
    return res

arr=[3,0,1,2,5]
print("the water stored in the space is:",tap_water(arr))

