#max sum of a subarray from the array
import sys
def max_cross(a,low,mid,high):
    left_sum=-1000
    right_sum=-1000
    sum=0
    for i in range(mid,low-1,-1):
        sum=sum+a[i]
        if sum>left_sum:
            left_sum=sum
    sum=0
    for i in range(mid+1,high+1):
        sum=sum+a[i]
        if sum>right_sum:
            right_sum=sum
    return max(left_sum+right_sum,left_sum,right_sum)
#call for the recurssion
def max_subarray(a,low,high):
    if low==high:
        return a[low]
    else:
        mid=(low+high)//2
        return max(max_subarray(a,low,mid),max_subarray(a,mid+1,high),max_cross(a,low,mid,high))
a=[2, 3, 4, 5, 7]
n=len(a)
print("the given array is:")
for i in range(n):
    print(a[i],end=" ")
print("\nThe maximum of the array is:",max_subarray(a,0,n-1))