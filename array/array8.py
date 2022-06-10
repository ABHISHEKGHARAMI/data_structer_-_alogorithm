'''window sliding problem  to find the maximum sum of a limited given number'''
#naive solution
def naive_window_slide(a,k):
    maxint=-9999999
    n=len(a)
    i=0
    for i in range(n-k+1):
        sum=0
        for j in range(k):
            sum=sum+a[i+j]
        maxint=max(maxint,sum)
    return maxint

#best solution of the problem
def best_window_slide(a,k):
    n=len(a)
    if  n<k:
        print("Invalid")
    window_sum=sum(a[:k])
    max_sum=window_sum
    for i in range(n-k):
        window_sum=window_sum-a[i]+a[i+k]
        max_sum=max(max_sum,window_sum)
    return max_sum
#insert array
print("The max sum of the given array is :",naive_window_slide([1,8,30,-5,20,7],3))
print("The max sum pf the given array is :",best_window_slide([1,8,30,-5,20,7],3))
