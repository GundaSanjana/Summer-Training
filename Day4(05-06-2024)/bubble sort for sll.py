class node:
    def __init__(self, u):
        self.data = u
        self.nxt = None

class sll:
    def _init_(self):
        self.head = None

    def display(self):
        t = self.head
        while t != None:
            print(t.data, end="->")
            t = t.nxt

    def addback(self, x):
        if not self.head:
            self.head = node(x)
        else:
            t = self.head
            while t.nxt != None:
                t = t.nxt
            t.nxt = node(x)
    def bsort(self):
        c=0
        T=self.head
        p=None
        while (T.nxt!=None):
            f=0
            t=self.head
            while(t.nxt!=p):
                if(t.data>t.nxt.data):
                    f=1
                    t.data,t.nxt.data=t.nxt.data,t.data
                t=t.nxt
                c=c+1
            if(f==0):
                break
            p=t
            T=T.nxt

l1 = sll()
l1.head = node(6)
l1.addback(7)
l1.addback(4)
l1.addback(8)
l1.addback(4)
l1.addback(2)
l1.addback(0)
l1.addback(1)
l1.display()
print()
b=l1.bsort()
l1.display()
print(b)
