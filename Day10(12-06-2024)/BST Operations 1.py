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
    def leftview(self,root,c,l):
        if root==None:
            return 
        if(c not in l):
            l.append(c)
            print(root.data,end=" ")
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)  
    def rightview(self,root,c,l):
        if root==None:
            return 
        if(c not in l):
            l.append(c)
            print(root.data,end=" ")
        self.rightview(root.left,c+1,l)
        self.rightview(root.right,c+1,l)
    '''def topview(self,root,d,q):
        if root==None:
            return
        d={}
        q=[(root,0)]
        while():
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            if(q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")''' #not working
    '''def topview(self,root):
        if root is None:
            return []
        top_view_map = {}
        queue = [(root, 0)]
        while queue:
            node, hd = queue.pop(0)
            if hd not in top_view_map:
                top_view_map[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        top_view_list = [top_view_map[hd] for hd in sorted(top_view_map.keys())]
        return top_view_list '''
    def topview(self, root):
        if root is None:
            return None
        d = {}
        q = [(root, 0)]
        while q:
            node, hd = q.pop(0)
            if hd not in d:
                d[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        for key in sorted(d):
            print(d[key], end=" ")
        print()
    def bottomview(self, root):
        if root is None:
            return None
        d = {}
        q = [(root, 0)]
        while q:
            node, hd = q.pop(0)
            d[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        for key in sorted(d):
            print(d[key], end=" ")
        print()
     
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
print("Left View:")
t1.leftview(t1.root,0,[])
print()
print("Right View:")
t1.rightview(t1.root,0,[])
print()
print("Top View:")
t1.topview(t1.root)
print("Bottom View:")
t1.bottomview(t1.root)
