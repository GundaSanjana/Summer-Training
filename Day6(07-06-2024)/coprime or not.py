#Coprime numbers or not
def gcd(a, b):
    while b!=0:
        a,b=b,a%b
    return a
n1=int(input())
n2=int(input()) 
if gcd(n1,n2)==1:
    print(n1,n2,"are coprime")
else:
    print(n1,n2,"are not coprime.")

#or
import math
n1=int(input())
n2=int(input()) 
g=math.gcd(n1,n2)
if g==1:
    print("Coprimes")
else:
    print("Not Coprimes")

#or
a=3
b=9
for i in range(2,(min(a,b)//2)+1):
    if(a%i==0) and (b%i==0):
        print("Not Co-primes")
        break
else:
    print("Co-primes")
