'''Take an integer and reverse it using recursion and then check if it
is palindrome or not.
ip:12321
op:palindrome '''

def fun(x,re):
    if(x==0):
        return re
    re=re*10+(x%10)
    return fun(x//10,re)
n=int(input())
if(n==fun(n,0)):
    print("palindrome")
else:
    print("not palindrome")

