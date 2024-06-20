#Calculate the number of houses the sunrays falls in morning & evening.
'''ip:3 5 9 6 8 10
op:{9,10,3,5}(10)'''
arr=list(map(int,input().split(" ")))
l=[0]*len(arr)
r=[0]*len(arr)
m,m1=0,0
s,c1,c2=0,0,0
for i in range(len(arr)):
    if arr[i]>m:
        m=arr[i]
        c1+=1
    l[i]=m
for i in range(len(arr)-1,-1,-1):
    if arr[i]>m1:
        m1=arr[i]
        c2+=1
    r[i]=m1
print(set(l),set(r))
print(c1,c2)
