#function for the sort using the stack
def sorted_insert_stack(s,element):
    if len(s)==0 or element>s[-1]:
        s.insert(-1,element)
        return
    else:
        temp=s.pop()
        sorted_insert_stack(s,element)
        s.append(temp)
#function for the simple sort of the stack
def sort_stack(s):
    if len(s)!=0:
        temp=s.pop()
        sort_stack(s)
        sorted_insert_stack(s,temp)
#calling the function
ar=[18,14,13,-3]
s=[]
for i in ar:
    s.append(i)
print("\nbefore the sorting the stack:",s,end=" ")
sorted_insert_stack(s,-5)
print("\nafter the sorting the stack:",s,end=" ")
print("\nbefore the sorting the entire stack is:",s,end=" ")
sort_stack(s)
print("\n after the sorting the entire stack is:",s,end=" ")
