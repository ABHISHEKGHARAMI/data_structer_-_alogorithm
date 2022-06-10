# insert  delete update search in array
arr1=[]
def def_insert(arr1,val):
    arr1.append(val)

def def_update(arr1,key,pos):
    if pos> len(arr1) and pos< len(arr1):
        print("Insering can't be done.")
    else:
        arr1.insert(pos-1,key)
def def_delete(arr1,pos):
    if pos> len(arr1) and pos< len(arr1):
        print("deleting can't be done.")
    else:
        data=arr1.pop(pos-1)
        print("data deleted is :",data)

def def_search(arr1,val):
    for i in range(len(arr1)):
        if arr1[i]==val:
            return i+1
            break


def def_print(arr1):
    for i in range(len(arr1)):
        print(arr1[i],end=" ")


def def_largest(arr1):
    arr1=sorted(arr1)
    return arr1[len(arr1)-1],arr1[len(arr1)-2]


def is_sorted(arr1):
    flag=0
    for i in range(len(arr1)-1):
        if arr1[i]>arr1[i+1]:
            flag=1
            break
    if flag==1:
        print("Array is not soretd.")
    else:
        print("Array is sorted")



def reverse_a(arr1):
    i=0
    j=len(arr1)-1
    while i<=j:
        temp=arr1[i]
        arr1[i]=arr1[j]
        arr1[j]=temp
        i+=1
        j-=1
    def_print(arr1)


def remove_duplicate(arr1):
    arr1=set(arr1)
    arr1=list(arr1)
    return arr1
    '''
    new_array=[]
    new_array.append(arr1[0])
    res=1
    for i in range(1,len(arr1)-1):
        if new_array[res-1]!=arr1[i]:
            new_array[res]=arr1[i]
            res+=1
    def_print(new_array)
    '''


while True:
    print("\n")
    print("========options==========")
    print("\n1:insert"," ","2:update"," ","3:delete")
    print("\n4:search"," ","5:show"," ","6:max ans smax")
    print("\n7:check sort"," ","8:reverse"," ","9:remove duplicate")
    print("\n0:end")
    print("=========================")
    choice=int(input("enter the choice :"))
    if choice==1:
        val=int(input("enter the value to be insert :"))
        def_insert(arr1,val)
        print("Inserted data.")
    elif choice==2:
        key,pos=map(int,input("enter the value and position to be update :").split(","))
        def_update(arr1,key,pos)
        print("value updated.")
    elif choice==3:
        pos=int(input("enter the position for deletion :"))
        def_delete(arr1,pos)
        print("data deleted.")
    elif choice==4:
        key=int(input("enter the data to searched."))
        pos=def_search(arr1,key)
        if pos<=0:
            print("The data is not present in the array.")
        else:
            print("\nThe data is presen in the position of :",pos)
    elif choice==5:
        print("printing data.......")
        def_print(arr1)
    elif choice==6:
        larg,slar=def_largest(arr1)
        print("The largest and second largest element is",larg,"\t and ",slar)
    elif choice==7:
        print("checking.....")
        is_sorted(arr1)
    elif choice==8:
        print("reversing array.....")
        reverse_a(arr1)
    elif choice==9:
        print("removing duplicate.....")
        def_print(remove_duplicate(arr1))
    elif choice==0:
        break
    else:
        print("wrong choice!!")

