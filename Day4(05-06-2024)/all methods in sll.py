#sll all methods
'''display,addfront,addback,addeven,2 sll,search,middle,
checklength even or odd,largest subsequence length,allpairs,bubblesort'''
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
    def larsub(self):
        t=self.head
        c=1
        m=1
        while(t.nxt!=None):
            if(t.data==t.nxt.data-1):
                c+=1
            else:
                if(c>m):
                    m=c
                c=1
            t=t.nxt
        if(c>m):
            m=c
        print(m)
    def allpairs(self):
        t=self.head
        while(t.nxt!=None):
            t1=t.nxt
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.nxt
            t=t.nxt
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
l1.checklen()
l1.larsub()
l1.allpairs()
l3=sll()
l3.head =node(6)
l3.addback(7)
l3.addback(9)
l3.addback(8)
l3.addback(4)
l3.addback(2)
l3.addback(0)
l3.addback(1)
l3.display()
print()
l3.larsub()
b=l3.bsort()
l3.display()
print(b)



