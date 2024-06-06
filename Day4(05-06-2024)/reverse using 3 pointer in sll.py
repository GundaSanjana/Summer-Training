class node:
    def __init__(self, u):
        self.data = u
        self.nxt = None

class sll:
    def __init__(self):
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
    def reverse(self):
        p = None
        t = self.head
        while t:
            temp = t.nxt
            t.nxt = p
            p = t
            t = temp
        self.head = p
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
l1.reverse()
l1.display()

