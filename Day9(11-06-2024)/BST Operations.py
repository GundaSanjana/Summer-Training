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
    def evensum(self,root):
        if root==None:
            return 0
        elif(root.data%2==0):
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            return self.evensum(root.left)+self.evensum(root.right)
    def oddsum(self,root):
        if root==None:
            return 0
        elif root.data%2!=0:
            return root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            return self.oddsum(root.left)+self.oddsum(root.right)
    def diff_evenoddsum(self,root):
        if root==None:
            return 0
        elif root.data%2==0:
            return root.data+(self.diff_evenoddsum(root.left)+self.diff_evenoddsum(root.right))
        return self.diff_evenoddsum(root.left)+self.diff_evenoddsum(root.right)-root.data
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
            
    def bal(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    
    def no_leafnode(self,root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        return self.no_leafnode(root.left)+self.no_leafnode(root.right)
    def leafnodes(self,root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            print(root.data,end=" ")
            return 1
        return self.leafnodes(root.left)+self.leafnodes(root.right)
    def sum_leafnodes(self,root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return root.data
        return self.sum_leafnodes(root.left)+self.sum_leafnodes(root.right)
    def search(self,root,x):
        if root==None:
            return "Not Found"
        elif root.data==x:
            return "Found"
        elif root.data>x:
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)
    def depth(self,root,x,c):
        if root==None:
            return -1
        elif root.data==x:
            return c
        elif root.data>x:
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)
            
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
print(t1.evensum(t1.root))
print("Sum of all Odd nodes:")
print(t1.oddsum(t1.root))
print("Difference of Even nodes and Odd nodes:")
print(abs(t1.evensum(t1.root))-(t1.oddsum(t1.root)))
print("Difference of Even nodes and Odd nodes:")
print(t1.diff_evenoddsum(t1.root))
print("The height of the tree is:")
print(t1.height(t1.root))
print("The given tree is:")
if(t1.bal(t1.root)):
        print("Balanced")
else:
    print("Not Balanced")
print("The number of leaf nodes are:")
print(t1.no_leafnode(t1.root))
print("The leafnodes are:")
t1.leafnodes(t1.root)
print()
print("The sum of leafnodes is:")
print(t1.sum_leafnodes(t1.root))
print("The element is:")
print(t1.search(t1.root,5))
print("The depth of the element is:")
print(t1.depth(t1.root,7,0))
