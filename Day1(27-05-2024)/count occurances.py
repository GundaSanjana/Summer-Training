'''Take input as list & count the number of occurances of each element.
ip:
    3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
op:
    3 - 4
    5 - 1
    4 - 2
    6 - 2
    7 - 2
    1 - 1
    2 - 1
    8 - 2'''

def count_occurances(arr):
    c={}
    for i in arr:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
    for i,count in c.items():
        print(f'{i} - {count}')
arr=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
count_occurances(arr)

#Second Method
a=list(map(int,input().split(',')))
b=[]
for i in a:
    if(i not in b):
        b.append(i)
for i in b:
    print(i,"-",a.count(i))
