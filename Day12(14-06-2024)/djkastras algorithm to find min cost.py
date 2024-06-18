d={5:[(7,1),(3,2)],7:[(5,1) ,(4,2),(3,8)],4:[(7,2),(8,9),(2,7)],8:[(3,4),(4,9),(2,6)],3:[(5,3),(7,8),(8,4)],2:[(4,7),(8,6)]}
def dj(d,start):
    visi=set()
    dis={node:float('inf')for node in d}
    dis[start]=0
    queue=[(0,start)]
    while queue:
        c,node=min(queue)
        queue.remove((c,node))
        if node not in visi:
            print(node)
            visi.add(node)
            if node in d:
                for nei,wt in d[node]:
                    if dis[node]+wt<dis[nei]:
                        dis[nei]=dis[node]+wt
                        queue.append((dis[nei],nei))
    return dis
print(dj(d,5))

#or
g={5:[(3,1),(1,2),(6,3)],1:[(5,2),(2,1)],3:[(5,1),(6,3)]}
def fun(g,x):
    d={5:9999,1:9999,3:9999,6:9999,2:9999}
    d[x]=0
    vi=[]
    q=[x]
    while(q):
        m=9999
        if i in q:
            if(d[i]<m):
               m=d[i]
               x=i
        for i in g[x]:
            if(i[0] not in vi):
                q.append(i[0])
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        vi.append(x)
        q.remove(x)
    return d
fun(g,5)
