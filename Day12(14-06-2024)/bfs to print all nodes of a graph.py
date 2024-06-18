d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
q=[]
v=[]
s=5
q.append(s)
while q:
    c=q.pop(0)
    if c not in v:
        v.append(c)
        for i in d[c]:
            if i not in v:
                q.append(i)
print(v)

#or
def bfs(d,n):
    v=[]
    q=[n]
    while(q):
        for i in d[q[0]]:   #d[n] or d[q[0]]
            if(i not in q and i not in v):
                q.append(i)
        v.append(q.pop(0))
        print(v[-1],end=" ")
        
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}              
bfs(d,5)
print()
d={2:[1],1:[1,2,5],4:[5,1],5:[1,4,6],6:[5]}
bfs(d,2)
