#Find the maximum of the subarray
def naive_sum_sub(arr):
    n=len(arr)
    res=arr[0]
    for i in range(n):
        curr=0
        for j in range(n):
            curr+=arr[j]
            res=max(curr,res)


    return res
#runtime O(n^2) very bad
def max_subarray(arr):
    n=len(arr)
    res=arr[0]
    maxlen=arr[0]
    for i in range(1,n):
        maxlen=max(maxlen+arr[i],arr[i])
        res=max(maxlen,res)
    return res
#runtime is the O(n)

print("The maximum subarray sum is :",naive_sum_sub([5,8,3]))

print("The Bestcase of the running is :",max_subarray([5,8,3]))
