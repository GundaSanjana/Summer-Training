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
    def checklen(self):
        f=self.head
        s=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        if(f==None):
            print("Even")
        else:
            print("Odd")
    def allpairs(self):
        t=self.head
        while(t.nxt!=None):
            t1=t.nxt
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.nxt
            t=t.nxt
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
l1.checklen()
l1.allpairs()
