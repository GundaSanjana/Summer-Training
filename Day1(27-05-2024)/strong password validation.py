'''Strong Validation Password
Conditions: min 8 characters,1 uppercase,1 lowercase,1 digit, 1 special character.
ip1:asd123!@#A
op1:-1
ip2:asd123!@#
op2:1
ip3:12345679
op3:3
ip4:ab
op4:6
ip5:A1234b
op5:2
ip6:A1234B
op6:2'''
    
p = input()
u = 0
l = 0
d = 0
s = 0

for char in p:
    if char.isupper():
        u = 1
    elif char.islower():
        l = 1
    elif char.isdigit():
        d = 1
    elif not char.isalnum():
        s = 1

f = sum([u,l,d,s])
if len(p) < 8:
    print(8 - len(p))
else:
    if f == 4:
        print(-1)
    else:
        m = 4 - f
        print(m)


''' or after if and else conditions
m=4-(u+l+d+s)
if(len(p)+m)<8:
    print(8-len(n))
else:
    print(m) '''
