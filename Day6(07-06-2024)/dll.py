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
    def interchange(self):   #works only for even length
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
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        self.tail.nxt=self.head
        self.head.prev=self.tail
        t1=s.prev
        t1.nxt=s.prev
        s.prev=None
        s.head=None
        self.tail=t1
    '''def swap(self):   #works only for even length
       t=self.head
       t1=t.nxt
       t3=None
       while(t!None):
           t.nxt=t1.nxt
           t1.nxt=t
           t1.prev=t3
           t.prev=t1
           h=t1 #for first t3.nxt=t1 for remaining iterations
           t,t1=t1,t
           t3=t1'''  
    def swap(self):     #works only for even length
        if not self.head or not self.head.nxt:
            return
        t=self.head
        self.head=t.nxt 
        while t and t.nxt:
            t1=t.nxt
            t3=t1.nxt
            t1.nxt=t
            t1.prev=t.prev
            t.nxt=t3
            t.prev=t1
            if t3:
                t3.prev=t
            if t1.prev:
                t1.prev.nxt=t1
            t=t3
    def parbal(self):
        stack=[]
        t=self.head
        index=1
        while t is not None:
            if t.data=='(' or t.data=='[' or t.data=='{':
                stack.append((t.data,index))
            elif t.data==')' or t.data==']' or t.data=='}':
                if not stack:
                    print(index)
                    return
                top,top_index=stack.pop()
                if(top=='(' and t.data!=')') or  (top=='[' and
                        t.data!=']') or (top=='{' and t.data!='}'):
                    print(index)
                    return
            t=t.nxt
            index+=1
        if stack:
            top_index=stack.pop()
            print(top_index)
        else:
            print(-1)
    def diff_evenoddsum(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.diff_evenoddsum(t.nxt,es,os)
    def even_odd_sum(self):
        def recur(node):
            if node is None:
                return 0,0
            ev,odd=recur(node.nxt)
            if node.data%2==0:
                ev+=node.data
            else:
                odd+=node.data
            return ev,odd
        ev,odd=recur(self.head)
        return ev-odd
    def is_prime(self,n,i=2):
        if n<=2:
            return True if n==2 else False
        if n%i==0:
            return False
        if i*i>n:
            return True
        return self.is_prime(n,i+1)
    def count_primes(self):
        def recur(node):
            if node is None:
                return 0
            if self.is_prime(node.data):
                return 1 + recur(node.nxt)
            else:
                return recur(node.nxt)
        return recur(self.head)
    def pr(self,t,c):
        if(t==None):
            return c
        def pnt(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return pnt(s+1,n)
        if(pnt(2,t.data)):
                c=c+1
        self.pr(t.nxt,c)
            
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
l2.interchange()
l3=dll()
l3.addback(1)
l3.addback(2)
l3.addback(3)
l3.addback(4)
l3.addback(5)
l3.addback(6)
l3.display()
l3.swap()
l3.display()
l4=dll()
l4.addback('[')
l4.addback('{')
l4.addback('(')
l4.addback(')')
l4.addback(']')
l4.addback(']')
l4.display()
l4.parbal()
l5=dll()
l5.addback('[')
l5.addback('(')
l5.addback(')')
l5.addback('{')
l5.addback('}')
l5.addback('{')
l5.addback('(')
l5.addback(')')
l5.addback('}')
l5.addback(']')
l5.display()
l5.parbal()
print(l1.even_odd_sum())
print(l1.diff_evenoddsum(l1.head,0,0))
print(l1.count_primes())
print(l1.pr(l1.head,0))
