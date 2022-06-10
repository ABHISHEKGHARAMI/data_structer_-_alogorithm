# print out the first and last occurence of a given number
def reverse(a):
    i=0
    j=len(a)-1
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=1
        j=j-1

#first occurence
def first(a,k):
    flag=0
    for i in range(len(a)):
        if a[i]==k:
            flag=1
        
            break
    if flag==1:
        return i+1
    else:
        return -1
#last occure
def last(a,k):
    flag=0
    reverse(a)
    for i in range(len(a)):
        if a[i]==k:
            flag=1
            break
    if flag==1:
        return len(a)-i
    else:
        return -1

#count occrence of the given key
def count(a,k):
    count=0
    for i in range(len(a)):
        if a[i]==k:
            count+=1
    return count

a=[1,2,3,3,4,5]
print("First Occurence :",first(a,2))
print("Last Occurence :",last(a,2))
print("The Frequency of the occurence of the given data is  :",count(a,3))