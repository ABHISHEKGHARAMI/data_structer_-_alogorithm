#python structer for basic operation
q=[]
def enQueue(element):
    q.append(element)
    print("{} is added in the Queue.")
def isEmpty():
    return True if len(q)==0 else False
def deQueue():
    if isEmpty()==True:
        print("The queue is underflowing.")
    else:
        ele=q.pop(0)
        return ele
def print_queue():
    for i in range(len(q)):
        print(q[i],end=" ")

while True:
    print("\n1:for Enqueue.\n2:check for empty.\n3:for Dequeue.")
    choice=int(input("Enter the choice:"))
    if choice==1:
        ele=int(input("Enter element to insert in the queue:"))
        enQueue(ele)
    elif choice==2:
        x=isEmpty()
        if x==True:
            print("The queue is empty.")
    elif choice==3:
        x=deQueue()
        print("{} is deleted from the queue.".format(x))
    elif choice==4:
        print_queue()
    elif choice==5:
        exit(0)
    else:
        print("error choice!!!")