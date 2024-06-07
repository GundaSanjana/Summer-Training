class node:
    def __init__(self,a):
        self.data=a
        self.nxt=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
        print()
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail = self.tail.nxt
            #self.tail.nxt=node(x)
            #self.tail.nxt.prev=self.tail
            #self.tail=self.tail.nxt
    def addfront(self,x):
        new_node = node(x)
        if self.head is None:
            self.head = node(x)
            self.tail = node(x)
        else:
            t=node(x)
            t.nxt = self.head
            self.head.prev = t
            self.head = t
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    def search(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
        #(or)while(t!=t1.nxt and t.prev.prev!=t1):
            if t.data==x or t1.data==x:
                return "Found"
            t=t.nxt
            t1=t1.prev
        if(t.data==x):
            return "Found"
        return "Not Found"
    def checklen(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            t=t.nxt
            t1=t1.prev
        if(t==t1):
            return "Odd"
        else:
            return "Even"
    def palindrome(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if t.data!=t1.data:
                return "Not Palindrome"
            t=t.nxt
            t1=t1.prev
        return "Palindrome"
    def find_middle(self):
        f=self.head
        s=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        print(s.data)
    def interchange(self):
        '''f=self.head
        s=self.head
        while(f!=None):
            f=f.nxt.nxt
            s=s.nxt
        t=self.head
        t1=s
        while(t1!=None):
            t.data,t1.data=t1.data,t.data
            t1=t1.nxt
            t=t.nxt'''
        f=self.head
        s=self.head
        while(f!=None):
            f=f.nxt.nxt
            s=s.nxt
        self.tail.nxt=self.head
        self.head.prev=self.tail
        t1=self.prev
        t1.nxt=None
        self.prev=None
        self.head=s
        self.tail=t1


        
l1=dll()
#l1.head=node(5)
#l1.tail=l1.head
l1.addback(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addback(60)
l1.addback(70)
l1.addfront(5)
l1.display()
l1.rev_display()
print(l1.search(30))
print(l1.search(90))
print(l1.checklen())
print(l1.palindrome())
l2=dll()
l2.addback(1)
l2.addback(2)
l2.addback(3)
l2.addback(2)
l2.addback(1)
l2.display()
print(l2.palindrome())
l1.interchange()
