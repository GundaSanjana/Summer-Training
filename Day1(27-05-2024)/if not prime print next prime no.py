'''Take a number from user check if it is prime or not if it is prime
number print it if it is not a prime number print the next prime number
ip1:13
op1:13
ip2:14
op2:17'''

n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
    #reduced from (1,n+1) to (2,n) to (2,(n//2)+1) to reduce time complexity.
    #it also increased efficiency.
        if(n%i==0):
            c+=1
            break
    if(c==0):           #reduced from c==2 to c==0
        print(n)
        break
    else:
        n=n+1
    

        
