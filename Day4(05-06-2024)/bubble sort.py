a=[4,3,8,2,9,6]
c=0
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
        c=c+1
print(a,c)
#output=[2,3,4,6,8]25

#or
a=[4,3,8,2,9,6]
c=0
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
        c=c+1
print(a,c)
#output=[2,3,4,6,8]15 c=no of iterations

#or
a=[4,3,8,2,9,6]
c=0
for i in range(len(a)-1):
    f=0
    for j in range(len(a)-1):
        if(a[j]>a[j+1]):
            f=1
            a[j],a[j+1]=a[j+1],a[j]
        c=c+1
    if(f==0):
        break
print(a,c)
#output=[2,3,4,6,8]20

#or
a=[4,3,8,2,9,6]
c=0
for i in range(len(a)-1):
    f=0
    for j in range(len(a)-1-i):
        if(a[j]>a[j+1]):
            f=1
            a[j],a[j+1]=a[j+1],a[j]
        c=c+1
    if(f==0):
        break
print(a,c)
#output=[2,3,4,6,8]14
