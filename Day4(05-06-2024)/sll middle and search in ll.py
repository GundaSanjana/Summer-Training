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
    def addfront(self,x):
        t=node(x)
        t.nxt=self.head
        self.head=t
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.nxt
        print(s)
    def search(self,key):
        t = self.head
        while t!=None:
            if t.data == key:
                return True
            t = t.nxt
        return False
    def middle(self):
        f=self.head
        s=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        print(s.data)
l1=sll()
l1.head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addback(60)
l1.addfront(7)
l1.addfront(5)
l1.display()
print()
l2=sll()
l2.head=node(100)
l2.addback(200)
l2.addback(300)
l2.display()
print()
l1.addeven()
l2.addeven()
print(l1.search(30))
l1.middle()
