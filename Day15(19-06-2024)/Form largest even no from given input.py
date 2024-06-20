#From the given input take the integers and form largest even no.
'''ip:tu5g2k1h8
      g5g8gd6h3
op:865312 '''

s1=input()
s2=input()
s=set()
for i in s1:
    if i.isdigit():
        s.add(i)
for i in s2:
    if i.isdigit():
        s.add(i)
d=list(sorted(s,reverse=True))
if(int(d[-1])%2==0):
    print(''.join(d))
else:
    for i in range(len(d)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop(i))
            print(''.join(d))
            break
        else:
            print(-1)
        

