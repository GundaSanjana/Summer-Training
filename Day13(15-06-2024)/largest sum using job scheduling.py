'''ip:[(1,3) (2,5) (4,6) (6,7) (5,8) (7,9)]
   [5,6,5,4,11,2]
op:17'''

jobs=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
for i in range(1,len(a)):
    for j in range(0,i):
        if(jobs[j][1]<=jobs[i][0]):
            if(b[j]+a[i]>b[i]):
                b[i]=b[j]+a[i]
print(max(b))
