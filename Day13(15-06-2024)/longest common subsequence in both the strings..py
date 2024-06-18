#longest common subsequence in both the strings.
'''ip:abcd
   axbdc
op:abd'''

s1="abcd"
s2="axbdc"
u=len(s1)
v=len(s2)
m=[]
s=""
for i in range(u+1):
    l=[0]*(v+1)
    m.append(l)
for i in range(1,u+1):
        for j in range(1,v+1):
            if(s1[i-1]==s2[j-1]):
                m[i][j]=m[i-1][j-1]+1
            else:
                m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[u][v])
while(u>0 and v>0):  #or u!=0 and v!=0
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u-1][v]>m[u][v-1]):
            u=u-1
        else:
            v=v-1
s=s[::-1]
print(s)

#or #2nd answer
s1="abcd"
s2="axbdc"
u=len(s1)
v=len(s2)
m=[]
s=""
for i in range(u+1):
    l=[0]*(v+1)
    m.append(l)
for i in range(1,u+1):
        for j in range(1,v+1):
            if(s1[i-1]==s2[j-1]):
                m[i][j]=m[i-1][j-1]+1
            else:
                m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[u][v])
while(u>0 and v>0):  #or u!=0 and v!=0
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u][v]>m[u-1][v]):
            v=v-1
        else:
            u=u-1
s=s[::-1]
print(s)
