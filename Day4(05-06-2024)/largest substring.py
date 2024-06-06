class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def larsub(self):
        t=self.head
        c=1
        m=1
        while(t.nxt!=None):
            if(t.data==t.nxt.data-1):
                c=c+1
            else:
                if(c>m):
                    m=c
                c=1
            t=t.nxt
        if(c>m):
            m=c
        print(m)
          
l1=sll()
l1.head=node(1)
l1.addback(2)
l1.addback(3)
l1.addback(4)
l1.addback(5)    
l1.addback(6)
l1.addback(7)
l1.addback(8)
l1.display()
print()
l1.larsub()
