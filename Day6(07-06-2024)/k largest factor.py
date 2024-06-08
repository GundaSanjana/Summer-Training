#Find the kth last factor of a number
'''ex:
ip:n=12 k=3
op:[1, 2, 3, 4, 6, 12]
    4 '''
n=int(input())
k=int(input())
f=[]
for i in range(1,n+1):
    if(n%i==0):
        f.append(i)
print(f)
if(k<len(f)):
    print(f[-k])
