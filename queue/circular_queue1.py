#circular queue implementation in python
class structer:
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(self.size)]
        self.front=self.rear=-1


    #function for the enQueue for the queue
    def enQueue(self,element):
        if (self.rear+1)%self.size==self.front:
            print("Queue is full...")
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=element
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=element
    #function for deQueue for the queue
    def deQueue(self):
        if self.front==-1:
            print("The Queue is empty.")
        elif self.front==self.rear:
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    #function for the print the queue
    def print_queue(self):
        if self.front==-1:
            print("The queue is empty..")
        elif self.rear>self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
        else:
            for i in range(0,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if (self.front+1)%self.size==self.rear:
            print("Queue is full.")
#calling the main function
size=int(input("Enter the number of the total size of the queue:"))
q1=structer(size)
while True:
    print("\n1:for enqueue.\n2:for dequeue.\n3:for print queue.\n4:for exit.")
    choice=int(input("Enter the choice:"))
    if choice==1:
        ele=int(input("Enter the element:"))
        q1.enQueue(ele)
    elif choice==2:
        x=q1.deQueue()
        print("{} deleted from the queue.".format(x))
    elif choice==3:
        q1.print_queue()
    elif choice==4:
        exit(0)
    else:
        print("error! choice!!!")
