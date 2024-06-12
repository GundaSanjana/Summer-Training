class Node:
    def __init__(self, u):
        self.data=u
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if(root==None):
            return Node(x)
        elif root.data > x:
            root.left=self.create(root.left, x)
        else:
            root.right=self.create(root.right, x)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def add_all(self,root):
        if root==None:
            return 0
        return root.data+self.add_all(root.left)+self.add_all(root.right)
    def add_even(self,root):
        s=0
        if root==None:
            return 0
        elif(root.data%2==0):
            return s+root.data+self.add_even(root.left)+self.add_even(root.right)
        else:
            return s+self.add_even(root.left)+self.add_even(root.right)
    def add_odd(self,root):
        s=0
        if root==None:
            return 0
        elif root.data%2!=0:
            return s+root.data+self.add_odd(root.left)+self.add_odd(root.right)
        else:
            return s+self.add_odd(root.left)+self.add_odd(root.right)

t1=Tree()
t1.root=t1.create(t1.root,10)
t1.root=t1.create(t1.root,5)
t1.root=t1.create(t1.root,20)
t1.root=t1.create(t1.root,7)
t1.root=t1.create(t1.root,1)
print("Inorder:")
t1.inorder(t1.root)
print("\nPreorder:")
t1.preorder(t1.root)
print("\nPostorder:")
t1.postorder(t1.root)
print()
print("Sum of all nodes:")
print(t1.add_all(t1.root))
print("Sum of all left Nodes:")
print(t1.add_all(t1.root.left))
print("Sum of all right Nodes:")
print(t1.add_all(t1.root.right))
print("Difference between left and right subtree:")
print(abs(t1.add_all(t1.root.left)-t1.add_all(t1.root.right)))
print("Sum of all Even nodes:")
print(t1.add_even(t1.root))
print("Sum of all Odd nodes:")
print(t1.add_odd(t1.root))
print("Difference of Even nodes and Odd node:")
print(abs(t1.add_even(t1.root))-(t1.add_odd(t1.root)))
