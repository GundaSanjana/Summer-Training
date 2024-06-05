'''Take input from user as string and print yes if string is in
format else print no.(format-first letter from first row,seond letter
from second row,third letter from third row ans so on.
ip1:
    3
    xyz
    pqr
    abc
    'yraxpazr'
op1:
    yes
ip2:
    4
    abcd
    xyze
    pqrw
    stuv
    'cyptdzsayq'
op2:no 


n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
for i in range(len(s)):
    if s[i] not in m[i%n]:
        print("no")
        break
else:
    print("yes")'''

#or
'''n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
f=1
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        f=0
        break
if(f==1):
    print("yes")
else:
    print("no")'''

    
#Another question
'''ip1:
    3
    xyz
    pqr
    abc
    'yraxpazr'
op1:
    no (no repeatation allowed)
ip2:
    3
    xyz
    pqr
    abc
    'yraxpbzr'
op2:
    yes
ip3:
    3
    xxx
    pqr
    abc
    'xraxpbxr'
op3:
    yes '''

n=int(input())
matrix=[]
for i in range(n):
    row=input()
    matrix.append(row)
s=input()
f=0
for i in range(len(s)):
    if s[i] not in matrix[i%n]:
        print("no")
        break
else:
    print("yes")





