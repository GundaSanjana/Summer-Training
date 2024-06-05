'''Pattern
ip:5
op:
    * * * * *
    * 1 2 3 *
    * 4 5 6 *
    * 7 8 9 *
    * * * * *  '''
a=4
k=1
for i in range(4):
    for j in range(4):
        if(i==0 or j==0 or i==a-1 or j==a-1):
            print("* ",end='')
        else:
            print(k,end=' ')
            k=k+1
    print()
