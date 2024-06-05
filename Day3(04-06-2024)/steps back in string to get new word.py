'''Take input from user and string and an integer.The elements of the
string should move backward to interger number of steps
ip1:khoor (k->h(h,i,j),h->e,o->l,o->l,r->o)
    3
op1:hello
ip2:bcdmnwc
    9
op2:student
ip3:bvec
    4
op3:xray '''

a=input()
s=int(input())
res=[]
for i in a:
    b=chr((ord(i)-ord('a')-s)%26+ord('a'))
    res.append(b)
print(''.join(res))

#or
a='bvec'
b=4
c=b%26
d=''
for i in a:
    if((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)
