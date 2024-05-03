class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None
class cdll:
    def __init__(self) -> None:
        self.head=None
    def insertaatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
        self.tail.next=self.head
        self.head.prev=self.tail
        return self.head

    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:#in dll no need of traversing to add ele at last bcoz we have
            new=node(data)#tail pointer we can use that
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
        self.tail.next=self.head
        self.head.prev=self.tail
    def printing(self):
        print(self.head.data)
        i=self.head.next
        while i!=self.head:
            print(i.data,end=' ')
            i=i.next    
l=[1,2,3,4,5]
c=cdll()
for i in l:
    c.insertaatbeg(i)
    c.insertatend(i)
c.printing()
for i in l:
    c.insertatend(i)
c.printing()    
