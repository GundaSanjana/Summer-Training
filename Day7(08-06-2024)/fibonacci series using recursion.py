def fun(x):
    if(x==1 or x==2):
        return 1
    return fun(x-1)+fun(x-2)
for i in range(1,10):
    print(fun(i),end=" ")

