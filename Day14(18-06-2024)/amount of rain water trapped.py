'''Given the height of different buildings. If ir rains calculate the
amount of water trapped.'''
'''ip:
    [2,5,2,3,6,7,1,0,5,7]
op:20
         |   |
        ||   |
     |  ||  ||
     |  ||  ||
     | |||  ||
    ||||||  ||
    ||||||| || '''

'''ip:[2,5,2,3,6,7,1,0,5]
op:14'''

'''ip:[4,3,4,5,6,1,0,6,7]
op:12'''

'''l=list(map(int,input().split(",")))  
l1=l.copy()
r=[]
c=0
j=len(l)-1
for i in range(0,len(l)-1):
    if(l1[i]>l1[i+1]):
        l1[i+1]=l1[i]
for i in range(len(l1)):
    r.append(max(l1))
    if l1[i]<=r[i]:
        c+=l1[i]-l[i]
print(c)'''

arr=list(map(int,input().split(",")))
l=[0]*len(arr)
r=[0]*len(arr)
m,m1=0,0
s=0
for i in range(len(arr)):
    if arr[i]>m:
        m=arr[i]
    l[i]=m
for i in range(len(arr)-1,-1,-1):
    if arr[i]>m1:
        m1=arr[i]
    r[i]=m1
for i in range(len(arr)):
    s=s+abs(min(l[i],r[i])-arr[i])
print(s)
    
