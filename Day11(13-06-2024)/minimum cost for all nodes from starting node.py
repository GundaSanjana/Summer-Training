#Minimum Cost
def fun(d,x,e,c,m,l1):
    l.append(x)
    if(x==e):
        if(c<m):
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=fun(d,i[0],e,c+i[1],m,l1)
    l.pop()
    return m,l1
d={5:[(7,2),(3,1)],7:[(5,2),(4,6),(3,2)],4:[(7,6),(8,1),(2,2)],
   8:[(3,3),(4,1),(2,1)],3:[(5,1),(7,2),(8,3)],2:[(4,2),(8,1)]}
l=[]
for i in d.keys():
    print(fun(d,5,i,0,99999,[]))
