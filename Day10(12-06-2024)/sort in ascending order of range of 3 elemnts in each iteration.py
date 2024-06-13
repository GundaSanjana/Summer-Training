#sort in ascending order of range of 3 elements in each iteration
'''ip:
    [4,9,8,2,14,3,5,6]
steps:
    4 8 9 2 14 3 5 6
      2 8 9 14 3 5 6
        8 9 14 3 5 6
          3 9 14 5 6
            5 9 14 6
              6 9 14
op:
    4 2 8 3 5 6 9 14'''

a=list(map(int,input().split(",")))
for i in range(len(a)-2):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1]>a[i+2]):
        a[i+1],a[i+2]=a[i+2],a[i+1]
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
print(a)

#or logic
'''a[0]=min(9,8,1)
a[2]=max(9,8,1)
a[1]=s-a[2]-a[0]'''
