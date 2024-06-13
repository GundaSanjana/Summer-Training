'''ip:
    "hello:5438,car:214,book:8799,apple:2187"
op:
    oaxp'''

a=input().split(",")
s=''
for i in a:
    b=i.split(":")
    l1=len(b[0])
    if(str(l1) in b[1]):
        s=s+b[0][-1]
    else:
        for i in range(l1-1,0,-1):
            if(str(i) in b[1]):
                s=s+b[0][i-1]
                break
        else:
            s=s+'x'
print(s)
 
#or
inp = "hello:5438,car:214,book:8799,apple:2187"
def leng(x, y):
    xi = len(x)
    while xi not in map(int, str(y)):
        xi -= 1
        if xi < 1:
            return 0  # Return xi if it becomes less than 1
    return xi
s = ''
for i in inp.split(','):
    x, y = i.split(':')
    if str(len(x)) in str(y):
        s += x[len(x) - 1]
    else:
        length = leng(x, y)
        if length < 1:
            s += 'x'
        
        else:
            s += x[length - 1]
print(s)
