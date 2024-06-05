'''Print the length of longest substring which is in sequence.
ip:"xyzabcdefklmnopqefgh"
op:7'''
s=input()
c=1
m=0
for i in range(len(s)-1):
    if ord(s[i])==ord(s[i+1])-1:
        c+=1
    else:
        if c>m:
            m=c
        c=1
if c>m:
    m=c
print(m)

