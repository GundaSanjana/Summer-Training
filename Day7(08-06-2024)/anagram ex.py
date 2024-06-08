#TCS Codevita Question
'''ip:
    school
    3
    L 2  --->hoolsc
    R 3  --->oolsch
    L 1  --->chools
#hoc is anagram of substring (sch,cho,hoo,ool)
op:
    yes'''

s='school'
n = len(s)
l,r,l2='','',''
for i in range(n):
    for j in range(i, n):
        a=s[i:j + 1]
    if n==1:
        l= s[n:] + s[:n]
    if n==2:
        l2= l= s[n:] + s[:n]
    if n==3:
        r= s[-n:] + s[:-n]
    new_string=l+r+l2
if new_string in a:
   print('yes')
else:
    print('no')

#or    #s using string
a=input()
n=int(input())
s=''
for i in range(n):
    b=input()
    if b[0]=='L':
        s=s+a[int(b[2])]
    else:
        s=s+a[-int(b[2])]
print(s)
s=list(s)
s.sort()
b=[]
for i in range(len(a)-n+1):
    t=list(a[i:n+i])
    t.sort()    
    b.append(t)
for i in b:
    if(i==s):
        print("yes")
        break
else:
    print("no")

#or   #s using list
a=input()
n=int(input())
s=[]
for i in range(n):
    b=input()
    if b[0]=="L":
        s.append(a[int(b[2])])
    else:
        s.append(a[-int(b[2])])
print(s)
s.sort()
b=[]
for i in range(len(a)-n+1):
    t=sorted(list(a[i:n+i]))
    b.append(t)
for i in b:
    if(i==s):
        print("Yes")
        break
else:
    print("No")

  
