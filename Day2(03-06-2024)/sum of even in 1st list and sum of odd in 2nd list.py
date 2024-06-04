'''Using recursion print sum of even numbers of first list and odd
numbers of second list.
ip:
a=[3,8,5,4,3]
b=[5,0,9,3,2]
op: (12,17) '''
def fun(x,s1,s2):
    if(x==len(a)):
        return s1,s2
    if(a[x]%2==0):
        s1=s1+a[x]
    if(b[x]%2!=0):
        s2=s2+b[x]
    return fun(x+1,s1,s2)
a=[3,8,5,4,3]
b=[5,0,9,3,2]
x,y=fun(0,0,0)
print(x,y)


    
