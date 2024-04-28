class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_end(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newNode
    def insert_at_beginning(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def display(self):
        current=self.head
        while current:
            print(current.data, end="-> ")
            current=current.next
    def insert_at_position (self,data,position):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            count=0
            while current:
                count+=1
                if count==position-1:
                    newNode.next=current.next
                    current.next=newNode
                    break
                current=current.next
            if count<position-1:
                self.insert_at_end(data)
                
    def search(self,key):
        current=self.head
        count=0
        while current:
            count=count+1
            if current.data==key:
                print("data found at position",count)
                count=-1
                break
            current=current.next
        if count!=-1:
            print("data is not found")

                
obj=linkedlist()
obj.insert_at_beginning(1)
obj.insert_at_beginning(3)
obj.insert_at_beginning(14)
obj.search(1)