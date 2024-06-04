'''Using recursion find sum of even numbers for given range.
ip:10
op:30 (2+4+6+8+10)   '''
def fun(x):
    if(x==0):
        return 0
    return x+fun(x-2)

n=10
if(n%2==0):
    print(fun(n))
else:
    print(fun(n-1))
