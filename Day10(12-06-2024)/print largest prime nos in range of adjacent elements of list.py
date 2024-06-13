#print largest prime nos in range of adjacent elements of list
'''ip:
    [4,8,14,22,36,68]
op:
    sum of (7 13 19 31 67)
    137'''

def prime(b):
    for i in range(2,(b//2)+1):
        if b%i==0:
            return 0
    return 1
def lar_prime(n,m):
    for i in range(m-1,n,-1):
        if(prime(i)):
            return i
    return 0
a=list(map(int,input().split(",")))
s=0
for i in range(0,len(a)-1):
    s=s+(lar_prime(a[i],a[i+1]))
print(s)
