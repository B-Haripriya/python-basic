class node:
        def __init__(self,data) -> None:
          self.data=data
          self.next=None
class sll:
    def __init__(self) -> None:
        self.head=None
    def insertatfront(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def rev(self):
            curr=self.head
            prev=None
            n=self.head.next
            while curr:
                curr.next=prev
                prev=curr
                curr=n
                if n:   
                  n=n.next
            self.head=prev            

    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=node(data)
            i=self.head
            while i.next:
              i=i.next
            i.next=temp      
    def printing(self):
        if self.head==None:
            return 
        i=self.head
        while i!=None:#also we can just write 'while i"
            print(i.data,end=' ')
            i=i.next
    def length(self):
        c=0
        i=self.head
        while i:
            c+=1
            i=i.next
        return c                   
l=[1,2,3,4,5]
o=sll()
for i in l:  
    o.insertatfront(i)
    #o.insertatend(i)          
o.printing()
o.rev()     
o.printing()                  
#print(o.length())      
