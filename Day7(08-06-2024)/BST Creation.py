def fun(root):
    if(root==None):
        root=node(x)
    elif(x<root.data):
        fun(root.left)
    else:
        fun(root.right)
