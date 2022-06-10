def two_pointer(a,k):
    flag=0
    for i in range(len(a)):
        j=i+1
        for j in range(len(a)):
            if a[i]+a[j]==k:
                flag=1
                break
    if flag==1:
        return 1
    else:
        return -1
#best solution
def best_two(a,k):
    left=0
    right=len(a)-1
    while left<right:
        if a[left]+a[right]==k:
            return True

        elif a[left]+a[right]>k:
            right=right-1
        else:
            left+=1
a=[3,5,9,2,8,10,11]
b=two_pointer(a,100)
if b==1:
    print("there exist a pair.")
else:
    print("there exist no pair.")
if best_two(a,17)==True:
    print("yes")
else:
    print("false.")