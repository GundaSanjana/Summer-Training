#ip:MMFFMFFMFMFMFFMMFFMMF
s='MMFFMFFMFMFMFFMMFFMMF'
c1,c2=0,0
for i in s:
    if i=='M':
        c1+=1
    else:
        c2+=1
if c1==c2:
    print(0)
elif c1>c2:
    print("M")
elif c2>c1:
    print("F")

#or To reduce space complexity
s='MMFFMFFMFMFMFFMMFFMMF'
c=0
for i in s:
    if i=='M':
        c+=1
    else:
        c-=1
if c==0:
    print(0)
elif c>0:
    print("M")
elif c<0:
    print("F")
