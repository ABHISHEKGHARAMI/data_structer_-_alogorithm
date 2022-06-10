def b_search(a,start,end,key):
    if start<end:
        mid=(start+end)//2
        if a[mid]==key:
            return mid+1
        elif a[mid]>key:
            return b_search(a,start,mid-1,key)
        else:
            return b_search(a,mid+1,end,key)
a=[1,2,3,4,5]
print(b_search(a,0,len(a),3))